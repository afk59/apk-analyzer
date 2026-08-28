"""Job queue: one worker subprocess per input file. See docs/decisions/0005.

    runner.submit(paths, target, skip_existing) -> run_id
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

    Progress is forwarded, never invented.
        The worker's stages come from the engine's own phase calls. Nothing
        here synthesises a percentage from elapsed time: this corpus runs from
        1.8 s to 1039 s per file, so a clock-driven bar is wrong exactly when
        someone is watching it.
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
# it is terminated. Generous enough for a normal interpreter teardown, short
# enough that a lingering 10 GB process cannot slow down the next file.
_REAP_GRACE_SEC = 20


class Run:
    def __init__(self, run_id: int, paths, target: str, input_label: str):
        self.id = run_id
        self.paths = list(paths)
        self.target = target
        self.input_label = input_label
        self.started_at = datetime.now().isoformat(timespec="seconds")
        self.finished_at = None
        self.status = "running"          # running | done | cancelled | failed
        self.events = []                 # append-only; SSE reads by cursor
        self.results = []                # one row per finished file
        self.failures = []
        self.current = None
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
            "file_count": len(self.paths),
            "done_count": len(self.results) + len(self.failures),
            "current": self.current,
            "results": self.results, "failures": self.failures,
        }


class JobRunner:
    def __init__(self):
        self._runs = {}
        self._next_id = 1
        self._lock = threading.Lock()

    # ----------------------------------------------------------- public
    def submit(self, paths, target="hmos", skip_existing=False, input_label="") -> int:
        with self._lock:
            run_id = self._next_id
            self._next_id += 1
            run = Run(run_id, paths, target, input_label or str(paths[0] if paths else ""))
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
    def _drive(self, run: Run, skip_existing: bool):
        run.push({"stage": "run_started", "file_count": len(run.paths)})
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
        run.finished_at = datetime.now().isoformat(timespec="seconds")
        run.status = "cancelled" if run.cancelled.is_set() else "done"
        run.push({"stage": "run_finished", "status": run.status,
                  "ok": len(run.results), "failed": len(run.failures)})

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
                # the hooks; keep it visible as a log line rather than crashing
                # the reader on it.
                run.push({"stage": "log", "level": "raw", "detail": line[:500],
                          "index": index, "file": path.name})
                continue
            ev["index"], ev["file"] = index, path.name
            if ev.get("stage") == "done":
                row, saw_done = ev.get("result"), True
            elif ev.get("stage") == "error":
                error = ev.get("error")
            run.push(ev)

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
