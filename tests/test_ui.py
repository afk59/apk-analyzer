"""The frontend, loaded in a real webview window.

Static checks on the HTML would pass while the page was broken at runtime, so
this drives the actual renderer: it starts the server, opens the window, waits
for the scripts, and asks the page about itself. A JS error anywhere in load
fails the test.

Skipped when there is no webview backend (headless CI, no WebView2).
"""

import json
import os
import subprocess
import sys
import textwrap
import unittest
from pathlib import Path

from tests.support import IsolatedTest, ROOT


def _webview_available():
    try:
        import webview  # noqa: F401
    except Exception:
        return False
    return os.environ.get("MA_SKIP_UI") != "1"


requires_webview = unittest.skipUnless(
    _webview_available(), "no webview backend (or MA_SKIP_UI=1)")

# Runs in its own process: pywebview owns the main thread and does not give it
# back, so it cannot share one with the test runner.
PROBE_SCRIPT = r'''
import json, sys, time
sys.path.insert(0, ROOT)
from app import config
from app.__main__ import _free_port, _serve, _wait_until_up

config.ensure_dirs()
port = _free_port()
base = f"http://{config.HOST}:{port}"
_serve(port)
if not _wait_until_up(f"{base}/api/health"):
    print(json.dumps({"error": "server did not start"})); sys.exit(1)

import webview
OUT = {}

CATCH = ("window.__errs = window.__errs || [];"
         "window.addEventListener('error', function (e) { window.__errs.push(String(e.message)); });"
         "window.addEventListener('unhandledrejection', function (e) {"
         "  window.__errs.push('unhandled rejection: ' + e.reason); });")

def probe(window):
    try:
        window.evaluate_js(CATCH)
        time.sleep(2.5)
        OUT["load"] = json.loads(window.evaluate_js(LOAD_PROBE))
        window.evaluate_js("showPanel('results')")
        time.sleep(2.0)
        OUT["results"] = json.loads(window.evaluate_js(RESULTS_PROBE))
        for mode in ("light", "dark", "system"):
            window.evaluate_js("setTheme('%s')" % mode)
            time.sleep(0.3)
            OUT.setdefault("themes", {})[mode] = json.loads(window.evaluate_js(THEME_PROBE))
        OUT["errors"] = json.loads(window.evaluate_js(
            "JSON.stringify(window.__errs || [])"))
    except Exception as exc:
        OUT["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        window.destroy()

w = webview.create_window("ui-test", base, width=1280, height=860)
webview.start(probe, w)
print(json.dumps(OUT))
'''

LOAD_PROBE = r"""
(function () {
  var ids = ['start','target','pick-file','pick-folder','packages','download',
             'run-bar','run-stages','run-log','run-cancel','results','rescan',
             'toast','nav-run','theme-toggle','status'];
  var missing = ids.filter(function (i) { return !document.getElementById(i); });
  var fns = {};
  ['startRun','startDownload','beginRun','handleEvent','loadResults','showPanel',
   'setTheme','cycleTheme','openPath','renderPicked','escapeHtml'].forEach(function (f) {
     fns[f] = typeof window[f];
  });
  return JSON.stringify({
    missingIds: missing,
    fns: fns,
    // `const API = ...` lives in the script scope, NOT on window -- unlike a
    // function declaration, which is why the handler probe above can use
    // window[f]. Reading it by bare name is the only thing that works.
    api: (typeof API !== 'undefined') ? Object.keys(API) : [],
    panels: document.querySelectorAll('.panel').length,
    visiblePanels: Array.from(document.querySelectorAll('.panel'))
                        .filter(function (p) { return !p.hidden; }).length,
    startDisabled: document.getElementById('start').disabled,
    progressHidden: document.getElementById('nav-run').hidden,
    status: document.getElementById('status').textContent,
    accent: getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()
  });
})()
"""

RESULTS_PROBE = r"""
(function () {
  return JSON.stringify({
    visible: !document.getElementById('panel-results').hidden,
    analyzeHidden: document.getElementById('panel-analyze').hidden,
    empty: !!document.querySelector('#results .empty'),
    errors: (window.__errs || []).length
  });
})()
"""

THEME_PROBE = r"""
(function () {
  var cs = getComputedStyle(document.documentElement);
  return JSON.stringify({
    attr: document.documentElement.getAttribute('data-theme'),
    bg: cs.getPropertyValue('--bg').trim(),
    text: cs.getPropertyValue('--text').trim(),
    stored: (function () { try { return localStorage.getItem('ma.theme'); }
                           catch (e) { return 'unavailable'; } })(),
    label: document.getElementById('theme-toggle').textContent
  });
})()
"""


@requires_webview
class TestFrontend(IsolatedTest):

    @classmethod
    def setUpClass(cls):
        cls._probe = None

    def _run_probe(self):
        if TestFrontend._probe is not None:
            return TestFrontend._probe
        script = self.tmp / "ui_probe.py"
        body = ("ROOT = " + repr(str(ROOT)) + "\n"
                + "LOAD_PROBE = " + repr(LOAD_PROBE) + "\n"
                + "RESULTS_PROBE = " + repr(RESULTS_PROBE) + "\n"
                + "THEME_PROBE = " + repr(THEME_PROBE) + "\n"
                + PROBE_SCRIPT)
        script.write_text(body, encoding="utf-8")
        env = {**dict(os.environ),
               "MA_RESULT_DIR": str(self.config.RESULT_DIR),
               "MA_DB_PATH": str(self.config.DB_PATH),
               "MA_INPUT_DIR": str(self.config.INPUT_DIR),
               "PYTHONIOENCODING": "utf-8"}
        proc = subprocess.run([sys.executable, "-u", str(script)],
                              cwd=str(ROOT), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", env=env, timeout=240)
        payload = None
        for line in proc.stdout.splitlines():
            line = line.strip()
            if line.startswith("{"):
                try:
                    payload = json.loads(line)
                except ValueError:
                    pass
        self.assertIsNotNone(payload,
                             f"probe produced no result\nSTDOUT{proc.stdout[-600:]}\n"
                             f"STDERR{proc.stderr[-600:]}")
        self.assertNotIn("error", payload, payload.get("error"))
        TestFrontend._probe = payload
        return payload

    def test_page_loads_with_no_javascript_errors(self):
        p = self._run_probe()
        self.assertEqual(p["errors"], [], f"JS errors during load: {p['errors']}")

    def test_every_control_is_present(self):
        p = self._run_probe()["load"]
        self.assertEqual(p["missingIds"], [], f"missing elements: {p['missingIds']}")

    def test_every_handler_is_defined(self):
        p = self._run_probe()["load"]
        undefined = [k for k, v in p["fns"].items() if v != "function"]
        self.assertEqual(undefined, [], f"not defined: {undefined}")

    def test_the_api_client_exposes_every_endpoint(self):
        p = self._run_probe()["load"]
        self.assertEqual(
            set(p["api"]),
            {"health", "pick", "open", "results", "startRun", "runState",
             "cancelRun", "rescan", "download"})

    def test_exactly_one_panel_is_visible_at_a_time(self):
        p = self._run_probe()["load"]
        self.assertEqual(p["panels"], 3)
        self.assertEqual(p["visiblePanels"], 1)

    def test_start_is_disabled_until_something_is_picked(self):
        p = self._run_probe()["load"]
        self.assertTrue(p["startDisabled"])

    def test_progress_is_hidden_before_the_first_run(self):
        p = self._run_probe()["load"]
        self.assertTrue(p["progressHidden"])

    def test_the_backend_reports_a_ready_engine(self):
        p = self._run_probe()["load"]
        self.assertEqual(p["status"], "engine ready")

    def test_switching_panels_works_and_shows_the_empty_state(self):
        p = self._run_probe()["results"]
        self.assertTrue(p["visible"])
        self.assertTrue(p["analyzeHidden"])
        self.assertTrue(p["empty"], "an empty library should say so")
        self.assertEqual(p["errors"], 0)


@requires_webview
class TestThemeStates(IsolatedTest):
    """Light, dark and system are three distinct, persisted states.

    Shares TestFrontend's single window session rather than inheriting from it:
    subclassing re-ran every load test under a second name.
    """

    def _themes(self):
        probe = TestFrontend._probe
        if probe is None:
            helper = TestFrontend(methodName="test_page_loads_with_no_javascript_errors")
            helper.setUp()
            try:
                probe = helper._run_probe()
            finally:
                helper.tearDown()
        return probe["themes"]

    def test_light_and_dark_produce_different_palettes(self):
        t = self._themes()
        self.assertNotEqual(t["light"]["bg"], t["dark"]["bg"])
        self.assertNotEqual(t["light"]["text"], t["dark"]["text"])

    def test_the_attribute_is_stamped_only_for_an_explicit_choice(self):
        t = self._themes()
        self.assertEqual(t["light"]["attr"], "light")
        self.assertEqual(t["dark"]["attr"], "dark")
        # System must REMOVE it, or prefers-color-scheme can never apply again.
        self.assertIn(t["system"]["attr"], (None, ""))

    def test_the_choice_is_remembered(self):
        t = self._themes()
        for mode in ("light", "dark", "system"):
            self.assertIn(t[mode]["stored"], (mode, "unavailable"))

    def test_the_button_says_which_mode_is_active(self):
        t = self._themes()
        self.assertEqual(t["light"]["label"], "Light")
        self.assertEqual(t["dark"]["label"], "Dark")
        self.assertEqual(t["system"]["label"], "Auto")


if __name__ == "__main__":
    unittest.main()
