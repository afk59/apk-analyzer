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
        # The new controls, driven the way a person would: a program folder
        # picked, a package list's events arriving, a result deleted.
        window.evaluate_js("setLang('en')")
        OUT["features"] = json.loads(window.evaluate_js(FEATURES_PROBE))
        import os
        from pathlib import Path
        from app.store import index as store_index
        rd = Path(os.environ["MA_RESULT_DIR"])
        rep = rd / "probe_apk_hmos_report.html"
        rep.write_text("<html></html>", encoding="utf-8")
        store_index.write_manifest({"id": 9, "started_at": "2026-10-02T01:00:00",
            "status": "done", "target": "hmos", "input": "probe", "file_count": 1,
            "results": [{"source_file": "probe.apk", "mode": "apk",
                         "report": str(rep)}], "failures": [], "downloads": []})
        store_index.rescan()
        window.evaluate_js("showPanel('results')")
        time.sleep(1.5)
        before = json.loads(window.evaluate_js(
            "JSON.stringify({rows: document.querySelectorAll('#results .result').length,"
            " dels: document.querySelectorAll('#results .result .del').length})"))
        window.evaluate_js("document.querySelector('#results .result .del').click()")
        time.sleep(0.3)
        armed = window.evaluate_js("document.querySelector('#results .result .del').textContent")
        window.evaluate_js("document.querySelector('#results .result .del').click()")
        time.sleep(2.0)
        after = json.loads(window.evaluate_js(
            "JSON.stringify({rows: document.querySelectorAll('#results .result').length})"))
        OUT["delete"] = {"before": before, "armed": armed, "after": after,
                         "fileGone": not rep.exists()}

        # Selection: three reports in two runs, ticked and deleted together.
        reps = []
        for i, names in enumerate((["s1", "s2"], ["s3"])):
            rows = []
            for n in names:
                rp = rd / f"{n}_apk_hmos_report.html"
                rp.write_text("<html></html>", encoding="utf-8")
                reps.append(rp)
                rows.append({"source_file": n + ".apk", "mode": "apk", "report": str(rp)})
            store_index.write_manifest({"id": 20 + i, "started_at": f"2026-10-0{i + 3}T01:00:00",
                "status": "done", "target": "hmos", "input": f"sel{i}", "file_count": len(rows),
                "results": rows, "failures": [], "downloads": []})
        store_index.rescan()
        window.evaluate_js("loadResults()")
        time.sleep(1.5)
        js = window.evaluate_js
        sel = {"bar": js("document.getElementById('selbar').hidden"),
               "boxes": js("document.querySelectorAll('#results input.pick').length"),
               "runBoxes": js("document.querySelectorAll('#results input.pick-run').length")}
        js("document.querySelector('#results input.pick-run').click()")
        time.sleep(0.2)
        sel["afterRunBox"] = js("document.getElementById('sel-count').textContent")
        sel["allIndeterminate"] = js("document.getElementById('sel-all').indeterminate")
        js("document.querySelector('#results input.pick-run').click()")
        js("document.getElementById('sel-all').click()")
        time.sleep(0.2)
        sel["afterAll"] = js("document.getElementById('sel-count').textContent")
        js("document.getElementById('del-selected').click()")
        time.sleep(0.2)
        sel["armed"] = js("document.getElementById('del-selected').textContent")
        sel["stillThere"] = all(p.exists() for p in reps)
        js("document.getElementById('del-selected').click()")
        time.sleep(2.5)
        sel["rowsAfter"] = js("document.querySelectorAll('#results .result').length")
        sel["filesGone"] = not any(p.exists() for p in reps)
        sel["barAfter"] = js("document.getElementById('selbar').hidden")
        OUT["select"] = sel
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
    skipHidden: document.getElementById('skip-wrap').hidden,
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
    startDisabled: document.getElementById('start').disabled,
    // The workbook step names itself instead of leaving the last file's name.
    aggregating: (function () {
      setLang('en');     // the language probe ran earlier and left it on zh
      handleEvent({ stage: 'aggregating', detail: 'x' });
      return document.getElementById('run-file').textContent;
    })()
  });
})()
"""

FEATURES_PROBE = r"""
(function () {
  renderPicked('folder', { name: 'Prog', path: 'C:/Prog', file_count: 0,
                           program: { top: 2, top_resources: 1, all: 5, all_resources: 3 } });
  var opts = document.getElementById('pc-opts');
  var count = function () { return document.getElementById('pc-count').textContent.trim(); };
  var out = { pcVisible: !opts.hidden, countDefault: count() };
  document.getElementById('pc-recursive').click();
  out.countTop = count();
  document.getElementById('pc-resources').click();
  out.countTopRes = count();
  document.querySelector('input[name=pc-mode][value=combined]').click();
  out.combinedDisablesBoxes = document.getElementById('pc-recursive').disabled;
  out.options = pcOptions();
  document.querySelector('input[name=pc-mode][value=batch]').click();
  document.getElementById('pc-recursive').click();
  document.getElementById('pc-resources').click();

  renderPicked('file', { name: 'a.apk', path: 'C:/a.apk' });
  out.pcHiddenForAFile = opts.hidden;

  // A package list's events, interleaved the way the pipelined run sends them.
  beginRun({ run_id: 999999, file_count: 2, input: '2 packages',
             packages: ['com.a', 'com.b'] }, false);
  if (run.source) { run.source.close(); run.source = null; }
  var st = function (p) {
    var rows = Array.from(document.querySelectorAll('#run-downloads .dlrow'));
    var r = rows.find(function (x) { return x.querySelector('.pkg').textContent === p; });
    return r ? r.dataset.state : null;
  };
  out.queued = [st('com.a'), st('com.b')];
  handleEvent({ stage: 'download_started', file: 'com.a' });
  handleEvent({ stage: 'download_progress', file: 'com.a', got: 5, total: 10 });
  handleEvent({ stage: 'download_done', file: 'com.a', source: 'apkpure', version: '1' });
  handleEvent({ stage: 'file_started', file: 'com.a.apk', index: 0 });
  handleEvent({ stage: 'download_started', file: 'com.b' });
  out.overlap = [st('com.a'), st('com.b')];
  handleEvent({ stage: 'download_failed', file: 'com.b', error: 'nope' });
  handleEvent({ stage: 'file_done', file: 'com.a.apk', index: 0,
                result: { source_file: 'com.a.apk', kit_count: 1 } });
  out.final = [st('com.a'), st('com.b')];
  out.rows = document.querySelectorAll('#run-downloads .dlrow').length;
  out.runLine = document.getElementById('run-file').textContent;
  return JSON.stringify(out);
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
                + "FEATURES_PROBE = " + repr(FEATURES_PROBE) + "\n"
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
             "latestRun", "cancelRun", "rescan", "download", "deleteResult",
         "deleteMany"})

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

    def test_a_program_folder_shows_its_options_and_counts(self):
        f = self._run_probe()["features"]
        self.assertTrue(f["pcVisible"])
        self.assertTrue(f["countDefault"].startswith("5 "), f["countDefault"])
        self.assertTrue(f["countTop"].startswith("2 "), f["countTop"])
        self.assertTrue(f["countTopRes"].startswith("3 "), f["countTopRes"])
        self.assertTrue(f["combinedDisablesBoxes"])
        self.assertEqual(f["options"]["pc_mode"], "combined")
        self.assertTrue(f["pcHiddenForAFile"])

    def test_each_package_has_its_own_progress_row(self):
        """Downloads overlap analysis, so a package's state cannot live on the
        run's one "current file" line."""
        f = self._run_probe()["features"]
        self.assertEqual(f["queued"], ["queued", "queued"])
        self.assertEqual(f["overlap"], ["analysing", "downloading"])
        self.assertEqual(f["final"], ["analysed", "failed"])
        self.assertEqual(f["rows"], 2)
        self.assertEqual(f["runLine"], "com.a.apk",
                         "a download's progress overwrote the file being analysed")

    def test_the_x_deletes_after_a_second_click(self):
        d = self._run_probe()["delete"]
        self.assertEqual(d["before"], {"rows": 1, "dels": 1})
        self.assertEqual(d["armed"], "Delete?", "the first click must only arm it")
        self.assertEqual(d["after"]["rows"], 0)
        self.assertTrue(d["fileGone"])

    def test_rows_can_be_selected_and_deleted_together(self):
        s = self._run_probe()["select"]
        self.assertFalse(s["bar"], "selection bar hidden with rows on screen")
        self.assertEqual((s["boxes"], s["runBoxes"]), (3, 2))
        self.assertEqual(s["afterRunBox"], "1 selected", "the newest run holds one row")
        self.assertTrue(s["allIndeterminate"])
        self.assertEqual(s["afterAll"], "3 selected")
        self.assertEqual(s["armed"], "Delete 3?")
        self.assertTrue(s["stillThere"], "the first click must only arm it")
        self.assertEqual(s["rowsAfter"], 0)
        self.assertTrue(s["filesGone"])
        self.assertTrue(s["barAfter"])

    def test_the_skip_toggle_waits_for_a_folder(self):
        """It only means something for a folder run; a picked file is always
        analysed."""
        self.assertTrue(self._run_probe()["load"]["skipHidden"])

    def test_the_workbook_step_is_shown(self):
        p = self._run_probe()["reload"]
        self.assertEqual(p["aggregating"], "Building the batch workbooks")

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
