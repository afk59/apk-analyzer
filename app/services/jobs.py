"""Job queue: one worker subprocess per input file. See docs/decisions/0005.

    runner.submit(paths, target, skip_existing, root=...) -> run_id
    runner.events(run_id, cursor)               -> (events, next_cursor, finished)
    runner.cancel(run_id)
    runner.get(run_id)

BEHAVIOUR THAT IS NOT NEGOTIABLE, and why

    Sequential, one worker at a time.
        Parallelism is tempting and wrong here. androguard's peak commit on the
        heaviest corpus file was ~30 GB against 15.8 GB of RAM; two at once
        swaps the machine rather than halving the time. Revisiting this needs a
        memory-aware scheduler, not a thread pool.

    Per-file isolation.
        A worker that dies takes only its own file with it. The run continues
        and records that file as failed, exactly as v1's batch loop does.

    Reap with a timeout.
        v1's heaviest file wrote all of its outputs, printed its completion
        line, and then LINGERED holding 8-11 GB while burning CPU; everything
        started afterwards ran 2-3x slower until it was killed by hand. So once
        "done" has been seen, the child gets a short grace period and is then
        terminated rather than waited on.

    UTF-8 on the pipe.
        stdout here is always a pipe, the exact condition under which v1 lost
        11 of 26 apps to a UnicodeEncodeError on a CJK app name.

    Downloads overlap analysis, analysis never overlaps itself.
        A package list is fetched on its own thread while the loop analyses
        whatever has already arrived, so five packages cost roughly "the
        slowest of download-all and analyse-all", not their sum. Downloading is
        network-bound and holds no androguard heap, so this does not break the
        one-worker-at-a-time rule above -- the worker is still alone.

    Progress is forwarded, never invented.
        The worker's stages come from the engine's own phase calls. Nothing
        here synthesises a percentage from elapsed time: this corpus runs from
        1.8 s to 1039 s per file, so a clock-driven bar is wrong exactly when
        someone is watching it.
"""

import collections
import json
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

from app import config

# Once the worker has emitted "done", how long the child may take to exit before
# it is terminated. Generous enough for a normal interpreter teardown, short
# enough that a lingering 10 GB process cannot slow down the next file.
_REAP_GRACE_SEC = 20


def _drain(stream):
    """Read a child's stderr on its own thread, keeping the tail.

    stdout is the protocol and is read line by line; stderr used to be read
    only after stdout ended (and never, for the aggregate step). A child that
    writes more than the OS pipe buffer to stderr then blocks on it while we
    block on stdout -- a deadlock (audit 2026-10-03, BUG-17). Returns the
    thread and a function giving what was read.
    """
    chunks = collections.deque(maxlen=64)      # last ~256 KB is plenty

    def pump():
        try:
            for chunk in iter(lambda: stream.read(4096), ""):
                chunks.append(chunk)
        except Exception:
            pass

    t = threading.Thread(target=pump, daemon=True, name="stderr-drain")
    t.start()
    return t, lambda: "".join(chunks)


class _Cancelled(Exception):
    """Raised from a download's progress callback to abort it mid-body. The
    downloader turns any exception there into a failed Result and deletes the
    partial file, which is exactly what a cancel should leave behind."""


def plan_names(paths, root=None, target="hmos"):
    """(labels, stems) for one run's inputs, both keyed by str(path).

    label -- what the UI and the batch workbook call the file. The bare name
             for a top-level file, exactly as before; the path relative to the
             picked folder for one found in a subfolder, so two `x.dll` in
             different subfolders stay distinguishable.
    stem  -- an output-name override, set ONLY for inputs that would otherwise
             write the same report as another input of this run. Everything
             else keeps the name the CLI gives it, so no existing report is
             renamed. Deterministic: the same folder always yields the same
             names, which is what skip_existing relies on.
    """
    from app.worker import resolve_mode

    labels, stems, by_report = {}, {}, {}
    for p in paths:
        p = Path(p)
        label = p.name
        if root is not None:
            try:
                label = p.relative_to(root).as_posix()
            except ValueError:
                pass
        labels[str(p)] = label
        mode, eff, stem = resolve_mode(p, target)
        # Lower-cased: Windows file names are case-insensitive, so Foo.dll and
        # foo.exe would still overwrite each other's report.
        by_report.setdefault(f"{stem}_{mode}_{eff}".lower(), []).append(p)
    for group in by_report.values():
        if len(group) < 2:
            continue
        for p in group:
            # The label with its extension kept, separators flattened:
            # ShareX.exe / ShareX.dll, plugins__x.dll / x.dll.
            stems[str(p)] = labels[str(p)].replace("/", "__")
    return labels, stems


class Run:
    def __init__(self, run_id: int, paths, target: str, input_label: str, packages=None,
                 root=None):
        self.id = run_id
        self.paths = list(paths)
        self.labels, self.stems = plan_names(self.paths, root, target)
        # Package names to fetch before analysing. They become entries in
        # self.paths as they arrive, so everything downstream -- the loop, the
        # aggregate step, the manifest -- sees ordinary files.
        self.packages = list(packages or [])
        # Fixed at construction. A downloaded package is APPENDED to paths while
        # it stays in packages, so counting both at read time double-counts it
        # and the progress bar's denominator grows as the run succeeds.
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
        # Provenance of every package fetched, kept in the manifest so the
        # index can rebuild it (docs/decisions/0006, rule 3).
        self.downloads = []
        self.cancelled = threading.Event()
        # True while the download thread may still append to self.paths.
        self.fetching = bool(self.packages)
        self.proc = None
        self.lock = threading.Lock()
        self.bell = threading.Condition(self.lock)

    def label(self, path) -> str:
        return self.labels.get(str(path)) or Path(path).name

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
            "downloads": self.downloads,
            "packages": self.packages,
        }


class JobRunner:
    def __init__(self):
        self._runs = {}
        self._next_id = 1
        self._lock = threading.Lock()

    # ----------------------------------------------------------- public
    def submit(self, paths, target="hmos", skip_existing=False, input_label="",
               packages=None, root=None) -> int:
        with self._lock:
            run_id = self._next_id
            self._next_id += 1
            run = Run(run_id, paths, target,
                      input_label or str(paths[0] if paths else (packages or [""])[0]),
                      packages=packages, root=root)
            self._runs[run_id] = run
        threading.Thread(target=self._drive, args=(run, skip_existing),
                         daemon=True, name=f"run-{run_id}").start()
        return run_id

    def get(self, run_id):
        return self._runs.get(run_id)

    def running(self) -> list:
        """Every run still in progress, oldest first."""
        with self._lock:
            return [self._runs[i] for i in sorted(self._runs)
                    if self._runs[i].status == "running"]

    def latest(self):
        """What a reloaded page re-attaches to: the most recent run still in
        progress, else the most recent run. Preferring a running one matters
        when two overlap -- the newer could finish first, and a reload would
        then show it and lose the run that is still going."""
        live = self.running()
        if live:
            return live[-1]
        with self._lock:
            return self._runs[max(self._runs)] if self._runs else None

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

        Returning on a timeout with nothing is deliberate: it lets the SSE
        endpoint emit a keep-alive so an idle proxy or a sleeping laptop does
        not silently drop a connection during a 17-minute file.
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
    def _next_path(self, run: Run, index: int):
        """The input at `index`, waiting for the download thread if it may
        still deliver one. None once there is nothing more to analyse."""
        with run.bell:
            while index >= len(run.paths) and run.fetching and not run.cancelled.is_set():
                run.bell.wait(0.5)
            return run.paths[index] if index < len(run.paths) else None

    def _drive(self, run: Run, skip_existing: bool):
        run.push({"stage": "run_started", "file_count": run.total})
        fetcher = None
        if run.packages:
            fetcher = threading.Thread(target=self._fetch_all, args=(run,),
                                       daemon=True, name=f"fetch-{run.id}")
            fetcher.start()
        index = 0
        while not run.cancelled.is_set():
            path = self._next_path(run, index)
            if path is None:
                break
            name = run.label(path)
            if skip_existing and self._outputs_exist(path, run.target, run.stems.get(str(path))):
                run.push({"stage": "file_skipped", "index": index,
                          "file": name, "reason": "already analysed"})
                run.results.append({"source_file": name, "skipped": True})
            else:
                run.current = name
                run.push({"stage": "file_started", "index": index,
                          "file": name, "total": run.total})
                self._run_one(run, path, index)
            index += 1
        if fetcher is not None:
            # A cancel aborts the body in flight (see _Cancelled), so this is
            # short; the timeout only guards against a stalled socket.
            fetcher.join(timeout=60)
        run.current = None
        if not run.cancelled.is_set():
            self._aggregate(run)
        run.finished_at = datetime.now().isoformat(timespec="seconds")
        final = "cancelled" if run.cancelled.is_set() else "done"

        # The manifest is what makes the SQLite index disposable: it is the
        # durable record of which apps belonged to which run, which nothing else
        # on disk carries. See docs/decisions/0002 and app/store/index.py.
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
        # is derived from it, so the SSE endpoint treats a non-running status
        # with no pending events as "the stream is over" and closes. Setting it
        # before the manifest write -- which takes hundreds of milliseconds --
        # left a window where the reader closed the stream before run_finished
        # was ever appended, and the UI's Start button stayed disabled forever.
        run.status = final

    def _fetch_all(self, run: Run):
        """Download every requested package, then let the normal loop analyse it.

        Downloading happens IN THIS THREAD rather than a worker subprocess: it is
        network-bound, not memory-bound, so the reason the analysis is isolated
        (androguard not returning its heap) does not apply. All the network code
        still lives in one module, which is the rule that actually matters.

        A package that cannot be fetched is recorded as a failure and the run
        continues -- same per-file isolation as a corrupt APK.
        """
        from app.services import downloader

        try:
            self._fetch_each(run, downloader)
        finally:
            with run.bell:
                run.fetching = False
                run.bell.notify_all()

    def _fetch_each(self, run: Run, downloader):
        for package in run.packages:
            if run.cancelled.is_set():
                break
            requested_at = datetime.now().isoformat(timespec="seconds")
            run.push({"stage": "download_started", "file": package})

            state = {"last": 0.0}

            def progress(got, total, note=None, _pkg=package, _st=state):
                if run.cancelled.is_set() and got is not None:
                    raise _Cancelled()
                if note:
                    run.push({"stage": "log", "level": "warn", "file": _pkg, "detail": note})
                    return
                # Throttled: a 124 MB app at 256 KB a chunk is ~500 events, and
                # every one of them goes down the SSE stream to a progress bar
                # that cannot show that much detail anyway.
                now = time.monotonic()
                if total and (now - _st["last"] > 0.4 or got >= total):
                    _st["last"] = now
                    run.push({"stage": "download_progress", "file": _pkg,
                              "got": got, "total": total})

            result = downloader.fetch(package, config.INPUT_DIR, progress)
            run.downloads.append({
                "package_name": package, "source": result.source,
                "state": result.state,
                "file_path": str(result.path) if result.path else None,
                "version": result.version, "size": result.size,
                "requested_at": requested_at, "error": result.error,
                "note": result.note,
            })

            if result.state == "ready":
                # Appended under the lock the analysis loop waits on, and the
                # event below wakes it: the file starts analysing while the
                # next package downloads.
                with run.bell:
                    run.paths.append(result.path)
                    run.labels[str(result.path)] = result.path.name
                run.push({"stage": "download_done", "file": package,
                          "path": str(result.path), "source": result.source,
                          "version": result.version, "size": result.size,
                          "note": result.note})
            else:
                error = "cancelled" if run.cancelled.is_set() else result.error
                run.failures.append({"source_file": package, "error": error})
                run.push({"stage": "download_failed", "file": package,
                          "error": error, "tried": result.tried})

    def _aggregate(self, run: Run):
        """The two batch workbooks, for a run that covered more than one file.

        v1's run_batch accumulates these inside its analysis loop. This design
        cannot: every file is analysed in a process that then exits. So the
        workers leave side-cars and app/aggregate.py replays the same
        aggregation over them, calling the REAL exporters -- reimplementing the
        sheets would create a second thing that could disagree about the corpus.

        Skipped files count: their side-car is still on disk from the earlier
        run, so a resumed batch still produces complete workbooks. A run with
        one file gets none, matching the CLI, where a single-file run has never
        produced them either.
        """
        entries = self._entries(run)

        # Fewer than two ANALYSED apps means there is nothing to aggregate --
        # the CLI has never produced these workbooks for a single file either.
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

        drain, _ = _drain(proc.stderr)
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
            drain.join(timeout=5)
            # Both pipes, or the reader leaks a file handle per run -- surfaced
            # as a ResourceWarning by the test suite.
            for stream in (proc.stdout, proc.stderr):
                try:
                    stream.close()
                except Exception:
                    pass
        try:
            Path(plan_path).unlink()
        except OSError:
            pass

    def _entries(self, run: Run) -> list:
        """The rows the two workbooks are built from.

        Built in the ORDER THE FILES WERE GIVEN, and including failures as
        ERROR rows -- that is what v1's run_batch writes, and a file that was
        attempted and failed belongs in the summary. Omitting it would make a
        workbook that quietly disagrees with the run it came from.
        """
        by_name = {r.get("source_file"): r for r in run.results}
        failed = {f.get("source_file"): f for f in run.failures}

        entries = []
        for path in run.paths:
            name = run.label(path)
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
                stem = run.stems.get(str(path))
                side = self._sidecar_for(path, run.target, stem)
                if side is None:
                    continue
                entries.append({"row": self._row_from_sidecar(
                                    row, side, self._report_for(path, run.target, stem)),
                                "sidecar": str(side)})
            else:
                entries.append({"row": row, "sidecar": row.get("sidecar")})
        return entries

    @staticmethod
    def _sidecar_for(path, target: str, stem=None):
        from app.worker import resolve_mode, sidecar_name
        mode, eff, stem = resolve_mode(Path(path), target, stem)
        p = config.RESULT_DIR / ".sidecars" / sidecar_name(stem, mode, eff)
        return p if p.exists() else None

    @staticmethod
    def _row_from_sidecar(row: dict, side_path: Path, report: Path) -> dict:
        """A batch row for a file that was skipped this time round.

        Everything the summary sheet needs was already written when the file was
        analysed, so a resumed run is not missing rows -- which is the whole
        point of being able to resume.
        """
        try:
            side = json.loads(Path(side_path).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            side = {}
        mode = side.get("mode") or "apk"
        if mode == "apk":
            kits = len({m["kit"] for m in side.get("mapped", [])})
            unmapped = len(side.get("unmapped", []))
        else:
            # EXE/IPA side-cars carry the row's own counts; there is no
            # namespace list to count them from.
            kits = side.get("kit_count", 0)
            unmapped = side.get("unmapped_count", 0)
        return {
            "source_file": row.get("source_file", ""),
            "mode": mode,
            "app_name": side.get("app_name") or "",
            "kit_count": kits,
            "unmapped_count": unmapped,
            "permission_count": side.get("permissions", 0),
            "report": str(report) if report.exists() else None,
        }

    @staticmethod
    def _report_for(path: Path, target: str, stem=None) -> Path:
        """Where the worker writes this input's report. The worker's own naming,
        not a copy of it: a resumed HMS run once looked for "_apk_hmos_" and
        lost every report link for the files it skipped."""
        from app.worker import resolve_mode
        mode, eff, stem = resolve_mode(path, target, stem)
        return config.RESULT_DIR / f"{stem}_{mode}_{eff}_report.html"

    @staticmethod
    def _outputs_exist(path: Path, target: str, stem=None) -> bool:
        return JobRunner._report_for(path, target, stem).exists()

    def _run_one(self, run: Run, path: Path, index: int):
        name = run.label(path)
        cmd = [sys.executable, "-u", "-m", "app.worker", str(path), "--target", run.target]
        if run.stems.get(str(path)):
            cmd += ["--stem", run.stems[str(path)]]
        try:
            proc = subprocess.Popen(
                cmd, cwd=str(config.ROOT),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, encoding="utf-8", errors="replace", bufsize=1,
            )
        except Exception as exc:
            run.failures.append({"source_file": name, "error": str(exc)})
            run.push({"stage": "file_failed", "index": index, "file": name,
                      "error": str(exc)})
            return

        run.proc = proc
        drain, stderr_text = _drain(proc.stderr)
        row, error, saw_done = None, None, False
        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except ValueError:
                # Not protocol output. Something printed straight to stdout past
                # the hooks; keep it visible as a log line rather than crashing
                # the reader on it.
                run.push({"stage": "log", "level": "raw", "detail": line[:500],
                          "index": index, "file": name})
                continue
            ev["index"], ev["file"] = index, name
            stage = ev.get("stage")
            if stage == "done":
                row, saw_done = ev.get("result"), True
            elif stage == "error":
                error = ev.get("error")
            run.push(ev)
            if stage in ("done", "error"):
                # BOTH ARE TERMINAL BY PROTOCOL, AND BREAKING HERE IS LOAD-BEARING.
                # `for line in proc.stdout` only ends when the child closes stdout,
                # so a worker that announces its result and then lingers -- the
                # exact v1 shape where the heaviest file held 8-11 GB after
                # finishing -- would block this reader forever and the reap
                # timeout below would never be reached. Found by the test that
                # simulates precisely that.
                break

        # Reading is over, so the child can be reaped. Closing our end first
        # means a child still writing gets a broken pipe instead of blocking.
        try:
            proc.stdout.close()
        except Exception:
            pass

        # See _REAP_GRACE_SEC: once the outputs exist we do not wait forever.
        try:
            proc.wait(timeout=_REAP_GRACE_SEC if saw_done else None)
        except subprocess.TimeoutExpired:
            run.push({"stage": "log", "level": "warn", "index": index, "file": name,
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
            # The child has exited (or been killed), so its end of the pipe is
            # closed and the drain thread is finishing; the timeout only covers
            # a grandchild that inherited the handle.
            drain.join(timeout=5)
            stderr = stderr_text().strip()
            # Closed, not just read: one leaked handle per file adds up over a
            # program folder of hundreds of binaries.
            try:
                proc.stderr.close()
            except Exception:
                pass
            run.proc = None

        if row:
            # The run's name for the file, not the worker's bare file name: they
            # differ only for a file found in a subfolder, where the bare name
            # is ambiguous.
            row["source_file"] = name
            run.results.append(row)
            run.push({"stage": "file_done", "index": index, "file": name, "result": row})
        else:
            msg = error or (stderr[-500:] if stderr else f"worker exited {proc.returncode}")
            if run.cancelled.is_set():
                msg = "cancelled"
            run.failures.append({"source_file": name, "error": msg})
            run.push({"stage": "file_failed", "index": index, "file": name, "error": msg})


runner = JobRunner()
