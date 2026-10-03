"""Report HTML must not execute text taken from the analysed app.

report_data is embedded in an inline <script>. App names, versions and
permission strings come from the input -- which the downloader may have fetched
from a third-party mirror -- so a "</script>" inside one must not close the block.
"""

import json
import plistlib
import re
import tempfile
import unittest
import zipfile
from pathlib import Path

from tests.support import ROOT

import sys
_ENGINE = ROOT / "engine"
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

PAYLOAD = "Evil</script><script>document.title='XSS'</script><!-- %%WORKBOOK_B64%%"


def _report_data(html: str):
    m = re.search(r"const REPORT_DATA = (.*?);\nconst WORKBOOK_B64", html, re.S)
    assert m, "REPORT_DATA block not found"
    return m.group(1)


class TestScriptJson(unittest.TestCase):

    def setUp(self):
        from core.renderer import _script_json
        self.enc = _script_json

    def test_the_value_round_trips_unchanged(self):
        data = {"app_name": PAYLOAD, "n": 3, "list": ["a</b", "<!--x"]}
        self.assertEqual(json.loads(self.enc(data)), data)

    def test_nothing_that_can_close_or_comment_the_block_survives(self):
        out = self.enc({"app_name": PAYLOAD})
        self.assertNotIn("</", out)
        self.assertNotIn("<!--", out)
        self.assertNotIn("%%", out)


class TestIpaReport(unittest.TestCase):
    """End to end through the real IPA engine and renderer."""

    def test_a_hostile_app_name_stays_inside_its_string(self):
        from core.ipa_engine import analyze_ipa
        from core.mapping import load_mapping
        from core.renderer import render_html_ipa

        with tempfile.TemporaryDirectory() as tmp:
            ipa = Path(tmp) / "evil.ipa"
            plist = plistlib.dumps({"CFBundleDisplayName": PAYLOAD,
                                    "CFBundleIdentifier": "com.example.evil",
                                    "CFBundleShortVersionString": "1.0"})
            with zipfile.ZipFile(ipa, "w") as z:
                z.writestr("Payload/Evil.app/Info.plist", plist)
            mapping = load_mapping(_ENGINE / "data" / "mappings" / "ios_mapping.json")
            html = render_html_ipa(analyze_ipa(str(ipa), mapping))

        block = _report_data(html)
        self.assertNotIn("</script>", block)
        self.assertEqual(json.loads(block)["app_name"], PAYLOAD)
        # The workbook placeholder in the payload was not expanded into it.
        self.assertNotIn("UEsDB", block)


if __name__ == "__main__":
    unittest.main()
