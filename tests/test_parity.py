"""The worker's artifacts must match what the v1 CLI produces.

This is M2's acceptance criterion made permanent. If it ever fails, the UI has
started doing the engine's job -- the single failure mode decisions/0003 exists
to prevent, and the closest thing this project has to a regression net over
7,100 lines of untested engine code.

WHY THIS ONE TEST TOUCHES THE REAL OUTPUT FOLDER
Everything else redirects through MA_RESULT_DIR. The ENGINE cannot: it is
frozen v1 code that resolves `script_dir / "result"` from its own file location
and knows nothing about the environment. `--output` moves the HTML but the agent
JSON still lands in engine/result/agent_outputs. So comparing against the CLI
means letting both sides write there -- and this file therefore backs up
anything it would overwrite and restores it afterwards, including on failure.

Slow: it analyses a real APK several times. Set MA_SKIP_SLOW=1 to skip.
"""

import hashlib
import os
import re
import shutil
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

from tests.support import IsolatedTest, ROOT, SAMPLE_APK, requires_apk

skip_slow = unittest.skipIf(os.environ.get("MA_SKIP_SLOW") == "1", "MA_SKIP_SLOW=1")

ENGINE_RESULT = ROOT / "engine" / "result"

# Values that are genuinely a measurement or a clock, so they differ between any
# two runs. v1 scrubs exactly these before comparing, for the same reason.
_VOLATILE = re.compile(
    r'\d+\.\d+s'
    r'|"generated_at":\s*"[^"]*"'
    r'|"analysis_time_sec":\s*[0-9.]+'
    r'|\d{4}-\d\d-\d\d[ T][\d:]+')


def digest(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    return hashlib.sha256(_VOLATILE.sub("X", text).encode()).hexdigest()


def xlsx_parts(path: Path) -> dict:
    with zipfile.ZipFile(path) as z:
        return {n: hashlib.sha256(z.read(n)).hexdigest() for n in sorted(z.namelist())}


class ParityTest(IsolatedTest):
    """Runs both sides in engine/result/, protecting whatever was already there."""

    def setUp(self):
        super().setUp()
        stem = SAMPLE_APK.stem if SAMPLE_APK else "none"
        self.html = ENGINE_RESULT / f"{stem}_apk_hmos_report.html"
        self.xlsx = self.html.with_suffix(".xlsx")
        self.agent = ENGINE_RESULT / "agent_outputs" / f"{stem}_apk_hmos_agent.json"
        self.sidecar = ENGINE_RESULT / ".sidecars" / f"{stem}_hmos.json"
        self.targets = [self.html, self.xlsx, self.agent, self.sidecar]

        # Back up only what exists; anything we create is removed at the end.
        self.backups = {}
        for p in self.targets:
            if p.exists():
                keep = self.tmp / ("backup_" + p.name)
                shutil.copy2(p, keep)
                self.backups[p] = keep

        # The engine ignores MA_*, so do NOT redirect here -- that would split
        # the two sides across two folders and compare nothing.
        self.env = {**dict(os.environ), "PYTHONIOENCODING": "utf-8"}
        self.env.pop("MA_RESULT_DIR", None)
        self.env.pop("MA_INPUT_DIR", None)
        self.env["MA_DB_PATH"] = str(self.config.DB_PATH)

    def tearDown(self):
        for p in self.targets:
            try:
                if p in self.backups:
                    shutil.copy2(self.backups[p], p)
                elif p.exists():
                    p.unlink()
            except OSError:
                pass
        super().tearDown()

    def _clear(self):
        for p in self.targets:
            if p.exists():
                p.unlink()

    def run_cli(self):
        self._clear()
        proc = subprocess.run(
            [sys.executable, "engine/analyzer.py", str(SAMPLE_APK), "--no-open", "--excel"],
            cwd=str(ROOT), capture_output=True, text=True,
            encoding="utf-8", errors="replace", env=self.env, timeout=1800)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        self.assertTrue(self.html.exists() and self.agent.exists(),
                        "the CLI did not write where this test expects")

    def run_worker(self):
        self._clear()
        proc = subprocess.run(
            [sys.executable, "-u", "-m", "app.worker", str(SAMPLE_APK), "--target", "hmos"],
            cwd=str(ROOT), capture_output=True, text=True,
            encoding="utf-8", errors="replace", env=self.env, timeout=1800)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])


@requires_apk
@skip_slow
class TestWorkerMatchesCli(ParityTest):

    def test_report_and_agent_json_are_identical(self):
        self.run_cli()
        cli = (digest(self.html), digest(self.agent))
        self.run_worker()
        worker = (digest(self.html), digest(self.agent))
        self.assertEqual(cli[0], worker[0],
                         "the UI is no longer producing the engine's report")
        self.assertEqual(cli[1], worker[1], "agent JSON diverged")

    def test_the_workbook_differs_only_in_timestamps(self):
        """openpyxl stamps a creation time and the Overview sheet carries the
        measured analysis time. Nothing else may differ."""
        self.run_cli()
        cli = xlsx_parts(self.xlsx)
        self.run_worker()
        worker = xlsx_parts(self.xlsx)
        self.assertEqual(set(cli), set(worker), "different sheets or parts")
        differing = {n for n in cli if cli[n] != worker[n]}
        self.assertLessEqual(
            differing, {"docProps/core.xml", "xl/worksheets/sheet1.xml"},
            f"unexpected differences: {sorted(differing)}")

    def test_only_the_worker_writes_a_sidecar(self):
        """The side-car is v2's addition. The CLI must not grow one, and the
        worker must produce one or the batch workbooks lose that app."""
        self.run_cli()
        self.assertFalse(self.sidecar.exists())
        self.run_worker()
        self.assertTrue(self.sidecar.exists())


@requires_apk
@skip_slow
class TestEngineIsDeterministic(ParityTest):
    """v1 spent two commits making reports reproducible. This keeps them so."""

    def test_two_worker_runs_of_the_same_apk_agree(self):
        seen = []
        for _ in range(2):
            self.run_worker()
            seen.append((digest(self.html), digest(self.agent)))
        self.assertEqual(seen[0], seen[1],
                         "the same APK produced two different reports")


if __name__ == "__main__":
    unittest.main()
