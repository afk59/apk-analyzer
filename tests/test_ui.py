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
_up, _why = _wait_until_up(f"{base}/api/health")
if not _up:
    print(json.dumps({"error": f"server did not start: {_why!r}"})); sys.exit(1)

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
        for lang in ("en", "tr", "zh"):
            window.evaluate_js("setLang('%s')" % lang)
            time.sleep(0.4)
            OUT.setdefault("langs", {})[lang] = json.loads(window.evaluate_js(LANG_PROBE))
        OUT["errors"] = json.loads(window.evaluate_js(
            "JSON.stringify(window.__errs || [])"))

        # LAST, because it leaves a run behind and reloads the page: a run that
        # finished while the page was away must come back on a reload.
        import os
        from pathlib import Path
        from app.services.jobs import runner
        fake = Path(os.environ["MA_INPUT_DIR"]) / "reload" / "a.apk"
        fake.parent.mkdir(parents=True, exist_ok=True)
        fake.write_bytes(b"not an apk")
        run = runner.get(runner.submit([fake], "hmos"))
        deadline = time.monotonic() + 120
        while run.status == "running" and time.monotonic() < deadline:
            time.sleep(0.2)
        window.evaluate_js("location.reload()")
        time.sleep(3.0)
        OUT["reload"] = json.loads(window.evaluate_js(RELOAD_PROBE))
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
    // The PROPERTY being true is not the same as the button being gone:
    // [hidden] is a UA-stylesheet rule and any author `display` beats it.
    progressRendered: getComputedStyle(
        document.getElementById('nav-run')).display !== 'none',
    status: document.getElementById('status').textContent,
    accent: getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()
  });
})()
"""

RELOAD_PROBE = r"""
(function () {
  return JSON.stringify({
    progressRendered: getComputedStyle(
        document.getElementById('nav-run')).display !== 'none',
    rows: document.querySelectorAll('#run-done .result').length,
    // A finished run is re-attached quietly: the page stays where it was.
    analyzeVisible: !document.getElementById('panel-analyze').hidden,
    startDisabled: document.getElementById('start').disabled
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


LANG_PROBE = r"""
(function () {
  var missing = [];
  document.querySelectorAll('[data-i18n]').forEach(function (el) {
    var v = (el.textContent || '').trim();
    if (!v || v === el.dataset.i18n) missing.push(el.dataset.i18n);
  });
  return JSON.stringify({
    lang: document.documentElement.lang,
    stored: (function () { try { return localStorage.getItem('ma.lang'); }
                           catch (e) { return 'unavailable'; } })(),
    navAnalyze: document.querySelector('nav.side button[data-panel=analyze]').textContent.trim(),
    startBtn: document.getElementById('start').textContent.trim(),
    hint: document.getElementById('start-hint').textContent.trim(),
    resultsTitle: document.querySelector('#panel-results h2 span').textContent.trim(),
    // Identifiers must NOT be translated -- they are the analysis output.
    targets: Array.from(document.getElementById('target').options).map(function (o) { return o.text; }),
    untranslated: missing,
    errors: (window.__errs || []).length
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
                + "RELOAD_PROBE = " + repr(RELOAD_PROBE) + "\n"
                + "THEME_PROBE = " + repr(THEME_PROBE) + "\n"
                + "LANG_PROBE = " + repr(LANG_PROBE) + "\n"
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
             "latestRun", "cancelRun", "rescan", "download"})

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

    def test_the_progress_tab_is_not_drawn_before_the_first_run(self):
        """The attribute being set is not enough, and asserting it was the gap.

        [hidden] lives in the UA stylesheet, so any author rule that sets
        `display` on the element wins over it. `nav.side button` sets
        `display: flex`, which left the tab on screen and clickable with no run
        behind it -- the panel then showed its static markup: an empty box
        headed "Running" with a Cancel button.
        """
        p = self._run_probe()["load"]
        self.assertFalse(p["progressRendered"],
                         "the Progress tab is still rendered before any run")

    def test_the_backend_reports_a_ready_engine(self):
        p = self._run_probe()["load"]
        self.assertEqual(p["status"], "engine ready")

    def test_a_reload_re_attaches_to_the_last_run(self):
        """Run state lives in the server; a reload used to drop the Progress
        view entirely. The replay must not double-count either."""
        p = self._run_probe()["reload"]
        self.assertTrue(p["progressRendered"], "Progress tab gone after a reload")
        self.assertEqual(p["rows"], 1)
        self.assertTrue(p["analyzeVisible"])
        self.assertTrue(p["startDisabled"], "Start enabled with nothing picked")

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


@requires_webview
class TestLanguages(IsolatedTest):
    """English, Turkish and Simplified Chinese.

    What is translated is the CHROME. Kit tokens, permission names, package
    names and the reports themselves are identifiers and deliverables, not
    prose -- a report that read differently per viewer could not be compared or
    forwarded, and "@kit.ArkUI" is not a phrase.
    """

    def _langs(self):
        probe = TestFrontend._probe
        if probe is None:
            helper = TestFrontend(methodName="test_page_loads_with_no_javascript_errors")
            helper.setUp()
            try:
                probe = helper._run_probe()
            finally:
                helper.tearDown()
        return probe["langs"]

    def test_every_marked_string_resolves_in_every_language(self):
        for lang, p in self._langs().items():
            self.assertEqual(p["untranslated"], [],
                             f"{lang}: keys with no translation: {p['untranslated']}")

    def test_the_document_language_is_stamped(self):
        for lang, p in self._langs().items():
            self.assertEqual(p["lang"], lang)

    def test_the_choice_is_remembered(self):
        for lang, p in self._langs().items():
            self.assertIn(p["stored"], (lang, "unavailable"))

    def test_the_chrome_actually_changes(self):
        langs = self._langs()
        self.assertEqual(langs["en"]["navAnalyze"], "Analyze")
        self.assertEqual(langs["tr"]["navAnalyze"], "Analiz")
        self.assertEqual(langs["zh"]["navAnalyze"], "分析")
        # Three distinct renderings, not one string leaking across.
        starts = {langs[l]["startBtn"] for l in ("en", "tr", "zh")}
        self.assertEqual(len(starts), 3, f"start button did not change: {starts}")

    def test_runtime_built_strings_switch_too(self):
        """The hint is written by JS, not by data-i18n, so it exercises the
        onLanguageChanged path rather than the markup scan."""
        langs = self._langs()
        hints = {langs[l]["hint"] for l in ("en", "tr", "zh")}
        self.assertEqual(len(hints), 3, f"runtime string did not switch: {hints}")

    def test_identifiers_are_never_translated(self):
        """Target names are platform identifiers. Translating them would make
        the report and the workbook disagree with the UI."""
        for lang, p in self._langs().items():
            self.assertEqual(p["targets"], ["HarmonyOS NEXT", "HMS Core"], lang)

    def test_switching_language_raises_nothing(self):
        for lang, p in self._langs().items():
            self.assertEqual(p["errors"], 0, f"{lang} produced JS errors")
