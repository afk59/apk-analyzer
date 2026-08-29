"""End-to-end user situations, and the edge cases that have actually bitten.

Everything here is a shape someone can put the app into: a non-ASCII filename, a
folder of mixed junk, two runs at once, a report opened twice, an index deleted
mid-session. These are cheap to get wrong and expensive to notice.
"""

import json
import os
import subprocess
import sys
import threading
import time
import unittest
from pathlib import Path

from tests.support import IsolatedTest


class TestNonAsciiInputs(IsolatedTest):
    """The failure that cost v1 eleven apps in one run.

    Its console summary raised UnicodeEncodeError on a CJK app name whenever
    stdout was a pipe, and the per-file handler swallowed the whole app. In v2
    stdout is ALWAYS a pipe, so this is not an edge case -- it is the norm.
    """

    def test_the_worker_protocol_survives_cjk_and_turkish_paths(self):
        from app import worker
        for name in ("智方便.apk", "香港地鐵.apk", "şişli-güncelleme.apk",
                     "приложение.apk", "日本語アプリ.apk"):
            p = self.config.INPUT_DIR / name
            p.write_bytes(b"not a real apk")
            proc = subprocess.run(
                [sys.executable, "-u", "-m", "app.worker", str(p)],
                cwd=str(self.config.ROOT), capture_output=True, text=True,
                encoding="utf-8", errors="replace", timeout=300,
                env={**dict(os.environ),
                     "MA_RESULT_DIR": str(self.config.RESULT_DIR),
                     "MA_INPUT_DIR": str(self.config.INPUT_DIR),
                     # Deliberately NOT setting PYTHONIOENCODING: the worker has
                     # to force UTF-8 itself, because nothing guarantees the
                     # parent sets it.
                     })
            events = []
            for line in proc.stdout.splitlines():
                try:
                    events.append(json.loads(line))
                except ValueError:
                    self.fail(f"{name}: non-protocol line {line[:120]!r}")
            self.assertTrue(events, f"{name}: no events at all")
            self.assertEqual(events[-1]["stage"], "error", name)
            # The failure must be the CORRUPT FILE, never an encoding error.
            self.assertNotIn("UnicodeEncodeError", json.dumps(events), name)

    def test_resolve_mode_keeps_a_non_ascii_stem(self):
        from app import worker
        p = self.config.INPUT_DIR / "智方便.apk"
        p.write_bytes(b"x")
        mode, target, stem = worker.resolve_mode(p, "hmos")
        self.assertEqual(stem, "智方便")

    def test_the_index_round_trips_non_ascii_names(self):
        from app.store import index
        self.make_report("智方便")
        self.make_agent_json("智方便", package="hk.gov.ogcio.iamsmart", app_name="智方便")
        index.rescan()
        app = index.library()["runs"][0]["apps"][0]
        self.assertEqual(app["app_name"], "智方便")


class TestMessyFolders(IsolatedTest):
    """What a real input folder looks like when nobody tidied it."""

    def _inputs(self, folder):
        from app.api.routes import _inputs_for
        return _inputs_for(folder)

    def test_ignores_everything_that_is_not_an_input(self):
        d = self.tmp / "messy"
        d.mkdir()
        for junk in ("notes.txt", "screenshot.png", "report.html",
                     "batch_summary.xlsx", ".DS_Store", "archive.zip"):
            (d / junk).write_bytes(b"x")
        self.make_fake_apk(d / "real.apk")
        files, label = self._inputs(d)
        self.assertEqual([p.name for p in files], ["real.apk"])

    def test_a_folder_with_only_junk_yields_nothing(self):
        d = self.tmp / "junk"
        d.mkdir()
        (d / "readme.md").write_bytes(b"x")
        files, _ = self._inputs(d)
        self.assertEqual(files, [])

    def test_subfolders_are_not_recursed_into(self):
        """Matching the CLI: run_batch globs one level. Recursing would silently
        analyse a whole tree someone did not mean to hand over."""
        d = self.tmp / "outer"
        (d / "inner").mkdir(parents=True)
        self.make_fake_apk(d / "top.apk")
        self.make_fake_apk(d / "inner" / "deep.apk")
        files, _ = self._inputs(d)
        self.assertEqual([p.name for p in files], ["top.apk"])

    def test_mixed_apk_and_binaries_is_treated_as_a_batch(self):
        # exe_folder mode is only for a folder that is ONLY binaries.
        d = self.tmp / "mixed"
        d.mkdir()
        self.make_fake_apk(d / "a.apk")
        (d / "tool.exe").write_bytes(b"MZ")
        files, label = self._inputs(d)
        self.assertEqual(len(files), 2)
        self.assertNotIn("(folder)", label)

    def test_a_single_file_path_is_itself(self):
        p = self.make_fake_apk(self.config.INPUT_DIR / "one.apk")
        files, label = self._inputs(p)
        self.assertEqual(files, [p])
        self.assertEqual(label, "one.apk")


class TestConcurrentRuns(IsolatedTest):
    """Two runs at once: the queues must not share state."""

    def setUp(self):
        super().setUp()
        from app.services import jobs
        self.jobs = jobs
        self.runner = jobs.JobRunner()
        script = self.tmp / "stub.py"
        script.write_text(
            "import json,sys,time\n"
            "time.sleep(0.4)\n"
            "print(json.dumps({'stage':'done','result':"
            "{'source_file': sys.argv[1].replace('\\\\','/').split('/')[-1],"
            " 'mode':'apk','kit_count':1}}))\n", encoding="utf-8")
        self.script = script

        def run_one(run, path, index):
            proc = subprocess.Popen(
                [sys.executable, "-u", str(script), str(path)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                encoding="utf-8", errors="replace")
            out, _ = proc.communicate(timeout=60)
            for line in out.splitlines():
                try:
                    ev = json.loads(line)
                except ValueError:
                    continue
                ev["index"], ev["file"] = index, path.name
                if ev.get("stage") == "done":
                    run.results.append(ev["result"])
                run.push(ev)
        self.runner._run_one = run_one

    def _files(self, prefix, n):
        out = []
        for i in range(n):
            p = self.config.INPUT_DIR / f"{prefix}{i}.apk"
            p.write_bytes(b"x")
            out.append(p)
        return out

    def test_two_runs_keep_separate_results_and_events(self):
        a = self.runner.submit(self._files("a", 3), "hmos")
        b = self.runner.submit(self._files("b", 3), "hmos")
        self.assertNotEqual(a, b)
        deadline = time.monotonic() + 90
        while time.monotonic() < deadline:
            if all(self.runner.get(i).status != "running" for i in (a, b)):
                break
            time.sleep(0.1)
        ra, rb = self.runner.get(a), self.runner.get(b)
        self.assertEqual(ra.status, "done")
        self.assertEqual(rb.status, "done")
        self.assertEqual({r["source_file"] for r in ra.results},
                         {"a0.apk", "a1.apk", "a2.apk"})
        self.assertEqual({r["source_file"] for r in rb.results},
                         {"b0.apk", "b1.apk", "b2.apk"})
        for run, prefix in ((ra, "a"), (rb, "b")):
            files = {e["file"] for e in run.events if e.get("file")}
            self.assertTrue(all(f.startswith(prefix) for f in files),
                            f"run {run.id} saw another run's files: {files}")

    def test_cancelling_one_run_leaves_the_other_alone(self):
        a = self.runner.submit(self._files("x", 6), "hmos")
        b = self.runner.submit(self._files("y", 2), "hmos")
        time.sleep(0.2)
        self.runner.cancel(a)
        deadline = time.monotonic() + 90
        while time.monotonic() < deadline:
            if all(self.runner.get(i).status != "running" for i in (a, b)):
                break
            time.sleep(0.1)
        self.assertEqual(self.runner.get(a).status, "cancelled")
        self.assertEqual(self.runner.get(b).status, "done")


class TestLibraryLifecycle(IsolatedTest):
    """What happens across sessions, deletions and repeats."""

    def test_reanalysing_replaces_rather_than_duplicates(self):
        from app.store import index
        report = self.make_report("dup")
        self.make_agent_json("dup", package="com.dup")
        for run_id, stamp in ((1, "2026-08-30T01:00:00"), (2, "2026-08-30T02:00:00")):
            index.write_manifest({
                "id": run_id, "status": "done", "target": "hmos", "input": f"run{run_id}",
                "started_at": stamp, "file_count": 1,
                "results": [{"source_file": "dup.apk", "report": str(report)}],
                "failures": []})
        index.rescan()
        lib = index.library()
        # The same report claimed by two manifests appears under both runs; what
        # must NOT happen is it also showing up as an orphan.
        self.assertEqual([r["input_path"] for r in lib["runs"]], ["run2", "run1"])
        self.assertNotIn("Unfiled", [r["input_path"] for r in lib["runs"]])

    def test_deleting_a_report_removes_it_on_the_next_rescan(self):
        from app.store import index
        r1 = self.make_report("keep")
        self.make_agent_json("keep")
        r2 = self.make_report("gone")
        self.make_agent_json("gone")
        index.rescan()
        self.assertEqual(len(index.library()["runs"][0]["apps"]), 2)
        r2.unlink()
        index.rescan()
        names = [a["source_file"] for a in index.library()["runs"][0]["apps"]]
        self.assertEqual(names, ["keep_apk_hmos"])

    def test_an_empty_result_folder_after_a_wipe_is_not_an_error(self):
        from app.store import index
        self.make_report("x")
        index.rescan()
        for p in self.config.RESULT_DIR.glob("*_report.html"):
            p.unlink()
        counts = index.rescan()
        self.assertEqual(counts["apps"], 0)
        self.assertEqual(index.library()["runs"], [])

    def test_hms_and_hmos_reports_for_one_app_coexist(self):
        from app.store import index
        self.make_report("both", target="hmos")
        self.make_agent_json("both", target="hmos", package="com.both")
        self.make_report("both", target="hms")
        self.make_agent_json("both", target="hms", package="com.both")
        index.rescan()
        names = sorted(a["source_file"] for a in index.library()["runs"][0]["apps"])
        self.assertEqual(names, ["both_apk_hmos", "both_apk_hms"])


class TestMappingDataIntegrity(IsolatedTest):
    """The mapping files are the product. These guard their shape."""

    def _mapping(self):
        return json.loads((self.config.MAPPINGS_DIR / "mapping.json").read_text(encoding="utf-8"))

    def test_no_duplicate_namespace_patterns(self):
        rows = self._mapping()["namespace_mappings"]
        seen = [e["android_namespace"] for e in rows]
        dupes = {n for n in seen if seen.count(n) > 1}
        self.assertEqual(dupes, set(), f"duplicate patterns: {dupes}")

    def test_no_duplicate_permission_entries(self):
        rows = self._mapping()["permission_mappings"]
        seen = [e["android"] for e in rows]
        dupes = {n for n in seen if seen.count(n) > 1}
        self.assertEqual(dupes, set(), f"duplicate permissions: {dupes}")

    def test_every_row_has_the_required_fields(self):
        for e in self._mapping()["namespace_mappings"]:
            for key in ("android_namespace", "android_display", "harmony_kit",
                        "confidence", "note"):
                self.assertIn(key, e, e.get("android_namespace"))
            self.assertIn(e["confidence"], ("high", "medium", "low", None),
                          e["android_namespace"])

    def test_every_kit_token_resolves_to_documentation(self):
        """A row whose kit has no doc URL renders without an Official Docs link."""
        sys.path.insert(0, str(self.config.ENGINE_DIR))
        from core.mapping import KIT_DOC_URLS
        kits = {e["harmony_kit"] for e in self._mapping()["namespace_mappings"]
                if e["harmony_kit"] and e["harmony_kit"].startswith("@kit.")}
        missing = sorted(k for k in kits if k not in KIT_DOC_URLS)
        self.assertEqual(missing, [], f"no doc URL for: {missing}")

    def test_every_suggested_permission_actually_exists(self):
        """The engine must not recommend a permission nobody can grant.

        Attested against the three sources: the curated permission lists, the
        crawled documentation, and the SDK's .d.ts @permission annotations.
        """
        import re
        names = set()
        for f in (self.config.ENGINE_DIR / "data" / "permissions").glob("*.txt"):
            names |= set(re.findall(r"ohos\.permission\.[A-Z_0-9]+",
                                    f.read_text(encoding="utf-8")))
        dts = self.config.DOCS_REF_DIR / "ArkTS-Harmonyos-apis-and-kits"
        if dts.is_dir():
            for p in dts.rglob("*.d.ts"):
                names |= set(re.findall(r"ohos\.permission\.[A-Z_0-9]+",
                                        p.read_text(encoding="utf-8", errors="ignore")))
        if len(names) < 100:
            self.skipTest("permission sources unavailable in this checkout")

        src = (self.config.ENGINE_DIR / "core" / "apk_engine.py").read_text(encoding="utf-8")
        catalogue = re.findall(r"ohos\.permission\.[A-Z_0-9]+",
                               src.split("_OHOS_PERM_CATALOGUE = [")[1].split("]")[0])
        bogus = sorted({p for p in catalogue if p not in names})
        self.assertEqual(bogus, [], f"suggester offers non-existent permissions: {bogus}")

        targets = {e["harmony"] for e in self._mapping()["permission_mappings"]
                   if e.get("harmony", "").startswith("ohos.permission.")}
        bad = sorted(t for t in targets if t not in names)
        self.assertEqual(bad, [], f"mapping targets that do not exist: {bad}")


if __name__ == "__main__":
    unittest.main()
