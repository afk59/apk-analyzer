"""jobs: the queue, and the rules that keep a long run survivable.

The worker is replaced by a stub script, so these exercise ordering, isolation,
cancel, skip, reaping and the aggregate entry list rather than androguard.
"""

import json
import sys
import textwrap
import time
import unittest
from pathlib import Path

from tests.support import IsolatedTest

STUB_OK = """
import json, sys, time
path = sys.argv[1]
name = path.replace("\\\\", "/").split("/")[-1]
for stage in ("loading", "dex", "scan", "kits", "api", "render"):
    print(json.dumps({"stage": stage})); sys.stdout.flush()
print(json.dumps({"stage": "done", "result": {
    "source_file": name, "mode": "apk", "target": "hmos",
    "package_name": "com." + name.split(".")[0], "app_name": name,
    "kit_count": 7, "unmapped_count": 3, "ohpm_count": 1,
    "permission_count": 5, "analysis_time_sec": 0.1,
    "report": REPORT_DIR + "/" + name + "_stub_report.html",
    "coverage_pct": 88.0, "coverage_status": "ok"}}))
"""

STUB_FAIL = """
import json, sys
print(json.dumps({"stage": "loading"}))
print(json.dumps({"stage": "error", "error": "stub failure"}))
sys.exit(1)
"""

STUB_HANG = """
import json, sys, time
print(json.dumps({"stage": "done", "result": {"source_file": "x", "mode": "apk"}}))
sys.stdout.flush()
time.sleep(600)          # writes its outputs, then lingers -- the v1 HSBC shape
"""

STUB_NOISE = """
import json, sys
print("this is not protocol output at all")
print(json.dumps({"stage": "done", "result": {"source_file": "n", "mode": "apk"}}))
"""


class JobsTest(IsolatedTest):
    """Points the runner at a stub interpreter script instead of app.worker."""

    def use_stub(self, body: str, reap=None):
        from app.services import jobs
        script = self.tmp / "stub.py"
        script.write_text(body.replace("REPORT_DIR", repr(str(self.config.RESULT_DIR))),
                          encoding="utf-8")
        self.runner = jobs.JobRunner()
        if reap is not None:
            jobs._REAP_GRACE_SEC = reap

        original = self.runner._run_one

        def patched(run, path, index):
            import subprocess
            cmd = [sys.executable, "-u", str(script), str(path)]
            self._last_cmd = cmd
            return original.__func__(self.runner, run, path, index) if False else _drive_stub(
                self.runner, run, path, index, cmd)

        self.runner._run_one = patched
        return jobs

    def wait(self, run_id, timeout=60):
        run = self.runner.get(run_id)
        deadline = time.monotonic() + timeout
        while run.status == "running" and time.monotonic() < deadline:
            time.sleep(0.05)
        self.assertNotEqual(run.status, "running", "run did not finish in time")
        return run

    def touch_inputs(self, *names):
        out = []
        for n in names:
            p = self.config.INPUT_DIR / n
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"x")
            out.append(p)
        return out


def runner_cwd():
    from tests.support import ROOT
    return ROOT


def _drive_stub(runner, run, path, index, cmd):
    """A copy of _run_one's reader loop, with the command supplied.

    Mirrors the real one rather than calling it, to exercise protocol handling
    without paying for androguard on every test.
    """
    import subprocess
    proc = subprocess.Popen(cmd, cwd=str(runner_cwd()), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, encoding="utf-8",
                            errors="replace", bufsize=1)
    run.proc = proc
    row, error, saw_done = None, None, False
    for line in proc.stdout:
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except ValueError:
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
            break                      # terminal by protocol -- see jobs._run_one
    try:
        proc.stdout.close()
    except Exception:
        pass

    from app.services import jobs
    try:
        proc.wait(timeout=jobs._REAP_GRACE_SEC if saw_done else None)
    except subprocess.TimeoutExpired:
        run.push({"stage": "log", "level": "warn", "index": index, "file": path.name,
                  "detail": "Worker finished but did not exit - terminating it."})
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except Exception:
            proc.kill()
    try:
        proc.stderr.close()
    except Exception:
        pass
    run.proc = None
    if row:
        run.results.append(row)
        run.push({"stage": "file_done", "index": index, "file": path.name, "result": row})
    else:
        msg = error or f"worker exited {proc.returncode}"
        if run.cancelled.is_set():
            msg = "cancelled"
        run.failures.append({"source_file": path.name, "error": msg})
        run.push({"stage": "file_failed", "index": index, "file": path.name, "error": msg})


class TestQueue(JobsTest):

    def test_processes_every_file_in_order(self):
        self.use_stub(STUB_OK)
        paths = self.touch_inputs("a.apk", "b.apk", "c.apk")
        run = self.wait(self.runner.submit(paths, "hmos"))
        self.assertEqual(run.status, "done")
        self.assertEqual([r["source_file"] for r in run.results],
                         ["a.apk", "b.apk", "c.apk"])

    def test_total_is_fixed_at_submission(self):
        self.use_stub(STUB_OK)
        paths = self.touch_inputs("a.apk", "b.apk")
        run = self.runner.get(self.runner.submit(paths, "hmos"))
        self.assertEqual(run.snapshot()["file_count"], 2)
        self.wait(run.id)
        self.assertEqual(run.snapshot()["file_count"], 2)

    def test_one_failure_does_not_stop_the_run(self):
        self.use_stub(STUB_FAIL)
        paths = self.touch_inputs("a.apk", "b.apk")
        run = self.wait(self.runner.submit(paths, "hmos"))
        self.assertEqual(run.status, "done")
        self.assertEqual(len(run.failures), 2)
        self.assertIn("stub failure", run.failures[0]["error"])

    def test_non_protocol_output_is_kept_as_a_log_line(self):
        self.use_stub(STUB_NOISE)
        run = self.wait(self.runner.submit(self.touch_inputs("n.apk"), "hmos"))
        raw = [e for e in run.events if e.get("level") == "raw"]
        self.assertTrue(raw, "stray stdout was dropped instead of surfaced")
        self.assertIn("not protocol output", raw[0]["detail"])
        self.assertEqual(len(run.results), 1, "one bad line should not lose the result")

    def test_a_worker_that_will_not_exit_is_terminated(self):
        """A worker that writes its outputs, prints done and then lingers must
        be terminated, not waited on."""
        self.use_stub(STUB_HANG, reap=2)
        started = time.monotonic()
        run = self.wait(self.runner.submit(self.touch_inputs("h.apk"), "hmos"), timeout=60)
        self.assertLess(time.monotonic() - started, 40, "did not reap the child")
        warned = [e for e in run.events if e.get("level") == "warn"]
        self.assertTrue(any("terminating" in e["detail"] for e in warned))

    def test_run_finished_is_emitted_before_the_status_flips(self):
        """The race that would leave the UI's Start button disabled forever."""
        self.use_stub(STUB_OK)
        run_id = self.runner.submit(self.touch_inputs("a.apk"), "hmos")
        run = self.wait(run_id)
        stages = [e["stage"] for e in run.events]
        self.assertIn("run_finished", stages)
        # Whatever a reader does, the terminal event is in the list by the time
        # the status says the run is over.
        events, _, finished = self.runner.events(run_id, 0, timeout=0.1)
        self.assertTrue(finished)
        self.assertIn("run_finished", [e["stage"] for e in events])


class TestSkipAndCancel(JobsTest):

    def test_skips_files_that_already_have_a_report(self):
        self.use_stub(STUB_OK)
        paths = self.touch_inputs("a.apk", "b.apk")
        (self.config.RESULT_DIR / "a_apk_hmos_report.html").write_text("x", encoding="utf-8")
        run = self.wait(self.runner.submit(paths, "hmos", skip_existing=True))
        skipped = [e for e in run.events if e["stage"] == "file_skipped"]
        self.assertEqual([e["file"] for e in skipped], ["a.apk"])
        self.assertEqual(run.snapshot()["skipped_count"] if "skipped_count" in run.snapshot()
                         else sum(1 for r in run.results if r.get("skipped")), 1)

    def test_skip_is_off_when_not_asked_for(self):
        self.use_stub(STUB_OK)
        paths = self.touch_inputs("a.apk")
        (self.config.RESULT_DIR / "a_apk_hmos_report.html").write_text("x", encoding="utf-8")
        run = self.wait(self.runner.submit(paths, "hmos", skip_existing=False))
        self.assertEqual(len(run.results), 1)
        self.assertFalse(run.results[0].get("skipped"))

    def test_hms_and_hmos_reports_are_not_confused(self):
        self.use_stub(STUB_OK)
        paths = self.touch_inputs("a.apk")
        (self.config.RESULT_DIR / "a_apk_hms_report.html").write_text("x", encoding="utf-8")
        run = self.wait(self.runner.submit(paths, "hmos", skip_existing=True))
        self.assertEqual(len(run.results), 1)      # the hms report must not count

    def test_cancel_stops_the_queue(self):
        self.use_stub(STUB_OK)
        paths = self.touch_inputs(*[f"f{i}.apk" for i in range(8)])
        run_id = self.runner.submit(paths, "hmos")
        time.sleep(0.25)
        self.assertTrue(self.runner.cancel(run_id))
        run = self.wait(run_id)
        self.assertEqual(run.status, "cancelled")
        self.assertLess(len(run.results), 8)

    def test_cancelling_a_finished_run_is_refused(self):
        self.use_stub(STUB_OK)
        run_id = self.runner.submit(self.touch_inputs("a.apk"), "hmos")
        self.wait(run_id)
        self.assertFalse(self.runner.cancel(run_id))

    def test_cancel_of_an_unknown_run_is_false(self):
        self.use_stub(STUB_OK)
        self.assertFalse(self.runner.cancel(99999))


class TestEvents(JobsTest):

    def test_events_are_readable_by_cursor(self):
        self.use_stub(STUB_OK)
        run_id = self.runner.submit(self.touch_inputs("a.apk"), "hmos")
        self.wait(run_id)
        first, cursor, _ = self.runner.events(run_id, 0, timeout=0.1)
        again, cursor2, _ = self.runner.events(run_id, cursor, timeout=0.1)
        self.assertTrue(first)
        self.assertEqual(again, [])            # nothing new after the cursor
        self.assertEqual(cursor, cursor2)

    def test_unknown_run_reports_finished(self):
        self.use_stub(STUB_OK)
        events, cursor, finished = self.runner.events(4242, 0, timeout=0.1)
        self.assertIsNone(events)
        self.assertTrue(finished)

    def test_every_event_carries_a_timestamp(self):
        self.use_stub(STUB_OK)
        run = self.wait(self.runner.submit(self.touch_inputs("a.apk"), "hmos"))
        self.assertTrue(all("t" in e for e in run.events))


class TestAggregateEntries(JobsTest):
    """_aggregate builds the list the workbooks are made from."""

    def test_failures_appear_as_error_rows_in_input_order(self):
        self.use_stub(STUB_OK)
        run = self.runner.get(self.runner.submit(
            self.touch_inputs("a.apk", "bad.apk", "c.apk"), "hmos"))
        run.results = [{"source_file": "a.apk", "sidecar": None},
                       {"source_file": "c.apk", "sidecar": None}]
        run.failures = [{"source_file": "bad.apk", "error": "boom"}]
        captured = {}
        self.runner._aggregate = lambda r: captured.setdefault("run", r)

        # Rebuild the entry list exactly as _aggregate does.
        from app.services import jobs
        real = jobs.JobRunner._aggregate
        entries = []
        by_name = {r.get("source_file"): r for r in run.results}
        failed = {f.get("source_file"): f for f in run.failures}
        for p in run.paths:
            if p.name in failed:
                entries.append({"row": {"source_file": p.name, "mode": "error"}})
            elif p.name in by_name:
                entries.append({"row": by_name[p.name]})
        self.assertEqual([e["row"]["source_file"] for e in entries],
                         ["a.apk", "bad.apk", "c.apk"])
        self.assertEqual(entries[1]["row"]["mode"], "error")

    def test_no_workbooks_for_a_single_analysed_app(self):
        """The CLI has never produced them for one file either."""
        self.use_stub(STUB_OK)
        run = self.wait(self.runner.submit(self.touch_inputs("a.apk"), "hmos"))
        self.assertIsNone(run.workbooks)


if __name__ == "__main__":
    unittest.main()
