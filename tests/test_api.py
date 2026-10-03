"""api: every endpoint, against a REAL server on a loopback port.

A real server rather than a test client, for two reasons: it needs no extra
dependency (starlette's TestClient wants httpx), and it exercises the actual
startup path -- free port, uvicorn on a thread, static mount -- which is where
M1's bugs would live.

The server runs with the MA_* redirections, so it writes only into the temp dir.
"""

import json
import os
import socket
import subprocess
import sys
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

from tests.support import IsolatedTest


class ApiTest(IsolatedTest):

    def setUp(self):
        super().setUp()
        self.proc = None
        self.base = None

    def tearDown(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        if self.proc:
            for s in (self.proc.stdout, self.proc.stderr):
                try:
                    s.close()
                except Exception:
                    pass
        super().tearDown()

    def start_server(self, timeout=60):
        env = {**dict(os.environ),
               "MA_RESULT_DIR": str(self.config.RESULT_DIR),
               "MA_DB_PATH": str(self.config.DB_PATH),
               "MA_INPUT_DIR": str(self.config.INPUT_DIR),
               "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
        self.proc = subprocess.Popen(
            [sys.executable, "-u", "-m", "app", "--no-window"],
            cwd=str(self.config.ROOT), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding="utf-8", errors="replace", env=env, bufsize=1)
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            line = self.proc.stdout.readline()
            if not line:
                if self.proc.poll() is not None:
                    self.fail("server exited: " + (self.proc.stderr.read() or "")[-800:])
                continue
            if "serving on" in line:
                self.base = line.split("serving on")[-1].strip()
                return self.base
        self.fail("server did not report a port in time")

    # ------------------------------------------------------------- helpers
    def get(self, path, timeout=30):
        with urllib.request.urlopen(self.base + path, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode("utf-8"))

    def post(self, path, data=None, timeout=60):
        req = urllib.request.Request(self.base + path, method="POST")
        req.add_header("Content-Type", "application/json")
        body = json.dumps(data or {}).encode()
        try:
            with urllib.request.urlopen(req, body, timeout=timeout) as r:
                return r.status, json.loads(r.read().decode("utf-8") or "{}")
        except urllib.error.HTTPError as e:
            with e:                       # closing it keeps the suite quiet
                raw = e.read().decode("utf-8", "replace")
            try:
                return e.code, json.loads(raw)
            except ValueError:
                return e.code, {"raw": raw}

    def expect_status(self, path, code, timeout=30):
        """A GET that must fail. Closing the HTTPError matters: it holds the
        socket, and an unclosed one shows up as a ResourceWarning later, in an
        unrelated test."""
        try:
            with urllib.request.urlopen(self.base + path, timeout=timeout):
                self.fail(f"{path} unexpectedly succeeded")
        except urllib.error.HTTPError as e:
            with e:
                e.read()
            self.assertEqual(e.code, code, path)

    def raw(self, path, timeout=30):
        with urllib.request.urlopen(self.base + path, timeout=timeout) as r:
            return r.status, r.read(), dict(r.headers)


class TestServerBasics(ApiTest):

    def test_binds_loopback_only(self):
        """This server opens local files and drives native dialogs. It must not
        be reachable from the network."""
        base = self.start_server()
        self.assertTrue(base.startswith("http://127.0.0.1:"), base)

    def test_health_reports_a_usable_engine(self):
        self.start_server()
        status, body = self.get("/api/health")
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertTrue(body["mappings"], "mapping.json not found by the server")
        self.assertTrue(body["result_dir"].startswith(str(self.tmp)))

    def test_serves_the_frontend_and_its_assets(self):
        self.start_server()
        status, body, headers = self.raw("/")
        self.assertEqual(status, 200)
        self.assertIn(b"Migration Analyzer", body)
        for asset in ("/css/tokens.css", "/css/app.css", "/js/api.js",
                      "/js/main.js", "/js/run.js", "/js/theme.js"):
            st, data, _ = self.raw(asset)
            self.assertEqual(st, 200, asset)
            self.assertGreater(len(data), 100, asset)

    def test_an_unknown_path_is_404_not_a_crash(self):
        self.start_server()
        self.expect_status("/nope/nothing", 404)


class TestOpenEndpoint(ApiTest):

    def test_refuses_a_path_outside_the_result_tree(self):
        self.start_server()
        for path in ("C:/Windows/notepad.exe", "/etc/passwd",
                     str(self.config.RESULT_DIR / ".." / ".." / "secret.txt")):
            status, body = self.post("/api/open", {"path": path})
            self.assertEqual(status, 403, path)
            self.assertIn("result folder", body["detail"])

    def test_reports_a_missing_file_inside_the_tree(self):
        self.start_server()
        status, body = self.post("/api/open", {"path": "nope.html"})
        # Relative paths resolve under ROOT, so this one is outside result/.
        self.assertIn(status, (403, 404))

    def test_missing_body_field_is_a_422(self):
        self.start_server()
        status, _ = self.post("/api/open", {})
        self.assertEqual(status, 422)


class TestRunEndpoint(ApiTest):

    def test_rejects_a_nonexistent_input(self):
        self.start_server()
        status, body = self.post("/api/runs", {"input": str(self.tmp / "ghost.apk")})
        self.assertEqual(status, 404)

    def test_rejects_an_unknown_target(self):
        self.start_server()
        p = self.make_fake_apk(self.config.INPUT_DIR / "x.apk")
        status, _ = self.post("/api/runs", {"input": str(p), "target": "android"})
        self.assertEqual(status, 400)

    def test_rejects_an_empty_folder(self):
        self.start_server()
        empty = self.tmp / "empty"
        empty.mkdir()
        status, body = self.post("/api/runs", {"input": str(empty)})
        self.assertEqual(status, 400)
        self.assertIn("Nothing analysable", body["detail"])

    def test_a_folder_of_apks_is_a_batch_and_defaults_to_skipping(self):
        self.start_server()
        d = self.tmp / "many"
        d.mkdir()
        for n in ("a.apk", "b.apk"):
            self.make_fake_apk(d / n)
        status, body = self.post("/api/runs", {"input": str(d)})
        self.assertEqual(status, 200)
        self.assertEqual(body["file_count"], 2)
        self.assertTrue(body["skip_existing"])
        self.post(f"/api/runs/{body['run_id']}/cancel")

    def test_a_single_file_is_never_skipped(self):
        self.start_server()
        p = self.make_fake_apk(self.config.INPUT_DIR / "solo.apk")
        status, body = self.post("/api/runs", {"input": str(p)})
        self.assertEqual(status, 200)
        self.assertFalse(body["skip_existing"])
        self.post(f"/api/runs/{body['run_id']}/cancel")

    def test_a_folder_of_binaries_can_be_one_exe_folder_application(self):
        """The engine's exe_folder mode -- the whole folder as ONE app, the
        report the CLI writes for a folder -- is the "combined" option. A
        program folder defaults to a per-binary batch (tests/test_batch_features)."""
        self.start_server()
        d = self.tmp / "pcapp"
        d.mkdir()
        (d / "app.exe").write_bytes(b"MZ")
        (d / "core.dll").write_bytes(b"MZ")
        status, body = self.post("/api/runs", {"input": str(d), "pc_mode": "combined"})
        self.assertEqual(status, 200)
        self.assertEqual(body["file_count"], 1)
        self.assertIn("(folder)", body["input"])
        self.post(f"/api/runs/{body['run_id']}/cancel")

    def test_bundles_are_not_picked_up_by_a_folder_run(self):
        self.start_server()
        d = self.tmp / "mixed"
        d.mkdir()
        self.make_fake_apk(d / "real.apk")
        self.make_bundle(d / "bundle.apkm")
        status, body = self.post("/api/runs", {"input": str(d)})
        self.assertEqual(body["file_count"], 1)
        self.post(f"/api/runs/{body['run_id']}/cancel")

    def test_latest_is_null_before_any_run_and_the_run_after_one(self):
        """A reloaded page re-attaches through this; "latest" must not be
        swallowed by /api/runs/{run_id} as a malformed integer."""
        self.start_server()
        self.assertEqual(self.get("/api/runs/latest"), (200, {"run": None}))
        d = self.tmp / "one"
        d.mkdir()
        self.make_fake_apk(d / "a.apk")
        _, body = self.post("/api/runs", {"input": str(d)})
        _, latest = self.get("/api/runs/latest")
        self.assertEqual(latest["run"]["id"], body["run_id"])

    def test_unknown_run_id_is_404(self):
        self.start_server()
        self.expect_status("/api/runs/99999", 404)

    def test_cancelling_an_unknown_run_is_409(self):
        self.start_server()
        status, _ = self.post("/api/runs/99999/cancel")
        self.assertEqual(status, 409)


class TestDownloadEndpoint(ApiTest):
    """Input validation only -- no network is touched."""

    def test_rejects_an_empty_list(self):
        self.start_server()
        for value in ("", "   ", ",,,", "\n\n"):
            status, _ = self.post("/api/downloads", {"packages": value})
            self.assertEqual(status, 400, repr(value))

    def test_rejects_things_that_are_not_package_names(self):
        self.start_server()
        # "x:y" / "C:evil" are drive-relative paths on Windows (audit BUG-14).
        for value in ("../etc/passwd", "a/b", "has space", "a\\b",
                      "x:y", "C:evil", "nodots", "com..x", "1com.x", "com.x."):
            status, body = self.post("/api/downloads", {"packages": value})
            self.assertEqual(status, 400, value)
            self.assertIn("Not package names", body["detail"])

    def test_accepts_commas_and_newlines(self):
        self.start_server()
        status, body = self.post("/api/downloads",
                                 {"packages": "com.a, com.b\ncom.c"})
        self.assertEqual(status, 200)
        self.assertEqual(body["file_count"], 3)
        self.post(f"/api/runs/{body['run_id']}/cancel")

    def test_rejects_an_unknown_target(self):
        self.start_server()
        status, _ = self.post("/api/downloads",
                              {"packages": "com.a", "target": "nope"})
        self.assertEqual(status, 400)


class TestLibraryEndpoints(ApiTest):

    def test_empty_library_is_empty_not_an_error(self):
        self.start_server()
        status, body = self.get("/api/results")
        self.assertEqual(status, 200)
        self.assertEqual(body["runs"], [])
        self.assertEqual(body["workbooks"], {})

    def test_self_heals_when_the_index_is_missing_but_reports_exist(self):
        self.make_report("healme")
        self.make_agent_json("healme", package="com.healme", app_name="Heal")
        self.start_server()
        status, body = self.get("/api/results")
        self.assertEqual(status, 200)
        self.assertEqual(len(body["runs"]), 1)
        self.assertEqual(body["runs"][0]["apps"][0]["app_name"], "Heal")

    def test_rescan_reports_what_it_found(self):
        self.make_report("a")
        self.make_agent_json("a")
        self.start_server()
        status, counts = self.post("/api/rescan")
        self.assertEqual(status, 200)
        self.assertEqual(counts["apps"], 1)
        self.assertEqual(counts["orphans"], 1)


class TestEventStream(ApiTest):

    def test_events_stream_and_terminate(self):
        self.start_server()
        d = self.tmp / "one"
        d.mkdir()
        self.make_fake_apk(d / "a.apk")
        status, body = self.post("/api/runs", {"input": str(d)})
        run_id = body["run_id"]

        stages, ended = [], False
        with urllib.request.urlopen(
                f"{self.base}/api/runs/{run_id}/events", timeout=180) as r:
            for raw in r:
                line = raw.decode("utf-8", "replace").strip()
                if line.startswith("data: "):
                    ev = json.loads(line[6:])
                    if ev.get("stage"):
                        stages.append(ev["stage"])
                    if ev.get("stage") == "run_finished":
                        ended = True
                        break
        self.assertTrue(ended, f"stream ended without run_finished: {stages}")
        self.assertIn("run_started", stages)
        # A fake APK cannot be analysed, so the file must fail -- and the RUN
        # must still finish. Per-file isolation is the property being checked.
        self.assertIn("file_failed", stages)

    def test_a_reconnect_resumes_after_the_last_event_id(self):
        """EventSource reconnects to the same URL and sends the last id it saw.
        Without ids, the replay counted every finished file twice in the UI."""
        self.start_server()
        d = self.tmp / "one"
        d.mkdir()
        self.make_fake_apk(d / "a.apk")
        _, body = self.post("/api/runs", {"input": str(d)})
        url = f"{self.base}/api/runs/{body['run_id']}/events"

        def read(req):
            got = []
            with urllib.request.urlopen(req, timeout=180) as r:
                ev_id = None
                for raw in r:
                    line = raw.decode("utf-8", "replace").strip()
                    if line.startswith("id: "):
                        ev_id = int(line[4:])
                    elif line.startswith("data: "):
                        got.append((ev_id, json.loads(line[6:]).get("stage")))
                    elif line.startswith("event: end"):
                        break
            return got

        first = read(url)
        ids = [i for i, _ in first]
        self.assertEqual(ids, list(range(len(first))), "ids must be positions")
        self.assertIn("run_finished", [s for _, s in first])

        req = urllib.request.Request(url, headers={"Last-Event-ID": str(ids[1])})
        self.assertEqual(read(req), first[2:])

    def test_events_for_an_unknown_run_are_404(self):
        self.start_server()
        self.expect_status("/api/runs/12345/events", 404)


if __name__ == "__main__":
    unittest.main()
