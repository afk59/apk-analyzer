"""Program-folder batches, pipelined downloads, and deleting a result.

Three features that reach the same queue from different directions:

  * A PC program folder is analysed as a BATCH -- one report per EXE/DLL, its
    subfolders included -- with the engine's merged exe_folder report still one
    option away. Program folders hold same-named binaries (X.exe beside X.dll),
    so the run must never let one report overwrite another.
  * A package list downloads on its own thread while the analysis works through
    what has already arrived.
  * A result can be deleted: files, manifest entries and index row together, so
    a rescan does not bring it back.
"""

import json
import os
import sys
import threading
import time
import unittest
from pathlib import Path

from tests import test_api
from tests.support import IsolatedTest

_SYS32 = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32"
_PE_OK = sys.platform == "win32" and all(
    (_SYS32 / n).is_file() for n in ("notepad.exe", "version.dll"))


def _touch(path: Path, data=b"MZ") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


# ====================================================================== folders
class TestProgramFolders(IsolatedTest):

    def program(self):
        d = self.tmp / "Prog"
        for rel in ("app.exe", "core.dll", "app.resources.dll",
                    "plugins/extra.dll", "plugins/deep/more.dll",
                    "tr/app.resources.dll", "readme.txt"):
            _touch(d / rel)
        return d

    def inputs(self, d, **kw):
        from app.api.routes import _inputs_for
        return _inputs_for(d, **kw)

    def test_a_program_folder_is_a_batch_through_its_subfolders(self):
        d = self.program()
        files, label, root = self.inputs(d)
        rel = [p.relative_to(d).as_posix() for p in files]
        # Top level first, then each subfolder; resource assemblies left out.
        self.assertEqual(rel, ["app.exe", "core.dll", "plugins/extra.dll",
                               "plugins/deep/more.dll"])
        self.assertEqual(root, d)
        self.assertIn("4 files", label)

    def test_subfolders_can_be_left_out(self):
        files, _, _ = self.inputs(self.program(), recursive=False)
        self.assertEqual([p.name for p in files], ["app.exe", "core.dll"])

    def test_resource_assemblies_only_when_asked_for(self):
        files, _, _ = self.inputs(self.program(), include_resources=True)
        names = [p.name for p in files]
        self.assertEqual(names.count("app.resources.dll"), 2)

    def test_combined_is_the_engines_one_report_mode(self):
        d = self.program()
        files, label, root = self.inputs(d, pc_mode="combined")
        self.assertEqual(files, [d])
        self.assertIn("(folder)", label)
        self.assertIsNone(root)

    def test_a_mixed_folder_keeps_its_flat_batch(self):
        d = self.tmp / "mixed"
        self.make_fake_apk(d / "a.apk")
        _touch(d / "tool.exe")
        _touch(d / "sub" / "deep.dll")
        files, _, root = self.inputs(d)
        self.assertEqual(sorted(p.name for p in files), ["a.apk", "tool.exe"])
        self.assertIsNone(root)

    def test_the_picker_counts_every_option(self):
        from app.api.routes import folder_info
        info = folder_info(self.program())
        self.assertEqual(info["program"], {"top": 2, "top_resources": 1,
                                           "all": 4, "all_resources": 2})

    def test_an_apk_folder_has_no_program_block(self):
        from app.api.routes import folder_info
        d = self.tmp / "apks"
        self.make_fake_apk(d / "a.apk")
        self.assertNotIn("program", folder_info(d))


# ======================================================================= naming
class TestOutputNames(IsolatedTest):

    def test_no_collision_means_no_override(self):
        from app.services.jobs import plan_names
        d = self.tmp / "p"
        paths = [_touch(d / "a.exe"), _touch(d / "b.dll")]
        labels, stems = plan_names(paths, d)
        self.assertEqual(stems, {}, "a file that collides with nothing keeps the CLI's name")
        self.assertEqual(sorted(labels.values()), ["a.exe", "b.dll"])

    def test_exe_and_dll_of_the_same_name_get_separate_reports(self):
        """Tool.exe beside Tool.dll: both map to Tool_exe_hmos_report.html."""
        from app.services.jobs import JobRunner, plan_names
        d = self.tmp / "Tool"
        paths = [_touch(d / "Tool.exe"), _touch(d / "Tool.dll"), _touch(d / "x.dll")]
        _, stems = plan_names(paths, d)
        reports = {JobRunner._report_for(p, "hmos", stems.get(str(p))).name for p in paths}
        self.assertEqual(reports, {"Tool.exe_exe_hmos_report.html",
                                   "Tool.dll_exe_hmos_report.html",
                                   "x_exe_hmos_report.html"})

    def test_same_name_in_two_subfolders(self):
        from app.services.jobs import plan_names
        d = self.tmp / "p"
        paths = [_touch(d / "x.dll"), _touch(d / "plugins" / "x.dll")]
        labels, stems = plan_names(paths, d)
        self.assertEqual(sorted(labels.values()), ["plugins/x.dll", "x.dll"])
        self.assertEqual(sorted(stems.values()), ["plugins__x.dll", "x.dll"])

    def test_collisions_are_case_insensitive(self):
        """Windows file names are: Foo.dll and foo.exe still overwrite."""
        from app.services.jobs import plan_names
        d = self.tmp / "p"
        _, stems = plan_names([_touch(d / "Foo.dll"), _touch(d / "foo.exe")], d)
        self.assertEqual(len(stems), 2)

    def test_the_worker_honours_the_override(self):
        from app.worker import resolve_mode, sidecar_name
        self.assertEqual(resolve_mode(Path("a/Tool.dll"), "hmos", "Tool.dll"),
                         ("exe", "hmos", "Tool.dll"))
        self.assertEqual(resolve_mode(Path("a/Tool.dll"), "hmos"),
                         ("exe", "hmos", "Tool"))
        # APK side-cars keep their historical name; the others carry the mode.
        self.assertEqual(sidecar_name("x", "apk", "hms"), "x_hms.json")
        self.assertEqual(sidecar_name("x", "exe", "hmos"), "x_exe_hmos.json")


# ============================================================ pipelined fetches
class TestPipelinedDownloads(IsolatedTest):
    """Downloads overlap analysis. The analysis itself stays one at a time."""

    def setUp(self):
        super().setUp()
        from app.services import downloader, jobs
        self.jobs, self.downloader = jobs, downloader
        self.runner = jobs.JobRunner()
        self.analysing = 0
        self.max_analysing = 0
        self.lock = threading.Lock()

        def fake_run_one(run, path, index):
            with self.lock:
                self.analysing += 1
                self.max_analysing = max(self.max_analysing, self.analysing)
            run.push({"stage": "file_started_stub", "file": path.name})
            time.sleep(0.6)
            with self.lock:
                self.analysing -= 1
            row = {"source_file": run.label(path), "mode": "apk", "kit_count": 1}
            run.results.append(row)
            run.push({"stage": "file_done", "index": index, "file": run.label(path),
                      "result": row})

        self.runner._run_one = fake_run_one
        self.runner._aggregate = lambda run: None

    def fake_fetch(self, delay, fail=()):
        def fetch(pkg, dest, progress=None):
            for i in range(10):
                time.sleep(delay / 10)
                if progress:
                    progress((i + 1) * 100, 1000)
            if pkg in fail:
                return self.downloader.Result(pkg, "not_found", tried=["apkpure"],
                                              error="nope")
            p = dest / f"{pkg}.apk"
            p.write_bytes(b"x")
            return self.downloader.Result(pkg, "ready", path=p, source="apkpure",
                                          version="1", size=1)
        return fetch

    def wait(self, run_id, timeout=60):
        run = self.runner.get(run_id)
        deadline = time.monotonic() + timeout
        while run.status == "running" and time.monotonic() < deadline:
            time.sleep(0.05)
        self.assertNotEqual(run.status, "running", "run did not finish")
        return run

    def test_the_first_apk_is_analysed_while_the_rest_download(self):
        self.downloader.fetch = self.fake_fetch(0.5)
        pkgs = ["com.a", "com.b", "com.c"]
        run = self.wait(self.runner.submit([], "hmos", packages=pkgs))
        stages = [(e["stage"], e.get("file")) for e in run.events]
        first_analysis = stages.index(("file_started_stub", "com.a.apk"))
        last_download = stages.index(("download_done", "com.c"))
        self.assertLess(first_analysis, last_download,
                        "analysis waited for every download to finish")
        self.assertEqual([r["source_file"] for r in run.results],
                         ["com.a.apk", "com.b.apk", "com.c.apk"])
        self.assertEqual(self.max_analysing, 1, "two analyses ran at once")
        self.assertEqual(run.status, "done")

    def test_overlap_saves_time(self):
        """3 x 0.5 s downloads and 3 x 0.6 s analyses: back to back that is
        3.3 s; overlapped, the last analysis starts right after the last
        download, so about 1.5 + 0.6 + a little scheduling."""
        self.downloader.fetch = self.fake_fetch(0.5)
        t0 = time.monotonic()
        self.wait(self.runner.submit([], "hmos", packages=["com.a", "com.b", "com.c"]))
        self.assertLess(time.monotonic() - t0, 3.0)

    def test_a_failed_download_does_not_block_the_others(self):
        self.downloader.fetch = self.fake_fetch(0.1, fail={"com.b"})
        run = self.wait(self.runner.submit([], "hmos", packages=["com.a", "com.b", "com.c"]))
        self.assertEqual([r["source_file"] for r in run.results], ["com.a.apk", "com.c.apk"])
        self.assertEqual([f["source_file"] for f in run.failures], ["com.b"])
        self.assertEqual(len(run.snapshot()["downloads"]), 3)

    def test_cancel_stops_a_download_mid_body(self):
        seen = {}

        def slow(pkg, dest, progress=None):
            try:
                for i in range(200):
                    time.sleep(0.05)
                    progress(i, 200)
            except Exception as exc:          # what the real _download does
                seen["exc"] = type(exc).__name__
                return self.downloader.Result(pkg, "failed", error="aborted")
            return self.downloader.Result(pkg, "failed", error="ran to the end")

        self.downloader.fetch = slow
        rid = self.runner.submit([], "hmos", packages=["com.slow", "com.next"])
        time.sleep(0.4)
        t0 = time.monotonic()
        self.assertTrue(self.runner.cancel(rid))
        run = self.wait(rid, timeout=20)
        self.assertLess(time.monotonic() - t0, 5, "cancel waited for the download")
        self.assertEqual(seen.get("exc"), "_Cancelled")
        self.assertEqual(run.status, "cancelled")
        self.assertEqual(run.failures, [{"source_file": "com.slow", "error": "cancelled"}])

    def test_the_snapshot_lists_the_packages(self):
        self.downloader.fetch = self.fake_fetch(0.05)
        run = self.wait(self.runner.submit([], "hmos", packages=["com.a"]))
        self.assertEqual(run.snapshot()["packages"], ["com.a"])


# ====================================================================== delete
class TestDelete(IsolatedTest):

    def analysed(self, stem, run_id=1, mode="apk", extra_results=(), failures=()):
        """A report with all its files, and a manifest that lists it."""
        from app.store import index
        report = self.make_report(stem, mode=mode)
        report.with_suffix(".xlsx").write_bytes(b"xlsx")
        self.make_agent_json(stem, mode=mode)
        side = self.config.RESULT_DIR / ".sidecars" / (
            f"{stem}_hmos.json" if mode == "apk" else f"{stem}_{mode}_hmos.json")
        side.parent.mkdir(parents=True, exist_ok=True)
        side.write_text("{}", encoding="utf-8")
        snap = {"id": run_id, "started_at": f"2026-10-0{run_id}T10:00:00",
                "finished_at": f"2026-10-0{run_id}T10:01:00", "status": "done",
                "target": "hmos", "input": f"run{run_id}", "file_count": 1,
                "results": [{"source_file": f"{stem}.apk", "mode": mode,
                             "report": str(report)}, *extra_results],
                "failures": list(failures), "downloads": []}
        mpath = index.write_manifest(snap)
        return report, side, mpath

    def test_deleting_removes_every_file_and_the_row(self):
        from app.store import index
        report, side, mpath = self.analysed("gone", extra_results=[
            {"source_file": "keep.apk", "mode": "apk",
             "report": str(self.make_report("keep"))}])
        index.rescan()
        out = index.delete_report(report)
        for f in (report, report.with_suffix(".xlsx"), side,
                  self.config.AGENT_DIR / "gone_apk_hmos_agent.json"):
            self.assertFalse(f.exists(), f.name)
        names = [a["source_file"] for r in index.library()["runs"] for a in r["apps"]]
        self.assertEqual(names, ["keep.apk"])
        self.assertEqual(out["manifests_changed"], 1)
        # And it stays gone: the manifest no longer lists it.
        index.rescan()
        names = [a["source_file"] for r in index.library()["runs"] for a in r["apps"]]
        self.assertEqual(names, ["keep.apk"])

    def test_a_run_left_empty_loses_its_manifest(self):
        from app.store import index
        report, _, mpath = self.analysed("only")
        index.delete_report(report)
        self.assertFalse(mpath.exists())
        self.assertEqual(index.library()["runs"], [])

    def test_every_run_that_lists_the_report_forgets_it(self):
        """Analysing the same input twice overwrites one report, listed by two
        manifests. Deleting it must clear both, or a rescan resurrects a row
        pointing at nothing."""
        from app.store import index
        report, _, m1 = self.analysed("twice", run_id=1)
        _, _, m2 = self.analysed("twice", run_id=2)
        index.delete_report(report)
        self.assertFalse(m1.exists())
        self.assertFalse(m2.exists())

    def test_an_unfiled_report_is_deleted_too(self):
        from app.store import index
        report = self.make_report("cli")
        index.rescan()
        self.assertEqual(len(index.library()["runs"]), 1)
        index.delete_report(report)
        self.assertEqual(index.library()["runs"], [])

    def test_an_exe_report_takes_its_own_sidecar(self):
        from app.store import index
        report, side, _ = self.analysed("tool", mode="exe")
        index.delete_report(report)
        self.assertFalse(side.exists())

    def test_deleting_a_failure(self):
        from app.store import index
        _, _, mpath = self.analysed("ok", failures=[
            {"source_file": "bad.apk", "error": "boom"}])
        index.rescan()
        out = index.delete_failure(mpath.name, "bad.apk")
        self.assertIsNotNone(out)
        snap = json.loads(mpath.read_text(encoding="utf-8"))
        self.assertEqual(snap["failures"], [])
        self.assertIsNone(index.delete_failure(mpath.name, "bad.apk"), "already gone")
        self.assertIsNone(index.delete_failure("../evil.json", "x"))

    def test_a_selection_goes_in_one_pass(self):
        """Reports from two runs and a failure, deleted together: every file
        gone, every manifest edited, one rescan -- and what was not selected
        stays."""
        from app.store import index
        a, _, m1 = self.analysed("sel_a", run_id=1, failures=[
            {"source_file": "bad.apk", "error": "boom"}])
        b, _, m2 = self.analysed("sel_b", run_id=2, extra_results=[
            {"source_file": "keep.apk", "mode": "apk",
             "report": str(self.make_report("keep"))}])
        index.rescan()
        calls = []
        real = index.rescan
        index.rescan = lambda: calls.append(1) or real()
        try:
            out = index.delete_many([a, b], [(m1.name, "bad.apk")])
        finally:
            index.rescan = real
        self.assertEqual(len(calls), 1, "one rescan for the whole selection")
        self.assertEqual((out["reports"], out["failures"]), (2, 1))
        self.assertFalse(a.exists() or b.exists())
        self.assertFalse(m1.exists(), "run 1 had nothing left")
        names = [x["source_file"] for r in index.library()["runs"] for x in r["apps"]]
        self.assertEqual(names, ["keep.apk"])

    def test_a_bad_manifest_name_in_a_selection_is_ignored(self):
        from app.store import index
        _, _, m = self.analysed("ok2", failures=[{"source_file": "x.apk", "error": "e"}])
        out = index.delete_many([], [("../evil.json", "x.apk")])
        self.assertEqual(out["failures"], 0)
        self.assertTrue(m.exists())

    def test_the_manifest_name_is_in_the_library(self):
        from app.store import index
        _, _, mpath = self.analysed("named")
        index.rescan()
        self.assertEqual(index.library()["runs"][0]["manifest"], mpath.name)


class TestDeleteEndpoint(test_api.ApiTest):

    def test_refuses_anything_outside_the_result_tree(self):
        self.start_server()
        outside = self.tmp / "elsewhere_apk_hmos_report.html"
        outside.write_text("x", encoding="utf-8")
        status, _ = self.post("/api/results/delete", {"report": str(outside)})
        self.assertEqual(status, 403)
        self.assertTrue(outside.exists())
        status, _ = self.post("/api/results/delete", {
            "report": str(self.config.RESULT_DIR / ".." / "elsewhere_apk_hmos_report.html")})
        self.assertEqual(status, 403)

    def test_refuses_a_file_that_is_not_a_report(self):
        self.start_server()
        wb = self.config.RESULT_DIR / "batch_summary.xlsx"
        wb.write_bytes(b"x")
        status, _ = self.post("/api/results/delete", {"report": str(wb)})
        self.assertEqual(status, 403)
        self.assertTrue(wb.exists())

    def test_deletes_through_the_api(self):
        self.start_server()
        report = self.make_report("api")
        self.make_agent_json("api")
        self.post("/api/rescan")
        status, body = self.post("/api/results/delete",
                                 {"report": self.config.rel_to_root(report)})
        self.assertEqual(status, 200, body)
        self.assertFalse(report.exists())
        _, lib = self.get("/api/results")
        self.assertEqual(lib["runs"], [])

    def test_a_report_that_does_not_exist_is_404_not_deleted(self):
        """Nothing deleted must not be reported as a delete."""
        self.start_server()
        ghost = self.config.RESULT_DIR / "ghost_apk_hmos_report.html"
        status, _ = self.post("/api/results/delete", {"report": str(ghost)})
        self.assertEqual(status, 404)
        status, body = self.post("/api/results/delete-many",
                                 {"items": [{"report": str(ghost)}]})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["reports"], 0)

    def test_a_listed_report_whose_file_is_gone_still_deletes(self):
        """The row exists only in a manifest: removing it IS a delete."""
        from app.store import index
        self.start_server()
        report = self.make_report("stale")
        index.write_manifest({
            "id": 1, "status": "done", "target": "hmos", "input": "x",
            "started_at": "2026-08-30T01:00:00", "file_count": 1,
            "results": [{"source_file": "stale.apk", "report": str(report)}],
            "failures": []})
        report.unlink()
        status, body = self.post("/api/results/delete", {"report": str(report)})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["reports"], 1)

    def test_a_selection_through_the_api_skips_what_it_must_refuse(self):
        self.start_server()
        r1, r2 = self.make_report("m1"), self.make_report("m2")
        outside = self.tmp / "x_apk_hmos_report.html"
        outside.write_text("x", encoding="utf-8")
        self.post("/api/rescan")
        status, body = self.post("/api/results/delete-many", {"items": [
            {"report": self.config.rel_to_root(r1)}, {"report": str(r2)},
            {"report": str(outside)}]})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["reports"], 2)
        self.assertEqual(len(body["refused"]), 1)
        self.assertFalse(r1.exists() or r2.exists())
        self.assertTrue(outside.exists(), "the refused one must be untouched")
        status, _ = self.post("/api/results/delete-many", {"items": []})
        self.assertEqual(status, 400)

    def test_needs_a_target(self):
        self.start_server()
        status, _ = self.post("/api/results/delete", {})
        self.assertEqual(status, 400)

    def test_a_program_folder_runs_as_a_batch_by_default(self):
        self.start_server()
        d = self.tmp / "pcapp"
        _touch(d / "app.exe")
        _touch(d / "core.dll")
        _touch(d / "plugins" / "p.dll")
        status, body = self.post("/api/runs", {"input": str(d)})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["file_count"], 3)
        self.assertTrue(body["skip_existing"])
        self.post(f"/api/runs/{body['run_id']}/cancel")
        status, body = self.post("/api/runs", {"input": str(d), "pc_mode": "combined"})
        self.assertEqual((status, body["file_count"]), (200, 1))
        self.post(f"/api/runs/{body['run_id']}/cancel")
        status, _ = self.post("/api/runs", {"input": str(d), "pc_mode": "nonsense"})
        self.assertEqual(status, 400)

    def test_repeated_packages_are_fetched_once(self):
        self.start_server()
        status, body = self.post("/api/downloads",
                                 {"packages": "com.a, com.b,com.a\ncom.b;com.c"})
        self.assertEqual(status, 200)
        self.assertEqual(body["packages"], ["com.a", "com.b", "com.c"])
        self.post(f"/api/runs/{body['run_id']}/cancel")


# ===================================================== real binaries, end to end
@unittest.skipUnless(_PE_OK, "no readable Windows PE samples")
class TestRealProgramFolder(IsolatedTest):
    """A program folder of real PE files through the real worker, including the
    exe/dll name clash and a subfolder."""

    def test_every_binary_gets_its_own_report_and_a_workbook_row(self):
        from app.api.routes import _inputs_for
        from app.services import jobs
        d = self.tmp / "RealProg"
        notepad = (_SYS32 / "notepad.exe").read_bytes()
        version = (_SYS32 / "version.dll").read_bytes()
        _touch(d / "notepad.exe", notepad)
        _touch(d / "notepad.dll", version)          # same stem as the exe
        _touch(d / "plugins" / "version.dll", version)
        files, label, root = _inputs_for(d)
        runner = jobs.JobRunner()
        run = runner.get(runner.submit(files, "hmos", skip_existing=True,
                                       input_label=label, root=root))
        deadline = time.monotonic() + 600
        while run.status == "running" and time.monotonic() < deadline:
            time.sleep(0.2)
        self.assertEqual(run.status, "done")
        self.assertEqual(run.failures, [])
        reports = sorted(Path(r["report"]).name for r in run.results)
        self.assertEqual(reports, ["notepad.dll_exe_hmos_report.html",
                                   "notepad.exe_exe_hmos_report.html",
                                   "version_exe_hmos_report.html"])
        self.assertEqual(sorted(r["source_file"] for r in run.results),
                         ["notepad.dll", "notepad.exe", "plugins/version.dll"])
        self.assertTrue(run.workbooks and Path(run.workbooks["batch_summary"]).exists())

        # Resume: everything is skipped and the workbook still has all three.
        run2 = runner.get(runner.submit(files, "hmos", skip_existing=True,
                                        input_label=label, root=root))
        deadline = time.monotonic() + 300
        while run2.status == "running" and time.monotonic() < deadline:
            time.sleep(0.2)
        self.assertTrue(all(r.get("skipped") for r in run2.results))
        import openpyxl
        wb = openpyxl.load_workbook(run2.workbooks["batch_summary"])
        files_col = [r[0] for r in wb.worksheets[0].iter_rows(min_row=3, values_only=True)
                     if r[0]]
        self.assertEqual(sorted(files_col),
                         ["notepad.dll", "notepad.exe", "plugins/version.dll"])


if __name__ == "__main__":
    unittest.main()
