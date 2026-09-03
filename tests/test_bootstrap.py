"""The first-run installer in app/__main__.py.

This is the code path nobody on a working machine ever executes, which is
exactly why it needs tests: it only runs on a fresh PC, where nobody is
watching and where a mistake looks like "the app does not open".

Nothing here touches the network or pip. Every install is faked; what is being
checked is the decision-making around it.
"""

import http.server
import subprocess
import threading
import unittest
import urllib.request
from unittest import mock

from tests.support import ROOT

from app import __main__ as entry


class TestRequirementParsing(unittest.TestCase):

    def test_reads_the_uncommented_lines_of_requirements(self):
        self.assertEqual(
            [entry._requirement_name(r) for r in entry._required_packages()],
            ["androguard", "openpyxl", "pefile", "macholib",
             "fastapi", "uvicorn", "pywebview"])

    def test_the_pins_survive_parsing(self):
        """What reaches pip must still carry the version specifier. A parser
        that helpfully stripped it would turn a pinned engine into an unpinned
        one, silently, which is the exact thing the pins exist to prevent."""
        by_name = {entry._requirement_name(r): r
                   for r in entry._required_packages()}
        self.assertEqual(by_name["androguard"], "androguard==4.1.3")
        self.assertTrue(by_name["fastapi"].startswith("fastapi>="))

    def test_the_engine_packages_are_pinned_exactly(self):
        """The engine is behaviour-frozen. A minor bump in the library that
        parses the APK changes analysis output without anyone deciding to."""
        by_name = {entry._requirement_name(r): r
                   for r in entry._required_packages()}
        for pkg in ("androguard", "openpyxl", "pefile", "macholib"):
            self.assertIn("==", by_name[pkg], f"{pkg} is not pinned exactly")

    def test_the_optional_block_stays_out(self):
        """requirements.txt lists google-play-scraper and httpx in a comment.

        They are commented FOR A REASON -- each backs one additive feature and
        failing to install it is a normal offline outcome. If the parser ever
        starts returning them, an offline first run turns a working app into a
        blocked one.
        """
        names = entry._required_packages()
        self.assertNotIn("google-play-scraper", names)
        self.assertNotIn("httpx", names)

    def test_every_fatal_package_is_actually_required(self):
        names = [entry._requirement_name(r) for r in entry._required_packages()]
        for pkg in entry._FATAL:
            self.assertIn(pkg, names, f"{pkg} is fatal but nothing installs it")

    def test_no_stale_import_name_mappings(self):
        """A mapping for a package no longer in requirements.txt is dead code
        that reads like documentation. Delete it with the package."""
        names = {entry._requirement_name(r) for r in entry._required_packages()}
        for pkg in entry._IMPORT_NAME:
            self.assertIn(pkg, names, f"_IMPORT_NAME maps {pkg}, nothing needs it")

    def test_the_fallback_list_matches_requirements(self):
        self.assertEqual(list(entry._FALLBACK), entry._required_packages())

    def test_a_missing_requirements_file_does_not_crash_the_app(self):
        with mock.patch("pathlib.Path.read_text", side_effect=OSError("gone")):
            self.assertEqual(entry._required_packages(), list(entry._FALLBACK))


class TestRequirementName(unittest.TestCase):
    """Splitting `androguard==4.1.3` into what pip gets and what gets imported."""

    def test_a_plain_name_is_left_alone(self):
        self.assertEqual(entry._requirement_name("pefile"), "pefile")

    def test_an_exact_pin(self):
        self.assertEqual(entry._requirement_name("androguard==4.1.3"),
                         "androguard")

    def test_a_range(self):
        self.assertEqual(entry._requirement_name("fastapi>=0.141.1,<1.0"),
                         "fastapi")

    def test_extras_do_not_become_part_of_the_name(self):
        """Nothing uses extras today. When something does, the name must not
        quietly become "uvicorn[standard]" and stop matching _IMPORT_NAME."""
        self.assertEqual(entry._requirement_name("uvicorn[standard]>=0.30"),
                         "uvicorn")

    def test_an_environment_marker_does_not_either(self):
        self.assertEqual(
            entry._requirement_name("pywebview>=6.2.1 ; sys_platform == 'win32'"),
            "pywebview")


class TestMissingDetection(unittest.TestCase):

    def test_a_pin_does_not_break_detection(self):
        """The regression that pinning introduces if the name is not split out:
        find_spec looks for a module called "sqlite3>=1.0", never finds one, and
        the whole list reinstalls on every launch."""
        self.assertEqual(entry._missing(["sqlite3>=1.0"]), [])

    def test_a_pinned_requirement_is_returned_whole_for_pip(self):
        """What comes back must still be installable, pin included."""
        self.assertEqual(entry._missing(["no-such-package-xyz==9.9.9"]),
                         ["no-such-package-xyz==9.9.9"])

    def test_pywebview_is_detected_under_its_import_name(self):
        """The one package whose pip name is not its import name. Get this
        wrong and every launch reinstalls pywebview forever."""
        try:
            import webview       # noqa: F401
        except ImportError:
            self.skipTest("pywebview not installed here")
        self.assertEqual(entry._missing(["pywebview"]), [])

    def test_a_package_that_does_not_exist_is_reported_missing(self):
        self.assertEqual(entry._missing(["no-such-package-xyz"]),
                         ["no-such-package-xyz"])

    def test_the_standard_library_is_never_missing(self):
        self.assertEqual(entry._missing(["json", "sqlite3"]), [])


class TestEnsureDeps(unittest.TestCase):

    def test_nothing_missing_means_pip_is_never_called(self):
        """The common case: every launch after the first. Shelling out to pip
        just to be told there is nothing to do costs seconds on every start."""
        with mock.patch.object(entry, "_missing", return_value=[]), \
             mock.patch.object(entry.subprocess, "check_call") as call:
            self.assertTrue(entry._ensure_deps())
        call.assert_not_called()

    def test_it_installs_what_is_missing_and_carries_on(self):
        calls = iter([["fastapi"], []])          # missing, then satisfied
        with mock.patch.object(entry, "_missing", side_effect=lambda p: next(calls)), \
             mock.patch.object(entry.subprocess, "check_call") as call:
            self.assertTrue(entry._ensure_deps())
        self.assertEqual(call.call_count, 1)
        argv = call.call_args[0][0]
        self.assertIn("install", argv)
        self.assertIn("fastapi", argv)

    def test_the_proxy_variables_are_stripped_for_pip(self):
        """v1's lesson: on the corporate network pip resolves through a proxy it
        cannot authenticate to and hangs, where a direct connection works."""
        env_in = {"HTTPS_PROXY": "http://proxy:8080", "http_proxy": "http://p",
                  "PATH": "/usr/bin"}
        calls = iter([["fastapi"], []])
        with mock.patch.object(entry, "_missing", side_effect=lambda p: next(calls)), \
             mock.patch.dict(entry.os.environ, env_in, clear=True), \
             mock.patch.object(entry.subprocess, "check_call") as call:
            entry._ensure_deps()
        env = call.call_args[1]["env"]
        for var in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            self.assertNotIn(var, env)
        self.assertEqual(env["NO_PROXY"], "*")
        self.assertEqual(env["PATH"], "/usr/bin", "the rest of the env survives")

    def test_a_pinned_fatal_package_still_aborts(self):
        """_FATAL lists distributions; `still` carries requirement lines. Compare
        them raw and a pinned uvicorn stops counting as fatal, so a machine that
        could not install it walks into the traceback this function exists to
        prevent."""
        pinned = ["uvicorn>=0.52.4,<1.0"]
        with mock.patch.object(entry, "_missing", return_value=pinned),              mock.patch.object(entry.subprocess, "check_call",
                               side_effect=subprocess.CalledProcessError(1, "pip")):
            self.assertFalse(entry._ensure_deps())

    def test_a_failed_install_of_a_fatal_package_aborts(self):
        calls = iter([["uvicorn"], ["uvicorn"]])   # still missing afterwards
        with mock.patch.object(entry, "_missing", side_effect=lambda p: next(calls)), \
             mock.patch.object(entry.subprocess, "check_call",
                               side_effect=subprocess.CalledProcessError(1, "pip")):
            self.assertFalse(entry._ensure_deps())

    def test_a_failed_install_of_an_optional_package_does_not(self):
        """pywebview failing is survivable -- main() opens the browser instead.
        Refusing to start over it would be worse than the thing it prevents."""
        calls = iter([["pywebview"], ["pywebview"]])
        with mock.patch.object(entry, "_missing", side_effect=lambda p: next(calls)), \
             mock.patch.object(entry.subprocess, "check_call",
                               side_effect=subprocess.CalledProcessError(1, "pip")):
            self.assertTrue(entry._ensure_deps())

    def test_pip_missing_entirely_is_not_a_crash(self):
        """A stripped Python has no pip. That is a message, not a traceback."""
        calls = iter([["uvicorn"], ["uvicorn"]])
        with mock.patch.object(entry, "_missing", side_effect=lambda p: next(calls)), \
             mock.patch.object(entry.subprocess, "check_call",
                               side_effect=OSError("no pip")):
            self.assertFalse(entry._ensure_deps())


class TestHealthProbeIgnoresProxies(unittest.TestCase):
    """The probe must never be sent to a proxy.

    On Windows urllib reads the WinINET proxy settings, and the "<local>"
    bypass entry matches only hostnames with NO DOT -- "127.0.0.1" has three.
    A managed machine with a system proxy therefore sends the health check to
    the corporate proxy, which cannot reach this process, and the app reports
    "the local server did not start" while the server is running fine.
    """

    def setUp(self):
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):                       # noqa: N802
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')

            def log_message(self, *a):              # keep the suite quiet
                pass

        self.httpd = http.server.HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.httpd.server_address[1]}/api/health"
        # addCleanup is LIFO, so register close first and shutdown second:
        # closing the socket while serve_forever is still selecting on it
        # raises WinError 10038 into the suite's output.
        self.addCleanup(self.httpd.server_close)
        self.addCleanup(self.httpd.shutdown)

    # Port 9 is discard: nothing listens, so a proxied request fails at once.
    PROXY = {"http_proxy": "http://127.0.0.1:9", "HTTP_PROXY": "http://127.0.0.1:9",
             "no_proxy": "", "NO_PROXY": ""}

    def test_the_probe_still_reaches_loopback(self):
        with mock.patch.dict(entry.os.environ, self.PROXY):
            ok, why = entry._wait_until_up(self.url, timeout=5)
        self.assertTrue(ok, f"probe failed with a proxy configured: {why!r}")

    def test_an_ordinary_opener_would_have_been_proxied(self):
        """Proves the bug is real rather than theoretical: an opener built the
        ordinary way, in the same environment, does not get through.

        build_opener() rather than urlopen(): urlopen caches one global opener
        on first use, which snapshots the proxy configuration as it was then,
        so asserting through it would pass or fail depending on whether some
        earlier test in the run had already built it.
        """
        with mock.patch.dict(entry.os.environ, self.PROXY):
            with self.assertRaises(OSError):
                urllib.request.build_opener().open(self.url, timeout=2)

    def test_a_server_that_never_answers_reports_the_last_error(self):
        """The failure has to say what it saw, or it is a dead end."""
        dead = "http://127.0.0.1:9/api/health"
        ok, why = entry._wait_until_up(dead, timeout=1)
        self.assertFalse(ok)
        self.assertIsNotNone(why)


class TestRunBat(unittest.TestCase):
    """run.bat is the only entry point a non-developer touches."""

    def setUp(self):
        self.text = (ROOT / "run.bat").read_text(encoding="utf-8", errors="ignore")

    def test_it_still_runs_the_app(self):
        self.assertIn("python -m app", self.text)

    def test_it_checks_for_python_before_using_it(self):
        """Without this, "Python is not installed" reads as
        "'python' is not recognized as an internal or external command"."""
        self.assertIn("where python", self.text)
        self.assertLess(self.text.index("where python"),
                        self.text.index("python -m app"))

    def test_it_does_not_ask_the_user_to_install_anything(self):
        """The whole point of the change: no manual pip step anywhere."""
        self.assertNotIn("pip install -r", self.text)

    def test_it_pauses_so_a_double_clicked_window_does_not_vanish(self):
        self.assertIn("pause", self.text)


if __name__ == "__main__":
    unittest.main()
