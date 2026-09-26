

import sys
import json
import argparse
import webbrowser
from pathlib import Path


def _force_utf8_stdio():
    """Console output is UTF-8 regardless of the locale codepage.

    Without this, redirecting output to a pipe or a file drops Python to the
    locale encoding and the first CJK app name raises UnicodeEncodeError, which
    in a batch takes the whole app down. errors="replace" so an exotic glyph
    degrades to "?" instead of ending a run.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


_force_utf8_stdio()


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


def _ensure_play_scraper():
    """Best-effort install of google-play-scraper. NEVER exits.

    Deliberately NOT part of _ensure_deps(), which sys.exit(1)s on failure.
    This backs one additive, online-only Excel sheet, so a failed install --
    the normal outcome offline -- must leave the batch fully working. Called
    lazily, only when there is something to fetch.
    """
    try:
        import google_play_scraper  # noqa: F401
        return
    except ImportError:
        pass
    print("[*] Installing optional: google-play-scraper ...")
    import subprocess, os
    cmd = [sys.executable, "-m", "pip", "install", "google-play-scraper",
           "--quiet", "--timeout", "10", "--retries", "1"]
    env = os.environ.copy()
    for var in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
        env.pop(var, None)
    env["NO_PROXY"] = "*"
    env["no_proxy"] = "*"
    try:
        subprocess.check_call(cmd, env=env, timeout=120,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        print("[*] Optional dependency unavailable — Play Store metadata will be skipped.")


def _silence_androguard_logs():
    """Drop loguru's default sink before any DEX parsing happens.

    androguard logs every map_item it parses at DEBUG through loguru; left on,
    a single APK writes ~31 MB. Must run after _ensure_deps() (loguru arrives
    as an androguard dependency) and before core.apk_engine's lazy import.

    NOTE: this removes *all* loguru sinks. Fine while androguard is the only
    loguru consumer; revisit if project code ever adopts it.
    """
    try:
        from loguru import logger
    except ImportError:
        return
    logger.remove()


_silence_androguard_logs()


from ui.terminal   import print_info, print_ok, print_warn, _c, C, interactive_session
from core.mapping  import load_mapping, load_ohpm_mapping
from core.apk_engine import analyze_apk
from core.exe_engine import analyze_exe, analyze_exe_folder
from core.ipa_engine import analyze_ipa
from core.renderer import (render_html_apk, render_html_exe, render_html_exe_folder, render_html_ipa,
                           export_excel_apk, export_excel_exe, export_excel_ipa,
                           export_excel_batch, export_excel_batch_unmapped,
                           write_agent_json, build_agent_json, OHPM_SCHEMA_NOTE)
from core.play_meta import fetch_metadata, cache_path_for
from core.framework_detect import detect_framework
from ui.terminal   import print_summary_apk, print_summary_exe, print_summary_exe_folder, print_summary_ipa


def run_batch(input_dir: Path, result_dir: Path, script_dir: Path, target: str = "hmos") -> None:
    apk_files = sorted(input_dir.glob("*.apk"))
    exe_files = sorted(input_dir.glob("*.exe")) + sorted(input_dir.glob("*.dll"))
    ipa_files = sorted(input_dir.glob("*.ipa"))
    all_files = apk_files + exe_files + ipa_files

    # APKM/XAPK are ZIPs of split APKs, not APKs: androguard finds no manifest
    # and no dex in them, so they are deliberately not globbed. Say so, instead
    # of leaving a file in input/ that never appears in any output.
    bundles = sorted(input_dir.glob("*.apkm")) + sorted(input_dir.glob("*.xapk"))
    if bundles:
        print_warn(f"Skipping {len(bundles)} split-APK bundle(s) — extract and analyze base.apk:")
        for b in bundles:
            print_warn(f"    {b.name}")

    if not all_files:
        print_warn("No APK, EXE, DLL, or IPA files found in input/")
        sys.exit(0)

    print_info(f"Batch mode: {len(all_files)} file(s) found")

    mappings_dir = script_dir / "data" / "mappings"
    apk_mapping_path = mappings_dir / ("hms_mapping.json" if target == "hms" else "mapping.json")
    exe_mapping_path = mappings_dir / "win_mapping.json"
    ipa_mapping_path = mappings_dir / "ios_mapping.json"
    apk_mapping = load_mapping(apk_mapping_path) if apk_files else None
    exe_mapping = load_mapping(exe_mapping_path) if exe_files else None
    ipa_mapping = load_mapping(ipa_mapping_path) if ipa_files else None
    # OHPM second tier: HMOS-only, optional, never fatal (see load_ohpm_mapping).
    ohpm_mapping = (load_ohpm_mapping(mappings_dir / "ohpm_mapping.json")
                    if apk_files and target != "hms" else None)

    agent_dir  = result_dir / "agent_outputs"
    agent_dir.mkdir(exist_ok=True)

    rows        = []
    agent_files = []
    unmapped_ns_agg      = {}
    unmapped_dll_agg     = {}
    unmapped_fw_agg      = {}
    apk_unmapped_by_file = {}
    mapped_ns_apps       = {}
    mapped_ns_kit        = {}
    unmapped_ns_apps     = {}
    ohpm_ns_apps         = {}
    ohpm_ns_meta         = {}
    apk_apps             = []
    frameworks           = {}
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
                result = analyze_apk(str(file_path), apk_mapping, file_target,
                                     ohpm_mapping=ohpm_mapping)
                # Descriptive only -- never read by mapping or matching. The
                # namespace keys let the detector tell a packed DEX from a
                # genuinely native app.
                result["framework"] = detect_framework(
                    str(file_path), package_name=result.get("package_name"),
                    namespaces=list(result.get("detected_namespaces", {}).keys()))
                html   = render_html_apk(result, apk_mapping)
                output_html.write_text(html, encoding="utf-8")
                # Summary is printed at the END of the try block, after the row
                # and the agent JSON exist. Printing here dropped the whole app
                # into the except handler on a formatting failure, even though
                # its HTML was already written.
                _summary = print_summary_apk
                rows.append({
                    "file_name":        file_path.name,
                    "app_name":         result.get("app_name") or "",
                    # Descriptive label for the Batch Summary "Platform" column.
                    # Carried on the row because that sheet has no package_name.
                    "framework":        result["framework"],
                    # Coverage is derived, not stored: export_excel_batch calls
                    # renderer.coverage_status() on the row, the same function
                    # the HTML stat card uses.
                    "total_detected_ns": result.get("total_detected_ns", 0),
                    "total_3p_ns":       result.get("total_3p_ns", 0),
                    "total_ohpm_ns":     result.get("total_ohpm_ns", 0),
                    "kit_count":        len(result["kit_matches"]),
                    "unmapped_count":   len(result.get("unmapped_namespaces", [])),
                    "permission_count": len(result.get("permissions", [])),
                    "html_path":        str(output_html),
                })
                apk_unmapped_by_file[file_path.stem] = result.get("unmapped_namespaces", [])
                if result.get("package_name"):
                    apk_apps.append((result["package_name"], result.get("app_name") or ""))
                    frameworks[result["package_name"]] = result["framework"]
                for km in result.get("kit_matches", []):
                    for src in km.get("android_sources", []):
                        ns = src["android_namespace"]
                        mapped_ns_apps.setdefault(ns, set()).add(file_path.name)
                        mapped_ns_kit.setdefault(ns, km["kit_name"])
                for u in result.get("unmapped_namespaces", []):
                    unmapped_ns_apps.setdefault(u["namespace"], set()).add(file_path.name)
                    agg = unmapped_ns_agg.setdefault(u["namespace"], {
                        "namespace": u["namespace"], "class_count": 0, "method_count": 0,
                        "sample_methods": set(), "apps": [],
                    })
                    agg["class_count"]  += u["class_count"]
                    agg["method_count"] += u["method_count"]
                    agg["sample_methods"].update(u["sample_methods"])
                    agg["apps"].append(file_path.name)
                # Second tier, aggregated cross-app on (namespace -> package)
                # so App Count is distinct APKs, matching the Common sheets.
                for om in result.get("ohpm_matches", []):
                    key = (om["namespace"], om["ohpm_package"])
                    ohpm_ns_apps.setdefault(key, set()).add(file_path.name)
                    prev = ohpm_ns_meta.setdefault(key, {
                        "install_cmd": om.get("install_cmd"),
                        "category":    om.get("category"),
                        "confidence":  om.get("confidence"),
                        "method_count": 0,
                    })
                    prev["method_count"] = max(prev["method_count"], om.get("method_count") or 0)
            elif mode == "ipa":
                result = analyze_ipa(str(file_path), ipa_mapping)
                html   = render_html_ipa(result)
                output_html.write_text(html, encoding="utf-8")
                _summary = print_summary_ipa
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
                _summary = print_summary_exe
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
            # Filename only, not str(agent_path): the file lives in the same
            # directory, so a bare name is unambiguous and survives being handed
            # to someone else. An absolute path resolves only on one machine.
            agent_files.append({"source_file": file_path.name, "agent_json": agent_path.name,
                                 **build_agent_json(result)})
            _summary(result)
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

    play_metadata = None
    if apk_apps:
        print()
        play_metadata = fetch_metadata(apk_apps, cache_path_for(script_dir),
                                       ensure_dep=_ensure_play_scraper)

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
        export_excel_batch(
            rows, batch_xlsx, unmapped_dll_list, unmapped_fw_list,
            mapped_ns_apps=mapped_ns_apps if apk_files else None,
            mapped_ns_kit=mapped_ns_kit,
            unmapped_ns_apps=unmapped_ns_apps if apk_files else None,
            ohpm_ns_apps=ohpm_ns_apps if apk_files else None,
            ohpm_ns_meta=ohpm_ns_meta,
            play_metadata=play_metadata,
            frameworks=frameworks if apk_files else None,
        )

        batch_unmapped_xlsx = result_dir / "batch_unmapped.xlsx"
        export_excel_batch_unmapped(apk_unmapped_by_file, batch_unmapped_xlsx)

        if frameworks:
            tally = {}
            for fw in frameworks.values():
                k = (fw or {}).get("framework") or "Unknown"
                tally[k] = tally.get(k, 0) + 1
            print_ok("Built with: " + " · ".join(
                f"{n} {name}" for name, n in
                sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))))

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
            # Once, here — not repeated in every per-app file. See OHPM_SCHEMA_NOTE.
            "schema_note":    OHPM_SCHEMA_NOTE,
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


def run_exe_folder(folder_path: Path, result_dir: Path, agent_dir: Path, mapping: dict, no_open: bool = False) -> None:
    sep = "  " + _c("-" * 58, C.BOLD, C.DRED)
    print(sep)
    print(f"  {_c('Migration Analyzer v2.0', C.BOLD, C.WHITE)}")
    print(f"  {_c('Mode    :', C.CYAN)}  {_c('EXE FOLDER', C.BOLD, C.WHITE)}")
    print(f"  {_c('Target  :', C.CYAN)}  {_c('HarmonyOS NEXT', C.BOLD, C.WHITE)}")
    print(f"  {_c('Folder  :', C.CYAN)}  {_c(folder_path.name, C.WHITE)}")
    print(f"  {_c('Huawei DTSE Turkey', C.GRAY)}")
    print(sep)

    result = analyze_exe_folder(str(folder_path), mapping)
    html   = render_html_exe_folder(result)

    output_html = result_dir / f"{folder_path.name}_exe_folder_hmos_report.html"
    output_html.write_text(html, encoding="utf-8")
    print_summary_exe_folder(result)
    print_ok(f"HTML report: {output_html}")

    agent_json_path = agent_dir / f"{folder_path.name}_exe_folder_hmos_agent.json"
    write_agent_json(result, agent_json_path)

    if not no_open:
        webbrowser.open(output_html.resolve().as_uri())

    print()
    print_ok("Done.")


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

CLI (EXE folder -- every .exe/.dll in one directory as a single app):
  python analyzer.py input/pc/myapp
  python analyzer.py input/pc/myapp --mode exe_folder --no-open
        """,
    )
    parser.add_argument("input",     nargs="?",                           help=".apk/.exe/.ipa file, or a folder for exe_folder mode")
    parser.add_argument("--mode",    "-M", choices=["apk", "exe", "ipa", "exe_folder"],
                        help="Input type: apk, exe, ipa, or exe_folder (a directory of .exe/.dll)")
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
        # A directory can only be exe_folder mode, so infer it rather than
        # falling through to "apk" and failing inside androguard.
        mode = args.mode or (
            "exe_folder" if file_path.is_dir()
            else "ipa" if sfx == ".ipa"
            else "exe" if sfx in (".exe", ".dll")
            else "apk"
        )
        if mode == "exe_folder" and not file_path.is_dir():
            print_warn(f"--mode exe_folder needs a directory of .exe/.dll files: {file_path}")
            sys.exit(1)
        target = "hmos" if mode in ("exe", "ipa", "exe_folder") else (args.target or "hmos")


    if mode == "batch":
        run_batch(input_dir, result_dir, script_dir, target)
        return

    if mode == "exe_folder":
        mapping = load_mapping(script_dir / "data" / "mappings" / "win_mapping.json")
        run_exe_folder(file_path, result_dir, agent_dir, mapping, args.no_open)
        return


    if args.mapping:
        mapping_path = Path(args.mapping)
    elif mode == "exe":
        mapping_path = script_dir / "data" / "mappings" / "win_mapping.json"
    elif mode == "ipa":
        mapping_path = script_dir / "data" / "mappings" / "ios_mapping.json"
    elif target == "hms":
        mapping_path = script_dir / "data" / "mappings" / "hms_mapping.json"
    else:
        mapping_path = script_dir / "data" / "mappings" / "mapping.json"


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
        ohpm_mapping = (load_ohpm_mapping(script_dir / "data" / "mappings" / "ohpm_mapping.json")
                        if target != "hms" else None)
        result = analyze_apk(str(file_path), mapping, target, ohpm_mapping=ohpm_mapping)
        result["framework"] = detect_framework(
            str(file_path), package_name=result.get("package_name"),
            namespaces=list(result.get("detected_namespaces", {}).keys()))
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
