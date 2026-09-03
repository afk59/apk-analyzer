"""Entry point: `python -m app` (and what run.bat calls).

Startup order matters:

  0. Install what is missing BEFORE anything third-party is imported.
  1. Bind a FREE port on 127.0.0.1 only. Never 0.0.0.0 -- this server opens
     local files and drives native dialogs.
  2. uvicorn goes on a BACKGROUND thread and pywebview gets the MAIN thread.
     pywebview must own the main thread on Windows; the other way round hangs.

If pywebview cannot start, fall back to the default browser at the same URL.

Printed strings use ASCII hyphens: em-dashes mojibake on the Windows console
under the locale codepage.
"""

import importlib.util
import os
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request

from app import config

# Packages whose absence stops the app dead. The rest are installed too, but
# failing to get one is survivable: pywebview falls back to the browser, and
# the engine's four are only needed by the analysis subprocess.
_FATAL = ("fastapi", "uvicorn")

# Distribution name -> import name, for the ones that differ. requirements.txt
# is the single source of truth for WHAT gets installed; this only says how to
# tell whether it is already there.
_IMPORT_NAME = {"pywebview": "webview"}

# Used only if requirements.txt is missing; a broken checkout should still open.
_FALLBACK = ("androguard==4.1.3", "openpyxl==3.1.5", "pefile==2024.8.26",
             "macholib==1.16.4", "fastapi>=0.141.1,<1.0",
             "uvicorn>=0.52.4,<1.0", "pywebview>=6.2.1,<7.0")

# Where a distribution name stops and its version specifier begins. Extras and
# environment markers end it too.
_SPEC_CHARS = "=<>!~[; "


def _requirement_name(req: str) -> str:
    """The bare distribution name out of a requirement line.

    `androguard==4.1.3` -> `androguard`. Feeding the pinned form to find_spec
    finds nothing and reinstalls the whole list on every launch.
    """
    for i, ch in enumerate(req):
        if ch in _SPEC_CHARS:
            return req[:i].strip()
    return req.strip()


def _required_packages() -> list[str]:
    """The uncommented lines of requirements.txt, pins and all, in order."""
    req = config.ROOT / "requirements.txt"
    try:
        text = req.read_text(encoding="utf-8")
    except OSError:
        return list(_FALLBACK)
    names = []
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            names.append(line)
    return names or list(_FALLBACK)


def _missing(packages) -> list[str]:
    """Which requirement lines have nothing importable behind them.

    Presence only, never version: a machine that already has a package keeps
    the one it has. Reproducing an exact environment is `pip install -r`.
    """
    importlib.invalidate_caches()
    out = []
    for pkg in packages:
        name = _IMPORT_NAME.get(_requirement_name(pkg), _requirement_name(pkg))
        try:
            found = importlib.util.find_spec(name) is not None
        except (ImportError, ValueError):
            found = False
        if not found:
            out.append(pkg)
    return out


def _ensure_deps() -> bool:
    """Install everything on first run, unattended. Returns False to abort.

    Mirrors engine/analyzer.py::_ensure_deps, with two differences: the
    engine's four are installed here too (the analysis subprocess needs them),
    and only _FATAL failures abort. Proxy variables are cleared because on the
    corporate network pip hangs against a proxy it cannot authenticate to.
    """
    packages = _required_packages()
    missing = _missing(packages)
    if not missing:
        return True

    print(f"[*] First run - installing: {', '.join(missing)}")
    print("[*] This happens once and needs internet. It can take a few minutes.")

    env = os.environ.copy()
    for var in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
        env.pop(var, None)
    env["NO_PROXY"] = "*"
    env["no_proxy"] = "*"
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", *missing, "--quiet"],
            env=env,
        )
    except (subprocess.CalledProcessError, OSError) as exc:
        print(f"[!] The install did not finish ({exc}).")

    still = _missing(packages)
    # Compare bare names: `still` carries pinned lines, _FATAL lists names.
    blocking = [p for p in still if _requirement_name(p) in _FATAL]
    if blocking:
        print(f"[!] Cannot start without: {', '.join(blocking)}")
        print("    Connect to the internet and run this once:")
        print(f"    \"{sys.executable}\" -m pip install -r "
              f"\"{config.ROOT / 'requirements.txt'}\"")
        return False
    if still:
        # Not fatal, but the reason a later step behaves oddly, so name it now.
        print(f"[*] Continuing without: {', '.join(still)}")
    else:
        print("[*] Setup complete.\n")
    return True


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
    """Poll /api/health rather than sleeping a guessed interval."""
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

    if not _ensure_deps():
        return 1

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
            # Blocks until the window closes; the daemon thread dies with it.
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
