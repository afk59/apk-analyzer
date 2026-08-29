"""Paths and constants. The single place that knows the layout on disk.

Everything is derived from the repo root so a moved or shared checkout still
resolves, and so `app` never assumes a working directory -- run.bat, `python -m
app` from a shell, and a spawned worker all start somewhere different.
"""

import os
from pathlib import Path

# app/config.py -> app/ -> repo root
ROOT = Path(__file__).resolve().parent.parent


def _env_dir(name: str, default: Path) -> Path:
    """Let a caller redirect where DATA is written, never where code lives.

    The test suite points these at a temp directory so it can exercise the real
    modules without writing into engine/result/ or over the real analyzer.db.
    ENGINE_DIR, WEB_DIR and DOCS_REF_DIR are deliberately NOT overridable: they
    locate code and reference material, and a test that redirected them would
    be testing something other than this application.
    """
    raw = os.environ.get(name)
    return Path(raw).expanduser().resolve() if raw else default


ENGINE_DIR   = ROOT / "engine"
INPUT_DIR    = _env_dir("MA_INPUT_DIR",  ENGINE_DIR / "input")
RESULT_DIR   = _env_dir("MA_RESULT_DIR", ENGINE_DIR / "result")
AGENT_DIR    = RESULT_DIR / "agent_outputs"
MAPPINGS_DIR = ENGINE_DIR / "data" / "mappings"
DOCS_REF_DIR = ROOT / "docs-ref"

DB_PATH  = _env_dir("MA_DB_PATH", ROOT / "app" / "store" / "analyzer.db")
WEB_DIR  = ROOT / "app" / "web"

# Loopback only, and a free port picked at startup. Never bind 0.0.0.0: this
# server can open local files and pick paths through native dialogs, so it must
# not be reachable from the network.
HOST = "127.0.0.1"

SUPPORTED_INPUTS = (".apk", ".exe", ".dll", ".ipa")
# Recognised but never analysed -- ZIPs of split APKs with no dex of their own.
# The engine reports these honestly; the UI should say so too rather than
# silently ignoring a file the user put in the folder.
BUNDLE_INPUTS = (".apkm", ".xapk")


def ensure_dirs() -> None:
    for d in (INPUT_DIR, RESULT_DIR, AGENT_DIR, DB_PATH.parent):
        d.mkdir(parents=True, exist_ok=True)


def rel_to_root(path) -> str:
    """A repo-root-relative, forward-slashed path.

    Everything the UI and the index store is written this way, so a moved or
    shared checkout still resolves. Falls back to the absolute path when the
    target genuinely lives outside the repo.
    """
    try:
        return str(Path(path).resolve().relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def is_inside_result(path: Path) -> bool:
    """Guard for POST /api/open.

    The window can ask the OS to open any path it is handed, so the server must
    refuse anything outside the result tree. Resolve first -- otherwise
    `result/../../../etc/passwd` passes a naive prefix check.
    """
    try:
        return RESULT_DIR.resolve() in path.resolve().parents
    except OSError:
        return False
