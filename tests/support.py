"""Shared test scaffolding: isolation, fixtures, and sample discovery.

ISOLATION IS THE FIRST REQUIREMENT. Every test that writes anything redirects
engine/result, the SQLite file and engine/input into a temp directory through
MA_RESULT_DIR / MA_DB_PATH / MA_INPUT_DIR, so a test run can never touch real
analysis output. `app.config` is reloaded per test because it resolves those at
import time.

What is deliberately NOT redirected: ENGINE_DIR, WEB_DIR, DOCS_REF_DIR. Those
locate code and reference material; a test that pointed them elsewhere would be
testing something other than this application.
"""

import importlib
import json
import os
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _silence_androguard():
    """androguard logs every AXML header it parses at DEBUG through loguru.

    v1 measured this at ~31 MB for a single APK and over 10 GB for a batch, and
    silencing it is part of the engine's own bootstrap. A test that touches
    androguard directly bypasses that bootstrap, so it has to be done here too
    or the suite's output is unreadable.
    """
    try:
        from loguru import logger
        logger.remove()
    except ImportError:
        pass


_silence_androguard()


def find_sample_apk():
    """A real APK, for the few tests that need androguard to parse one.

    Synthetic zips cover every shape check, but "this really is package X"
    needs a real binary AndroidManifest.xml, which cannot be faked cheaply.
    Corpus binaries are gitignored, so those tests skip on a clean clone rather
    than failing -- a missing corpus is not a broken build.
    """
    env = os.environ.get("MA_TEST_APK")
    if env and Path(env).exists():
        return Path(env)
    for candidate in (
        ROOT / "engine" / "input",
        ROOT.parent / "apk-analyzer-side" / "src" / "input",
    ):
        if not candidate.is_dir():
            continue
        apks = sorted(candidate.glob("*.apk"), key=lambda p: p.stat().st_size)
        if apks:
            return apks[0]          # smallest: these tests pay for it in seconds
    return None


SAMPLE_APK = find_sample_apk()
requires_apk = unittest.skipUnless(
    SAMPLE_APK is not None,
    "no sample APK available (set MA_TEST_APK or populate engine/input)")


class IsolatedTest(unittest.TestCase):
    """Redirects all data paths into a temp dir and reloads the app modules."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ma-test-"))
        self._saved_env = {k: os.environ.get(k) for k in
                           ("MA_RESULT_DIR", "MA_DB_PATH", "MA_INPUT_DIR")}
        os.environ["MA_RESULT_DIR"] = str(self.tmp / "result")
        os.environ["MA_DB_PATH"] = str(self.tmp / "analyzer.db")
        os.environ["MA_INPUT_DIR"] = str(self.tmp / "input")

        self.config = importlib.reload(importlib.import_module("app.config"))
        # Reload consumers too: they hold `from app import config`, which is the
        # module object, but any module-level constant computed from it is stale.
        for name in ("app.store.db", "app.store.index", "app.services.jobs",
                     "app.services.downloader", "app.aggregate"):
            if name in sys.modules:
                importlib.reload(sys.modules[name])
        self.config.ensure_dirs()

    def tearDown(self):
        for k, v in self._saved_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(self.tmp, ignore_errors=True)

    # ------------------------------------------------------------ fixtures
    def make_zip(self, path: Path, members: dict) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path, "w") as z:
            for name, data in members.items():
                z.writestr(name, data)
        return path

    def make_fake_apk(self, path: Path) -> Path:
        """APK-shaped: passes the ZIP structure checks, not androguard."""
        return self.make_zip(path, {
            "classes.dex": b"dex\n035\x00fake",
            "AndroidManifest.xml": b"\x03\x00\x08\x00fake-axml",
            "resources.arsc": b"fake",
        })

    def make_bundle(self, path: Path, splits=3) -> Path:
        members = {"base.apk": b"P" * 5000, "meta.json": b"{}"}
        for i in range(splits):
            members[f"split_config.abi{i}.apk"] = b"S" * 100
        return self.make_zip(path, members)

    def make_report(self, stem: str, mode="apk", target="hmos",
                    detected=90, total=100, framework=None) -> Path:
        """A report carrying the embedded report_data the index reads back."""
        payload = {
            "mode": mode, "total_detected_ns": detected, "total_3p_ns": total,
            "framework": framework or {},
        }
        path = self.config.RESULT_DIR / f"{stem}_{mode}_{target}_report.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "<html><body><script>const report_data = "
            + json.dumps(payload) + ";</script></body></html>",
            encoding="utf-8")
        return path

    def make_agent_json(self, stem: str, mode="apk", target="hmos", **meta) -> Path:
        doc = {
            "schema_version": "1.0", "mode": mode, "target": target,
            "app_metadata": {
                "package_name": meta.get("package", "com.example.app"),
                "app_name": meta.get("app_name", "Example"),
                "version_name": meta.get("version", "1.0"),
            },
            "kit_list": [{"kit_name": f"@kit.K{i}"} for i in range(meta.get("kits", 3))],
            "ohpm_matches": [{} for _ in range(meta.get("ohpm", 0))],
            "framework": meta.get("framework", {}),
        }
        path = self.config.AGENT_DIR / f"{stem}_{mode}_{target}_agent.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc), encoding="utf-8")
        return path

    def make_sidecar(self, stem: str, target="hmos", **kw) -> Path:
        doc = {
            "package_name": kw.get("package", "com.example.app"),
            "app_name": kw.get("app_name", "Example"),
            "framework": kw.get("framework", {"framework": "Native (Java/Kotlin)"}),
            "permissions": kw.get("permissions", 5),
            "total_detected_ns": kw.get("detected", 90),
            "total_3p_ns": kw.get("total", 100),
            "mapped": kw.get("mapped", [{"namespace": "okhttp3", "kit": "@kit.NetworkKit"}]),
            "unmapped": kw.get("unmapped", [{
                "namespace": "com.example.unknown", "class_count": 2,
                "method_count": 7, "sample_methods": ["a", "b"]}]),
            "ohpm": kw.get("ohpm", []),
        }
        path = self.config.RESULT_DIR / ".sidecars" / f"{stem}_{target}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc), encoding="utf-8")
        return path
