"""Entry point: `python -m app` (and what run.bat calls).

M1 in docs/ROADMAP.md wires this up. The startup order is written down now
because two parts of it are load-bearing:

    1. Pick a FREE port on 127.0.0.1 and bind there. Never 0.0.0.0 -- this
       server can open local files and drive native dialogs, so it must not be
       reachable from the network.
    2. Start uvicorn in a background thread, then create the pywebview window
       on the MAIN thread. pywebview must own the main thread on Windows; doing
       it the other way round is a hang, not an error message.
    3. If pywebview is unavailable (no WebView2, import failed), open the
       default browser at the same URL and SAY SO on the console. Degrading
       silently would leave someone staring at a window that never appears.
"""

import sys


def main(argv: list[str]) -> int:
    # ASCII hyphen, not an em-dash: printed strings mojibake on the Windows
    # console under the locale codepage. Same convention as engine/core/ohpm_fetch.py
    # -- docstrings and comments still use em-dashes, printed text does not.
    print("Migration Analyzer v2 - the app shell is not built yet (M1).")
    print("See docs/ROADMAP.md.")
    print()
    print("The v1 CLI is fully working in the meantime:")
    print("    python engine/analyzer.py <file.apk> --no-open")
    print("    python engine/analyzer.py --batch")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
