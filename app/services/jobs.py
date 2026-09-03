"""Job queue: one worker subprocess per input file. See docs/decisions/0005.

    runner.submit(paths, target, skip_existing) -> run_id
    runner.events(run_id, cursor)               -> (events, next_cursor, finished)
    runner.cancel(run_id)
    runner.get(run_id)

BEHAVIOUR THAT IS NOT NEGOTIABLE

    Sequential, one worker at a time. androguard's peak commit on the heaviest
    corpus file was ~30 GB against 15.8 GB of RAM; two at once swaps the
    machine. Revisiting this needs a memory-aware scheduler, not a thread pool.

    Per-file isolation. A worker that dies takes only its own file with it.

    Reap with a timeout. Once "done" has been seen the child gets a short grace
    period and is then terminated rather than waited on.

    UTF-8 on the pipe. stdout here is always a pipe, the exact condition under
    which a CJK app name raises UnicodeEncodeError.

    Progress is forwarded, never invented. Nothing here synthesises a
    percentage from elapsed time.
"""

import json
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

from app import config

# Once the worker has emitted "done", how long the child may take to exit before
# it is terminated.
_REAP_GRACE_SEC = 20


class Run:
    def __init__(self, run_id: int, paths, target: str, input_label: str, packages=None):
        self.id = run_id
        self.paths = list(paths)
        # Package names to fetch before analysing. They become entries in
        # self.paths as they arrive, so everything downstream sees ordinary files.
        self.packages = list(packages or [])
        # Fixed at construction. A downloaded package is APPENDED to paths while
        # it stays in packages, so counting both at read time double-counts it.
        self.total = len(self.paths) + len(self.packages)
        self.target = target
        self.input_label = input_label
        self.started_at = datetime.now().isoformat(timespec="seconds")
        self.finished_at = None
        self.status = "running"          # running | done | cancelled | failed
        self.events = []                 # append-only; SSE reads by cursor
        self.results = []                # one row per finished file
        self.failures = []
        self.current = None
        self.workbooks = None            # set by the aggregate step, if it ran
        self.cancelled = threading.Event()
        self.proc = None
        self.lock = threading.Lock()
        self.bell = threading.Condition(self.lock)

    def push(self, ev: dict):
        ev = {**ev, "t": time.time()}
        with self.bell:
            self.events.append(ev)
            self.bell.notify_all()

    def snapshot(self):
        return {
            "id": self.id, "status": self.status, "target": self.target,
            "input": self.input_label,
            "started_at": self.started_at, "finished_at": self.finished_at,
            "file_count": self.total,
            "done_count": len(self.results) + len(self.failures),
            "current": self.current,
            "results": self.results, "failures": self.failures,
            "workbooks": self.workbooks,
        }


class JobRunner:
    def __init__(self):
        self._runs = {}
        self._next_id = 1
        self._lock = threading.Lock()

    # ----------------------------------------------------------- public
    def submit(self, paths, target="hmos", skip_existing=False, input_label="",
               packages=None) -> int:
        with self._lock:
            run_id = self._next_id
            self._next_id += 1
            run = Run(run_id, paths, target,
                      input_label or str(paths[0] if paths else (packages or [""])[0]),
                      packages=packages)
            self._runs[run_id] = run
        threading.Thread(target=self._drive, args=(run, skip_existing),
                         daemon=True, name=f"run-{run_id}").start()
        return run_id

    def get(self, run_id):
        return self._runs.get(run_id)

    def cancel(self, run_id) -> bool:
        run = self._runs.get(run_id)
        if not run or run.status != "running":
            return False
        run.cancelled.set()
        proc = run.proc
        if proc and proc.poll() is None:
            try:
                proc.terminate()
            except Exception:
                pass
        return True

    def events(self, run_id, cursor: int, timeout: float = 20.0):
        """Block until there is something after `cursor`, or the timeout lapses.

        Returning on a timeout with nothing lets the SSE endpoint emit a
        keep-alive, so an idle proxy does not drop a long-running connection.
        """
        run = self._runs.get(run_id)
        if run is None:
            return None, cursor, True
        deadline = time.monotonic() + timeout
        with run.bell:
            while len(run.events) <= cursor and run.status == "running":
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    break
                run.bell.wait(remaining)
            out = run.events[cursor:]
            return out, cursor + len(out), run.status != "running"

    # ----------------------------------------------------------- internals
    def _drive(self, run: Run, skip_existing: bool):
        run.push({"stage": "run_started", "file_count": run.total})
        if run.packages:
            self._fetch_all(run)
        for index, path in enumerate(run.paths):
            if run.cancelled.is_set():
                break
            if skip_existing and self._outputs_exist(path, run.target):
                run.push({"stage": "file_skipped", "index": index,
                          "file": path.name, "reason": "already analysed"})
                run.results.append({"source_file": path.name, "skipped": True})
                continue
            run.current = path.name
            run.push({"stage": "file_started", "index": index,
                      "file": path.name, "total": len(run.paths)})
            self._run_one(run, path, index)
        run.current = None
        if not run.cancelled.is_set():
            self._aggregate(run)
        run.finished_at = datetime.now().isoformat(timespec="seconds")
        final = "cancelled" if run.cancelled.is_set() else "done"

        # The manifest is what makes the SQLite index disposable: it is the
        # durable record of which apps belonged to which run.
        try:
            from app.store import index as store_index
            store_index.write_manifest({**run.snapshot(), "status": final,
                                        "finished_at": run.finished_at})
            store_index.rescan()
        except Exception as exc:
            run.push({"stage": "log", "level": "warn",
                      "detail": f"Could not update the results index: {exc}"})

        run.push({"stage": "run_finished", "status": final,
                  "ok": len(run.results), "failed": len(run.failures),
                  "workbooks": run.workbooks})
        # STATUS IS SET LAST, and it must stay that way. `finished` in events()
        # is derived from it, so setting it before the manifest write leaves a
        # window where the reader closes the stream before run_finished is
        # appended, and the UI's Start button stays disabled forever.
        run.status = final

    def _fetch_all(self, run: Run):
        """Download every requested package, then let the normal loop analyse it.

        Downloading happens IN THIS THREAD rather than a worker subprocess: it
        is network-bound, not memory-bound. A package that cannot be fetched is
        recorded as a failure and the run continues.
        """
        from app.services import downloader

        for package in run.packages:
            if run.cancelled.is_set():
                break
            run.push({"stage": "download_started", "file": package})

            state = {"last": 0.0}

            def progress(got, total, note=None, _pkg=package, _st=state):
                if note:
                    run.push({"stage": "log", "level": "warn", "file": _pkg, "detail": note})
                    return
                # Throttled: a 124 MB app at 256 KB a chunk is ~500 events.
                now = time.monotonic()
                if total and (now - _st["last"] > 0.4 or got >= total):
                    _st["last"] = now
                    run.push({"stage": "download_progress", "file": _pkg,
                              "got": got, "total": total})

            result = downloader.fetch(package, config.INPUT_DIR, progress)

            if result.state == "ready":
                run.paths.append(result.path)
                run.push({"stage": "download_done", "file": package,
                          "path": str(result.path), "source": result.source,
                          "version": result.version, "size": result.size,
                          "note": result.note})
            else:
                run.failures.append({"source_file": package, "error": result.error})
                run.push({"stage": "download_failed", "file": package,
                          "error": result.error, "tried": result.tried})

    def _aggregate(self, run: Run):
        """The two batch workbooks, for a run that covered more than one file.

        Every file is analysed in a process that then exits, so the workers
        leave side-cars and app/aggregate.py replays the aggregation over them,
        calling the REAL exporters. Skipped files count: their side-car is still
        on disk, so a resumed batch still produces complete workbooks.
        """
        # Built in the ORDER THE FILES WERE GIVEN, and including failures as
        # ERROR rows -- that is what the CLI's run_batch writes.
        by_name = {r.get("source_file"): r for r in run.results}
        failed = {f.get("source_file"): f for f in run.failures}

        entries = []
        for path in run.paths:
            name = path.name
            if name in failed:
                entries.append({"row": {
                    "source_file": name, "mode": "error", "app_name": "ERROR",
                    "kit_count": 0, "unmapped_count": 0, "permission_count": 0,
                    "report": None,
                }, "sidecar": None})
                continue
            row = by_name.get(name)
            if row is None:
                continue
            if row.get("skipped"):
                side = self._sidecar_for(name, run.target)
                if side is None:
                    continue
                entries.append({"row": self._row_from_sidecar(row, side), "sidecar": str(side)})
            else:
                entries.append({"row": row, "sidecar": row.get("sidecar")})

        # Fewer than two ANALYSED apps means there is nothing to aggregate.
        if sum(1 for e in entries if e["row"].get("mode") != "error") < 2:
            return

        import tempfile
        plan = {"entries": entries, "result_dir": str(config.RESULT_DIR), "target": run.target}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8") as fh:
            json.dump(plan, fh, ensure_ascii=False, default=str)
            plan_path = fh.name

        run.push({"stage": "aggregating", "detail": f"Building workbooks from {len(entries)} app(s)"})
        try:
            proc = subprocess.Popen(
                [sys.executable, "-u", "-m", "app.aggregate", plan_path],
                cwd=str(config.ROOT), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, encoding="utf-8", errors="replace", bufsize=1,
            )
        except Exception as exc:
            run.push({"stage": "log", "level": "warn",
                      "detail": f"Could not build the batch workbooks: {exc}"})
            return

        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if ev.get("stage") == "aggregate_done":
                run.workbooks = ev.get("result")
            run.push(ev)
        try:
            proc.wait(timeout=120)
        except subprocess.TimeoutExpired:
            run.push({"stage": "log", "level": "warn",
                      "detail": "The workbook step did not exit - terminating it."})
            proc.terminate()
        finally:
            # Both pipes, or the reader leaks a file handle per run.
            for stream in (proc.stdout, proc.stderr):
                try:
                    stream.close()
                except Exception:
                    pass
        try:
            Path(plan_path).unlink()
        except OSError:
            pass

    @staticmethod
    def _sidecar_for(source_file: str, target: str):
        stem = Path(source_file).stem
        p = config.RESULT_DIR / ".sidecars" / f"{stem}_{target}.json"
        return p if p.exists() else None

    @staticmethod
    def _row_from_sidecar(row: dict, side_path: Path) -> dict:
        """A batch row for a file that was skipped this time round.

        Everything the summary sheet needs was written when the file was
        analysed, so a resumed run is not missing rows.
        """
        try:
            side = json.loads(Path(side_path).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            side = {}
        stem = Path(row.get("source_file", "")).stem
        report = config.RESULT_DIR / f"{stem}_apk_hmos_report.html"
        return {
            "source_file": row.get("source_file", ""),
            "mode": "apk",
            "app_name": side.get("app_name") or "",
            "kit_count": len({m["kit"] for m in side.get("mapped", [])}),
            "unmapped_count": len(side.get("unmapped", [])),
            "permission_count": side.get("permissions", 0),
            "report": str(report) if report.exists() else None,
        }

    @staticmethod
    def _outputs_exist(path: Path, target: str) -> bool:
        sfx = path.suffix.lower()
        mode = ("exe_folder" if path.is_dir() else
                "ipa" if sfx == ".ipa" else
                "exe" if sfx in (".exe", ".dll") else "apk")
        stem = path.name if mode == "exe_folder" else path.stem
        eff = target if mode == "apk" else "hmos"
        return (config.RESULT_DIR / f"{stem}_{mode}_{eff}_report.html").exists()

    def _run_one(self, run: Run, path: Path, index: int):
        cmd = [sys.executable, "-u", "-m", "app.worker", str(path), "--target", run.target]
        try:
            proc = subprocess.Popen(
                cmd, cwd=str(config.ROOT),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, encoding="utf-8", errors="replace", bufsize=1,
            )
        except Exception as exc:
            run.failures.append({"source_file": path.name, "error": str(exc)})
            run.push({"stage": "file_failed", "index": index, "file": path.name,
                      "error": str(exc)})
            return

        run.proc = proc
        row, error, saw_done = None, None, False
        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except ValueError:
                # Not protocol output. Something printed straight to stdout past
                # the hooks; keep it visible rather than crashing the reader.
                run.push({"stage": "log", "level": "raw", "detail": line[:500],
                          "index": index, "file": path.name})
                continue
            ev["index"], ev["file"] = index, path.name
            stage = ev.get("stage")
            if stage == "done":
                row, saw_done = ev.get("result"), True
            elif stage == "error":
                error = ev.get("error")
            run.push(ev)
            if stage in ("done", "error"):
                # BOTH ARE TERMINAL BY PROTOCOL, AND BREAKING HERE IS LOAD-BEARING.
                # `for line in proc.stdout` only ends when the child closes
                # stdout, so a worker that announces its result and then lingers
                # would block this reader forever and the reap timeout below
                # would never be reached.
                break

        # Closing our end first means a child still writing gets a broken pipe
        # instead of blocking.
        try:
            proc.stdout.close()
        except Exception:
            pass

        # See _REAP_GRACE_SEC: once the outputs exist we do not wait forever.
        try:
            proc.wait(timeout=_REAP_GRACE_SEC if saw_done else None)
        except subprocess.TimeoutExpired:
            run.push({"stage": "log", "level": "warn", "index": index, "file": path.name,
                      "detail": f"Worker finished but did not exit within "
                                f"{_REAP_GRACE_SEC}s - terminating it."})
            try:
                proc.terminate()
                proc.wait(timeout=10)
            except Exception:
                try:
                    proc.kill()
                except Exception:
                    pass
        finally:
            stderr = (proc.stderr.read() or "").strip() if proc.stderr else ""
            run.proc = None

        if row:
            run.results.append(row)
            run.push({"stage": "file_done", "index": index, "file": path.name, "result": row})
        else:
            msg = error or (stderr[-500:] if stderr else f"worker exited {proc.returncode}")
            if run.cancelled.is_set():
                msg = "cancelled"
            run.failures.append({"source_file": path.name, "error": msg})
            run.push({"stage": "file_failed", "index": index, "file": path.name, "error": msg})


runner = JobRunner()
