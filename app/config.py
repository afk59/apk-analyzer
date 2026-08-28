"""Paths and constants. The single place that knows the layout on disk.

Everything is derived from the repo root so a moved or shared checkout still
resolves, and so `app` never assumes a working directory -- run.bat, `python -m
app` from a shell, and a spawned worker all start somewhere different.
"""

from pathlib import Path

# app/config.py -> app/ -> repo root
ROOT = Path(__file__).resolve().parent.parent

ENGINE_DIR   = ROOT / "engine"
INPUT_DIR    = ENGINE_DIR / "input"
RESULT_DIR   = ENGINE_DIR / "result"
AGENT_DIR    = RESULT_DIR / "agent_outputs"
MAPPINGS_DIR = ENGINE_DIR / "data" / "mappings"
DOCS_REF_DIR = ROOT / "docs-ref"

DB_PATH  = ROOT / "app" / "store" / "analyzer.db"
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
