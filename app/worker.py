"""Analyse ONE input file in its own process. See docs/decisions/0005.

    python -m app.worker <path> [--target hmos|hms]

Not implemented yet -- M2 in docs/ROADMAP.md. What IS fixed here is the
contract, because the JobRunner and the UI are written against it.

WHY A SEPARATE PROCESS
    androguard's AnalyzeAPK builds the full DEX xref graph in memory and does
    not give it back. v1 measured a single-process batch dying four times over
    the 43-app corpus, against 42/43 with zero failures and roughly half the
    wall-clock when each APK got a fresh process. The worker exits, the OS
    reclaims the memory, and a crash costs only the file in flight.

PROTOCOL -- one JSON object per line on stdout, nothing else
    {"stage": "loading",   "file": "com.foo.apk"}
    {"stage": "dex",       "file": "com.foo.apk"}
    {"stage": "kits",      "file": "com.foo.apk"}
    {"stage": "api",       "file": "com.foo.apk"}
    {"stage": "render",    "file": "com.foo.apk"}
    {"stage": "done",      "file": "com.foo.apk", "result": { ...row... }}
    {"stage": "error",     "file": "com.foo.apk", "error": "..."}

    Stages mirror the engine's real phases; they are not a timer. A progress
    bar that moves on a clock lies during the 100-second files and that is
    exactly when the user is watching it.

    "result" carries only what the index needs -- package, app name, version,
    framework, coverage_status()'s two values, the four counts, and the paths
    of the artifacts written. Never the whole result dict: it is megabytes.

RULES
    * stdout is ALWAYS a pipe here, so UTF-8 must be forced before anything
      prints. v1 lost 11 of 26 apps in one run to a UnicodeEncodeError on a CJK
      app name under exactly this condition -- see engine/analyzer.py
      ::_force_utf8_stdio.
    * Progress goes to stdout, human noise goes to stderr. The engine prints a
      lot; none of it may reach the protocol stream.
    * Write the outputs BEFORE announcing "done". v1's ordering bug -- printing
      a summary before persisting the row -- is the reason that rule is written
      down.
    * Exit non-zero only on a real failure. A file that legitimately produces
      nothing (a packed DEX, a split bundle) is a successful analysis with an
      honest result.
"""

import sys


def main(argv: list[str]) -> int:
    raise NotImplementedError("M2 — see docs/ROADMAP.md")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
