"""worker: input classification, the protocol, and one real analysis.

Getting the mode or the stem wrong does not crash -- it silently writes the
report under a name nobody looks for, and then skip_existing skips the wrong
file. So classification gets exhaustive cheap tests, and the expensive
end-to-end case runs once against a real APK.
"""

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

from tests.support import IsolatedTest, SAMPLE_APK, requires_apk


class TestModeResolution(IsolatedTest):

    def resolve(self, name, target="hmos", directory=False):
        from app import worker
        p = self.tmp / name
        if directory:
            p.mkdir(parents=True, exist_ok=True)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"x")
        return worker.resolve_mode(p, target)

    def test_apk(self):
        self.assertEqual(self.resolve("a.apk"), ("apk", "hmos", "a"))

    def test_apk_keeps_the_hms_target(self):
        self.assertEqual(self.resolve("a.apk", "hms"), ("apk", "hms", "a"))

    def test_ipa_is_forced_to_hmos(self):
        """HMS is an Android concept. An IPA has no HMS target to choose."""
        self.assertEqual(self.resolve("a.ipa", "hms"), ("ipa", "hmos", "a"))

    def test_exe_and_dll_are_forced_to_hmos(self):
        self.assertEqual(self.resolve("a.exe", "hms"), ("exe", "hmos", "a"))
        self.assertEqual(self.resolve("a.dll", "hms"), ("exe", "hmos", "a"))

    def test_a_directory_is_exe_folder_and_keeps_its_full_name(self):
        mode, target, stem = self.resolve("myapp.v2", directory=True)
        self.assertEqual((mode, target), ("exe_folder", "hmos"))
        self.assertEqual(stem, "myapp.v2", "a folder's stem must not lose a dotted suffix")

    def test_extension_case_does_not_matter(self):
        self.assertEqual(self.resolve("A.APK")[0], "apk")
        self.assertEqual(self.resolve("A.IPA")[0], "ipa")
        self.assertEqual(self.resolve("A.DLL")[0], "exe")

    def test_an_unknown_extension_falls_back_to_apk(self):
        # The engine will reject it honestly; guessing another mode would be
        # worse than trying the default and reporting the real failure.
        self.assertEqual(self.resolve("mystery.bin")[0], "apk")

    def test_a_dotted_filename_keeps_its_package_style_stem(self):
        self.assertEqual(self.resolve("com.example.app.apk")[2], "com.example.app")


class TestStageClassification(IsolatedTest):

    def test_engine_phrases_map_to_stages(self):
        from app import worker
        cases = {
            "Loading APK: com.x.apk": "loading",
            "Loading EXE: a.exe": "loading",
            "Loading IPA: a.ipa": "loading",
            "Loading folder: pcapp": "loading",
            "Analyzing DEX bytecode...": "dex",
            "Scanning method references...": "scan",
            "Parsing import table...": "imports",
            "Matching HarmonyOS APIs...": "api",
            "Matching HarmonyOS NEXT kits...": "kits",
            "Matching HMS Core kits...": "kits",
        }
        for message, expected in cases.items():
            self.assertEqual(worker._classify(message), expected, message)

    def test_an_unknown_message_is_not_forced_into_a_stage(self):
        from app import worker
        self.assertIsNone(worker._classify("Something new the engine says"))

    def test_ansi_colour_is_stripped_before_matching(self):
        from app import worker
        coloured = "\x1b[1m\x1b[38;5;45mAnalyzing DEX bytecode...\x1b[0m"
        cleaned = worker._ANSI.sub("", coloured)
        self.assertEqual(worker._classify(cleaned), "dex")


class TestSidecarShape(IsolatedTest):

    def test_carries_exactly_what_the_workbooks_need(self):
        from app import worker
        result = {
            "package_name": "com.x", "app_name": "X",
            "permissions": ["a", "b"], "total_detected_ns": 80, "total_3p_ns": 100,
            "kit_matches": [{"kit_name": "@kit.NetworkKit",
                             "android_sources": [{"android_namespace": "okhttp3"},
                                                 {"android_namespace": "retrofit2"}]}],
            "unmapped_namespaces": [{"namespace": "com.unknown", "class_count": 1,
                                     "method_count": 2, "sample_methods": ["m"]}],
            "ohpm_matches": [{"namespace": "com.airbnb.lottie", "ohpm_package": "@ohos/lottie",
                              "install_cmd": "ohpm install @ohos/lottie", "category": None,
                              "confidence": "high", "method_count": 9, "note": "dropped"}],
            "detected_namespaces": {"huge": "should not be carried"},
        }
        side = worker._sidecar(result, {"framework": "React Native"})
        self.assertEqual(side["permissions"], 2)          # a COUNT, not the list
        self.assertEqual([m["namespace"] for m in side["mapped"]], ["okhttp3", "retrofit2"])
        self.assertEqual(side["mapped"][0]["kit"], "@kit.NetworkKit")
        self.assertNotIn("detected_namespaces", side)     # the megabytes stay out
        self.assertNotIn("note", side["ohpm"][0])         # only the six fields

    def test_survives_a_result_with_nothing_in_it(self):
        from app import worker
        side = worker._sidecar({}, None)
        self.assertEqual(side["mapped"], [])
        self.assertEqual(side["unmapped"], [])
        self.assertEqual(side["permissions"], 0)


class TestWorkerProcess(IsolatedTest):
    """The worker as the JobRunner actually invokes it."""

    def run_worker(self, arg, target="hmos", timeout=600):
        env = {**dict(os.environ),
               "MA_RESULT_DIR": str(self.config.RESULT_DIR),
               "MA_DB_PATH": str(self.config.DB_PATH),
               "MA_INPUT_DIR": str(self.config.INPUT_DIR),
               "PYTHONIOENCODING": "utf-8"}
        proc = subprocess.run(
            [sys.executable, "-u", "-m", "app.worker", str(arg), "--target", target],
            cwd=str(self.config.ROOT), capture_output=True, text=True,
            encoding="utf-8", errors="replace", env=env, timeout=timeout)
        events = []
        for line in proc.stdout.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                self.fail(f"non-protocol line on stdout: {line[:200]!r}")
        return proc, events

    def test_a_missing_file_is_a_clean_error(self):
        proc, events = self.run_worker(self.tmp / "ghost.apk", timeout=120)
        self.assertEqual(proc.returncode, 2)
        self.assertEqual(events[-1]["stage"], "error")
        self.assertIn("Not found", events[-1]["error"])

    def test_a_corrupt_apk_errors_without_a_traceback_on_stdout(self):
        bad = self.config.INPUT_DIR / "bad.apk"
        bad.write_bytes(b"not a zip")
        proc, events = self.run_worker(bad, timeout=300)
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(events[-1]["stage"], "error")
        self.assertTrue(events[-1].get("traceback"), "no traceback captured for triage")

    @requires_apk
    def test_analyses_a_real_apk_and_writes_everything(self):
        proc, events = self.run_worker(SAMPLE_APK, timeout=900)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])

        stages = [e["stage"] for e in events if e.get("stage")]
        for expected in ("loading", "dex", "scan", "kits", "api", "render", "done"):
            self.assertIn(expected, stages)
        self.assertEqual(stages[-1], "done", "done must be the terminal event")

        row = events[-1]["result"]
        for key in ("source_file", "mode", "target", "package_name", "kit_count",
                    "report", "agent_json", "sidecar", "coverage_status"):
            self.assertIn(key, row)
        self.assertEqual(row["mode"], "apk")

        # Written under the REDIRECTED result dir, not the real one.
        for key in ("report", "agent_json", "sidecar"):
            p = Path(row[key])
            self.assertTrue(p.exists(), key)
            self.assertTrue(str(p).startswith(str(self.tmp)),
                            f"{key} escaped the test sandbox: {p}")
        self.assertTrue(Path(row["xlsx"]).exists())

    @requires_apk
    def test_the_hms_target_names_its_own_outputs(self):
        proc, events = self.run_worker(SAMPLE_APK, target="hms", timeout=900)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        row = events[-1]["result"]
        self.assertEqual(row["target"], "hms")
        self.assertIn("_apk_hms_report.html", row["report"])
        # HMS is Android-based, so the OHPM second tier does not apply there.
        self.assertEqual(row["ohpm_count"], 0)


if __name__ == "__main__":
    unittest.main()
