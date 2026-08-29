"""config: path resolution and the /api/open guard.

is_inside_result is the only thing standing between a crafted request and
os.startfile on an arbitrary path, so it gets the most cases here.
"""

import os
import unittest
from pathlib import Path

from tests.support import IsolatedTest, ROOT


class TestPaths(IsolatedTest):

    def test_root_is_the_repo(self):
        self.assertTrue((self.config.ROOT / "app").is_dir())
        self.assertTrue((self.config.ENGINE_DIR / "analyzer.py").is_file())

    def test_engine_paths_are_not_redirectable(self):
        # Redirecting these would mean testing something other than this app.
        self.assertEqual(self.config.ENGINE_DIR, ROOT / "engine")
        self.assertEqual(self.config.WEB_DIR, ROOT / "app" / "web")

    def test_data_paths_follow_the_environment(self):
        self.assertTrue(str(self.config.RESULT_DIR).startswith(str(self.tmp)))
        self.assertTrue(str(self.config.DB_PATH).startswith(str(self.tmp)))
        self.assertTrue(str(self.config.INPUT_DIR).startswith(str(self.tmp)))

    def test_agent_dir_is_under_result(self):
        self.assertEqual(self.config.AGENT_DIR.parent, self.config.RESULT_DIR)

    def test_ensure_dirs_is_idempotent(self):
        self.config.ensure_dirs()
        self.config.ensure_dirs()
        for d in (self.config.INPUT_DIR, self.config.RESULT_DIR, self.config.AGENT_DIR):
            self.assertTrue(d.is_dir())

    def test_mappings_are_where_the_engine_expects(self):
        self.assertTrue((self.config.MAPPINGS_DIR / "mapping.json").is_file())
        self.assertTrue((self.config.MAPPINGS_DIR / "ohpm_mapping.json").is_file())


class TestRelToRoot(IsolatedTest):

    def test_inside_the_repo_is_relative_and_posix(self):
        got = self.config.rel_to_root(ROOT / "app" / "web" / "index.html")
        self.assertEqual(got, "app/web/index.html")
        self.assertNotIn("\\", got)

    def test_outside_the_repo_stays_absolute(self):
        outside = self.tmp / "elsewhere.txt"
        self.assertEqual(self.config.rel_to_root(outside), str(outside))

    def test_accepts_a_string(self):
        self.assertEqual(self.config.rel_to_root(str(ROOT / "run.bat")), "run.bat")


class TestOpenGuard(IsolatedTest):
    """The guard resolves before comparing. A prefix test would let '..' pass."""

    def test_accepts_a_file_inside_result(self):
        p = self.config.RESULT_DIR / "a_report.html"
        p.write_text("x", encoding="utf-8")
        self.assertTrue(self.config.is_inside_result(p))

    def test_accepts_a_nested_file(self):
        p = self.config.AGENT_DIR / "x_agent.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("{}", encoding="utf-8")
        self.assertTrue(self.config.is_inside_result(p))

    def test_rejects_traversal_out_of_result(self):
        crafted = self.config.RESULT_DIR / ".." / ".." / "etc" / "passwd"
        self.assertFalse(self.config.is_inside_result(crafted))

    def test_rejects_a_path_outside(self):
        self.assertFalse(self.config.is_inside_result(Path("C:/Windows/notepad.exe")))
        self.assertFalse(self.config.is_inside_result(Path("/etc/hosts")))

    def test_rejects_the_result_dir_itself(self):
        # Opening the directory is not a report; only things INSIDE it qualify.
        self.assertFalse(self.config.is_inside_result(self.config.RESULT_DIR))

    def test_rejects_a_sibling_with_a_shared_prefix(self):
        # "result-backup" starts with "result" -- a string prefix check would
        # wrongly accept it. Path.parents comparison does not.
        sibling = self.config.RESULT_DIR.parent / (self.config.RESULT_DIR.name + "-backup")
        sibling.mkdir(parents=True, exist_ok=True)
        victim = sibling / "x.html"
        victim.write_text("x", encoding="utf-8")
        self.assertFalse(self.config.is_inside_result(victim))

    def test_does_not_raise_on_a_nonexistent_path(self):
        self.assertIsInstance(
            self.config.is_inside_result(self.config.RESULT_DIR / "nope.html"), bool)

    @unittest.skipUnless(os.name == "nt", "windows path forms")
    def test_rejects_a_windows_device_path(self):
        self.assertFalse(self.config.is_inside_result(Path(r"\\.\PhysicalDrive0")))


if __name__ == "__main__":
    unittest.main()
