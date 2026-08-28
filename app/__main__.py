"""Entry point: `python -m app` (and what run.bat calls).

Startup order matters in two places:

  1. Bind a FREE port on 127.0.0.1 only. Never 0.0.0.0 -- this server opens
     local files and drives native dialogs, so it must not be reachable from
     the network.
  2. uvicorn goes on a BACKGROUND thread and pywebview gets the MAIN thread.
     pywebview must own the main thread on Windows; the other way round is a
     hang, not an error message.

If pywebview cannot start (no WebView2, import failure, headless), open the
default browser at the same URL and SAY SO. Degrading silently leaves someone
staring at a window that never appears.

Printed strings use ASCII hyphens: em-dashes mojibake on the Windows console
under the locale codepage. Same convention as engine/core/ohpm_fetch.py --
docstrings and comments still use em-dashes.
"""

import socket
import sys
import threading
import time
import urllib.error
import urllib.request

from app import config


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((config.HOST, 0))
        return s.getsockname()[1]


def _serve(port: int):
    """uvicorn in a daemon thread. Returns the thread once it is listening."""
    import uvicorn
    from app.api.routes import app as fastapi_app

    server = uvicorn.Server(uvicorn.Config(
        fastapi_app, host=config.HOST, port=port,
        log_level="warning", access_log=False,
    ))
    thread = threading.Thread(target=server.run, daemon=True, name="uvicorn")
    thread.start()
    return server, thread


def _wait_until_up(url: str, timeout: float = 20.0) -> bool:
    """Poll /api/health rather than sleeping a guessed interval.

    A fixed sleep is either too short on a cold start (blank window) or wasted
    time on a warm one.
    """
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=1) as r:
                if r.status == 200:
                    return True
        except (urllib.error.URLError, OSError):
            time.sleep(0.15)
    return False


def main(argv: list[str]) -> int:
    config.ensure_dirs()

    port = _free_port()
    base = f"http://{config.HOST}:{port}"
    server, _thread = _serve(port)

    if not _wait_until_up(f"{base}/api/health"):
        print("[!] The local server did not start. Nothing was opened.")
        return 1

    print(f"[*] Migration Analyzer v2 - serving on {base}")

    if "--no-window" in argv:
        print("[*] --no-window: not opening a window. Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            return 0

    try:
        import webview
    except ImportError:
        webview = None

    if webview is not None:
        try:
            webview.create_window(
                "Migration Analyzer", base,
                width=1240, height=820, min_size=(900, 600),
            )
            # Blocks until the window is closed; the daemon server thread dies
            # with the process.
            webview.start()
            return 0
        except Exception as exc:
            print(f"[!] Could not open the app window ({exc}).")

    print("[*] Falling back to your default browser.")
    import webbrowser
    webbrowser.open(base)
    print("[*] Close this console window to stop the server.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
