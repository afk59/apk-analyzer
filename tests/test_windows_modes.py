"""EXE and EXE-folder analysis, using real Windows binaries.

These modes reach the app through the same picker and the same queue as an APK,
but nothing was exercising them: the mode classifier had unit tests and the
engine had none. PE parsing is fast, so a real end-to-end run costs a second or
two rather than the minute an APK costs.

Skipped off Windows, and skipped if the system binaries are not readable.
"""

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

from tests.support import IsolatedTest

_SYS32 = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32"
_SAMPLES = [_SYS32 / n for n in ("notepad.exe", "version.dll", "shell32.dll")]
_AVAILABLE = sys.platform == "win32" and all(p.is_file() for p in _SAMPLES)

requires_pe = unittest.skipUnless(_AVAILABLE, "no readable Windows PE samples")


@requires_pe
class TestWindowsAnalysis(IsolatedTest):

    def run_worker(self, target_path, timeout=600):
        env = {**dict(os.environ),
               "MA_RESULT_DIR": str(self.config.RESULT_DIR),
               "MA_DB_PATH": str(self.config.DB_PATH),
               "MA_INPUT_DIR": str(self.config.INPUT_DIR),
               "PYTHONIOENCODING": "utf-8"}
        proc = subprocess.run(
            [sys.executable, "-u", "-m", "app.worker", str(target_path)],
            cwd=str(self.config.ROOT), capture_output=True, text=True,
            encoding="utf-8", errors="replace", env=env, timeout=timeout)
        events = []
        for line in proc.stdout.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                self.fail(f"non-protocol line: {line[:200]!r}")
        return proc, events

    def test_a_single_exe_produces_a_report(self):
        exe = self.config.INPUT_DIR / "notepad.exe"
        exe.write_bytes((_SYS32 / "notepad.exe").read_bytes())
        proc, events = self.run_worker(exe)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        row = events[-1]["result"]
        self.assertEqual(row["mode"], "exe")
        self.assertEqual(row["target"], "hmos", "EXE has no HMS target to choose")
        self.assertTrue(Path(row["report"]).exists())
        self.assertTrue(Path(row["xlsx"]).exists())
        # No side-car and no coverage: both are APK concepts.
        self.assertIsNone(row.get("sidecar"))
        self.assertNotIn("coverage_status", row)

    def test_a_dll_is_analysed_the_same_way(self):
        dll = self.config.INPUT_DIR / "version.dll"
        dll.write_bytes((_SYS32 / "version.dll").read_bytes())
        proc, events = self.run_worker(dll)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        self.assertEqual(events[-1]["result"]["mode"], "exe")

    def test_a_folder_of_binaries_is_one_application(self):
        """exe_folder merges the imports of every binary into a single report --
        the engine's decision, and the reason the API must not re-make it."""
        folder = self.config.INPUT_DIR / "myapp"
        folder.mkdir(parents=True, exist_ok=True)
        for src in (_SYS32 / "notepad.exe", _SYS32 / "version.dll"):
            (folder / src.name).write_bytes(src.read_bytes())
        proc, events = self.run_worker(folder)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        row = events[-1]["result"]
        self.assertEqual(row["mode"], "exe_folder")
        report = Path(row["report"])
        self.assertTrue(report.exists())
        # The folder's FULL name is the stem, dots included.
        self.assertIn("myapp_exe_folder_hmos_report.html", report.name)

    def test_the_exe_stage_sequence_is_the_engine_s_own(self):
        exe = self.config.INPUT_DIR / "notepad2.exe"
        exe.write_bytes((_SYS32 / "notepad.exe").read_bytes())
        _, events = self.run_worker(exe)
        stages = [e["stage"] for e in events if e.get("stage")]
        self.assertIn("loading", stages)
        self.assertIn("imports", stages, "the import-table phase was not reported")
        self.assertIn("kits", stages)
        # DEX phases belong to APKs and must never appear here.
        self.assertNotIn("dex", stages)
        self.assertNotIn("scan", stages)
        self.assertEqual(stages[-1], "done")

    def test_a_windows_report_lands_in_the_library(self):
        exe = self.config.INPUT_DIR / "notepad3.exe"
        exe.write_bytes((_SYS32 / "notepad.exe").read_bytes())
        self.run_worker(exe)
        from app.store import index
        index.rescan()
        apps = index.library()["runs"][0]["apps"]
        self.assertEqual(len(apps), 1)
        self.assertIn("exe", apps[0]["source_file"])
        # An EXE has no coverage; the library must not invent one.
        self.assertIsNone(apps[0]["coverage_pct"])

    def test_a_file_that_is_not_a_pe_explains_itself(self):
        """The engine calls sys.exit(1) here after printing the reason, and
        SystemExit is a BaseException that `except Exception` does not catch --
        so this used to exit 1 with no error event and the UI showed
        "worker exited 1" instead of what the engine actually said."""
        fake = self.config.INPUT_DIR / "broken.exe"
        fake.write_bytes(b"this is not a PE file at all")
        proc, events = self.run_worker(fake, timeout=300)
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(events[-1]["stage"], "error")
        self.assertIn("PE file", events[-1]["error"],
                      "the failure must carry the engine's own explanation")


if __name__ == "__main__":
    unittest.main()
