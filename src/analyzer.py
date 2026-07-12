

import sys
import json
import argparse
import webbrowser
from pathlib import Path


_src_dir = Path(__file__).parent
if str(_src_dir) not in sys.path:
    sys.path.insert(0, str(_src_dir))


def _ensure_deps():
    missing = []
    try:    import androguard
    except ImportError: missing.append("androguard")
    try:    import openpyxl
    except ImportError: missing.append("openpyxl")
    try:    import pefile
    except ImportError: missing.append("pefile")
    try:    import macholib
    except ImportError: missing.append("macholib")
    if missing:
        print(f"[*] Installing: {', '.join(missing)} ...")
        import subprocess, os
        cmd = [sys.executable, "-m", "pip", "install"] + missing + ["--quiet"]
        env = os.environ.copy()
        for var in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            env.pop(var, None)
        env["NO_PROXY"] = "*"
        env["no_proxy"] = "*"
        try:
            subprocess.check_call(cmd, env=env)
        except subprocess.CalledProcessError:
            print("[!] Install failed. Please run manually:")
            print(f"    pip install {' '.join(missing)}")
            sys.exit(1)
        print("[*] Done.\n")

_ensure_deps()


from ui.terminal   import print_info, print_ok, print_warn, _c, C, interactive_session
from core.mapping  import load_mapping
from core.apk_engine import analyze_apk
from core.exe_engine import analyze_exe
from core.ipa_engine import analyze_ipa
from core.renderer import (render_html_apk, render_html_exe, render_html_ipa,
                           export_excel_apk, export_excel_exe, export_excel_ipa,
                           export_excel_batch, export_excel_batch_unmapped,
                           write_agent_json, build_agent_json)
from ui.terminal   import print_summary_apk, print_summary_exe, print_summary_ipa


def run_batch(input_dir: Path, result_dir: Path, script_dir: Path, target: str = "hmos") -> None:
    apk_files = sorted(input_dir.glob("*.apk"))
    exe_files = sorted(input_dir.glob("*.exe"))
    ipa_files = sorted(input_dir.glob("*.ipa"))
    all_files = apk_files + exe_files + ipa_files

    if not all_files:
        print_warn("No APK, EXE, or IPA files found in input/")
        sys.exit(0)

    print_info(f"Batch mode: {len(all_files)} file(s) found")

    apk_mapping_path = script_dir / ("hms_mapping.json" if target == "hms" else "mapping.json")
    exe_mapping_path = script_dir / "win_mapping.json"
    ipa_mapping_path = script_dir / "ios_mapping.json"
    apk_mapping = load_mapping(apk_mapping_path) if apk_files else None
    exe_mapping = load_mapping(exe_mapping_path) if exe_files else None
    ipa_mapping = load_mapping(ipa_mapping_path) if ipa_files else None

    agent_dir  = result_dir / "agent_outputs"
    agent_dir.mkdir(exist_ok=True)

    rows        = []
    agent_files = []
    unmapped_ns_agg      = {}
    unmapped_dll_agg     = {}
    unmapped_fw_agg      = {}
    apk_unmapped_by_file = {}
    for file_path in all_files:
        sfx = file_path.suffix.lower()
        if sfx == ".ipa":
            mode = "ipa"
        elif sfx in (".exe", ".dll"):
            mode = "exe"
        else:
            mode = "apk"
        file_target = "hmos" if mode in ("exe", "ipa") else target
        output_html = result_dir / f"{file_path.stem}_{mode}_{file_target}_report.html"
        agent_path  = agent_dir / f"{file_path.stem}_{mode}_{file_target}_agent.json"

        print()
        sep = "  " + _c("-" * 58, C.BOLD, C.DRED)
        print(sep)
        print(f"  {_c(file_path.name, C.BOLD, C.WHITE)}  {_c(f'({mode.upper()})', C.CYAN)}")
        print(sep)

        try:
            if mode == "apk":
                result = analyze_apk(str(file_path), apk_mapping, file_target)
                html   = render_html_apk(result, apk_mapping)
                output_html.write_text(html, encoding="utf-8")
                print_summary_apk(result)
                rows.append({
                    "file_name":        file_path.name,
                    "app_name":         result.get("app_name") or "",
                    "kit_count":        len(result["kit_matches"]),
                    "unmapped_count":   len(result.get("unmapped_namespaces", [])),
                    "permission_count": len(result.get("permissions", [])),
                    "html_path":        str(output_html),
                })
                apk_unmapped_by_file[file_path.stem] = result.get("unmapped_namespaces", [])
                for u in result.get("unmapped_namespaces", []):
                    agg = unmapped_ns_agg.setdefault(u["namespace"], {
                        "namespace": u["namespace"], "class_count": 0, "method_count": 0,
                        "sample_methods": set(), "apps": [],
                    })
                    agg["class_count"]  += u["class_count"]
                    agg["method_count"] += u["method_count"]
                    agg["sample_methods"].update(u["sample_methods"])
                    agg["apps"].append(file_path.name)
            elif mode == "ipa":
                result = analyze_ipa(str(file_path), ipa_mapping)
                html   = render_html_ipa(result)
                output_html.write_text(html, encoding="utf-8")
                print_summary_ipa(result)
                rows.append({
                    "file_name":        file_path.name,
                    "app_name":         result.get("app_name") or "",
                    "kit_count":        len(result["kit_matches"]),
                    "unmapped_count":   len(result.get("unmapped_frameworks", [])),
                    "permission_count": len(result.get("permissions", [])),
                    "html_path":        str(output_html),
                })
                for fw in result.get("unmapped_frameworks", []):
                    agg = unmapped_fw_agg.setdefault(fw, {"framework": fw, "apps": []})
                    agg["apps"].append(file_path.name)
            else:
                result = analyze_exe(str(file_path), exe_mapping)
                html   = render_html_exe(result)
                output_html.write_text(html, encoding="utf-8")
                print_summary_exe(result)
                rows.append({
                    "file_name":        file_path.name,
                    "app_name":         result.get("file_name", file_path.name),
                    "kit_count":        len(result["kit_matches"]),
                    "unmapped_count":   len(result.get("unmapped_dlls", [])),
                    "permission_count": 0,
                    "html_path":        str(output_html),
                })
                for u in result.get("unmapped_dlls", []):
                    agg = unmapped_dll_agg.setdefault(u["dll_name"], {
                        "dll_name": u["dll_name"], "func_count": 0,
                        "sample_funcs": set(), "apps": [],
                    })
                    agg["func_count"] += u["func_count"]
                    agg["sample_funcs"].update(u["sample_funcs"])
                    agg["apps"].append(file_path.name)
            print_ok(f"HTML report: {output_html}")
            write_agent_json(result, agent_path)
            agent_files.append({"source_file": file_path.name, "agent_json": str(agent_path),
                                 **build_agent_json(result)})
        except Exception as exc:
            print_warn(f"Failed: {file_path.name} — {exc}")
            rows.append({
                "file_name":        file_path.name,
                "app_name":         "ERROR",
                "kit_count":        0,
                "unmapped_count":   0,
                "permission_count": 0,
                "html_path":        None,
            })

    if rows:
        for agg in unmapped_ns_agg.values():
            agg["sample_methods"] = sorted(agg["sample_methods"])[:8]
        for agg in unmapped_dll_agg.values():
            agg["sample_funcs"] = sorted(agg["sample_funcs"])[:8]

        unmapped_ns_list = sorted(
            unmapped_ns_agg.values(), key=lambda x: (len(x["apps"]), x["method_count"]), reverse=True
        )
        unmapped_dll_list = sorted(
            unmapped_dll_agg.values(), key=lambda x: (len(x["apps"]), x["func_count"]), reverse=True
        )
        unmapped_fw_list = sorted(
            unmapped_fw_agg.values(), key=lambda x: len(x["apps"]), reverse=True
        )

        batch_xlsx = result_dir / "batch_summary.xlsx"
        export_excel_batch(rows, batch_xlsx, unmapped_dll_list, unmapped_fw_list)

        batch_unmapped_xlsx = result_dir / "batch_unmapped.xlsx"
        export_excel_batch_unmapped(apk_unmapped_by_file, batch_unmapped_xlsx)

        if unmapped_ns_list or unmapped_dll_list or unmapped_fw_list:
            print_ok(
                f"Unique unmapped: {len(unmapped_ns_list)} namespace(s), "
                f"{len(unmapped_dll_list)} DLL(s), {len(unmapped_fw_list)} framework(s)"
            )

    if agent_files:
        from datetime import datetime as _dt
        summary = {
            "schema_version": "1.0",
            "generated_at":   _dt.now().isoformat(timespec="seconds"),
            "file_count":     len(agent_files),
            "files":          agent_files,
        }
        summary_path = agent_dir / "agent_summary.json"
        summary_path.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )
        print_ok(f"Agent summary: {summary_path}")

    print()
    print_ok(f"Batch complete — {len(rows)} file(s) processed.")


def main():
    parser = argparse.ArgumentParser(
        description="Migration Analyzer v2.0 -- Huawei DTSE Turkey",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Run without arguments for full interactive mode:
  python analyzer.py

CLI (APK):
  python analyzer.py myapp.apk --target hmos
  python analyzer.py myapp.apk --target hms  --excel

CLI (EXE):
  python analyzer.py myapp.exe --mode exe
  python analyzer.py myapp.exe --mode exe --excel --json
        """,
    )
    parser.add_argument("input",     nargs="?",                           help=".apk, .exe, or .ipa file")
    parser.add_argument("--mode",    "-M", choices=["apk", "exe", "ipa"], help="Input type: apk, exe, or ipa")
    parser.add_argument("--target",  "-t", choices=["hmos", "hms"],       help="APK target (EXE/IPA always hmos)")
    parser.add_argument("--output",  "-o",                          help="HTML output path")
    parser.add_argument("--json",    "-j", action="store_true",     help="Also produce JSON output")
    parser.add_argument("--excel",   "-e", action="store_true",     help="Also produce Excel (.xlsx)")
    parser.add_argument("--mapping", "-m",                          help="Custom mapping file path")
    parser.add_argument("--no-open",       action="store_true",     help="Do not auto-open HTML")
    parser.add_argument("--batch",   "-b", action="store_true",     help="Analyze all APK/EXE in input/ dir")
    args = parser.parse_args()

    script_dir = (
        Path(sys.executable).parent
        if getattr(sys, "frozen", False)
        else Path(__file__).parent
    )
    input_dir  = script_dir / "input"
    result_dir = script_dir / "result"
    agent_dir  = result_dir / "agent_outputs"
    input_dir.mkdir(exist_ok=True)
    result_dir.mkdir(exist_ok=True)
    agent_dir.mkdir(exist_ok=True)


    if args.batch:
        file_path, mode, target = None, "batch", (args.target or "hmos")
    elif not args.input:
        file_path, mode, target = interactive_session(input_dir)
    else:
        file_path = Path(args.input)
        if not file_path.exists():
            print_warn(f"File not found: {file_path}")
            sys.exit(1)
        sfx = file_path.suffix.lower()
        mode = args.mode or (
            "ipa" if sfx == ".ipa"
            else "exe" if sfx in (".exe", ".dll")
            else "apk"
        )
        target = "hmos" if mode in ("exe", "ipa") else (args.target or "hmos")


    if mode == "batch":
        run_batch(input_dir, result_dir, script_dir, target)
        return


    if args.mapping:
        mapping_path = Path(args.mapping)
    elif mode == "exe":
        mapping_path = script_dir / "win_mapping.json"
    elif mode == "ipa":
        mapping_path = script_dir / "ios_mapping.json"
    elif target == "hms":
        mapping_path = script_dir / "hms_mapping.json"
    else:
        mapping_path = script_dir / "mapping.json"


    output_html = (
        Path(args.output) if args.output
        else result_dir / f"{file_path.stem}_{mode}_{target}_report.html"
    )


    sep = "  " + _c("-" * 58, C.BOLD, C.DRED)
    print(sep)
    print(f"  {_c('Migration Analyzer v2.0', C.BOLD, C.WHITE)}")
    print(f"  {_c('Mode    :', C.CYAN)}  {_c(mode.upper(), C.BOLD, C.WHITE)}")
    print(f"  {_c('Target  :', C.CYAN)}  {_c('HarmonyOS NEXT' if target == 'hmos' else 'HMS Core', C.BOLD, C.WHITE)}")
    print(f"  {_c('File    :', C.CYAN)}  {_c(file_path.name, C.WHITE)}")
    print(f"  {_c('Huawei DTSE Turkey', C.GRAY)}")
    print(sep)


    mapping = load_mapping(mapping_path)

    if mode == "apk":
        result = analyze_apk(str(file_path), mapping, target)
        html   = render_html_apk(result, mapping)
        if args.excel:
            export_excel_apk(result, output_html.with_suffix(".xlsx"))
        print_summary_apk(result)
    elif mode == "ipa":
        result = analyze_ipa(str(file_path), mapping)
        html   = render_html_ipa(result)
        if args.excel:
            export_excel_ipa(result, output_html.with_suffix(".xlsx"))
        print_summary_ipa(result)
    else:
        result = analyze_exe(str(file_path), mapping)
        html   = render_html_exe(result)
        if args.excel:
            export_excel_exe(result, output_html.with_suffix(".xlsx"))
        print_summary_exe(result)

    output_html.write_text(html, encoding="utf-8")
    print_ok(f"HTML report: {output_html}")

    agent_json_path = agent_dir / f"{file_path.stem}_{mode}_{target}_agent.json"
    write_agent_json(result, agent_json_path)

    if args.json:
        jp = output_html.with_suffix(".json")
        jp.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print_ok(f"JSON output: {jp}")

    if not args.no_open:
        webbrowser.open(output_html.resolve().as_uri())

    print()
    print_ok("Done.")


if __name__ == "__main__":
    main()