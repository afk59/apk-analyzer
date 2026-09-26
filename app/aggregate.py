"""Build the two batch workbooks from a finished run.

    python -m app.aggregate <plan.json>

Each file is analysed in its own process and that process exits
(docs/decisions/0005), so cross-app sheets cannot be accumulated in the loop
the way the CLI does. Each worker writes a compact side-car and this step
replays the same aggregation over them, then calls the REAL
export_excel_batch / export_excel_batch_unmapped. Re-implementing the sheets
would mean two things that could disagree about the same corpus.

Runs in its own process: openpyxl holds the whole workbook in memory, and this
is where the Play Store fetch happens -- the only network call in an analysis
run. Emits the same JSONL protocol as the worker.
"""

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_ENGINE = _ROOT / "engine"


def emit(obj) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False, default=str) + "\n")
    sys.stdout.flush()


def build(rows_and_sidecars, result_dir: Path, target: str) -> dict:
    import analyzer as cli
    from core.renderer import export_excel_batch, export_excel_batch_unmapped
    from core.play_meta import fetch_metadata, cache_path_for

    rows = []
    apk_unmapped_by_file = {}
    mapped_ns_apps, mapped_ns_kit = {}, {}
    unmapped_ns_apps, unmapped_ns_agg = {}, {}
    ohpm_ns_apps, ohpm_ns_meta = {}, {}
    apk_apps, frameworks = [], {}

    for entry in rows_and_sidecars:
        row = entry["row"]
        file_name = row["source_file"]
        side_path = entry.get("sidecar")
        side = {}
        if side_path and Path(side_path).exists():
            try:
                side = json.loads(Path(side_path).read_text(encoding="utf-8"))
            except (OSError, ValueError):
                side = {}

        if row.get("mode") == "error":
            # Matches run_batch's own failure row: named, counted as attempted,
            # and contributing to no aggregate sheet.
            rows.append({
                "file_name": file_name, "app_name": "ERROR", "framework": {},
                "total_detected_ns": 0, "total_3p_ns": 0,
                "kit_count": 0, "unmapped_count": 0, "permission_count": 0,
                "html_path": None,
            })
            continue

        rows.append({
            "file_name":         file_name,
            "app_name":          row.get("app_name") or "",
            "framework":         side.get("framework") or {},
            "total_detected_ns": side.get("total_detected_ns", 0),
            "total_3p_ns":       side.get("total_3p_ns", 0),
            "total_ohpm_ns":     side.get("total_ohpm_ns", 0),
            "kit_count":         row.get("kit_count", 0),
            "unmapped_count":    row.get("unmapped_count", 0),
            "permission_count":  row.get("permission_count", 0),
            "html_path":         row.get("report"),
        })

        if row.get("mode") != "apk":
            continue

        stem = Path(file_name).stem
        apk_unmapped_by_file[stem] = side.get("unmapped", [])

        pkg = side.get("package_name")
        if pkg:
            apk_apps.append((pkg, side.get("app_name") or ""))
            frameworks[pkg] = side.get("framework") or {}

        # Values are SETS, so an App Count is a number of distinct apps and never
        # a number of occurrences.
        for m in side.get("mapped", []):
            mapped_ns_apps.setdefault(m["namespace"], set()).add(file_name)
            mapped_ns_kit.setdefault(m["namespace"], m["kit"])

        for u in side.get("unmapped", []):
            unmapped_ns_apps.setdefault(u["namespace"], set()).add(file_name)
            agg = unmapped_ns_agg.setdefault(u["namespace"], {
                "namespace": u["namespace"], "class_count": 0, "method_count": 0,
                "sample_methods": set(), "apps": [],
            })
            agg["class_count"] += u.get("class_count", 0)
            agg["method_count"] += u.get("method_count", 0)
            agg["sample_methods"].update(u.get("sample_methods", []))
            agg["apps"].append(file_name)

        for om in side.get("ohpm", []):
            key = (om["namespace"], om["ohpm_package"])
            ohpm_ns_apps.setdefault(key, set()).add(file_name)
            prev = ohpm_ns_meta.setdefault(key, {
                "install_cmd": om.get("install_cmd"),
                "category":    om.get("category"),
                "confidence":  om.get("confidence"),
                "method_count": 0,
            })
            prev["method_count"] = max(prev["method_count"], om.get("method_count") or 0)

    for agg in unmapped_ns_agg.values():
        agg["sample_methods"] = sorted(agg["sample_methods"])[:8]

    play_metadata = None
    if apk_apps:
        emit({"stage": "metadata", "detail": f"Looking up {len(apk_apps)} app(s) on Google Play"})
        # Never fatal and never slow when offline: fetch_metadata probes once,
        # commits to a mode, and fills the rest with a placeholder. This phase
        # runs AFTER every report is already on disk.
        play_metadata = fetch_metadata(apk_apps, cache_path_for(_ENGINE),
                                       ensure_dep=cli._ensure_play_scraper)

    emit({"stage": "workbooks", "detail": "Writing batch_summary.xlsx"})
    summary = result_dir / "batch_summary.xlsx"
    export_excel_batch(
        rows, summary, [], [],
        mapped_ns_apps=mapped_ns_apps or None,
        mapped_ns_kit=mapped_ns_kit,
        unmapped_ns_apps=unmapped_ns_apps or None,
        ohpm_ns_apps=ohpm_ns_apps or None,
        ohpm_ns_meta=ohpm_ns_meta,
        play_metadata=play_metadata,
        frameworks=frameworks or None,
    )

    emit({"stage": "workbooks", "detail": "Writing batch_unmapped.xlsx"})
    unmapped_book = result_dir / "batch_unmapped.xlsx"
    export_excel_batch_unmapped(apk_unmapped_by_file, unmapped_book)

    return {
        "batch_summary":  str(summary),
        "batch_unmapped": str(unmapped_book),
        "apps":           len(rows),
        "apk_apps":       len(apk_apps),
        "unique_unmapped": len(unmapped_ns_agg),
    }


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    if not argv:
        emit({"stage": "error", "error": "usage: python -m app.aggregate <plan.json>"})
        return 2

    plan = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    if str(_ENGINE) not in sys.path:
        sys.path.insert(0, str(_ENGINE))

    # The engine prints, and stdout here is the protocol stream.
    import ui.terminal as term
    term.print_info = lambda m: emit({"stage": "log", "level": "info", "detail": str(m)})
    term.print_ok = lambda m: emit({"stage": "log", "level": "ok", "detail": str(m)})
    term.print_warn = lambda m: emit({"stage": "log", "level": "warn", "detail": str(m)})

    try:
        out = build(plan["entries"], Path(plan["result_dir"]), plan.get("target", "hmos"))
    except Exception as exc:
        import traceback
        emit({"stage": "error", "error": f"{type(exc).__name__}: {exc}",
              "traceback": traceback.format_exc()[-2000:]})
        return 1

    emit({"stage": "aggregate_done", "result": out})
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
