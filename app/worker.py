"""Analyse ONE input file in its own process. See docs/decisions/0005.

    python -m app.worker <path> [--target hmos|hms]

A separate process because androguard's AnalyzeAPK builds the full DEX xref
graph in memory and does not give it back. The worker exits, the OS reclaims
the memory, and a crash costs only the file in flight.

It IMPORTS the engine rather than shelling out to analyzer.py: `import
analyzer` runs the CLI's own bootstrap (dependency install, loguru silencing,
UTF-8 stdio) and exposes the same bound functions the CLI calls, so the output
comes from the same code path and the in-memory result is still here for the
progress events and the side-car. Being in-process is also what makes progress
STRUCTURED: ui.terminal's print_info is patched before the engine modules bind
it, so stages come from the engine's own phase calls.

PROTOCOL -- one JSON object per line on stdout, nothing else:

    {"stage": "loading"|"dex"|"scan"|"kits"|"api"|"render", "detail": "..."}
    {"stage": "log",   "level": "warn", "detail": "..."}
    {"stage": "done",  "result": {...row...}}
    {"stage": "error", "error": "..."}

Stages mirror the engine's real phases; they are not a timer.
"""

import argparse
import json
import re
import sys
import traceback
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
_ENGINE = _ROOT / "engine"

_ANSI = re.compile(r"\x1b\[[0-9;]*m")


def emit(obj) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False, default=str) + "\n")
    sys.stdout.flush()


# Substring -> stage. Matched against the engine's own print_info text with the
# colour codes stripped. An unrecognised message is still forwarded as a log
# line, so a future engine phase degrades to "no stage change", never to a lie.
_STAGES = (
    ("loading APK",              "loading"),
    ("loading exe",              "loading"),
    ("loading ipa",              "loading"),
    ("loading folder",           "loading"),
    ("analyzing dex",            "dex"),
    ("scanning method references", "scan"),
    ("parsing import table",     "imports"),
    ("matching harmonyos apis",  "api"),
    ("kits",                     "kits"),      # "Matching <target> kits..."
)


def _classify(msg: str):
    low = msg.lower()
    for needle, stage in _STAGES:
        if needle.lower() in low:
            return stage
    return None


_LAST_WARN = []


def _install_hooks():
    """Route the engine's console output into the JSONL stream.

    MUST run before the core modules are imported: they do
    `from ui.terminal import print_info`, binding the name at import time.
    """
    import ui.terminal as term

    def info(msg):
        clean = _ANSI.sub("", str(msg)).strip()
        stage = _classify(clean)
        emit({"stage": stage, "detail": clean} if stage
             else {"stage": "log", "level": "info", "detail": clean})

    def ok(msg):
        emit({"stage": "log", "level": "ok", "detail": _ANSI.sub("", str(msg)).strip()})

    def warn(msg):
        clean = _ANSI.sub("", str(msg)).strip()
        # Kept so a SystemExit can explain itself: sys.exit carries no message.
        _LAST_WARN.append(clean)
        emit({"stage": "log", "level": "warn", "detail": clean})

    term.print_info, term.print_ok, term.print_warn = info, ok, warn


def _sidecar(result: dict, framework: dict) -> dict:
    """The minimum an aggregate workbook needs from one app.

    Storing exactly these keeps a 43-app run's side-cars in the low megabytes;
    the whole result dict would be ~2 MB for a SMALL app, most of it
    detected_namespaces, which no sheet reads.
    """
    return {
        "package_name":  result.get("package_name"),
        "app_name":      result.get("app_name") or "",
        "framework":     framework,
        "permissions":   len(result.get("permissions") or []),
        "total_detected_ns": result.get("total_detected_ns", 0),
        "total_3p_ns":       result.get("total_3p_ns", 0),
        "mapped": [
            {"namespace": src["android_namespace"], "kit": km["kit_name"]}
            for km in result.get("kit_matches", [])
            for src in km.get("android_sources", [])
        ],
        "unmapped":  result.get("unmapped_namespaces", []),
        "ohpm": [
            {k: om.get(k) for k in
             ("namespace", "ohpm_package", "install_cmd", "category",
              "confidence", "method_count")}
            for om in result.get("ohpm_matches", [])
        ],
    }


def resolve_mode(path: Path, target: str):
    """(mode, effective_target, output_stem) for one input.

    Getting it wrong silently produces a report under the wrong name, which
    then makes skip_existing skip the wrong thing. Only APK has a target
    choice: HMS is an Android concept, so an EXE or an IPA is always HarmonyOS.
    """
    sfx = path.suffix.lower()
    if path.is_dir():
        mode = "exe_folder"
    elif sfx == ".ipa":
        mode = "ipa"
    elif sfx in (".exe", ".dll"):
        mode = "exe"
    else:
        mode = "apk"
    if mode != "apk":
        target = "hmos"
    stem = path.name if mode == "exe_folder" else path.stem
    return mode, target, stem


def _run(path: Path, target: str) -> dict:
    """Mirror engine/analyzer.py's single-file branch exactly.

    The order and the filenames are verbatim: the artifacts must be
    byte-identical to the CLI's.
    """
    import analyzer as cli          # runs deps bootstrap + loguru silencing
    from app import config

    # config, not a hardcoded _ENGINE/"result": the worker is a child process, so
    # it re-reads the environment, and a hardcoded path makes MA_RESULT_DIR a lie.
    result_dir = config.RESULT_DIR
    agent_dir = config.AGENT_DIR
    result_dir.mkdir(parents=True, exist_ok=True)
    agent_dir.mkdir(parents=True, exist_ok=True)
    mappings = config.MAPPINGS_DIR

    mode, target, stem = resolve_mode(path, target)
    output_html = result_dir / f"{stem}_{mode}_{target}_report.html"
    agent_path = agent_dir / f"{stem}_{mode}_{target}_agent.json"

    if mode == "exe_folder":
        mapping = cli.load_mapping(mappings / "win_mapping.json")
        result = cli.analyze_exe_folder(str(path), mapping)
        html = cli.render_html_exe_folder(result)
        framework = None
    elif mode == "apk":
        mapping = cli.load_mapping(mappings / ("hms_mapping.json" if target == "hms" else "mapping.json"))
        ohpm = cli.load_ohpm_mapping(mappings / "ohpm_mapping.json") if target != "hms" else None
        result = cli.analyze_apk(str(path), mapping, target, ohpm_mapping=ohpm)
        result["framework"] = cli.detect_framework(
            str(path), package_name=result.get("package_name"),
            namespaces=list(result.get("detected_namespaces", {}).keys()))
        framework = result["framework"]
        emit({"stage": "render"})
        html = cli.render_html_apk(result, mapping)
        cli.export_excel_apk(result, output_html.with_suffix(".xlsx"))
    elif mode == "ipa":
        mapping = cli.load_mapping(mappings / "ios_mapping.json")
        result = cli.analyze_ipa(str(path), mapping)
        emit({"stage": "render"})
        html = cli.render_html_ipa(result)
        cli.export_excel_ipa(result, output_html.with_suffix(".xlsx"))
        framework = None
    else:
        mapping = cli.load_mapping(mappings / "win_mapping.json")
        result = cli.analyze_exe(str(path), mapping)
        emit({"stage": "render"})
        html = cli.render_html_exe(result)
        cli.export_excel_exe(result, output_html.with_suffix(".xlsx"))
        framework = None

    if mode == "exe_folder":
        emit({"stage": "render"})

    # Outputs BEFORE the "done" event: never announce a result before it is
    # persisted.
    output_html.write_text(html, encoding="utf-8")
    cli.write_agent_json(result, agent_path)

    xlsx = output_html.with_suffix(".xlsx")
    row = {
        "source_file":   path.name,
        "mode":          mode,
        "target":        target,
        "package_name":  result.get("package_name"),
        "app_name":      result.get("app_name") or result.get("file_name") or result.get("folder_name") or "",
        "version":       result.get("version_name") or result.get("version"),
        "kit_count":     len(result.get("kit_matches") or []),
        "unmapped_count": len(result.get("unmapped_namespaces")
                              or result.get("unmapped_dlls")
                              or result.get("unmapped_frameworks") or []),
        "ohpm_count":    len(result.get("ohpm_matches") or []),
        "permission_count": len(result.get("permissions") or []),
        "analysis_time_sec": result.get("analysis_time_sec"),
        "report": str(output_html),
        "xlsx":   str(xlsx) if xlsx.exists() else None,
        "agent_json": str(agent_path),
    }

    if framework:
        row["framework"] = framework.get("framework")
        row["engine_name"] = framework.get("engine")
        row["packer"] = (framework.get("detail") or {}).get("packer")

    # Coverage is NOT recomputed here. coverage_status() is the one source of
    # truth the HTML card and the batch workbook already share.
    if mode == "apk":
        from core.renderer import coverage_status
        pct, status = coverage_status(result)
        row["coverage_pct"], row["coverage_status"] = pct, status

        side_dir = result_dir / ".sidecars"
        side_dir.mkdir(exist_ok=True)
        side = side_dir / f"{stem}_{target}.json"
        side.write_text(json.dumps(_sidecar(result, framework), ensure_ascii=False, default=str),
                        encoding="utf-8")
        row["sidecar"] = str(side)

    return row


def main(argv: list[str]) -> int:
    # stdout is ALWAYS a pipe here, the exact condition under which a CJK app
    # name raises UnicodeEncodeError.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    ap = argparse.ArgumentParser(prog="app.worker")
    ap.add_argument("path")
    ap.add_argument("--target", default="hmos", choices=["hmos", "hms"])
    args = ap.parse_args(argv)

    path = Path(args.path)
    if not path.exists():
        emit({"stage": "error", "error": f"Not found: {path}"})
        return 2

    if str(_ENGINE) not in sys.path:
        sys.path.insert(0, str(_ENGINE))

    try:
        _install_hooks()
        row = _run(path, args.target)
    except SystemExit as exc:
        # SystemExit is a BaseException, so `except Exception` does NOT catch it
        # -- and engine/core/exe_engine.py calls sys.exit(1) on an unreadable PE
        # after printing the reason.
        reason = _LAST_WARN[-1] if _LAST_WARN else f"the engine exited ({exc.code})"
        emit({"stage": "error", "error": reason})
        return int(exc.code) if isinstance(exc.code, int) and exc.code else 1
    except Exception as exc:
        emit({"stage": "error", "error": f"{type(exc).__name__}: {exc}",
              "traceback": traceback.format_exc()[-2000:]})
        return 1

    emit({"stage": "done", "result": row})
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
