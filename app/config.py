"""Paths and constants. Everything is derived from the repo root, so a moved
or shared checkout still resolves and nothing assumes a working directory.
"""

import os
from pathlib import Path

# app/config.py -> app/ -> repo root
ROOT = Path(__file__).resolve().parent.parent


def _env_dir(name: str, default: Path) -> Path:
    """Redirect where DATA is written, never where code lives.

    ENGINE_DIR, WEB_DIR and DOCS_REF_DIR are deliberately NOT overridable.
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
# server opens local files and drives native dialogs.
HOST = "127.0.0.1"

SUPPORTED_INPUTS = (".apk", ".exe", ".dll", ".ipa")
# Recognised but never analysed -- ZIPs of split APKs with no dex of their own.
BUNDLE_INPUTS = (".apkm", ".xapk")


def ensure_dirs() -> None:
    for d in (INPUT_DIR, RESULT_DIR, AGENT_DIR, DB_PATH.parent):
        d.mkdir(parents=True, exist_ok=True)


def rel_to_root(path) -> str:
    """A repo-root-relative, forward-slashed path; absolute when outside the repo."""
    try:
        return str(Path(path).resolve().relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def is_inside_result(path: Path) -> bool:
    """Guard for POST /api/open: refuse anything outside the result tree.

    Resolve first -- `result/../../../etc/passwd` passes a naive prefix check.
    """
    try:
        return RESULT_DIR.resolve() in path.resolve().parents
    except OSError:
        return False
