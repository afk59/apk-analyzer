"""aggregate: rebuilding the cross-app sheets from side-cars.

The workbook writers themselves are the engine's and are not re-tested here.
What IS tested is the aggregation that replaces run_batch's in-loop
accumulation: set-based app counts, ERROR rows, missing side-cars, and the fact
that the real exporters get called with the shape they expect.
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

from tests.support import IsolatedTest


class TestAggregation(IsolatedTest):

    def _plan(self, entries):
        plan = {"entries": entries, "result_dir": str(self.config.RESULT_DIR),
                "target": "hmos"}
        p = self.tmp / "plan.json"
        p.write_text(json.dumps(plan, default=str), encoding="utf-8")
        return p

    def _row(self, name, **kw):
        row = {"source_file": name, "mode": "apk", "app_name": kw.get("app_name", name),
               "kit_count": kw.get("kits", 5), "unmapped_count": kw.get("unmapped", 2),
               "permission_count": kw.get("perms", 4),
               "report": str(self.config.RESULT_DIR / f"{Path(name).stem}_apk_hmos_report.html")}
        row.update(kw.get("extra", {}))
        return row

    def run_aggregate(self, entries):
        """Run the real module in a subprocess, as the JobRunner does."""
        plan = self._plan(entries)
        env = {**dict(__import__("os").environ),
               "MA_RESULT_DIR": str(self.config.RESULT_DIR),
               "MA_DB_PATH": str(self.config.DB_PATH),
               "MA_INPUT_DIR": str(self.config.INPUT_DIR),
               "PYTHONIOENCODING": "utf-8"}
        proc = subprocess.run(
            [sys.executable, "-u", "-m", "app.aggregate", str(plan)],
            cwd=str(self.config.ROOT), capture_output=True, text=True,
            encoding="utf-8", errors="replace", env=env, timeout=300)
        events = []
        for line in proc.stdout.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
        return proc, events

    def test_two_apps_produce_both_workbooks(self):
        for name in ("a.apk", "b.apk"):
            stem = Path(name).stem
            self.make_report(stem)
            self.make_sidecar(stem, package=f"com.{stem}")
        entries = [{"row": self._row(n),
                    "sidecar": str(self.config.RESULT_DIR / ".sidecars" / f"{Path(n).stem}_hmos.json")}
                   for n in ("a.apk", "b.apk")]
        proc, events = self.run_aggregate(entries)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        done = [e for e in events if e.get("stage") == "aggregate_done"]
        self.assertTrue(done, proc.stdout[-800:] + proc.stderr[-800:])
        self.assertEqual(done[0]["result"]["apk_apps"], 2)
        self.assertTrue((self.config.RESULT_DIR / "batch_summary.xlsx").exists())
        self.assertTrue((self.config.RESULT_DIR / "batch_unmapped.xlsx").exists())

    def test_summary_coverage_counts_ohpm_matches(self):
        """The workbook's Coverage column goes through the same coverage_status()
        as the stat card, so it must see total_ohpm_ns from the side-car."""
        import openpyxl
        for name, ohpm in (("a.apk", 10), ("b.apk", 0)):
            stem = Path(name).stem
            self.make_report(stem)
            self.make_sidecar(stem, package=f"com.{stem}", detected=80, total=100,
                              ohpm_ns=ohpm)
        entries = [{"row": self._row(n),
                    "sidecar": str(self.config.RESULT_DIR / ".sidecars" / f"{Path(n).stem}_hmos.json")}
                   for n in ("a.apk", "b.apk")]
        proc, _ = self.run_aggregate(entries)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        ws = openpyxl.load_workbook(self.config.RESULT_DIR / "batch_summary.xlsx")["Batch Summary"]
        rows = list(ws.iter_rows(values_only=True))
        hdr_i = next(i for i, r in enumerate(rows) if r and "Coverage %" in r)
        col = rows[hdr_i].index("Coverage %")
        by_app = {r[rows[hdr_i].index("File")]: r[col]
                  for r in rows[hdr_i + 1:] if r and r[col] is not None}
        self.assertEqual(by_app.get("a.apk"), 90.0)
        self.assertEqual(by_app.get("b.apk"), 80.0)

    def test_error_rows_are_included_but_contribute_nothing(self):
        for name in ("a.apk", "b.apk"):
            stem = Path(name).stem
            self.make_report(stem)
            self.make_sidecar(stem, package=f"com.{stem}")
        entries = [
            {"row": self._row("a.apk"),
             "sidecar": str(self.config.RESULT_DIR / ".sidecars" / "a_hmos.json")},
            {"row": {"source_file": "bad.apk", "mode": "error"}, "sidecar": None},
            {"row": self._row("b.apk"),
             "sidecar": str(self.config.RESULT_DIR / ".sidecars" / "b_hmos.json")},
        ]
        proc, events = self.run_aggregate(entries)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        result = [e for e in events if e.get("stage") == "aggregate_done"][0]["result"]
        self.assertEqual(result["apps"], 3)       # the failure is a row
        self.assertEqual(result["apk_apps"], 2)   # but not an analysed app

    def test_a_missing_sidecar_does_not_abort(self):
        self.make_report("a")
        self.make_sidecar("a")
        entries = [
            {"row": self._row("a.apk"),
             "sidecar": str(self.config.RESULT_DIR / ".sidecars" / "a_hmos.json")},
            {"row": self._row("gone.apk"), "sidecar": str(self.tmp / "nope.json")},
        ]
        proc, events = self.run_aggregate(entries)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        self.assertTrue([e for e in events if e.get("stage") == "aggregate_done"])

    def test_app_counts_are_distinct_apps_not_occurrences(self):
        """The Common sheets count SETS of apps. Two apps sharing a namespace is
        an App Count of 2, and the same app twice is still 1."""
        shared = [{"namespace": "com.shared.lib", "class_count": 1,
                   "method_count": 3, "sample_methods": ["m"]}]
        for name in ("a", "b"):
            self.make_report(name)
            self.make_sidecar(name, package=f"com.{name}", unmapped=shared,
                              mapped=[{"namespace": "okhttp3", "kit": "@kit.NetworkKit"}])
        entries = [{"row": self._row(f"{n}.apk"),
                    "sidecar": str(self.config.RESULT_DIR / ".sidecars" / f"{n}_hmos.json")}
                   for n in ("a", "b")]
        proc, events = self.run_aggregate(entries)
        result = [e for e in events if e.get("stage") == "aggregate_done"][0]["result"]
        self.assertEqual(result["unique_unmapped"], 1)

        from openpyxl import load_workbook
        wb = load_workbook(self.config.RESULT_DIR / "batch_summary.xlsx", read_only=True)
        rows = [tuple(r) for r in wb["Common Unmapped"].iter_rows(values_only=True)]
        wb.close()
        data = [r for r in rows if r and r[0] == "com.shared.lib"]
        self.assertTrue(data, rows)
        self.assertEqual(data[0][1], 2, "App Count should be distinct apps")

    def test_offline_metadata_does_not_stop_the_workbooks(self):
        """The guarantee Sprint 11 built, now that the fetch lives in its own
        process: no network means one warning and every other sheet intact."""
        import os
        for name in ("a", "b"):
            self.make_report(name)
            self.make_sidecar(name, package=f"com.{name}")
        entries = [{"row": self._row(f"{n}.apk"),
                    "sidecar": str(self.config.RESULT_DIR / ".sidecars" / f"{n}_hmos.json")}
                   for n in ("a", "b")]
        plan = self._plan(entries)
        env = {**dict(os.environ),
               "MA_RESULT_DIR": str(self.config.RESULT_DIR),
               "MA_DB_PATH": str(self.config.DB_PATH),
               "PYTHONIOENCODING": "utf-8",
               # Force every outbound name to fail to resolve.
               "http_proxy": "http://127.0.0.1:1", "https_proxy": "http://127.0.0.1:1"}
        proc = subprocess.run([sys.executable, "-u", "-m", "app.aggregate", str(plan)],
                              cwd=str(self.config.ROOT), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", env=env, timeout=300)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        self.assertTrue((self.config.RESULT_DIR / "batch_summary.xlsx").exists())
        self.assertTrue((self.config.RESULT_DIR / "batch_unmapped.xlsx").exists())

    def test_a_broken_plan_reports_an_error_and_exits_nonzero(self):
        p = self.tmp / "bad.json"
        p.write_text("{not json", encoding="utf-8")
        proc = subprocess.run([sys.executable, "-u", "-m", "app.aggregate", str(p)],
                              cwd=str(self.config.ROOT), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=120)
        self.assertNotEqual(proc.returncode, 0)

    def test_no_arguments_is_a_usage_error(self):
        proc = subprocess.run([sys.executable, "-u", "-m", "app.aggregate"],
                              cwd=str(self.config.ROOT), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=120)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("usage", proc.stdout.lower())


if __name__ == "__main__":
    unittest.main()
