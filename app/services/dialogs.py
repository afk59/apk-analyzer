"""Native file and folder pickers.

    pick_file()   -> Path | None
    pick_folder() -> Path | None

A browser's <input type="file"> gives file CONTENT, never a path, and has no
folder picker at all. The engine needs a real absolute path and batch mode
needs a directory. That gap is what decided the whole stack
(docs/decisions/0001).

Two implementations, tried in order:

    1. pywebview's own dialog, when a window exists. Parented to the app
       window, so it cannot end up behind it.
    2. app/_dialog_proc.py in a throwaway process. Owns its own GUI main
       thread, and works in browser-fallback mode where there is no window.

Cancel returns None. Cancel is not an error and must never surface as one.
"""

import subprocess
import sys
from pathlib import Path

_FILE_TYPES = ("Supported (*.apk;*.exe;*.dll;*.ipa)", "All files (*.*)")


def _via_webview(kind: str):
    """pywebview's dialog, or None if there is no window / it is unavailable.

    Returns (handled, path). `handled` False means fall through to the
    subprocess, so a cancelled dialog is never mistaken for "pywebview is
    missing".
    """
    try:
        import webview
    except ImportError:
        return False, None
    windows = getattr(webview, "windows", None) or []
    if not windows:
        return False, None
    try:
        if kind == "folder":
            res = windows[0].create_file_dialog(webview.FOLDER_DIALOG)
        else:
            res = windows[0].create_file_dialog(
                webview.OPEN_DIALOG, allow_multiple=False,
                file_types=(f"Supported files (*.apk;*.exe;*.dll;*.ipa)", "All files (*.*)"),
            )
    except Exception:
        # Any GUI-thread or backend problem: fall through rather than fail.
        return False, None
    if not res:
        return True, None            # cancelled -- a real answer
    first = res[0] if isinstance(res, (list, tuple)) else res
    return True, Path(str(first))


def _via_subprocess(kind: str):
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "app._dialog_proc", kind],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            cwd=str(Path(__file__).resolve().parent.parent.parent),
            timeout=600,
        )
    except Exception:
        return None
    out = (proc.stdout or "").strip()
    return Path(out) if out else None


def _pick(kind: str):
    handled, path = _via_webview(kind)
    if handled:
        return path
    return _via_subprocess(kind)


def pick_file():
    return _pick("file")


def pick_folder():
    return _pick("folder")
