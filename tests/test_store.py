"""store: the schema, and the invariant that the index is disposable.

The claim in docs/decisions/0002 is that deleting analyzer.db and rescanning
reproduces the library exactly. That is the property most of this file exercises,
because it is the one that stops the database quietly becoming a source of truth.
"""

import json
import sqlite3
import sys
import unittest

from tests.support import IsolatedTest


def shape(library):
    """Everything a reader would notice, in a comparable form."""
    return [
        (r["input_path"], r["status"], r["file_count"], r["skipped_count"],
         sorted((a["source_file"], a["app_name"], a["package_name"], a["kit_count"],
                 a["coverage_pct"], a["coverage_status"], a["framework"],
                 a["packer"], a["status"],
                 tuple(sorted((a["artifacts"] or {}).items())))
                for a in r["apps"]))
        for r in library["runs"]
    ]


class TestSchema(IsolatedTest):

    def test_creates_all_tables(self):
        from app.store import db
        conn = db.connect()
        names = {r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite%'")}
        conn.close()
        self.assertEqual(names, {"runs", "apps", "artifacts", "downloads"})

    def test_connect_is_idempotent(self):
        from app.store import db
        for _ in range(3):
            db.connect().close()
        conn = db.connect()
        self.assertEqual(conn.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 0)
        conn.close()

    def test_foreign_keys_cascade(self):
        from app.store import db
        conn = db.connect()
        conn.execute("INSERT INTO runs (started_at, mode, target, status, input_path)"
                     " VALUES ('t','single','hmos','done','x')")
        rid = conn.execute("SELECT id FROM runs").fetchone()[0]
        conn.execute("INSERT INTO apps (run_id, source_file, status) VALUES (?,?,?)",
                     (rid, "a.apk", "done"))
        aid = conn.execute("SELECT id FROM apps").fetchone()[0]
        conn.execute("INSERT INTO artifacts (app_id, kind, path) VALUES (?,?,?)",
                     (aid, "html", "p"))
        conn.execute("DELETE FROM runs WHERE id=?", (rid,))
        conn.commit()
        self.assertEqual(conn.execute("SELECT COUNT(*) FROM apps").fetchone()[0], 0)
        self.assertEqual(conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0], 0)
        conn.close()

    def test_a_version_mismatch_rebuilds_rather_than_alters(self):
        """The trap this guards: CREATE TABLE IF NOT EXISTS silently does nothing
        when the table exists, so a new column would be missing at runtime."""
        from app.store import db
        conn = db.connect()
        conn.execute("INSERT INTO runs (started_at, mode, target, status, input_path)"
                     " VALUES ('t','single','hmos','done','x')")
        conn.commit()
        conn.execute(f"PRAGMA user_version = {db.SCHEMA_VERSION - 1}")
        conn.commit()
        conn.close()

        conn = db.connect()                       # sees the older version
        self.assertEqual(conn.execute("SELECT COUNT(*) FROM runs").fetchone()[0], 0)
        self.assertEqual(conn.execute("PRAGMA user_version").fetchone()[0],
                         db.SCHEMA_VERSION)
        conn.close()

    def test_rel_is_the_one_in_config(self):
        from app.store import db
        self.assertIs(db.rel, self.config.rel_to_root)


class TestRescan(IsolatedTest):

    def _one_run_on_disk(self):
        report = self.make_report("com.a", detected=90, total=100)
        self.make_agent_json("com.a", package="com.a", app_name="Alpha", kits=4)
        (self.config.RESULT_DIR / "com.a_apk_hmos_report.xlsx").write_bytes(b"x")
        from app.store import index
        index.write_manifest({
            "id": 1, "status": "done", "target": "hmos", "input": "folder (2 files)",
            "started_at": "2026-08-30T01:00:00", "finished_at": "2026-08-30T01:05:00",
            "file_count": 2,
            "results": [{"source_file": "com.a.apk", "report": str(report),
                         "app_name": "Alpha", "kit_count": 4, "coverage_pct": 90.0,
                         "coverage_status": "ok", "package_name": "com.a"}],
            "failures": [{"source_file": "bad.apk", "error": "not a zip"}],
        })
        return report

    def test_empty_disk_gives_an_empty_library(self):
        from app.store import index
        counts = index.rescan()
        self.assertEqual(counts["runs"], 0)
        self.assertEqual(index.library()["runs"], [])

    def test_manifest_becomes_a_run_with_its_apps_and_failures(self):
        from app.store import index
        self._one_run_on_disk()
        counts = index.rescan()
        self.assertEqual(counts["manifests"], 1)
        self.assertEqual(counts["runs"], 1)
        self.assertEqual(counts["apps"], 2)          # one done, one failed
        run = index.library()["runs"][0]
        self.assertEqual(run["input_path"], "folder (2 files)")
        self.assertEqual(run["mode"], "batch")       # file_count > 1
        statuses = sorted(a["status"] for a in run["apps"])
        self.assertEqual(statuses, ["done", "failed"])

    def test_artifacts_are_recorded_and_resolvable(self):
        """Stored paths are repo-relative when the target is inside the repo and
        absolute otherwise (rel_to_root's documented fallback). Under test the
        result dir is a temp dir, i.e. outside -- so the contract to assert is
        that every stored path still RESOLVES, not that it is relative."""
        from app.store import index
        from pathlib import Path
        self._one_run_on_disk()
        index.rescan()
        app = [a for a in index.library()["runs"][0]["apps"] if a["status"] == "done"][0]
        self.assertEqual(set(app["artifacts"]), {"html", "xlsx", "agent_json"})
        for stored in app["artifacts"].values():
            p = Path(stored)
            resolved = p if p.is_absolute() else (self.config.ROOT / stored)
            self.assertTrue(resolved.exists(), f"unresolvable artifact path: {stored}")

    def test_paths_inside_the_repo_are_stored_relative_and_posix(self):
        # The production case: RESULT_DIR sits under the repo, so what lands in
        # the index travels with the folder.
        rel = self.config.rel_to_root(self.config.ROOT / "engine" / "result" / "x.html")
        self.assertEqual(rel, "engine/result/x.html")

    def test_a_report_with_no_manifest_is_listed_as_unfiled(self):
        from app.store import index
        self.make_report("orphan")
        self.make_agent_json("orphan", package="com.orphan", app_name="Orphan")
        counts = index.rescan()
        self.assertEqual(counts["orphans"], 1)
        run = index.library()["runs"][0]
        self.assertEqual(run["input_path"], "Unfiled")
        self.assertIsNotNone(run["started_at"])      # dated from the report's mtime

    def test_coverage_is_recovered_from_the_report_when_there_is_no_manifest(self):
        """The agent JSON carries no namespace counts. Without reading them back
        out of the report, a rebuilt index would silently lose the column."""
        from app.store import index
        self.make_report("cov", detected=873, total=1000)
        self.make_agent_json("cov")
        index.rescan()
        app = index.library()["runs"][0]["apps"][0]
        self.assertEqual(app["coverage_status"], "ok")
        self.assertAlmostEqual(app["coverage_pct"], 87.3, places=1)

    def test_coverage_counts_ohpm_matches_as_covered(self):
        """A namespace with an OHPM port has a migration path. 800 kit + 73 OHPM
        of 1000 is 87.3%, not the kit-only 80.0%."""
        from app.store import index
        self.make_report("ohpm", detected=800, total=1000, ohpm=73)
        self.make_agent_json("ohpm")
        index.rescan()
        app = index.library()["runs"][0]["apps"][0]
        self.assertEqual(app["coverage_status"], "ok")
        self.assertAlmostEqual(app["coverage_pct"], 87.3, places=1)

    def test_a_report_without_the_ohpm_count_keeps_its_published_figure(self):
        """Reports written before total_ohpm_ns existed are not re-rated."""
        if str(self.config.ENGINE_DIR) not in sys.path:
            sys.path.insert(0, str(self.config.ENGINE_DIR))
        from core.renderer import coverage_status
        self.assertEqual(coverage_status({"total_detected_ns": 800, "total_3p_ns": 1000}),
                         (80.0, "ok"))
        self.assertEqual(coverage_status({"total_detected_ns": 800, "total_3p_ns": 1000,
                                          "total_ohpm_ns": 73}), (87.3, "ok"))

    def test_a_packed_app_gets_no_percentage(self):
        from app.store import index
        fw = {"framework": "Unknown", "detail": {"packer": "SecNeo",
                                                 "note": "DEX packed, corroboration unavailable"}}
        self.make_report("packed", detected=3, total=3, framework=fw)
        self.make_agent_json("packed", framework=fw)
        index.rescan()
        app = index.library()["runs"][0]["apps"][0]
        self.assertEqual(app["coverage_status"], "packed")
        self.assertIsNone(app["coverage_pct"])
        self.assertEqual(app["packer"], "SecNeo")

    def test_a_tiny_sample_is_not_rated(self):
        from app.store import index
        self.make_report("tiny", detected=8, total=9)      # under _LOW_SAMPLE_NS
        self.make_agent_json("tiny")
        index.rescan()
        app = index.library()["runs"][0]["apps"][0]
        self.assertEqual(app["coverage_status"], "low")
        self.assertIsNone(app["coverage_pct"])

    def test_downloads_are_rebuilt_from_the_manifest(self):
        """ADR 0006: a result must trace to where its binary came from. The
        manifest carries it, so it survives deleting the database."""
        from app.store import index
        apk = self.config.INPUT_DIR / "com.a.apk"
        index.write_manifest({
            "id": 3, "status": "done", "target": "hmos", "input": "2 packages",
            "started_at": "2026-08-30T03:00:00", "file_count": 2,
            "results": [], "failures": [{"source_file": "com.b", "error": "x"}],
            "downloads": [
                {"package_name": "com.a", "source": "apkpure", "state": "ready",
                 "file_path": str(apk), "version": "1.2.3", "size": 10,
                 "requested_at": "2026-08-30T03:00:01", "error": None, "note": None},
                {"package_name": "com.b", "source": None, "state": "failed",
                 "file_path": None, "version": None, "size": None,
                 "requested_at": "2026-08-30T03:00:05", "error": "blocked", "note": None},
            ],
        })
        self.assertEqual(index.rescan()["downloads"], 2)
        [run] = index.library()["runs"]
        by_pkg = {d["package_name"]: d for d in run["downloads"]}
        self.assertEqual(by_pkg["com.a"]["source"], "apkpure")
        self.assertEqual(by_pkg["com.a"]["version"], "1.2.3")
        from app.store.db import rel
        self.assertEqual(by_pkg["com.a"]["file_path"], rel(apk))   # stored like every path
        self.assertEqual(by_pkg["com.b"]["error"], "blocked")

    def test_skipped_files_count_but_are_not_listed_twice(self):
        from app.store import index
        report = self.make_report("com.a")
        self.make_agent_json("com.a")
        index.write_manifest({
            "id": 2, "status": "done", "target": "hmos", "input": "again",
            "started_at": "2026-08-30T02:00:00", "file_count": 1,
            "results": [{"source_file": "com.a.apk", "skipped": True}],
            "failures": [],
        })
        index.rescan()
        runs = {r["input_path"]: r for r in index.library()["runs"]}
        self.assertEqual(runs["again"]["skipped_count"], 1)
        self.assertEqual(len(runs["again"]["apps"]), 0)
        # ...and the report is still visible, under the run that produced it.
        self.assertEqual(len(runs["Unfiled"]["apps"]), 1)

    def test_the_index_is_disposable(self):
        """DELETE THE DATABASE, RESCAN, GET THE SAME LIBRARY. This is the claim
        docs/decisions/0002 makes, and the reason nothing may live only here."""
        from app.store import index
        self._one_run_on_disk()
        self.make_report("orphan")
        self.make_agent_json("orphan", package="com.orphan")
        index.rescan()
        before = shape(index.library())

        self.config.DB_PATH.unlink()
        for suffix in ("-wal", "-shm"):
            side = self.config.DB_PATH.with_name(self.config.DB_PATH.name + suffix)
            if side.exists():
                side.unlink()

        index.rescan()
        self.assertEqual(before, shape(index.library()))

    def test_rescan_is_repeatable_without_duplicating(self):
        from app.store import index
        self._one_run_on_disk()
        first = index.rescan()
        second = index.rescan()
        self.assertEqual(first, second)

    def test_a_corrupt_manifest_is_skipped_not_fatal(self):
        from app.store import index
        self._one_run_on_disk()
        (index.runs_dir() / "run-broken-9.json").write_text("{not json", encoding="utf-8")
        counts = index.rescan()
        self.assertEqual(counts["runs"], 1)          # the good one survived

    def test_a_report_with_no_agent_json_still_appears(self):
        from app.store import index
        self.make_report("bare")
        index.rescan()
        app = index.library()["runs"][0]["apps"][0]
        self.assertEqual(app["source_file"], "bare_apk_hmos")
        self.assertIsNone(app["app_name"])
        self.assertEqual(set(app["artifacts"]), {"html"})

    def test_workbooks_are_reported_when_present(self):
        from app.store import index
        (self.config.RESULT_DIR / "batch_summary.xlsx").write_bytes(b"x")
        (self.config.RESULT_DIR / "batch_unmapped.xlsx").write_bytes(b"x")
        index.rescan()
        self.assertEqual(set(index.library()["workbooks"]),
                         {"batch_summary.xlsx", "batch_unmapped.xlsx"})

    def test_runs_are_newest_first(self):
        from app.store import index
        for i, stamp in enumerate(["2026-08-01T00:00:00", "2026-08-20T00:00:00"]):
            index.write_manifest({"id": i, "status": "done", "target": "hmos",
                                  "input": f"run{i}", "started_at": stamp,
                                  "file_count": 1, "results": [], "failures": []})
        index.rescan()
        order = [r["input_path"] for r in index.library()["runs"]]
        self.assertEqual(order, ["run1", "run0"])


if __name__ == "__main__":
    unittest.main()
