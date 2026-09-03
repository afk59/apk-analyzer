
import os
import re
import json
from pathlib import Path
from datetime import datetime

_OBFUS_SIMPLE = re.compile(r'^[A-Za-z]{1,2}[0-9]{0,2}$')
_OBFUS_SHORT  = re.compile(r'^[A-Z]\.[A-Za-z0-9]{2,5}$')

# Minimum number of distinct APKs a namespace must appear in to be considered
# "common" and listed in the batch_summary.xlsx Common Mapped / Common Unmapped
# sheets. Set to 1 to list every namespace in the batch.
_COMMON_MIN_APPS = 2
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from core.mapping import get_doc_url
from ui.terminal import print_ok as _print_ok, C


def _esc(s: str) -> str:
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def confidence_badge(c: str) -> str:
    label = {"high": "High", "medium": "Medium", "low": "Low"}.get(c, c)
    return f'<span class="badge {c}">{label}</span>'


def _qt6_banner(qt6_dlls: list) -> str:
    if not qt6_dlls:
        return ""
    dlls_list = ", ".join(qt6_dlls)
    return (
        f'<div style="background:#fff8e1;border:1.5px solid #f59e0b;border-radius:8px;'
        f'padding:14px 18px;margin-bottom:14px;display:flex;gap:12px;align-items:flex-start">'
        f'<span style="font-size:1.3rem">&#9888;&#65039;</span>'
        f'<div><div style="font-weight:700;color:#92400e;margin-bottom:4px">'
        f'Qt6 — HarmonyOS support not yet available</div>'
        f'<div style="font-size:.84rem;color:#78350f">'
        f'Detected: {_esc(dlls_list)}. Qt 6.x has no official HarmonyOS port yet — Qt 6.12 formal release '
        f'expected ~Q4 2026. Migration path not yet available; monitor before planning.</div></div></div>'
    )


def _packed_dex_banner(fw: dict, total_3p_ns: int, kit_count: int) -> str:
    """Say plainly that a packed APK's numbers describe the stub, not the app.

    Without this the report is actively misleading rather than merely thin: a
    packed app exposing three namespaces renders "100% coverage", which reads
    BETTER than an app that was genuinely analysed end to end.
    """
    detail = (fw or {}).get("detail") or {}
    if "packed" not in (detail.get("note") or "").lower():
        return ""
    packer = detail.get("packer") or "unknown packer"
    return (
        f'<div style="background:#fef2f2;border:1.5px solid #dc2626;border-radius:8px;'
        f'padding:14px 18px;margin-bottom:14px;display:flex;gap:12px;align-items:flex-start">'
        f'<span style="font-size:1.3rem">&#128274;</span>'
        f'<div><div style="font-weight:700;color:#991b1b;margin-bottom:4px">'
        f'DEX is packed &mdash; {_esc(packer)}. The figures below describe the loader, not the app.</div>'
        f'<div style="font-size:.84rem;color:#7f1d1d">'
        f'The real classes are encrypted and are only decrypted at runtime, so bytecode analysis sees '
        f'the unpacking stub. This report found <b>{kit_count}</b> kit match(es) across '
        f'<b>{total_3p_ns}</b> third-party namespace(s) &mdash; an analysable app in this corpus exposes '
        f'400&ndash;6,700. The coverage percentage is withheld for that reason: a high ratio over a '
        f'handful of references means nothing. '
        f'To assess this app for real, obtain an unpacked build or dump the DEX from a running instance; '
        f'the manifest, permissions and native libraries below ARE accurate, because they are read from '
        f'the archive rather than the bytecode.</div></div></div>'
    )


# Below this many third-party namespaces a percentage is arithmetic, not a
# measurement.
_LOW_SAMPLE_NS = 50


def coverage_status(result: dict) -> tuple:
    """(percent, status) for native namespace coverage.

    ONE source of truth, deliberately: the HTML stat card and the batch sheet's
    Coverage column both call this, so a report and the workbook can never
    disagree about an app. status is "ok" | "packed" | "low" | "none", and the
    percent is None for everything except "ok".

    Withholding beats reporting. A packed APK exposes only the unpacking stub,
    so a percentage off a denominator of 3 reads better than a real one off
    2,020.

    Accepts anything carrying total_detected_ns / total_3p_ns / framework, which
    is true of both a result dict and a batch row.
    """
    matched = result.get("total_detected_ns", 0) or 0
    total   = result.get("total_3p_ns", 0) or 0
    detail  = (result.get("framework") or {}).get("detail") or {}
    if "packed" in (detail.get("note") or "").lower():
        return None, "packed"
    if total <= 0:
        return None, "none"
    if total < _LOW_SAMPLE_NS:
        return None, "low"
    return round(matched / total * 100, 1), "ok"


def _framework_badge(fw: dict) -> str:
    """The "Built with" bar. Descriptive only -- nothing here feeds matching.

    Three shapes, because the honest answer differs:
      * determined      -> "Built with React Native (Hermes)"
      * hybrid          -> primary, then "with embedded Capacitor", never one
                           merged label; the reason is spelled out under evidence
      * packed DEX      -> "Unknown", the packer named, and no framework guessed
    """
    if not fw:
        return ""
    name   = fw.get("framework") or "Unknown"
    conf   = fw.get("confidence") or "none"
    packer = (fw.get("detail") or {}).get("packer")
    note   = (fw.get("detail") or {}).get("note") or ""
    packed = "packed" in note.lower()

    bits = []
    if fw.get("engine") and fw["engine"] != "N/A":
        bits.append(_esc(fw["engine"]))
    if fw.get("version") and fw["version"] != "N/A":
        bits.append("v" + _esc(fw["version"]))
    meta = (" &nbsp;&middot;&nbsp; " + " &nbsp;&middot;&nbsp; ".join(bits)) if bits else ""

    hybrid = fw.get("hybrid") or []
    hyb_inline = ""
    if hybrid:
        hyb_inline = ('<span class="fw-meta">with embedded '
                      + ", ".join(_esc(h["framework"]) for h in hybrid) + "</span>")

    packed_chip = (f'<span class="fw-packed">DEX packed{" &middot; " + _esc(packer) if packer else ""}</span>'
                   if packed else "")
    conf_chip = (f'<span class="badge {conf}">{_esc(conf)}</span>'
                 if conf in ("high", "medium", "low") else "")

    rows = []
    if fw.get("evidence"):
        rows.append('<div class="fw-ev-row">Signature files: '
                    + "".join(f'<span class="fw-file">{_esc(e)}</span>' for e in fw["evidence"])
                    + "</div>")
    for h in hybrid:
        extra = f' &mdash; {_esc(h["note"])}' if h.get("note") else ""
        rows.append(f'<div class="fw-ev-row"><b>{_esc(h["framework"])}</b> '
                    f'({_esc(h.get("confidence", ""))}): '
                    + "".join(f'<span class="fw-file">{_esc(e)}</span>'
                              for e in h.get("evidence", []))
                    + extra + "</div>")
    for k, v in (fw.get("detail") or {}).items():
        rows.append(f'<div class="fw-ev-row">{_esc(k)}: {_esc(str(v))}</div>')
    if not rows:
        rows.append('<div class="fw-ev-row">No signature file matched.</div>')

    return (
        '<div class="fw-bar" id="fw-bar">'
        '<div class="fw-line">'
        '<span class="fw-label">Built with</span>'
        f'<span class="fw-name">{_esc(name)}</span>'
        f'<span class="fw-meta">{meta}</span>'
        f'{hyb_inline}{conf_chip}{packed_chip}'
        '<button class="fw-toggle" onclick="document.getElementById(\'fw-bar\')'
        '.classList.toggle(\'open\')">Evidence</button>'
        '</div>'
        f'<div class="fw-eviqq">{"".join(rows)}</div>'
        '</div>'
    )


_HTML_BASE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%%REPORT_TITLE%%</title>
<style>
  :root {
    --bg:#f4f6fb; --surface:#ffffff; --surface2:#eef0f8;
    --accent:#c8002a; --accent-dark:#8a001c;
    --text:#1a1d2e; --text2:#4b5270; --text3:#8a91ad;
    --high:#16a34a; --med:#d97706; --low:#dc2626;
    --border:#dde1f0; --shadow:0 1px 4px rgba(0,0,0,.07);
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:'Segoe UI',system-ui,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }
  .header { background:linear-gradient(135deg,var(--accent) 0%,var(--accent-dark) 100%); padding:32px 40px; color:#fff; }
  .header h1 { font-size:1.65rem; font-weight:700; }
  .header .sub { color:rgba(255,255,255,.8); margin-top:5px; font-size:.92rem; }
  .header .meta { display:flex; gap:14px; margin-top:14px; flex-wrap:wrap; }
  .header .meta span { background:rgba(0,0,0,.18); padding:3px 13px; border-radius:20px; font-size:.8rem; }
  .target-badge { display:inline-block; margin-top:12px; background:rgba(255,255,255,.2);
    border:1px solid rgba(255,255,255,.4); padding:4px 16px; border-radius:20px;
    font-size:.82rem; font-weight:600; letter-spacing:.3px; }
  .btn-export { margin-top:16px; display:inline-block; background:#fff; color:var(--accent);
    border:none; padding:9px 22px; border-radius:6px; font-size:.86rem; font-weight:700;
    cursor:pointer; box-shadow:0 2px 6px rgba(0,0,0,.15); transition:opacity .15s; }
  .btn-export:hover { opacity:.87; }
  .container { max-width:100%; margin:0 auto; padding:30px 24px; }
  .stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:13px; margin-bottom:30px; }
  .stat { background:var(--surface); border:1px solid var(--border); border-radius:10px;
          padding:18px 14px; text-align:center; box-shadow:var(--shadow); }
  .stat .num { font-size:2rem; font-weight:700; color:var(--accent); }
  .stat .label { font-size:.74rem; color:var(--text2); margin-top:3px; text-transform:uppercase; letter-spacing:.6px; }
  .stat .sublabel { font-size:.68rem; color:var(--text3); margin-top:5px; letter-spacing:.2px; }
  .stat.clickable { cursor:pointer; text-decoration:none; color:inherit; display:block; transition:box-shadow .15s,transform .15s; }
  .stat.clickable:hover { box-shadow:0 4px 12px rgba(200,0,42,.18); transform:translateY(-2px); }
  .section { margin-bottom:28px; }
  .section-title { font-size:.98rem; font-weight:700; color:var(--text); margin-bottom:13px;
                   padding-bottom:7px; border-bottom:2px solid var(--accent); }
  .kit-card { background:var(--surface); border:1px solid var(--border); border-radius:8px;
              margin-bottom:9px; overflow:hidden; box-shadow:var(--shadow); }
  .kit-header { display:flex; align-items:center; gap:10px; padding:12px 16px;
                background:var(--surface2); cursor:pointer; user-select:none; }
  .kit-header:hover { background:#e5e8f5; }
  .kit-name { font-size:.92rem; font-weight:600; color:#1d4ed8; font-family:monospace; }
  .kit-body { padding:14px 16px; display:none; }
  .kit-card.open .kit-body { display:block; }
  .chevron { margin-left:auto; color:var(--text3); transition:transform .2s; font-size:.85rem; }
  .doc-link { margin-left:6px; color:var(--accent); font-size:.82rem; text-decoration:none;
              border:1px solid var(--border); border-radius:4px; padding:1px 7px;
              font-weight:600; transition:all .15s; }
  .doc-link:hover { color:#fff; background:var(--accent); border-color:var(--accent); }
  .sample-link  { color:#16a34a; border-color:#bbf7d0; }
  .sample-link:hover  { background:#16a34a; border-color:#16a34a; }
  .codelab-link { color:#1d4ed8; border-color:#bfdbfe; }
  .codelab-link:hover { background:#1d4ed8; border-color:#1d4ed8; }
  .kit-card.open .chevron { transform:rotate(180deg); }
  .badge { padding:2px 10px; border-radius:20px; font-size:.68rem; font-weight:700; text-transform:uppercase; letter-spacing:.5px; }
  .badge.high   { background:#dcfce7; color:var(--high); border:1px solid #bbf7d0; }
  .badge.medium { background:#fef3c7; color:var(--med);  border:1px solid #fde68a; }
  .badge.low    { background:#fee2e2; color:var(--low);  border:1px solid #fecaca; }
  .delay-badge  { background:#ede9fe; color:#6d28d9; border:1px solid #ddd6fe;
                  padding:1px 8px; border-radius:20px; font-size:.65rem; font-weight:600; }
  /* "Built with" bar. Descriptive metadata, so it is deliberately neutral slate
     rather than accent red -- red is reserved for HarmonyOS kit chrome. */
  .fw-bar { background:var(--surface); border:1px solid var(--border); border-left:4px solid var(--text2);
            border-radius:7px; padding:13px 17px; margin-bottom:18px; }
  .fw-line { display:flex; align-items:center; gap:11px; flex-wrap:wrap; }
  .fw-label { font-size:.72rem; color:var(--text3); text-transform:uppercase; letter-spacing:.7px; font-weight:700; }
  .fw-name { font-size:1.06rem; font-weight:700; color:var(--text); }
  .fw-meta { font-size:.84rem; color:var(--text2); }
  .fw-packed { background:#fee2e2; color:var(--low); border:1px solid #fecaca;
               padding:2px 10px; border-radius:20px; font-size:.68rem; font-weight:700; }
  .fw-toggle { margin-left:auto; background:none; border:1px solid var(--border); border-radius:5px;
               color:var(--text2); font-size:.75rem; padding:3px 11px; cursor:pointer; }
  .fw-toggle:hover { background:var(--surface2); }
  .fw-eviqq { display:none; margin-top:11px; padding-top:11px; border-top:1px dashed var(--border); }
  .fw-bar.open .fw-eviqq { display:block; }
  .fw-ev-row { font-size:.8rem; color:var(--text2); margin-bottom:5px; }
  .fw-ev-row .mono, .fw-file { font-family:monospace; font-size:.76rem; background:var(--bg);
            border:1px solid var(--border); border-radius:4px; padding:1px 7px; color:var(--text2); margin-right:5px; }
  .import-tag   { background:#eff6ff; border:1px solid #bfdbfe; color:#1d4ed8;
                  border-radius:5px; padding:2px 9px; font-size:.73rem; font-family:monospace; }
  .note { background:#fff5f5; border-left:3px solid var(--accent); padding:7px 12px;
          border-radius:0 5px 5px 0; font-size:.84rem; color:var(--text2); margin-bottom:12px; }
  .source-item { margin-bottom:9px; padding:10px 12px; background:var(--bg);
                 border-radius:6px; border:1px solid var(--border); }
  .source-ns      { font-family:monospace; font-size:.83rem; color:#6d28d9; }
  .source-display { font-size:.8rem; color:var(--text2); margin-top:2px; }
  .source-counts  { font-size:.76rem; color:var(--text3); margin-top:2px; }
  .methods-list { margin-top:6px; }
  .method-tag { display:inline-block; background:var(--surface2); border:1px solid var(--border);
                border-radius:4px; padding:1px 7px; font-size:.7rem; font-family:monospace;
                color:var(--text2); margin:2px; }
  .perm-grid  { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:8px; }
  .perm-item  { background:var(--surface); border:1px solid var(--border); border-radius:7px;
                padding:10px 12px; box-shadow:var(--shadow); }
  .perm-android  { font-family:monospace; font-size:.76rem; color:#dc2626; }
  .perm-arrow    { color:var(--text3); margin:0 5px; }
  .perm-harmony  { font-family:monospace; font-size:.76rem; color:var(--high); }
  .perm-note     { font-size:.72rem; color:var(--text3); margin-top:3px; }
  .tag-list { display:flex; flex-wrap:wrap; gap:6px; }
  .tag { background:var(--surface); border:1px solid var(--border); border-radius:5px;
         padding:3px 9px; font-size:.78rem; font-family:monospace; color:var(--text2); }
  .unmapped-item { background:var(--surface); border:1px solid var(--border); border-radius:7px;
                   padding:10px 12px; margin-bottom:7px; box-shadow:var(--shadow); }
  .unmapped-ns { font-family:monospace; font-size:.83rem; color:var(--med); }
  .pe-meta-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:10px; margin-bottom:20px; }
  .pe-meta-card { background:var(--surface); border:1px solid var(--border); border-radius:8px;
                  padding:12px 16px; box-shadow:var(--shadow); }
  .pe-meta-label { font-size:.72rem; color:var(--text3); text-transform:uppercase; letter-spacing:.5px; }
  .pe-meta-value { font-size:.92rem; font-weight:600; color:var(--text); margin-top:2px; font-family:monospace; }
  .section-table { width:100%; border-collapse:collapse; font-size:.83rem; }
  .section-table th { background:var(--accent); color:#fff; padding:7px 11px; text-align:left; font-weight:600; }
  .section-table td { padding:6px 11px; border-bottom:1px solid var(--border); font-family:monospace; }
  .section-table tr:nth-child(even) td { background:var(--surface2); }
  .xml-block { background:#1e2030; color:#cdd6f4; border-radius:8px; padding:16px 20px;
               font-family:'Cascadia Code','Consolas',monospace; font-size:.76rem;
               overflow-x:auto; white-space:pre; max-height:400px; overflow-y:auto;
               border:1px solid #2d3148; }
  .footer { text-align:center; color:var(--text3); font-size:.78rem; padding:26px;
            border-top:1px solid var(--border); margin-top:14px; }
  .kit-table-wrapper { overflow-x:auto; }
  .kit-table { width:100%; border-collapse:collapse; font-size:.85rem; }
  .kit-table thead th { background:var(--accent); color:#fff; padding:8px 12px; text-align:left; font-weight:600; }
  .kit-table .kit-row { cursor:pointer; background:var(--surface2); }
  .kit-table .kit-row:hover { background:#e5e8f5; }
  .kit-table .kit-row td { padding:10px 12px; border-bottom:1px solid var(--border); vertical-align:middle; }
  .kit-table .kit-row.open .kit-chevron { transform:rotate(180deg); }
  .kit-table .ns-row td { padding:6px 12px 6px 32px; background:var(--surface); border-bottom:1px solid var(--border); }
  .kit-table .kit-row.hidden,.kit-table .ns-row.hidden,.kit-table .inner-row.hidden { display:none; }
  .kit-table .group-row { background:#d7dbef; cursor:pointer; user-select:none; }
  .kit-table .group-row:hover { background:#c9cee8; }
  .kit-table .group-row td { padding:9px 12px; font-weight:700; color:var(--text); border-bottom:1px solid var(--border); }
  .group-chevron { display:inline-block; transition:transform .2s; font-size:.7rem; color:var(--text2); }
  .kit-table .group-row.open .group-chevron { transform:rotate(90deg); }
  .kit-table .inner-row td { padding:4px 12px 4px 56px; background:var(--bg); border-bottom:1px solid var(--border); font-size:.78rem; }
  .kit-table .ns-row.open .ns-chevron { transform:rotate(180deg); }
  .kit-chevron,.ns-chevron { display:inline-block; transition:transform .2s; font-size:.72rem; color:var(--text3); }
  .kit-chevron { float:right; }
  .kit-row-name { font-family:monospace; font-size:.9rem; font-weight:600; color:#1d4ed8; }
  /* OHPM second tier — deliberately NOT accent-red, so it never reads as a native kit table. */
  .ohpm-note { background:#fffbeb; border:1px solid #fde68a; border-left:4px solid var(--med);
    border-radius:6px; padding:10px 14px; margin-bottom:13px; font-size:.82rem; color:var(--text2); }
  .ohpm-note strong { color:var(--med); }
  .ohpm-note code { background:rgba(0,0,0,.06); padding:1px 5px; border-radius:3px; font-size:.78rem; }
  .kit-table.ohpm-table thead th { background:var(--text2); }
  .kit-table.ohpm-table td { padding:8px 12px; border-bottom:1px solid var(--border);
    font-family:monospace; font-size:.8rem; vertical-align:middle; }
  .kit-table.ohpm-table tbody tr:nth-child(even) { background:var(--surface2); }
  .kit-table.ohpm-table code { background:rgba(0,0,0,.05); padding:1px 6px; border-radius:3px; }
  .kit-table.ohpm-table a { color:var(--accent); text-decoration:none; }
  .kit-table.ohpm-table a:hover { text-decoration:underline; }
  .badge.status-green { background:#dcfce7; color:#16a34a; border:1px solid #bbf7d0; }
  .badge.status-amber { background:#fef3c7; color:#d97706; border:1px solid #fde68a; }
  .badge.status-blue  { background:#eff6ff; color:#1d4ed8; border:1px solid #bfdbfe; }
  .section-title { display:flex; justify-content:space-between; align-items:center; }
  .section-title.collapsible { cursor:pointer; user-select:none; }
  .section-toggle { font-size:.75rem; color:var(--text3); transition:transform .15s; }
  .sidebar { position:fixed; top:0; left:0; width:200px; height:100vh; overflow-y:auto;
    background:var(--surface); border-right:1px solid var(--border); padding-top:20px; z-index:100;
    transform:translateX(0); transition:transform .2s ease; box-shadow:0 0 0 rgba(0,0,0,0); }
  .sidebar nav { display:flex; flex-direction:column; }
  .sidebar nav a { color:var(--text2); text-decoration:none; padding:9px 20px; font-size:.82rem;
    border-left:3px solid transparent; transition:color .15s,background .15s; }
  .sidebar nav a:hover { color:var(--accent); }
  .sidebar nav a.active { color:var(--accent); font-weight:700; border-left-color:var(--accent); background:var(--surface2); }
  .container.with-sidebar { margin-left:200px; transition:margin-left .2s ease; }
  body.sidebar-closed .sidebar { transform:translateX(-100%); }
  body.sidebar-closed .container.with-sidebar { margin-left:0; }
  .sidebar-toggle { position:fixed; bottom:18px; left:18px; z-index:300; width:34px; height:34px;
    border:none; border-radius:6px; background:rgba(0,0,0,.85); color:#fff; font-size:1.15rem;
    line-height:1; cursor:pointer; display:flex; align-items:center; justify-content:center;
    transition:background .15s,box-shadow .15s;
    animation:toggle-glow 3.2s ease-in-out infinite; }
  .sidebar-toggle:hover { background:rgba(0,0,0,.8); animation-play-state:paused;
    box-shadow:0 0 11px 3px rgba(200,0,42,.42); }
  .sidebar-toggle:focus-visible { outline:2px solid rgba(200,0,42,.9); outline-offset:2px; }
  @keyframes toggle-glow {
    0%,100% { box-shadow:0 0 4px 0 rgba(200,0,42,.16); }
    50%     { box-shadow:0 0 12px 3px rgba(200,0,42,.36); }
  }
  @media (prefers-reduced-motion: reduce) {
    .sidebar-toggle { animation:none; box-shadow:0 0 6px 1px rgba(200,0,42,.24); }
  }
  .header.with-toggle { padding-left:74px; margin-left:200px; transition:margin-left .2s ease; }
  body.sidebar-closed .header.with-toggle { margin-left:0; }
  @media(max-width:768px){
    .sidebar { transform:translateX(-100%); box-shadow:2px 0 14px rgba(0,0,0,.2); }
    .container.with-sidebar { margin-left:0; }
    .header.with-toggle { margin-left:0; }
    body.sidebar-open .sidebar { transform:translateX(0); }
  }
  @media(max-width:600px){ .header{padding:20px;} .container{padding:14px;} }
  @media (max-width: 767px) {
    .sidebar { display: none; }
    .main-content { margin-left: 0 !important; }
    .container { padding: 14px; }
    .header { padding: 20px; }
  }
</style>
</head>
<body class="sidebar-closed">
%%SIDEBAR_TOGGLE_HTML%%
<div class="header %%HEADER_EXTRA_CLASS%%">
  <h1>%%REPORT_HEADING%%</h1>
  <div class="sub">%%REPORT_SUB%%</div>
  <div class="meta">%%HEADER_META%%</div>
  <div class="target-badge">%%TARGET_LABEL%%</div><br>
  <button class="btn-export" onclick="exportExcel()">Export to Excel</button>
</div>

%%SIDEBAR_HTML%%
<div class="container %%CONTAINER_EXTRA_CLASS%%">
  <div class="stats">%%STAT_CARDS%%</div>
  %%BODY_SECTIONS%%
</div>

<div class="footer">
  Huawei DTSE Turkey &nbsp;&middot;&nbsp; Migration Analyzer v2.0 &nbsp;&middot;&nbsp; %%REPORT_DATE%%
</div>

<script>
const REPORT_DATA = %%REPORT_DATA_JSON%%;
document.querySelectorAll('.kit-header').forEach(h =>
  h.addEventListener('click', () => h.closest('.kit-card').classList.toggle('open')));
if (REPORT_DATA.mode !== 'apk') {
  document.querySelectorAll('.kit-card[data-confidence="high"]').forEach(c => c.classList.add('open'));
}

function revealSection(id){
  const el=document.getElementById(id);
  if(!el)return;
  el.style.display='block';
  setTimeout(()=>el.scrollIntoView({behavior:'smooth',block:'start'}),50);
}
function collapseChildren(parentRow){
  if(!parentRow)return;
  const m=parentRow.id.match(/^group-row-(\d+)$/);
  if(m){
    document.querySelectorAll('.group-child-'+m[1]).forEach(child=>{
      child.classList.add('hidden');
      child.classList.remove('open');
      collapseChildren(child);
    });
    return;
  }
  const k=parentRow.id.match(/^kit-row-(\d+)$/);
  if(k){
    document.querySelectorAll('.ns-group-'+k[1]).forEach(child=>{
      child.classList.add('hidden');
      child.classList.remove('open');
      collapseChildren(child);
    });
    return;
  }
  const n=parentRow.id.match(/^ns-row-(\d+)-(\d+)$/);
  if(n){
    document.querySelectorAll('.inner-group-'+n[1]+'-'+n[2]).forEach(child=>{
      child.classList.add('hidden');
    });
  }
}
function toggleKitRow(idx){
  const r=document.getElementById('kit-row-'+idx);
  if(!r)return;
  const open=r.classList.toggle('open');
  document.querySelectorAll('.ns-group-'+idx).forEach(el=>el.classList.toggle('hidden',!open));
  if(!open) collapseChildren(r);
}
function toggleNsRow(ki,ni){
  const r=document.getElementById('ns-row-'+ki+'-'+ni);
  if(!r)return;
  const open=r.classList.toggle('open');
  document.querySelectorAll('.inner-group-'+ki+'-'+ni).forEach(el=>el.classList.toggle('hidden',!open));
  if(!open) collapseChildren(r);
}
function toggleSidebar(){
  const isDesktop = window.matchMedia('(min-width:769px)').matches;
  const b = document.body;
  if(isDesktop){
    b.classList.remove('sidebar-open');
    b.classList.toggle('sidebar-closed');
  } else {
    b.classList.remove('sidebar-closed');
    b.classList.toggle('sidebar-open');
  }
}
function toggleGroupRow(gi){
  const r=document.getElementById('group-row-'+gi);
  if(!r)return;
  const open=r.classList.toggle('open');
  document.querySelectorAll('.group-child-'+gi).forEach(el=>el.classList.toggle('hidden',!open));
  if(!open) collapseChildren(r);
}
function toggleDllRow(i){
  const r=document.getElementById('dll-row-'+i);
  if(!r)return;
  const open=r.classList.toggle('open');
  const d=document.getElementById('dll-detail-'+i);
  if(d) d.classList.toggle('hidden',!open);
}
function toggleSection(id){
  const body=document.getElementById('body-'+id);
  if(!body)return;
  const collapsed=body.style.display==='none';
  body.style.display=collapsed?'':'none';
  const toggle=document.querySelector('#'+id+' .section-toggle');
  if(toggle) toggle.innerHTML=collapsed?'&#9660;':'&#9654;';
}
(function(){
  const navLinks=document.querySelectorAll('.sidebar nav a');
  if(!navLinks.length)return;
  const map={};
  navLinks.forEach(a=>{
    map[a.getAttribute('href').slice(1)]=a;
    a.addEventListener('click', ()=>{
      if(window.matchMedia('(max-width:768px)').matches) document.body.classList.remove('sidebar-open');
    });
  });
  const observer=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      const link=map[e.target.id];
      if(!link)return;
      if(e.isIntersecting){
        navLinks.forEach(a=>a.classList.remove('active'));
        link.classList.add('active');
      }
    });
  }, {rootMargin:'-20% 0px -70% 0px', threshold:0});
  Object.keys(map).forEach(id=>{
    const el=document.getElementById(id);
    if(el) observer.observe(el);
  });
})();

function exportExcel() {
  if (typeof XLSX !== 'undefined') { buildExcel(); return; }
  const s = document.createElement('script');
  s.src = 'https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js';
  s.onload = buildExcel;
  document.head.appendChild(s);
}

function buildExcel() {
  const wb = XLSX.utils.book_new();
  const d  = REPORT_DATA;

  if (d.mode === 'ipa') {
    const ov = [
      ['IPA → HarmonyOS NEXT Migration Report'], [],
      ['Field','Value'],
      ['File', d.file_name],
      ['Bundle ID', d.bundle_id || '—'],
      ['App Name', d.app_name || '—'],
      ['Version', d.version || '—'],
      ['Min iOS Version', d.min_ios_version || '—'],
      ['Analysis Date', d.report_date],
      ['Analysis Time (s)', d.analysis_time_sec],
      [], ['Metric','Count'],
      ['Kit Matches', d.kit_matches.length],
      ['Frameworks (total)', d.frameworks.length],
      ['Unmapped Frameworks', d.unmapped_frameworks.length],
      ['Permissions (total)', d.permissions.length],
      ['Permission Matches', d.permission_matches.length],
    ];
    const ws1 = XLSX.utils.aoa_to_sheet(ov);
    ws1['!cols'] = [{wch:28},{wch:52}];
    XLSX.utils.book_append_sheet(wb, ws1, 'Overview');

    const km_rows = [['Framework Name','Framework Display','HarmonyOS Kit','Import Path','Coverage','Recommendation']];
    d.kit_matches.forEach(km => km.framework_sources.forEach(src =>
      km_rows.push([src.framework_name, src.framework_display, km.kit_name,
        km.harmony_import||'', km.confidence, km.note])));
    const ws2 = XLSX.utils.aoa_to_sheet(km_rows);
    ws2['!cols'] = [{wch:28},{wch:36},{wch:32},{wch:28},{wch:12},{wch:55}];
    XLSX.utils.book_append_sheet(wb, ws2, 'Kit Matches');

    const pm_rows = [['iOS Key','iOS Display','HarmonyOS Permission','HarmonyOS Kit']];
    const mapped_keys = new Set(d.permission_matches.map(p=>p.ios_key));
    d.permission_matches.forEach(p => pm_rows.push([p.ios_key, p.ios_display||'', p.harmony||'', p.kit||'']));
    d.permissions.filter(p=>!mapped_keys.has(p)).forEach(p => pm_rows.push([p,'—','—','—']));
    const ws3 = XLSX.utils.aoa_to_sheet(pm_rows);
    ws3['!cols'] = [{wch:50},{wch:32},{wch:50},{wch:28}];
    XLSX.utils.book_append_sheet(wb, ws3, 'Permissions');

  } else if (d.mode === 'exe') {
    const ov = [
      ['EXE → HarmonyOS NEXT Migration Report'], [],
      ['Field','Value'],
      ['File', d.file_name],
      ['Architecture', d.machine],
      ['Subsystem', d.subsystem],
      ['Entry Point', d.entry_point],
      ['Image Base', d.image_base],
      ['Image Size (bytes)', d.image_size],
      ['Timestamp', d.timestamp],
      ['Is DLL', d.is_dll ? 'Yes' : 'No'],
      ['Is .NET', d.is_dotnet ? 'Yes' : 'No'],
      [], ['Version Info'],
    ];
    Object.entries(d.version_info||{}).forEach(([k,v]) => ov.push([k, v]));
    ov.push([], ['Metric','Count'],
      ['Kit Matches', d.kit_matches.length],
      ['Unmapped DLLs', d.unmapped_dlls.length],
      ['Total Imported DLLs', Object.keys(d.imports||{}).length],
      ['Exported Symbols', (d.exports||[]).length],
    );
    const ws1 = XLSX.utils.aoa_to_sheet(ov);
    ws1['!cols'] = [{wch:28},{wch:52}];
    XLSX.utils.book_append_sheet(wb, ws1, 'Overview');

    const km_rows = [['DLL Name','DLL Description','HarmonyOS Kit','Import Path','Coverage','Recommendation','Delay Import']];
    d.kit_matches.forEach(km => km.dll_sources.forEach(src =>
      km_rows.push([src.dll_name, src.dll_display, km.kit_name,
        km.harmony_import||'', km.confidence,
        km.note, src.is_delay ? 'Yes' : 'No'])));
    const ws2 = XLSX.utils.aoa_to_sheet(km_rows);
    ws2['!cols'] = [{wch:28},{wch:36},{wch:32},{wch:28},{wch:12},{wch:55},{wch:14}];
    XLSX.utils.book_append_sheet(wb, ws2, 'Kit Matches');

    const imp_rows = [['DLL','Function','Type']];
    Object.entries(d.imports||{}).forEach(([dll,funcs]) =>
      funcs.forEach(f => imp_rows.push([dll, f, 'Import'])));
    Object.entries(d.delay_imports||{}).forEach(([dll,funcs]) =>
      funcs.forEach(f => imp_rows.push([dll, f, 'Delay Import'])));
    const ws3 = XLSX.utils.aoa_to_sheet(imp_rows);
    ws3['!cols'] = [{wch:36},{wch:48},{wch:14}];
    XLSX.utils.book_append_sheet(wb, ws3, 'Imports');

    const un_rows = [['DLL Name','Function Count','Sample Functions','Delay Import']];
    (d.unmapped_dlls||[]).forEach(u =>
      un_rows.push([u.dll_name, u.func_count, (u.sample_funcs||[]).join(', '), u.is_delay ? 'Yes' : 'No']));
    const ws4 = XLSX.utils.aoa_to_sheet(un_rows);
    ws4['!cols'] = [{wch:34},{wch:14},{wch:60},{wch:14}];
    XLSX.utils.book_append_sheet(wb, ws4, 'Unmapped DLLs');

  } else if (d.mode === 'exe_folder') {
    const ov = [
      ['EXE Folder → HarmonyOS NEXT Migration Report'], [],
      ['Folder', d.folder_name],
      ['Files Analyzed', d.file_count],
      ['Analysis Date', d.report_date],
      ['Analysis Time (s)', d.analysis_time_sec],
      [], ['Metric','Count'],
      ['Kit Matches', d.kit_matches.length],
      ['Unmapped DLLs', d.unmapped_dlls.length],
      ['Total Imported DLLs', Object.keys(d.imports||{}).length],
    ];
    const ws1 = XLSX.utils.aoa_to_sheet(ov);
    ws1['!cols'] = [{wch:28},{wch:52}];
    XLSX.utils.book_append_sheet(wb, ws1, 'Overview');

    const f_rows = [['File','Architecture','Subsystem','Type','Packed','Packer Hint','Error']];
    (d.files||[]).forEach(f => f_rows.push([
      f.file_name, f.machine||'', f.is_dll ? 'N/A (library)' : (f.subsystem||''),
      f.is_dll ? 'DLL' : 'EXE', f.is_packed ? 'Yes' : 'No',
      f.packer_hint || '', f.error || '',
    ]));
    const wsF = XLSX.utils.aoa_to_sheet(f_rows);
    wsF['!cols'] = [{wch:30},{wch:16},{wch:20},{wch:10},{wch:10},{wch:30},{wch:40}];
    XLSX.utils.book_append_sheet(wb, wsF, 'Files');

    const km_rows = [['DLL Name','DLL Description','Source Files','HarmonyOS Kit','Import Path','Coverage','Recommendation','Delay Import']];
    d.kit_matches.forEach(km => km.dll_sources.forEach(src =>
      km_rows.push([src.dll_name, src.dll_display, (src.source_files||[]).join(', '), km.kit_name,
        km.harmony_import||'', km.confidence,
        km.note, src.is_delay ? 'Yes' : 'No'])));
    const ws2 = XLSX.utils.aoa_to_sheet(km_rows);
    ws2['!cols'] = [{wch:28},{wch:36},{wch:30},{wch:32},{wch:28},{wch:12},{wch:55},{wch:14}];
    XLSX.utils.book_append_sheet(wb, ws2, 'Kit Matches');

    const imp_rows = [['DLL','Function','Type','Source Files']];
    Object.entries(d.imports||{}).forEach(([dll,funcs]) => {
      const isDelay = (d.delay_dlls||[]).includes(dll);
      const srcs = (d.import_sources||{})[dll] || [];
      funcs.forEach(f => imp_rows.push([dll, f, isDelay ? 'Delay Import' : 'Import', srcs.join(', ')]));
    });
    const ws3 = XLSX.utils.aoa_to_sheet(imp_rows);
    ws3['!cols'] = [{wch:36},{wch:48},{wch:14},{wch:40}];
    XLSX.utils.book_append_sheet(wb, ws3, 'Imports');

    const un_rows = [['DLL Name','Function Count','Source Files','Sample Functions','Delay Import']];
    (d.unmapped_dlls||[]).forEach(u =>
      un_rows.push([u.dll_name, u.func_count, (u.source_files||[]).join(', '), (u.sample_funcs||[]).join(', '), u.is_delay ? 'Yes' : 'No']));
    const ws4 = XLSX.utils.aoa_to_sheet(un_rows);
    ws4['!cols'] = [{wch:34},{wch:14},{wch:30},{wch:60},{wch:14}];
    XLSX.utils.book_append_sheet(wb, ws4, 'Unmapped DLLs');

  } else {
    const isHmos = d.target === 'hmos';
    const ov = [
      ['APK Migration Report -- ' + (isHmos ? 'HarmonyOS NEXT' : 'HMS Core')], [],
      ['Field','Value'],
      ['App Name',d.app_name],['Package',d.package_name],
      ['Version',d.version_name+' (build '+d.version_code+')'],
      ['Min SDK',d.min_sdk],['Target SDK',d.target_sdk],
      ['Analysis Date',d.report_date],['Analysis Time (s)',d.analysis_time_sec],
      [],['Metric','Count'],
      ['Kit Matches',d.kit_matches.length],
      ['Mapped Namespace Rows',d.kit_matches.reduce((n,km)=>n+(km.android_sources||[]).length,0)],
      ['3rd Party (OHPM)',(d.ohpm_matches||[]).length],
      ['Built With',(d.framework||{}).framework||'N/A'],
      ['Permission Matches',d.permission_matches.length],
      ['Total Permissions',d.permissions.length],
      ['Native .so Libraries',d.native_libs.length],
      ['Private Libs',(d.private_libs||[]).length],
    ];
    const ws1 = XLSX.utils.aoa_to_sheet(ov);
    ws1['!cols'] = [{wch:28},{wch:52}];
    XLSX.utils.book_append_sheet(wb, ws1, 'Overview');

    const kitCol = isHmos ? 'HarmonyOS Kit' : 'HMS Kit';
    const confStatusMap = {high:'Supported', medium:'Replaceable', low:'Should Confirm'};
    const km_rows = [['Android Library / Namespace','Android Display Name',
      kitCol, isHmos?'Import Path':'', 'Status','Recommendation','Status']];
    d.kit_matches.forEach(km => km.android_sources.forEach(src =>
      km_rows.push([src.android_namespace, src.android_display,
        km.kit_name, isHmos?(km.harmony_import||''):'',
        confStatusMap[km.confidence] || 'Should Confirm',
        km.note, km.status||''])));
    const ws2 = XLSX.utils.aoa_to_sheet(km_rows);
    ws2['!cols'] = [{wch:42},{wch:34},{wch:30},{wch:28},{wch:12},{wch:55},{wch:16}];
    XLSX.utils.book_append_sheet(wb, ws2, 'Kit Matches');

    // Second tier. REPORT_DATA has carried ohpm_matches since phase 3B but no
    // sheet was ever written from it, so the tier existed only in the batch
    // workbook. Skipped when empty, matching the report's own section.
    if ((d.ohpm_matches||[]).length) {
      const oh_rows = [['Android Namespace','OHPM Package','Install Command','Category',
        'Confidence','Class Count','Method Count','Sample Methods','Repository']];
      d.ohpm_matches.forEach(om => oh_rows.push([om.namespace, om.ohpm_package,
        om.install_cmd||'', om.category||'--', om.confidence||'',
        om.class_count, om.method_count, (om.sample_methods||[]).join(', '),
        om.source_repo||'--']));
      const wso = XLSX.utils.aoa_to_sheet(oh_rows);
      wso['!cols'] = [{wch:44},{wch:30},{wch:34},{wch:30},{wch:12},{wch:12},{wch:13},{wch:55},{wch:40}];
      XLSX.utils.book_append_sheet(wb, wso, '3rd Party (OHPM)');
    }

    const hdrs = isHmos
      ? ['Android Permission','HarmonyOS Permission','HarmonyOS Kit','Status']
      : ['Android Permission','HMS Note','Status'];
    const pm_rows = [hdrs];
    const mapped = new Set(d.permission_matches.map(p=>p.android));
    if (isHmos) {
      d.permission_matches.forEach(p => pm_rows.push([p.android,p.harmony||'',p.kit||'','Mapped']));
      d.permissions.filter(p=>!mapped.has(p)).forEach(p => pm_rows.push([p,'--','--','No mapping']));
    } else {
      d.permission_matches.forEach(p => pm_rows.push([p.android,p.hms_note||'','Noted']));
      d.permissions.filter(p=>!mapped.has(p)).forEach(p => pm_rows.push([p,'--','No mapping']));
    }
    const ws3 = XLSX.utils.aoa_to_sheet(pm_rows);
    ws3['!cols'] = isHmos ? [{wch:52},{wch:52},{wch:30},{wch:14}] : [{wch:52},{wch:60},{wch:14}];
    XLSX.utils.book_append_sheet(wb, ws3, 'Permissions');

    const un_rows = [['Namespace','Class Count','Method Count','Sample Methods']];
    (d.unmapped_namespaces||[]).forEach(u =>
      un_rows.push([u.namespace, u.class_count, u.method_count, (u.sample_methods||[]).join(', ')]));
    const ws4 = XLSX.utils.aoa_to_sheet(un_rows);
    ws4['!cols'] = [{wch:50},{wch:12},{wch:14},{wch:60}];
    XLSX.utils.book_append_sheet(wb, ws4, 'Unmapped Libraries');

    const fl_rows = [['Obfuscated Count', d.obfuscated_count||0],[],
      ['Namespace','Class Count','Method Count','Sample Methods']];
    (d.unresolvable_namespaces||[]).forEach(u =>
      fl_rows.push([u.namespace, u.class_count, u.method_count, (u.sample_methods||[]).join(', ')]));
    const ws5 = XLSX.utils.aoa_to_sheet(fl_rows);
    ws5['!cols'] = [{wch:50},{wch:12},{wch:14},{wch:60}];
    XLSX.utils.book_append_sheet(wb, ws5, 'Filtered Libraries');

    const pl_rows = [['Namespace','Class Count','Method Count','Sample Methods']];
    (d.private_libs||[]).forEach(pl =>
      pl_rows.push([pl.namespace, pl.class_count, pl.method_count, (pl.sample_methods||[]).join(', ')]));
    const ws6 = XLSX.utils.aoa_to_sheet(pl_rows);
    ws6['!cols'] = [{wch:50},{wch:12},{wch:14},{wch:60}];
    XLSX.utils.book_append_sheet(wb, ws6, 'Custom Private Libs');
  }

  XLSX.writeFile(wb, 'migration_report.xlsx');
}
</script>
</body>
</html>
"""


def _render_kit_cards(kit_matches, mode="apk", is_hmos=True) -> str:
    cards = []
    for km in kit_matches:
        sources_html = ""
        if mode == "apk":
            for src in km["android_sources"]:
                methods = "".join(
                    f'<span class="method-tag">{_esc(m.split(".")[-1] if "." in m else m)}</span>'
                    for m in src["sample_methods"]
                )
                sources_html += (
                    f'<div class="source-item">'
                    f'<div class="source-ns">{_esc(src["android_namespace"])}</div>'
                    f'<div class="source-display">{_esc(src["android_display"])}</div>'
                    f'<div class="source-counts">{src["class_count"]} classes &middot; {src["method_count"]} method calls</div>'
                    f'<div class="methods-list">{methods}</div></div>'
                )
        elif mode == "ipa":
            for src in km["framework_sources"]:
                sources_html += (
                    f'<div class="source-item">'
                    f'<div class="source-ns">{_esc(src["framework_name"])}</div>'
                    f'<div class="source-display">{_esc(src["framework_display"])}</div>'
                    f'</div>'
                )
        else:
            for src in km["dll_sources"]:
                delay = '<span class="delay-badge">delay</span> ' if src["is_delay"] else ""
                src_files = src.get("source_files")
                src_files_html = (
                    f'<div class="source-counts">from: {_esc(", ".join(src_files))}</div>'
                    if src_files else ""
                )
                sources_html += (
                    f'<div class="source-item">'
                    f'<div class="source-ns">{delay}{_esc(src["dll_name"])}</div>'
                    f'<div class="source-display">{_esc(src["dll_display"])}</div>'
                    f'<div class="source-counts">{src["func_count"]} imported functions</div>'
                    f'{src_files_html}'
                    f'</div>'
                )

        import_tag = ""
        if km.get("harmony_import"):
            import_tag = f'<span class="import-tag">{_esc(km["harmony_import"])}</span>'

        if mode == "exe" and km.get("status"):
            badge = f'<span class="badge status-{km["status_color"]}">{_esc(km["status"])}</span>'
        else:
            badge = confidence_badge(km["confidence"])

        _target  = "hms" if (mode == "apk" and not is_hmos) else "hmos"
        doc_url  = get_doc_url(km["kit_name"], _target)
        doc_link = (
            f'<a class="doc-link" href="{doc_url}" target="_blank" title="Official documentation">'
            f'&#8599;</a>'
            if doc_url else ""
        )
        sample_url  = km.get("sample_url")
        sample_link = (
            f'<a class="doc-link sample-link" href="{sample_url}" target="_blank" title="Sample code">'
            f'&#123;&#125; Sample</a>'
            if sample_url else ""
        )
        codelab_url  = km.get("codelab_url")
        codelab_link = (
            f'<a class="doc-link codelab-link" href="{codelab_url}" target="_blank" title="Codelab">'
            f'&#9654; Codelab</a>'
            if codelab_url else ""
        )
        cards.append(
            f'<div class="kit-card" data-confidence="{km["confidence"]}">'
            f'<div class="kit-header">'
            f'<span class="kit-name">{_esc(km["kit_name"])}</span>{import_tag}{badge}'
            f'{doc_link}{sample_link}{codelab_link}'
            f'<span class="chevron">&#9660;</span></div>'
            f'<div class="kit-body"><div class="note">{_esc(km["note"])}</div>{sources_html}</div></div>'
        )
    return "\n".join(cards)


_SENTENCE_SPLIT = re.compile(r'(?<=[.!?])\s+')


def _first_two_sentences(text: str) -> str:
    if not text:
        return ""
    parts = _SENTENCE_SPLIT.split(text.strip())
    return " ".join(parts[:2]).strip()


def _flatten_namespace_rows(kit_matches: list) -> list:
    rows = [
        (km, src)
        for km in kit_matches
        for src in km.get("android_sources", [])
    ]
    rows.sort(key=lambda pair: pair[1]["android_namespace"])
    return rows


_GENERIC_ROOTS = {"com", "org", "net", "io"}


def _group_root(ns: str) -> str:
    parts = ns.split(".")
    if parts[0] in _GENERIC_ROOTS and len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}"
    return parts[0]


def _render_kit_table_apk(flat_rows: list, ns_lookup: dict, is_hmos: bool = True) -> str:
    if not flat_rows:
        return '<p style="color:var(--text3);font-size:.85rem">No kit matches found.</p>'

    _target = "hmos" if is_hmos else "hms"

    groups: dict = {}
    for ri, (km, src) in enumerate(flat_rows):
        groups.setdefault(_group_root(src["android_namespace"]), []).append(ri)

    rows: list = []

    for gi, (group_name, ri_list) in enumerate(groups.items()):
        rows.append(
            f'<tr class="group-row" id="group-row-{gi}" onclick="toggleGroupRow({gi})">'
            f'<td colspan="6">'
            f'<span class="group-chevron">&#9654;</span> '
            f'<span>{_esc(group_name)}</span> '
            f'<span style="font-weight:400;color:var(--text2);font-size:.78rem">'
            f'({len(ri_list)} namespace{"s" if len(ri_list) != 1 else ""})</span>'
            f'</td></tr>'
        )
        for ri in ri_list:
            km, src = flat_rows[ri]
            ns_entry   = ns_lookup.get(src["android_namespace"], {})
            note       = ns_entry.get("note") or km.get("note", "")
            sample_url = ns_entry.get("sample_url") or km.get("sample_url")
            status     = km.get("status", "Should Confirm")
            s_color    = km.get("status_color", "blue")

            doc_url     = get_doc_url(km["kit_name"], _target)
            doc_link    = (f'<a class="doc-link" href="{doc_url}" target="_blank">Official Docs</a>'
                           if doc_url else "")
            sample_link = (f'<a class="doc-link sample-link" href="{sample_url}" target="_blank">Sample App</a>'
                           if sample_url else "")

            import_tag = ""
            if km.get("harmony_import") and is_hmos:
                import_tag = f' <span class="import-tag">{_esc(km["harmony_import"])}</span>'

            note_html = (
                f'<div style="font-size:.78rem;color:var(--text2);margin-top:4px;">'
                f'{_esc(_first_two_sentences(note))}</div>'
                if note else ""
            )

            sample_methods = src.get("sample_methods", [])
            has_children   = bool(sample_methods)
            row_onclick    = f' onclick="toggleKitRow({ri})"' if has_children else ""
            row_cursor     = "cursor:pointer;" if has_children else ""
            chevron        = '<span class="kit-chevron">&#9660;</span>' if has_children else ""

            rows.append(
                f'<tr class="kit-row hidden group-child-{gi}" id="kit-row-{ri}"{row_onclick} style="{row_cursor}">'
                f'<td style="padding-left:28px">'
                f'<span class="ns-name" style="font-family:monospace;color:#6d28d9;font-size:.87rem">'
                f'{_esc(src["android_namespace"])}</span>'
                f'<div class="source-display">{_esc(src["android_display"])}</div>'
                f'{note_html}'
                f'</td>'
                f'<td class="source-counts" style="white-space:nowrap">{src["class_count"]} cls &middot; {src["method_count"]} calls</td>'
                f'<td><span class="kit-row-name">{_esc(km["kit_name"])}</span>{import_tag}</td>'
                f'<td><span class="badge status-{s_color}">{_esc(status)}</span></td>'
                f'<td style="white-space:nowrap">{doc_link} {sample_link}</td>'
                f'<td style="width:24px;text-align:right">{chevron}</td>'
                f'</tr>'
            )

            inner_methods = src.get("inner_methods", [])
            for mi, method in enumerate(sample_methods):
                inner_matches = [im for im in inner_methods if im["method_name"] == method]
                has_inner  = bool(inner_matches)
                ns_onclick = (f' onclick="event.stopPropagation();toggleNsRow({ri},{mi})"'
                              if has_inner else "")
                ns_cursor  = "cursor:pointer;" if has_inner else ""
                ns_chevron = '<span class="ns-chevron">&#9660;</span>' if has_inner else ""

                rows.append(
                    f'<tr class="ns-row hidden ns-group-{ri}" id="ns-row-{ri}-{mi}"'
                    f'{ns_onclick} style="{ns_cursor}">'
                    f'<td colspan="6">'
                    f'<span class="ns-name" style="font-family:monospace;color:#6d28d9;font-size:.82rem">'
                    f'{_esc(method)}</span>'
                    f' {ns_chevron}'
                    f'</td></tr>'
                )

                for im in inner_matches:
                    # The HarmonyOS side, NOT im["method_name"] -- that is the
                    # Android method already printed by the ns-row above, so
                    # printing it again made level 3 a duplicate of level 2.
                    hmos = im.get("hmos_method") or ""
                    st   = im.get("status", "Supported")
                    sc   = im.get("status_color", "green")
                    body = (f'<span style="font-family:monospace;font-size:.75rem;color:var(--text2)">'
                            f'{_esc(hmos)}</span> <span class="badge status-{sc}">{_esc(st)}</span>'
                            if hmos else
                            '<span style="font-size:.75rem;color:var(--text3)">'
                            'No import statement recorded for this API</span>')
                    rows.append(
                        f'<tr class="inner-row hidden inner-group-{ri}-{mi}">'
                        f'<td colspan="6" style="padding-left:44px">'
                        f'<span style="color:var(--text3);margin-right:6px">&rarr;</span>'
                        f'{body}'
                        f'</td></tr>'
                    )

    return (
        f'<div class="kit-table-wrapper">'
        f'<table class="kit-table">'
        f'<thead><tr>'
        f'<th>Namespaces</th><th>Count</th><th>HarmonyOS Kit</th>'
        f'<th>Status</th><th>Links</th><th></th>'
        f'</tr></thead>'
        f'<tbody>{"".join(rows)}</tbody>'
        f'</table>'
        f'</div>'
    )


def _flatten_dll_rows(kit_matches: list) -> list:
    rows = [
        (km, src)
        for km in kit_matches
        for src in km.get("dll_sources", [])
    ]
    rows.sort(key=lambda pair: pair[1]["dll_name"])
    return rows


def _group_dll_families(dll_names: list, min_group_size: int = 3) -> dict:
    stems = {name: re.sub(r'\.dll$', '', name, flags=re.IGNORECASE).split('-') for name in dll_names}
    assigned: set = set()
    family_of: dict = {}
    max_tokens = max((len(toks) for toks in stems.values()), default=0)

    for k in range(max_tokens, 1, -1):
        buckets: dict = {}
        for name, toks in stems.items():
            if name in assigned or len(toks) <= k:
                continue
            key = tuple(t.lower() for t in toks[:k])
            buckets.setdefault(key, []).append(name)
        for key, names in buckets.items():
            if len(names) >= min_group_size:
                label = "-".join(key) + "-*"
                for name in names:
                    family_of[name] = label
                assigned.update(names)

    return family_of


def _render_kit_table_exe(kit_matches: list) -> str:
    flat_rows = _flatten_dll_rows(kit_matches)
    if not flat_rows:
        return '<p style="color:var(--text3);font-size:.85rem">No kit matches found.</p>'

    family_of = _group_dll_families([src["dll_name"] for _, src in flat_rows])
    group_index_by_label: dict = {}

    rows = []
    for i, (km, src) in enumerate(flat_rows):
        dll_name = src["dll_name"]
        label = family_of.get(dll_name)
        group_idx = None

        if label is not None:
            if label not in group_index_by_label:
                group_idx = len(group_index_by_label)
                group_index_by_label[label] = group_idx
                member_count = sum(1 for v in family_of.values() if v == label)
                rows.append(
                    f'<tr class="group-row" id="group-row-{group_idx}" onclick="toggleGroupRow({group_idx})">'
                    f'<td colspan="6">'
                    f'<span class="group-chevron">&#9654;</span> '
                    f'<span>{_esc(label)}</span> '
                    f'<span style="font-weight:400;color:var(--text2);font-size:.78rem">'
                    f'({member_count} file{"s" if member_count != 1 else ""})</span>'
                    f'</td></tr>'
                )
            else:
                group_idx = group_index_by_label[label]

        delay = '<span class="delay-badge">delay</span> ' if src.get("is_delay") else ""

        doc_url  = get_doc_url(km["kit_name"], "hmos")
        doc_link = (f'<a class="doc-link" href="{doc_url}" target="_blank">Official Docs</a>'
                    if doc_url else "")
        sample_url  = km.get("sample_url")
        sample_link = (f'<a class="doc-link sample-link" href="{sample_url}" target="_blank">Sample App</a>'
                       if sample_url else "")

        status  = km.get("status", "Should Confirm")
        s_color = km.get("status_color", "blue")

        source_files = src.get("source_files")
        has_children = bool(source_files)
        row_onclick  = f' onclick="toggleDllRow({i})"' if has_children else ""
        row_cursor   = "cursor:pointer;" if has_children else ""
        chevron      = '<span class="kit-chevron">&#9660;</span>' if has_children else ""

        row_classes = "kit-row"
        row_cell_style = row_cursor
        if group_idx is not None:
            row_classes += f" hidden group-child-{group_idx}"
            row_cell_style = f"padding-left:28px;{row_cursor}"

        rows.append(
            f'<tr class="{row_classes}" id="dll-row-{i}"{row_onclick} style="{row_cell_style}">'
            f'<td>'
            f'<span class="ns-name" style="font-family:monospace;color:#6d28d9;font-size:.87rem">'
            f'{delay}{_esc(src["dll_name"])}</span>'
            f'<div class="source-display">{_esc(src.get("dll_display",""))}</div>'
            f'</td>'
            f'<td class="source-counts" style="white-space:nowrap">{src["func_count"]} funcs</td>'
            f'<td><span class="import-tag">{_esc(km["kit_name"])}</span></td>'
            f'<td><span class="badge status-{s_color}">{_esc(status)}</span></td>'
            f'<td style="white-space:nowrap">{doc_link} {sample_link}</td>'
            f'<td style="width:24px;text-align:right">{chevron}</td>'
            f'</tr>'
        )

        if source_files:
            detail_classes = "ns-row hidden"
            if group_idx is not None:
                detail_classes += f" group-child-{group_idx}"
            rows.append(
                f'<tr class="{detail_classes}" id="dll-detail-{i}">'
                f'<td colspan="6">'
                f'<span style="font-size:.78rem;color:var(--text2)">Found in: '
                f'{_esc(", ".join(source_files))}</span>'
                f'</td></tr>'
            )

    return (
        f'<div class="kit-table-wrapper">'
        f'<table class="kit-table">'
        f'<thead><tr>'
        f'<th>DLLs</th><th>Count</th><th>HarmonyOS Kit</th>'
        f'<th>Status</th><th>Links</th><th></th>'
        f'</tr></thead>'
        f'<tbody>{"".join(rows)}</tbody>'
        f'</table>'
        f'</div>'
    )


def _render_ohpm_table(ohpm_matches: list) -> str:
    """Second-tier OHPM suggestions.

    Deliberately styled apart from the native kit table -- amber lead-in, neutral
    header -- so it cannot be mistaken for a native @kit.* match. Native kits
    stay the recommendation.
    """
    if not ohpm_matches:
        return ""

    # Group by package, mirroring how the native kit table groups by kit — an app
    # pulling one library shows one row, not 20 near-identical sub-namespace rows.
    groups: dict = {}
    for m in ohpm_matches:
        groups.setdefault(m["ohpm_package"], []).append(m)
    ordered = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    # Offset the group ids so they cannot collide with the native table's, which
    # shares the same toggleGroupRow() handler and `group-row-<n>` id space.
    _GID_BASE = 9000
    rows = []
    for i, (pkg, members) in enumerate(ordered):
        gi   = _GID_BASE + i
        head = members[0]
        repo = head.get("source_repo")
        repo_cell = (f'<a href="{_esc(repo)}" target="_blank" rel="noopener">{_esc(repo)}</a>'
                     if repo else '<span style="color:var(--text3)">&mdash;</span>')
        conf = (head.get("confidence") or "low").lower()
        cat  = head.get("category")
        n    = len(members)
        rows.append(
            f'<tr class="group-row" id="group-row-{gi}" onclick="toggleGroupRow({gi})">'
            f'<td><span class="group-chevron">&#9654;</span> {n} namespace{"s" if n != 1 else ""}</td>'
            f'<td><strong>{_esc(pkg)}</strong></td>'
            f'<td><code>{_esc(head.get("install_cmd") or "")}</code></td>'
            f'<td style="font-family:inherit">{_esc(cat) if cat else "&mdash;"}</td>'
            f'<td><span class="badge {conf}">{_esc(conf)}</span></td>'
            f'<td style="font-size:.76rem;word-break:break-all">{repo_cell}</td>'
            f'</tr>'
        )
        for m in sorted(members, key=lambda x: x["namespace"]):
            rows.append(
                f'<tr class="ns-row group-child-{gi} hidden">'
                f'<td colspan="2">{_esc(m["namespace"])}</td>'
                f'<td colspan="4" style="color:var(--text3);font-size:.76rem">'
                f'{m["method_count"]} methods &nbsp;&middot;&nbsp; {m["class_count"]} classes</td>'
                f'</tr>'
            )

    return (
        '<div class="ohpm-note">'
        '<strong>Second tier &mdash; third-party packages, not HarmonyOS kits.</strong> '
        'These namespaces have no native <code>@kit.*</code> equivalent, so an OHPM '
        'community/vendor package is suggested instead. Prefer a native kit wherever one '
        'exists; verify licence and maintenance before adopting any package below.'
        '</div>'
        '<div class="kit-table-wrapper"><table class="kit-table ohpm-table">'
        '<thead><tr>'
        '<th>Android Namespace</th><th>OHPM Package</th><th>Install</th>'
        '<th>Category</th><th>Confidence</th><th>Source Repo</th>'
        '</tr></thead><tbody>'
        + "".join(rows) +
        '</tbody></table></div>'
    )


def _collapsible_section(section_id: str, title: str, content: str) -> str:
    return (
        f'<div class="section" id="{section_id}">'
        f'<div class="section-title collapsible" onclick="toggleSection(\'{section_id}\')">'
        f'<span>{title}</span>'
        f'<span class="section-toggle">&#9660;</span>'
        f'</div>'
        f'<div class="section-body" id="body-{section_id}">{content}</div>'
        f'</div>'
    )


def render_html_apk(result: dict, mapping: dict = None) -> str:
    is_hmos = result["target"] == "hmos"
    now     = datetime.now().strftime("%Y-%m-%d %H:%M")

    ns_lookup = {e["android_namespace"]: e for e in (mapping or {}).get("namespace_mappings", [])}
    flat_ns_rows = _flatten_namespace_rows(result["kit_matches"])

    kit_section_title = "HarmonyOS NEXT Kit Matches" if is_hmos else "HMS Core Kit Matches"
    report_title      = "APK → HarmonyOS NEXT Report" if is_hmos else "APK → HMS Core Report"

    matched_android = {p["android"] for p in result["permission_matches"]}
    perm_rows = []
    if is_hmos:
        perm_table_header = (
            '<tr><th>Android Permission</th><th>HarmonyOS Permission</th><th>Kit</th></tr>'
        )
        for pm in result["permission_matches"]:
            android = pm["android"].replace("android.permission.", "")
            harmony = pm.get("harmony", "")
            kit     = pm.get("kit", "")
            kit_badge = f'<span class="kit-row-name">{_esc(kit)}</span>' if kit else ""
            perm_rows.append(
                f'<tr>'
                f'<td class="perm-android">{_esc(android)}</td>'
                f'<td class="perm-harmony">{_esc(harmony)}</td>'
                f'<td>{kit_badge}</td>'
                f'</tr>'
            )
    else:
        perm_table_header = '<tr><th>Android Permission</th><th colspan="2">HMS Note</th></tr>'
        for pm in result["permission_matches"]:
            android = pm["android"].replace("android.permission.", "")
            perm_rows.append(
                f'<tr>'
                f'<td class="perm-android">{_esc(android)}</td>'
                f'<td colspan="2">{_esc(pm.get("hms_note",""))}</td>'
                f'</tr>'
            )
    perm_table_html = (
        f'<table class="section-table">'
        f'<thead>{perm_table_header}</thead>'
        f'<tbody>{"".join(perm_rows)}</tbody>'
        f'</table>'
    )

    unmatched = [p for p in result["permissions"] if p not in matched_android]
    unmatched_perms = ""
    if unmatched:
        tags = "".join(f'<span class="tag">{_esc(p)}</span>' for p in unmatched)
        unmatched_perms = _collapsible_section(
            "unmatched-perms-section",
            f"Unmatched Permissions ({len(unmatched)})",
            f'<div class="tag-list">{tags}</div>'
        )

    perm_gaps_html = ""
    perm_gaps = result.get("permission_gaps", [])
    if perm_gaps:
        _conf_color = {"high": "#22c55e", "medium": "#f59e0b", "low": "#94a3b8"}
        gap_rows = ""
        for g in perm_gaps:
            android  = g["android_perm"].replace("android.permission.", "")
            conf     = g["confidence"]
            color    = _conf_color.get(conf, "#94a3b8")
            gap_rows += (
                f'<tr>'
                f'<td class="perm-android">{_esc(android)}</td>'
                f'<td class="perm-harmony">{_esc(g["suggested_hmos"])}</td>'
                f'<td><span style="color:{color};font-weight:600;text-transform:uppercase;font-size:.75rem">{_esc(conf)}</span></td>'
                f'</tr>'
            )
        gap_table_html = (
            f'<table class="section-table">'
            f'<thead><tr><th>Android Permission</th><th>Suggested HarmonyOS Permission</th><th>Confidence</th></tr></thead>'
            f'<tbody>{gap_rows}</tbody>'
            f'</table>'
        )
        perm_gaps_html = _collapsible_section(
            "permission-gaps-section",
            f"Permission Gaps — Suggested HarmonyOS Alternatives ({len(perm_gaps)})",
            f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
            f'Android permissions with no direct mapping, matched by keyword to the closest HarmonyOS permission.</p>'
            f'{gap_table_html}'
        )

    native_libs = ""
    if result["native_libs"]:
        tags = "".join(f'<span class="tag">{_esc(lib)}</span>' for lib in result["native_libs"])
        native_libs = _collapsible_section(
            "native-libs-section",
            f"Native Libraries ({len(result['native_libs'])})",
            f'<div class="tag-list">{tags}</div>'
        )

    unmapped = ""
    if result["unmapped_namespaces"]:
        # Capped at 30 rows, and the cap is STATED below. Silent, it read as
        # "this app has 30 unrecognised libraries" for an app with 1,458. A
        # truncation nobody can see reads as completeness.
        _UNMAPPED_SHOWN = 30
        items = ""
        for u in result["unmapped_namespaces"][:_UNMAPPED_SHOWN]:
            methods = "".join(
                f'<span class="method-tag">{_esc(m.split(".")[-1])}</span>'
                for m in u["sample_methods"]
            )
            items += (
                f'<div class="unmapped-item">'
                f'<div class="unmapped-ns">{_esc(u["namespace"])}</div>'
                f'<div class="source-counts">{u["class_count"]} classes &middot; {u["method_count"]} methods</div>'
                f'<div class="methods-list">{methods}</div></div>'
            )
        _un_total = len(result["unmapped_namespaces"])
        _un_note  = (f' Showing the {_UNMAPPED_SHOWN} with the most method references; '
                     f'all {_un_total} are in the Excel export.'
                     if _un_total > _UNMAPPED_SHOWN else "")
        unmapped = _collapsible_section(
            "unmapped-section",
            f"Unrecognized Third-Party Libraries ({_un_total})",
            f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
            f'External libraries with no current mapping.{_un_note}</p>{items}'
        )

    manifest_xml = ""
    if result.get("manifest_xml"):
        manifest_xml = _collapsible_section(
            "manifest-xml-section",
            "AndroidManifest.xml",
            f'<div class="xml-block">{_esc(result["manifest_xml"])}</div>'
        )

    manifest_sections = ""
    for label, items in [
        ("Activities", result["activities"]),
        ("Services",   result["services"]),
        ("Receivers",  result["receivers"]),
        ("Providers",  result["providers"]),
    ]:
        if items:
            tags = "".join(f'<span class="tag">{_esc(i.split(".")[-1])}</span>' for i in items)
            manifest_sections += (
                f'<div class="stat" style="text-align:left">'
                f'<div style="font-weight:600;margin-bottom:7px;font-size:.86rem;">{label} ({len(items)})</div>'
                f'<div class="tag-list">{tags}</div></div>'
            )

    kit_count     = len(flat_ns_rows)
    private_libs  = result.get("private_libs", [])
    private_count = len(private_libs)


    matched_ns = result.get("total_detected_ns", 0)
    total_ns   = result.get("total_3p_ns", 0)
    coverage_pct, _cov_status = coverage_status(result)
    is_packed  = _cov_status == "packed"
    low_sample = _cov_status == "low"
    if coverage_pct is None:
        coverage_color = "var(--low)"
    elif coverage_pct >= 70:
        coverage_color = "var(--high)"
    elif coverage_pct >= 40:
        coverage_color = "var(--med)"
    else:
        coverage_color = "var(--low)"


    _grant_counts = {"system_grant": 0, "user_grant": 0, "restricted": 0}
    for _pm in result["permission_matches"]:
        gl = _pm.get("grant_level", "")
        if gl in _grant_counts:
            _grant_counts[gl] += 1
    perm_sublabel = (
        f'System: {_grant_counts["system_grant"]} &middot; '
        f'User: {_grant_counts["user_grant"]} &middot; '
        f'Restricted: {_grant_counts["restricted"]}'
    )

    if not is_hmos:
        coverage_sublabel = ""
    elif is_packed:
        coverage_sublabel = ('<div class="sublabel" style="color:var(--low);font-weight:700">'
                             'coverage not measurable</div>')
    elif low_sample:
        coverage_sublabel = ('<div class="sublabel" style="color:var(--med);font-weight:700">'
                             f'{total_ns} refs &mdash; too few to rate</div>')
    else:
        coverage_sublabel = (f'<div class="sublabel" style="color:{coverage_color};'
                             f'font-weight:700">{coverage_pct}% coverage</div>')
    stat_cards = (
        f'<a class="stat clickable" href="#kit-matches-section">'
        f'<div class="num">{kit_count}</div>'
        f'{coverage_sublabel}'
        f'<div class="label">Number of Libraries Mapped</div>'
        f'</a>'
        f'<a class="stat clickable" href="#private-libs-section"'
        f' onclick="revealSection(\'private-libs-section\')">'
        f'<div class="num">{private_count}</div>'
        f'<div class="label">Private Libs</div>'
        f'<div class="sublabel">Custom app-internal classes &mdash; excluded from matching</div>'
        f'</a>'
        f'<a class="stat clickable" href="#permission-mapping-section">'
        f'<div class="num">{len(result["permission_matches"])} / {len(result["permissions"])}</div>'
        f'<div class="label">Permission Coverage</div>'
        f'<div class="sublabel">{perm_sublabel}</div>'
        f'</a>'
        f'<div class="stat"><div class="num">{len(result["native_libs"])}</div><div class="label">Native .so Libs</div></div>'
    )

    header_meta = (
        f'<span>v{_esc(result["version_name"] or "?")} (build {_esc(result["version_code"] or "?")})</span>'
        f'<span>Min SDK: {_esc(result["min_sdk"] or "?")} &nbsp;&middot;&nbsp; Target SDK: {_esc(result["target_sdk"] or "?")}</span>'
        f'<span>Analysis: {result["analysis_time_sec"]}s</span>'
        f'<span>{now}</span>'
    )


    if private_libs:
        _pl_items = ""
        for pl in private_libs:
            _pl_methods = "".join(
                f'<span class="method-tag">{_esc(m.split(".")[-1] if "." in m else m)}</span>'
                for m in pl["sample_methods"]
            )
            _pl_items += (
                f'<div class="unmapped-item">'
                f'<div class="unmapped-ns" style="color:#6d28d9">{_esc(pl["namespace"])}</div>'
                f'<div class="source-counts">{pl["class_count"]} classes &middot; {pl["method_count"]} methods</div>'
                f'<div class="methods-list">{_pl_methods}</div></div>'
            )
        private_libs_section = (
            f'<div class="section" id="private-libs-section" style="display:none">'
            f'<div class="section-title">Private Libraries ({private_count})</div>'
            f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
            f'App-internal classes detected from the app\'s own bundle namespace. '
            f'Excluded from all matching ratios and counts.</p>'
            f'{_pl_items}</div>'
        )
    else:
        private_libs_section = (
            f'<div class="section" id="private-libs-section" style="display:none">'
            f'<div class="section-title">Private Libraries (0)</div>'
            f'<p style="font-size:.83rem;color:var(--text3)">No private/custom namespaces detected.</p>'
            f'</div>'
        )

    # Second tier. Sits directly under the native kit table, and is omitted
    # entirely when empty so a clean app shows no hollow section.
    ohpm_matches = result.get("ohpm_matches") or []
    ohpm_section = (
        _collapsible_section(
            "ohpm-matches-section",
            f"3rd Party (OHPM) &mdash; {len(ohpm_matches)} namespace"
            f"{'s' if len(ohpm_matches) != 1 else ''}",
            _render_ohpm_table(ohpm_matches),
        )
        if ohpm_matches else ""
    )

    body_sections = (
        # Packed first: it changes how everything below it must be read.
        _packed_dex_banner(result.get("framework"), total_ns, kit_count)
        # sits above the kit table: it describes what the app IS, which frames
        # everything below it. Informational -- it feeds no count or ratio.
        + _framework_badge(result.get("framework"))
        + _collapsible_section(
            "kit-matches-section", kit_section_title,
            _render_kit_table_apk(flat_ns_rows, ns_lookup, is_hmos=is_hmos)
        )
        + ohpm_section
        + _collapsible_section("permission-mapping-section", "Permission Mapping", perm_table_html)
        + unmatched_perms + perm_gaps_html + native_libs + unmapped
        + private_libs_section
        + manifest_xml
        + _collapsible_section(
            "manifest-components-section", "Manifest Components",
            f'<div class="stats" style="grid-template-columns:repeat(auto-fill,minmax(250px,1fr))">'
            f'{manifest_sections}</div>'
        )
    )

    sidebar_links = [
        (kit_section_title, "kit-matches-section"),
    ] + ([("3rd Party (OHPM)", "ohpm-matches-section")] if ohpm_matches else []) + [
        ("Permission Mapping", "permission-mapping-section"),
        ("Unmatched Permissions", "unmatched-perms-section"),
        ("Permission Gaps", "permission-gaps-section"),
        ("Unrecognized Libraries", "unmapped-section"),
        ("AndroidManifest.xml", "manifest-xml-section"),
        ("Manifest Components", "manifest-components-section"),
    ]
    # Drop links whose section was not rendered. Several sections are conditional
    # but the sidebar listed them unconditionally, so the link scrolled nowhere.
    # Testing body_sections rather than repeating each section's own condition
    # keeps this correct if a condition later changes.
    sidebar_links = [(label, sid) for label, sid in sidebar_links
                     if f'id="{sid}"' in body_sections]
    sidebar_html = (
        '<div class="sidebar"><nav>'
        + "".join(f'<a href="#{sid}">{_esc(label)}</a>' for label, sid in sidebar_links)
        + '</nav></div>'
    )

    report_data = {
        "mode":                    "apk",
        "target":                  result["target"],
        "app_name":                result["app_name"] or "N/A",
        "package_name":            result["package_name"],
        "version_name":            result["version_name"] or "?",
        "version_code":            result["version_code"] or "?",
        "min_sdk":                 result["min_sdk"] or "?",
        "target_sdk":              result["target_sdk"] or "?",
        "report_date":             now,
        "analysis_time_sec":       result["analysis_time_sec"],
        "kit_matches":             result["kit_matches"],
        "permission_matches":      result["permission_matches"],
        "permissions":             result["permissions"],
        "native_libs":             result["native_libs"],
        "unmapped_namespaces":     result["unmapped_namespaces"],
        "unresolvable_namespaces": result.get("unresolvable_namespaces", []),
        "private_libs":            result.get("private_libs", []),
        "obfuscated_count":        result.get("obfuscated_count", 0),
        "total_detected_ns":       result.get("total_detected_ns", 0),
        "total_3p_ns":             result.get("total_3p_ns", 0),
        "ohpm_matches":            result.get("ohpm_matches", []),
        "framework":               result.get("framework") or {},
    }

    subs = {
        "REPORT_TITLE":   report_title,
        "REPORT_HEADING": "APK Migration Report",
        "REPORT_SUB":     f'{_esc(result["app_name"] or "N/A")} &nbsp;&middot;&nbsp; {_esc(result["package_name"])}',
        "HEADER_META":    header_meta,
        "TARGET_LABEL":   "Target: HarmonyOS NEXT" if is_hmos else "Target: HMS Core",
        "STAT_CARDS":     stat_cards,
        "BODY_SECTIONS":  body_sections,
        "REPORT_DATE":    now,
        "REPORT_DATA_JSON": json.dumps(report_data, ensure_ascii=False, default=str),
        "SIDEBAR_HTML":   sidebar_html,
        "CONTAINER_EXTRA_CLASS": "with-sidebar",
        "SIDEBAR_TOGGLE_HTML": (
            '<button class="sidebar-toggle" onclick="toggleSidebar()" '
            'title="Toggle navigation">&#9776;</button>'
        ),
        "HEADER_EXTRA_CLASS": "with-toggle",
    }
    html = _HTML_BASE
    for k, v in subs.items():
        html = html.replace(f"%%{k}%%", v)
    return html


def render_html_exe(result: dict) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")


    packed_banner = ""
    if result.get("is_packed") or result.get("string_scan_mode"):
        hint  = result.get("packer_hint") or "Unknown packer / stripped import table"
        ent   = result.get("avg_entropy", "?")
        mode_note = (
            "Import table was empty. Results below are from <strong>string-scan fallback</strong> "
            "— DLL names and API calls extracted from raw binary strings. "
            "Accuracy is best-effort; some detections may be false positives or incomplete."
            if result.get("string_scan_mode")
            else "Import table parsed normally, but high entropy sections detected."
        )
        packed_banner = (
            f'<div style="background:#fff8e1;border:1.5px solid #f59e0b;border-radius:8px;'
            f'padding:14px 18px;margin-bottom:22px;display:flex;gap:12px;align-items:flex-start">'
            f'<span style="font-size:1.4rem">⚠️</span>'
            f'<div><div style="font-weight:700;color:#92400e;margin-bottom:4px">'
            f'Packed / Protected Binary Detected</div>'
            f'<div style="font-size:.84rem;color:#78350f">'
            f'<strong>Hint:</strong> {_esc(hint)} &nbsp;&middot;&nbsp; '
            f'<strong>Avg entropy:</strong> {ent}<br>{mode_note}</div></div></div>'
        )


    vi = result["version_info"]
    subsystem_label = "N/A (library)" if result["is_dll"] else result["subsystem"]
    pe_meta = ""
    for label, val in [
        ("Architecture",   result["machine"]),
        ("Subsystem",      subsystem_label),
        ("Entry Point",    result["entry_point"]),
        ("Image Base",     result["image_base"]),
        ("Image Size",     f"{result['image_size']:,} bytes"),
        ("Avg Entropy",    str(result.get("avg_entropy", "?"))),
        ("Packer / Guard", result.get("packer_hint") or "None detected"),
        ("Compile Time",   result["timestamp"]),
        ("Is DLL",         "Yes" if result["is_dll"] else "No"),
        ("Is .NET / CLR",  "Yes" if result["is_dotnet"] else "No"),
        ("Company",        vi.get("CompanyName", "—")),
        ("Product",        vi.get("ProductName", "—")),
        ("File Version",   vi.get("FileVersion", "—")),
        ("Description",    vi.get("FileDescription", "—")),
    ]:
        pe_meta += (
            f'<div class="pe-meta-card">'
            f'<div class="pe-meta-label">{_esc(label)}</div>'
            f'<div class="pe-meta-value">{_esc(str(val))}</div></div>'
        )

    pe_meta_section = _collapsible_section(
        "pe-metadata-section", "PE Metadata",
        f'<div class="pe-meta-grid">{pe_meta}</div>'
    )


    sec_rows = ""
    for s in result["sections"]:
        exec_badge = '<span class="badge high">exec</span>' if s["exec"] else ""
        sec_rows += (
            f'<tr><td>{_esc(s["name"])}</td>'
            f'<td>{s["vsize"]:,}</td>'
            f'<td>{s["raw_size"]:,}</td>'
            f'<td>{s["entropy"]}</td>'
            f'<td>{exec_badge}</td></tr>'
        )
    sections_section = _collapsible_section(
        "pe-sections-section", f'PE Sections ({len(result["sections"])})',
        f'<table class="section-table">'
        f'<tr><th>Name</th><th>Virtual Size</th><th>Raw Size</th><th>Entropy</th><th>Flags</th></tr>'
        f'{sec_rows}</table>'
    )


    kit_table = _render_kit_table_exe(result["kit_matches"])
    kit_section = _collapsible_section(
        "kit-matches-section", "HarmonyOS NEXT Kit Matches",
        f'{_qt6_banner(result.get("qt6_dlls", []))}{kit_table}'
    )


    all_imports = {**result["imports"], **result["delay_imports"]}
    import_cards = ""
    for dll, funcs in sorted(all_imports.items()):
        is_delay = dll in result["delay_imports"]
        delay    = '<span class="delay-badge">delay</span> ' if is_delay else ""
        import_cards += (
            f'<div class="source-item">'
            f'<div class="source-ns">{delay}{_esc(dll)}</div>'
            f'<div class="source-counts">{len(funcs)} imported functions</div>'
            f'</div>'
        )

    exports_section = ""
    if result["exports"]:
        _exp_total = len(result["exports"])
        tags = "".join(f'<span class="tag">{_esc(e)}</span>' for e in result["exports"][:100])
        _exp_note = (f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
                     f'Showing the first 100 of {_exp_total}.</p>' if _exp_total > 100 else "")
        exports_section = _collapsible_section(
            "exports-section", f'Export Table ({_exp_total} symbols)',
            f'{_exp_note}<div class="tag-list">{tags}</div>'
        )


    unmapped = ""
    if result["unmapped_dlls"]:
        items = ""
        for u in result["unmapped_dlls"]:
            delay    = '<span class="delay-badge">delay</span> ' if u["is_delay"] else ""
            func_tags = "".join(f'<span class="method-tag">{_esc(f)}</span>' for f in u["sample_funcs"])
            items += (
                f'<div class="unmapped-item">'
                f'<div class="unmapped-ns">{delay}{_esc(u["dll_name"])}</div>'
                f'<div class="source-counts">{u["func_count"]} imported functions</div>'
                f'<div class="methods-list">{func_tags}</div></div>'
            )
        unmapped = _collapsible_section(
            "unmapped-dlls-section", f'Unmapped DLLs ({len(result["unmapped_dlls"])})',
            f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
            f'DLLs with no current HarmonyOS NEXT mapping. May need manual research.</p>'
            f'{items}'
        )

    total_funcs = sum(len(v) for v in result["imports"].values())
    mapped_dll_count = sum(len(km.get("dll_sources", [])) for km in result["kit_matches"])
    total_dll_count  = mapped_dll_count + len(result["unmapped_dlls"])
    dll_coverage_pct = round(mapped_dll_count / total_dll_count * 100, 1) if total_dll_count > 0 else 0
    if dll_coverage_pct >= 70:
        dll_coverage_color = "var(--high)"
    elif dll_coverage_pct >= 40:
        dll_coverage_color = "var(--med)"
    else:
        dll_coverage_color = "var(--low)"
    stat_cards = (
        f'<a class="stat clickable" href="#kit-matches-section">'
        f'<div class="num">{len(result["kit_matches"])}</div><div class="label">Kit Matches</div></a>'
        f'<a class="stat clickable" href="#import-table-section">'
        f'<div class="num">{len(result["imports"])}</div><div class="label">Imported DLLs</div></a>'
        f'<a class="stat clickable" href="#import-table-section">'
        f'<div class="num">{total_funcs}</div><div class="label">Imported Functions</div></a>'
        f'<a class="stat clickable" href="#exports-section">'
        f'<div class="num">{len(result["exports"])}</div><div class="label">Exported Symbols</div></a>'
        f'<a class="stat clickable" href="#kit-matches-section">'
        f'<div class="num">{mapped_dll_count}/{total_dll_count}</div>'
        f'<div class="sublabel" style="color:{dll_coverage_color};font-weight:700">{dll_coverage_pct}% coverage</div>'
        f'<div class="label">Mapped DLLs</div></a>'
    )

    header_meta = (
        f'<span>{_esc(result["machine"])}</span>'
        f'<span>{_esc(subsystem_label)}</span>'
        f'<span>Analysis: {result["analysis_time_sec"]}s</span>'
        f'<span>{now}</span>'
    )


    import_title_note = ""
    if result.get("string_scan_mode"):
        import_title_note = ' <span style="font-size:.75rem;color:#d97706;font-weight:600">[string-scan — best effort]</span>'

    imports_section = _collapsible_section(
        "import-table-section", f'Import Table ({len(all_imports)} DLLs){import_title_note}',
        import_cards
    )

    body_sections = (
        packed_banner
        + pe_meta_section
        + sections_section
        + kit_section
        + imports_section
        + exports_section
        + unmapped
    )

    sidebar_links = [
        ("PE Metadata", "pe-metadata-section"),
        ("PE Sections", "pe-sections-section"),
        ("HarmonyOS NEXT Kit Matches", "kit-matches-section"),
        ("Import Table", "import-table-section"),
        ("Export Table", "exports-section"),
        ("Unmapped DLLs", "unmapped-dlls-section"),
    ]
    # Same guard as render_html_apk: the Export Table / Unmapped DLLs section is conditional, so an unconditional
    # link scrolled nowhere when it was absent.
    sidebar_links = [(label, sid) for label, sid in sidebar_links
                     if f'id="{sid}"' in body_sections]
    sidebar_html = (
        '<div class="sidebar"><nav>'
        + "".join(f'<a href="#{sid}">{_esc(label)}</a>' for label, sid in sidebar_links)
        + '</nav></div>'
    )

    report_data = {
        "mode":          "exe",
        "target":        "hmos",
        "file_name":     result["file_name"],
        "machine":       result["machine"],
        "subsystem":     subsystem_label,
        "entry_point":   result["entry_point"],
        "image_base":    result["image_base"],
        "image_size":    result["image_size"],
        "timestamp":     result["timestamp"],
        "is_dll":        result["is_dll"],
        "is_dotnet":     result["is_dotnet"],
        "version_info":  result["version_info"],
        "imports":       {k: v for k, v in result["imports"].items()},
        "delay_imports": {k: v for k, v in result["delay_imports"].items()},
        "exports":       result["exports"],
        "kit_matches":   result["kit_matches"],
        "unmapped_dlls": result["unmapped_dlls"],
        "report_date":   now,
        "analysis_time_sec": result["analysis_time_sec"],
    }

    subs = {
        "REPORT_TITLE":   "EXE → HarmonyOS NEXT Report",
        "REPORT_HEADING": "EXE Migration Report",
        "REPORT_SUB":     f'{_esc(result["file_name"])}',
        "HEADER_META":    header_meta,
        "TARGET_LABEL":   "Target: HarmonyOS NEXT",
        "STAT_CARDS":     stat_cards,
        "BODY_SECTIONS":  body_sections,
        "REPORT_DATE":    now,
        "REPORT_DATA_JSON": json.dumps(report_data, ensure_ascii=False, default=str),
        "SIDEBAR_HTML":   sidebar_html,
        "CONTAINER_EXTRA_CLASS": "with-sidebar",
        "SIDEBAR_TOGGLE_HTML": (
            '<button class="sidebar-toggle" onclick="toggleSidebar()" '
            'title="Toggle navigation">&#9776;</button>'
        ),
        "HEADER_EXTRA_CLASS": "with-toggle",
    }
    html = _HTML_BASE
    for k, v in subs.items():
        html = html.replace(f"%%{k}%%", v)
    return html


def render_html_exe_folder(result: dict) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    files_rows = ""
    for f in result["files"]:
        if f.get("error"):
            files_rows += (
                f'<tr><td>{_esc(f["file_name"])}</td>'
                f'<td colspan="4" style="color:#b91c1c">Failed to parse: {_esc(f["error"])}</td></tr>'
            )
            continue
        packed_badge = (
            f'<span class="badge low">{_esc(f["packer_hint"] or "packed")}</span>'
            if f["is_packed"] else '<span class="badge high">clean</span>'
        )
        subsystem_label = "N/A (library)" if f["is_dll"] else f["subsystem"]
        files_rows += (
            f'<tr><td>{_esc(f["file_name"])}</td>'
            f'<td>{_esc(f["machine"])}</td>'
            f'<td>{_esc(subsystem_label)}</td>'
            f'<td>{"DLL" if f["is_dll"] else "EXE"}{" / .NET" if f["is_dotnet"] else ""}</td>'
            f'<td>{packed_badge}</td></tr>'
        )
    files_section = _collapsible_section(
        "analyzed-files-section", f'Analyzed Files ({result["file_count"]})',
        f'<table class="section-table">'
        f'<tr><th>File</th><th>Architecture</th><th>Subsystem</th><th>Type</th><th>Packer</th></tr>'
        f'{files_rows}</table>'
    )

    kit_table = _render_kit_table_exe(result["kit_matches"])
    kit_section = _collapsible_section(
        "kit-matches-section", "HarmonyOS NEXT Kit Matches",
        f'{_qt6_banner(result.get("qt6_dlls", []))}{kit_table}'
    )

    import_cards = ""
    for dll, funcs in sorted(result["imports"].items()):
        is_delay = dll in result["delay_dlls"]
        delay    = '<span class="delay-badge">delay</span> ' if is_delay else ""
        src_files = result["import_sources"].get(dll, [])
        src_html  = (
            f'<div class="source-counts">from: {_esc(", ".join(src_files))}</div>' if src_files else ""
        )
        import_cards += (
            f'<div class="source-item">'
            f'<div class="source-ns">{delay}{_esc(dll)}</div>'
            f'<div class="source-counts">{len(funcs)} imported functions</div>'
            f'{src_html}'
            f'</div>'
        )
    imports_section = _collapsible_section(
        "import-table-section", f'Merged Import Table ({len(result["imports"])} DLLs)',
        import_cards
    )

    unmapped = ""
    if result["unmapped_dlls"]:
        items = ""
        for u in result["unmapped_dlls"]:
            delay     = '<span class="delay-badge">delay</span> ' if u["is_delay"] else ""
            src_files = u.get("source_files") or []
            src_html  = (
                f'<div class="source-counts">from: {_esc(", ".join(src_files))}</div>' if src_files else ""
            )
            func_tags = "".join(f'<span class="method-tag">{_esc(f)}</span>' for f in u["sample_funcs"])
            items += (
                f'<div class="unmapped-item">'
                f'<div class="unmapped-ns">{delay}{_esc(u["dll_name"])}</div>'
                f'<div class="source-counts">{u["func_count"]} imported functions</div>'
                f'{src_html}'
                f'<div class="methods-list">{func_tags}</div></div>'
            )
        unmapped = _collapsible_section(
            "unmapped-dlls-section", f'Unmapped DLLs ({len(result["unmapped_dlls"])})',
            f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
            f'DLLs with no current HarmonyOS NEXT mapping. May need manual research.</p>'
            f'{items}'
        )

    total_funcs = sum(len(v) for v in result["imports"].values())

    self_names = {f["file_name"].lower() for f in result["files"] if not f.get("error")}
    mapped_dll_count = sum(
        1 for km in result["kit_matches"] for src in km.get("dll_sources", [])
        if src["dll_name"].lower() not in self_names
    )
    unmapped_ext_count = sum(
        1 for u in result["unmapped_dlls"] if u["dll_name"].lower() not in self_names
    )
    total_dll_count  = mapped_dll_count + unmapped_ext_count
    dll_coverage_pct = round(mapped_dll_count / total_dll_count * 100, 1) if total_dll_count > 0 else 0
    if dll_coverage_pct >= 70:
        dll_coverage_color = "var(--high)"
    elif dll_coverage_pct >= 40:
        dll_coverage_color = "var(--med)"
    else:
        dll_coverage_color = "var(--low)"

    stat_cards = (
        f'<a class="stat clickable" href="#kit-matches-section">'
        f'<div class="num">{len(result["kit_matches"])}</div><div class="label">Kit Matches</div></a>'
        f'<a class="stat clickable" href="#analyzed-files-section">'
        f'<div class="num">{result["file_count"]}</div><div class="label">Files Analyzed</div></a>'
        f'<a class="stat clickable" href="#import-table-section">'
        f'<div class="num">{len(result["imports"])}</div><div class="label">Imported DLLs</div></a>'
        f'<a class="stat clickable" href="#import-table-section">'
        f'<div class="num">{total_funcs}</div><div class="label">Imported Functions</div></a>'
        f'<a class="stat clickable" href="#kit-matches-section">'
        f'<div class="num">{mapped_dll_count}/{total_dll_count}</div>'
        f'<div class="sublabel" style="color:{dll_coverage_color};font-weight:700">{dll_coverage_pct}% coverage</div>'
        f'<div class="label">Mapped DLLs</div></a>'
    )

    header_meta = (
        f'<span>{result["file_count"]} dosya</span>'
        f'<span>Analysis: {result["analysis_time_sec"]}s</span>'
        f'<span>{now}</span>'
    )

    body_sections = files_section + kit_section + imports_section + unmapped

    sidebar_links = [
        ("Analyzed Files", "analyzed-files-section"),
        ("HarmonyOS NEXT Kit Matches", "kit-matches-section"),
        ("Merged Import Table", "import-table-section"),
        ("Unmapped DLLs", "unmapped-dlls-section"),
    ]
    # Same guard as render_html_apk: the Export Table / Unmapped DLLs section is conditional, so an unconditional
    # link scrolled nowhere when it was absent.
    sidebar_links = [(label, sid) for label, sid in sidebar_links
                     if f'id="{sid}"' in body_sections]
    sidebar_html = (
        '<div class="sidebar"><nav>'
        + "".join(f'<a href="#{sid}">{_esc(label)}</a>' for label, sid in sidebar_links)
        + '</nav></div>'
    )

    report_data = {
        "mode":           "exe_folder",
        "target":         "hmos",
        "folder_name":    result["folder_name"],
        "file_count":     result["file_count"],
        "files":          result["files"],
        "imports":        result["imports"],
        "delay_dlls":     result["delay_dlls"],
        "import_sources": result["import_sources"],
        "kit_matches":    result["kit_matches"],
        "unmapped_dlls":  result["unmapped_dlls"],
        "report_date":    now,
        "analysis_time_sec": result["analysis_time_sec"],
    }

    subs = {
        "REPORT_TITLE":   "EXE Folder → HarmonyOS NEXT Report",
        "REPORT_HEADING": "EXE Folder Migration Report",
        "REPORT_SUB":     f'{_esc(result["folder_name"])} &nbsp;&middot;&nbsp; {result["file_count"]} dosya analiz edildi',
        "HEADER_META":    header_meta,
        "TARGET_LABEL":   "Target: HarmonyOS NEXT",
        "STAT_CARDS":     stat_cards,
        "BODY_SECTIONS":  body_sections,
        "REPORT_DATE":    now,
        "REPORT_DATA_JSON": json.dumps(report_data, ensure_ascii=False, default=str),
        "SIDEBAR_HTML":   sidebar_html,
        "CONTAINER_EXTRA_CLASS": "with-sidebar",
        "SIDEBAR_TOGGLE_HTML": (
            '<button class="sidebar-toggle" onclick="toggleSidebar()" '
            'title="Toggle navigation">&#9776;</button>'
        ),
        "HEADER_EXTRA_CLASS": "with-toggle",
    }
    html = _HTML_BASE
    for k, v in subs.items():
        html = html.replace(f"%%{k}%%", v)
    return html


def render_html_ipa(result: dict) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")


    meta_items = [
        ("Bundle ID",       result.get("bundle_id") or "—"),
        ("Min iOS Version", result.get("min_ios_version") or "—"),
        ("URL Schemes",     ", ".join(result["url_schemes"]) if result["url_schemes"] else "—"),
        ("Extensions",      str(len(result["extensions"])) if result["extensions"] else "0"),
    ]
    meta_html = "".join(
        f'<div class="pe-meta-card">'
        f'<div class="pe-meta-label">{_esc(label)}</div>'
        f'<div class="pe-meta-value">{_esc(str(val))}</div></div>'
        for label, val in meta_items
    )
    meta_section = (
        f'<div class="section"><div class="section-title">App Metadata</div>'
        f'<div class="pe-meta-grid">{meta_html}</div></div>'
    )


    kit_cards = _render_kit_cards(result["kit_matches"], mode="ipa")
    kit_section = (
        f'<div class="section"><div class="section-title">HarmonyOS NEXT Kit Matches</div>'
        f'{kit_cards}</div>'
    )


    matched_keys = {pm["ios_key"] for pm in result["permission_matches"]}
    perm_items_html = ""
    for pm in result["permission_matches"]:
        ios_key   = pm["ios_key"].replace("NSUsageDescription", "").replace("NS", "").replace("UsageDescription", "")
        perm_items_html += (
            f'<div class="perm-item"><div>'
            f'<span class="perm-android">{_esc(pm["ios_display"] or pm["ios_key"])}</span>'
            f'<span class="perm-arrow">&rarr;</span>'
            f'<span class="perm-harmony">{_esc(pm.get("harmony") or "—")}</span></div>'
            f'<div class="perm-note">{_esc(pm.get("kit") or "")}</div></div>'
        )
    unmatched_perm_tags = "".join(
        f'<span class="tag">{_esc(p)}</span>'
        for p in result["permissions"] if p not in matched_keys
    )
    unmatched_perm_section = ""
    unmatched_count = len(result["permissions"]) - len(result["permission_matches"])
    if unmatched_count > 0:
        unmatched_perm_section = (
            f'<div class="section"><div class="section-title">Unmatched Permissions ({unmatched_count})</div>'
            f'<div class="tag-list">{unmatched_perm_tags}</div></div>'
        )
    perm_section = (
        f'<div class="section"><div class="section-title">Permission Mapping</div>'
        f'<div class="perm-grid">{perm_items_html}</div></div>'
        + unmatched_perm_section
    )


    url_section = ""
    if result["url_schemes"]:
        tags = "".join(f'<span class="tag">{_esc(s)}</span>' for s in result["url_schemes"])
        url_section = (
            f'<div class="section"><div class="section-title">URL Schemes ({len(result["url_schemes"])})</div>'
            f'<div class="tag-list">{tags}</div></div>'
        )


    ext_section = ""
    if result["extensions"]:
        tags = "".join(f'<span class="tag">{_esc(e)}</span>' for e in result["extensions"])
        ext_section = (
            f'<div class="section"><div class="section-title">App Extensions ({len(result["extensions"])})</div>'
            f'<div class="tag-list">{tags}</div></div>'
        )


    unmapped_section = ""
    if result["unmapped_frameworks"]:
        items = "".join(
            f'<div class="unmapped-item"><div class="unmapped-ns">{_esc(fw)}</div></div>'
            for fw in result["unmapped_frameworks"]
        )
        unmapped_section = (
            f'<div class="section"><div class="section-title">'
            f'Unmapped Frameworks ({len(result["unmapped_frameworks"])})</div>'
            f'<p style="font-size:.83rem;color:var(--text2);margin-bottom:11px;">'
            f'Frameworks with no current HarmonyOS NEXT mapping. May need manual research.</p>'
            f'{items}</div>'
        )

    stat_cards = (
        f'<div class="stat"><div class="num">{len(result["kit_matches"])}</div><div class="label">Kit Matches</div></div>'
        f'<div class="stat"><div class="num">{len(result["frameworks"])}</div><div class="label">Frameworks</div></div>'
        f'<div class="stat"><div class="num">{len(result["unmapped_frameworks"])}</div><div class="label">Unmapped</div></div>'
        f'<div class="stat"><div class="num">{len(result["permission_matches"])} / {len(result["permissions"])}</div><div class="label">Permissions</div></div>'
        f'<div class="stat"><div class="num">{len(result["extensions"])}</div><div class="label">Extensions</div></div>'
    )

    header_meta = (
        f'<span>v{_esc(result.get("version") or "?")}</span>'
        f'<span>Min iOS: {_esc(result.get("min_ios_version") or "?")}</span>'
        f'<span>Analysis: {result["analysis_time_sec"]}s</span>'
        f'<span>{now}</span>'
    )

    static_linking_banner = ""
    if result.get("static_linking_likely"):
        static_linking_banner = (
            '<div style="background:#fff8e1;border:1.5px solid #f59e0b;border-radius:8px;'
            'padding:14px 18px;margin-bottom:22px;display:flex;gap:12px;align-items:flex-start">'
            '<span style="font-size:1.4rem">&#9432;</span>'
            '<div><div style="font-weight:700;color:#92400e;margin-bottom:4px">'
            'Static Linking Likely</div>'
            '<div style="font-size:.84rem;color:#78350f">'
            'Note: This app likely uses static linking. Only dynamically linked '
            'frameworks are visible. Binary analysis requires a decrypted build.'
            '</div></div></div>'
        )

    body_sections = (
        static_linking_banner
        + meta_section
        + kit_section
        + perm_section
        + url_section
        + ext_section
        + unmapped_section
    )

    report_data = {
        "mode":                "ipa",
        "target":              "hmos",
        "file_name":           result["file_name"],
        "bundle_id":           result.get("bundle_id"),
        "app_name":            result.get("app_name"),
        "version":             result.get("version"),
        "min_ios_version":     result.get("min_ios_version"),
        "frameworks":          result["frameworks"],
        "extensions":          result["extensions"],
        "url_schemes":         result["url_schemes"],
        "kit_matches":         result["kit_matches"],
        "unmapped_frameworks": result["unmapped_frameworks"],
        "permissions":         result["permissions"],
        "permission_matches":  result["permission_matches"],
        "report_date":         now,
        "analysis_time_sec":   result["analysis_time_sec"],
    }

    app_title = result.get("app_name") or result["file_name"]
    subs = {
        "REPORT_TITLE":   "IPA → HarmonyOS NEXT Report",
        "REPORT_HEADING": "IPA Migration Report",
        "REPORT_SUB":     f'{_esc(app_title)} &nbsp;&middot;&nbsp; {_esc(result.get("bundle_id") or "")}',
        "HEADER_META":    header_meta,
        "TARGET_LABEL":   "Target: HarmonyOS NEXT",
        "STAT_CARDS":     stat_cards,
        "BODY_SECTIONS":  body_sections,
        "REPORT_DATE":    now,
        "REPORT_DATA_JSON": json.dumps(report_data, ensure_ascii=False, default=str),
        "SIDEBAR_HTML":   "",
        "CONTAINER_EXTRA_CLASS": "",
        "SIDEBAR_TOGGLE_HTML": "",
        "HEADER_EXTRA_CLASS": "",
    }
    html = _HTML_BASE
    for k, v in subs.items():
        html = html.replace(f"%%{k}%%", v)
    return html


def _excel_styles():
    RED, GRAY, WHITE = "C8002A", "F0F2F8", "FFFFFF"
    GRN, AMB, RED_C  = "16A34A", "D97706", "DC2626"
    thin = Side(style="thin", color="DDE1F0")
    bdr  = Border(left=thin, right=thin, top=thin, bottom=thin)

    def hdr(cell, bg=RED, fg="FFFFFF"):
        cell.font      = Font(bold=True, color=fg, name="Arial", size=10)
        cell.fill      = PatternFill("solid", start_color=bg)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border    = bdr

    def dat(cell, bold=False, color="1A1D2E", wrap=False, align="left"):
        cell.font      = Font(bold=bold, color=color, name="Arial", size=9)
        cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
        cell.border    = bdr

    return hdr, dat, bdr, RED, GRAY, WHITE, GRN, AMB, RED_C


def export_excel_apk(result: dict, output_path: Path):
    is_hmos = result["target"] == "hmos"
    hdr, dat, bdr, RED, GRAY, WHITE, GRN, AMB, RED_C = _excel_styles()
    conf_clr = {"high": GRN, "medium": AMB, "low": RED_C}

    wb = Workbook()


    ws1 = wb.active
    ws1.title = "Overview"
    ws1.sheet_view.showGridLines = False
    ws1.merge_cells("A1:B1")
    ws1["A1"] = f"APK Migration Report -- {'HarmonyOS NEXT' if is_hmos else 'HMS Core'}"
    ws1["A1"].font      = Font(bold=True, size=14, color=RED, name="Arial")
    ws1["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws1.row_dimensions[1].height = 30
    ws1.merge_cells("A3:B3")
    ws1["A3"] = "App Info"
    hdr(ws1["A3"])
    for i, (k, v) in enumerate([
        ("App Name",   result["app_name"] or "N/A"),
        ("Package",    result["package_name"]),
        ("Version",    f"{result['version_name'] or '?'} (build {result['version_code'] or '?'})"),
        ("Min SDK",    result["min_sdk"] or "?"),
        ("Target SDK", result["target_sdk"] or "?"),
        ("Date",       datetime.now().strftime("%Y-%m-%d %H:%M")),
        ("Time (s)",   result["analysis_time_sec"]),
    ], start=4):
        bg = GRAY if i % 2 == 0 else WHITE
        ws1[f"A{i}"] = k
        ws1[f"B{i}"] = v
        ws1[f"A{i}"].font = Font(bold=True, name="Arial", size=9, color="4B5270")
        ws1[f"A{i}"].fill = ws1[f"B{i}"].fill = PatternFill("solid", start_color=bg)
        dat(ws1[f"B{i}"])
    r = 12
    ws1.merge_cells(f"A{r}:B{r}")
    ws1[f"A{r}"] = "Summary"
    hdr(ws1[f"A{r}"])
    # "Number of Libraries Mapped" used to sit here carrying len(kit_matches),
    # while the HTML stat card of the SAME NAME carries the namespace-row count.
    # Both numbers are useful, so both are emitted under names that say which.
    _ns_rows = sum(len(km.get("android_sources", [])) for km in result["kit_matches"])
    for i, (k, v) in enumerate([
        ("Kit Matches",           len(result["kit_matches"])),
        ("Mapped Namespace Rows", _ns_rows),
        ("3rd Party (OHPM)",      len(result.get("ohpm_matches", []))),
        ("Built With",            (result.get("framework") or {}).get("framework") or "N/A"),
        ("Permission Matches",    len(result["permission_matches"])),
        ("Total Permissions",     len(result["permissions"])),
        ("Native .so Libraries",  len(result["native_libs"])),
        ("Private Libs",          len(result.get("private_libs", []))),
    ], start=r + 1):
        bg = GRAY if i % 2 == 0 else WHITE
        ws1[f"A{i}"] = k
        ws1[f"B{i}"] = v
        ws1[f"A{i}"].font  = Font(bold=True, name="Arial", size=9, color="4B5270")
        ws1[f"A{i}"].fill  = ws1[f"B{i}"].fill = PatternFill("solid", start_color=bg)
        ws1[f"B{i}"].font  = Font(bold=True, size=11, color=RED, name="Arial")
        ws1[f"B{i}"].alignment = Alignment(horizontal="center", vertical="center")
        ws1[f"A{i}"].border = ws1[f"B{i}"].border = bdr
    ws1.column_dimensions["A"].width = 28
    ws1.column_dimensions["B"].width = 46


    ws2 = wb.create_sheet("Kit Matches")
    ws2.sheet_view.showGridLines = False
    BLUE_S   = "1D4ED8"
    status_clr = {"Supported": GRN, "Replaceable": AMB, "Should Confirm": BLUE_S}
    conf_status_map = {"high": "Supported", "medium": "Replaceable", "low": "Should Confirm"}
    kit_col = "HarmonyOS Kit" if is_hmos else "HMS Kit"
    hdrs2 = ["Android Library / Namespace", "Android Display Name",
             kit_col, "Import Path" if is_hmos else "", "Status", "Recommendation", "Status"]
    for ci, h in enumerate(hdrs2, 1):
        hdr(ws2.cell(row=1, column=ci, value=h))
    ws2.row_dimensions[1].height = 22
    row = 2
    for km in result["kit_matches"]:
        for src in km["android_sources"]:
            bg        = WHITE if row % 2 == 0 else GRAY
            imp_val   = km.get("harmony_import", "") if is_hmos else ""
            status_v  = km.get("status", "Should Confirm")
            vals      = [src.get("android_namespace", ""), src.get("android_display", ""),
                         km.get("kit_name", ""), imp_val,
                         conf_status_map.get(km.get("confidence"), "Should Confirm"), km.get("note") or "",
                         status_v]
            for ci, v in enumerate(vals, 1):
                c = ws2.cell(row=row, column=ci, value=v)
                dat(c, wrap=(ci == 6))
                c.fill = PatternFill("solid", start_color=bg)
                if ci == 5:
                    c.font      = Font(bold=True, color=conf_clr.get(km.get("confidence"), "000000"), name="Arial", size=9)
                    c.alignment = Alignment(horizontal="center", vertical="center")
                if ci == 7:
                    c.font      = Font(bold=True, color=status_clr.get(status_v, BLUE_S), name="Arial", size=9)
                    c.alignment = Alignment(horizontal="center", vertical="center")
            ws2.row_dimensions[row].height = 18
            row += 1
    for ci, w in enumerate([42, 34, 28, 28, 12, 55, 16], 1):
        ws2.column_dimensions[get_column_letter(ci)].width = w
    ws2.freeze_panes = "A2"
    ws2.auto_filter.ref = f"A1:{get_column_letter(len(hdrs2))}1"


    # Second tier. Omitted when empty, exactly like the HTML section. Created
    # here so it lands directly after Kit Matches, mirroring the report's own
    # section order.
    ohpm_rows = result.get("ohpm_matches", [])
    if ohpm_rows:
        wso = wb.create_sheet("3rd Party (OHPM)")
        wso.sheet_view.showGridLines = False
        hdrs_o = ["Android Namespace", "OHPM Package", "Install Command", "Category",
                  "Confidence", "Class Count", "Method Count", "Sample Methods", "Repository"]
        for ci, h in enumerate(hdrs_o, 1):
            hdr(wso.cell(row=1, column=ci, value=h))
        wso.row_dimensions[1].height = 22
        for ri_o, om in enumerate(ohpm_rows, start=2):
            bg_o = WHITE if ri_o % 2 == 0 else GRAY
            vals_o = [om.get("namespace", ""), om.get("ohpm_package", ""),
                      om.get("install_cmd", ""), om.get("category") or "--",
                      om.get("confidence", ""), om.get("class_count", ""),
                      om.get("method_count", ""), ", ".join(om.get("sample_methods", [])),
                      om.get("source_repo") or "--"]
            for ci, v in enumerate(vals_o, 1):
                c = wso.cell(row=ri_o, column=ci, value=v)
                dat(c, align=("center" if ci in (5, 6, 7) else "left"), wrap=(ci == 8))
                c.fill = PatternFill("solid", start_color=bg_o)
            wso.row_dimensions[ri_o].height = 16
        for ci, w in enumerate([44, 30, 34, 30, 12, 12, 13, 55, 40], 1):
            wso.column_dimensions[get_column_letter(ci)].width = w
        wso.freeze_panes = "A2"
        wso.auto_filter.ref = f"A1:{get_column_letter(len(hdrs_o))}1"


    ws3 = wb.create_sheet("Permissions")
    ws3.sheet_view.showGridLines = False
    hdrs3 = (["Android Permission", "HarmonyOS Permission", "HarmonyOS Kit", "Status"]
             if is_hmos else ["Android Permission", "HMS Note", "Status"])
    for ci, h in enumerate(hdrs3, 1):
        hdr(ws3.cell(row=1, column=ci, value=h))
    ws3.row_dimensions[1].height = 22
    matched = {p["android"] for p in result["permission_matches"]}
    row = 2
    for pm in result["permission_matches"]:
        bg   = WHITE if row % 2 == 0 else GRAY
        vals = ([pm["android"], pm.get("harmony",""), pm.get("kit",""), "Mapped"]
                if is_hmos else [pm["android"], pm.get("hms_note",""), "Noted"])
        for ci, v in enumerate(vals, 1):
            c = ws3.cell(row=row, column=ci, value=v)
            dat(c)
            c.fill = PatternFill("solid", start_color=bg)
            if ci == len(vals):
                c.font      = Font(bold=True, color=GRN, name="Arial", size=9)
                c.alignment = Alignment(horizontal="center", vertical="center")
        ws3.row_dimensions[row].height = 16
        row += 1
    for perm in result["permissions"]:
        if perm in matched:
            continue
        bg   = WHITE if row % 2 == 0 else GRAY
        vals = ([perm, "--", "--", "No mapping"] if is_hmos else [perm, "--", "No mapping"])
        for ci, v in enumerate(vals, 1):
            c = ws3.cell(row=row, column=ci, value=v)
            dat(c)
            c.fill = PatternFill("solid", start_color=bg)
            if ci == len(vals):
                c.font      = Font(bold=True, color=AMB, name="Arial", size=9)
                c.alignment = Alignment(horizontal="center", vertical="center")
        ws3.row_dimensions[row].height = 16
        row += 1
    col_w = [52, 52, 30, 14] if is_hmos else [52, 60, 14]
    for ci, w in enumerate(col_w, 1):
        ws3.column_dimensions[get_column_letter(ci)].width = w
    ws3.freeze_panes = "A2"
    ws3.auto_filter.ref = f"A1:{get_column_letter(len(hdrs3))}1"


    ws4 = wb.create_sheet("Unmapped Libraries")
    ws4.sheet_view.showGridLines = False


    hdrs4 = ["Namespace", "Class Count", "Method Count", "Sample Methods"]
    for ci, h in enumerate(hdrs4, 1):
        hdr(ws4.cell(row=1, column=ci, value=h))
    ws4.row_dimensions[1].height = 22
    row = 2
    for u in result["unmapped_namespaces"]:
        bg = WHITE if row % 2 == 0 else GRAY
        vals = [u["namespace"], u["class_count"], u["method_count"],
                ", ".join(u["sample_methods"])]
        for ci, v in enumerate(vals, 1):
            c = ws4.cell(row=row, column=ci, value=v)
            dat(c, wrap=(ci == 4))
            c.fill = PatternFill("solid", start_color=bg)
        ws4.row_dimensions[row].height = 16
        row += 1
    for ci, w in enumerate([50, 12, 14, 60], 1):
        ws4.column_dimensions[get_column_letter(ci)].width = w
    ws4.freeze_panes = "A2"
    ws4.auto_filter.ref = f"A1:{get_column_letter(len(hdrs4))}1"
    ws4_last_row = row


    ws5 = wb.create_sheet("Filtered Libraries")
    ws5.sheet_view.showGridLines = False
    ws5["A1"] = "Obfuscated Count"
    ws5["A1"].font  = Font(bold=True, name="Arial", size=9, color="4B5270")
    ws5["A1"].fill  = PatternFill("solid", start_color=GRAY)
    ws5["B1"].value = result.get("obfuscated_count", 0)
    ws5["B1"].font  = Font(bold=True, size=11, color=RED, name="Arial")
    ws5["B1"].alignment = Alignment(horizontal="center", vertical="center")
    ws5["A1"].border = ws5["B1"].border = bdr
    ws5.row_dimensions[1].height = 20

    hdrs5 = ["Namespace", "Class Count", "Method Count", "Sample Methods"]
    for ci, h in enumerate(hdrs5, 1):
        hdr(ws5.cell(row=3, column=ci, value=h))
    ws5.row_dimensions[3].height = 22
    row = 4
    for u in result.get("unresolvable_namespaces", []):
        bg = WHITE if row % 2 == 0 else GRAY
        vals = [u["namespace"], u["class_count"], u["method_count"],
                ", ".join(u["sample_methods"])]
        for ci, v in enumerate(vals, 1):
            c = ws5.cell(row=row, column=ci, value=v)
            dat(c, wrap=(ci == 4))
            c.fill = PatternFill("solid", start_color=bg)
        ws5.row_dimensions[row].height = 16
        row += 1
    for ci, w in enumerate([50, 12, 14, 60], 1):
        ws5.column_dimensions[get_column_letter(ci)].width = w
    ws5.freeze_panes = "A4"
    ws5.auto_filter.ref = f"A3:{get_column_letter(len(hdrs5))}3"


    ws6 = wb.create_sheet("Custom Private Libs")
    ws6.sheet_view.showGridLines = False
    hdrs6 = ["Namespace", "Class Count", "Method Count", "Sample Methods"]
    for ci, h in enumerate(hdrs6, 1):
        hdr(ws6.cell(row=1, column=ci, value=h))
    ws6.row_dimensions[1].height = 22
    row = 2
    for pl in result.get("private_libs", []):
        bg = WHITE if row % 2 == 0 else GRAY
        vals = [pl["namespace"], pl["class_count"], pl["method_count"],
                ", ".join(pl["sample_methods"])]
        for ci, v in enumerate(vals, 1):
            c = ws6.cell(row=row, column=ci, value=v)
            dat(c, wrap=(ci == 4))
            c.fill = PatternFill("solid", start_color=bg)
        ws6.row_dimensions[row].height = 16
        row += 1
    for ci, w in enumerate([50, 12, 14, 60], 1):
        ws6.column_dimensions[get_column_letter(ci)].width = w
    ws6.freeze_panes = "A2"
    ws6.auto_filter.ref = f"A1:{get_column_letter(len(hdrs6))}1"


    perm_gaps = result.get("permission_gaps", [])
    if perm_gaps:
        gap_start = ws4_last_row + 2
        hdrs4b = ["Android Permission", "Suggested HarmonyOS", "Confidence"]
        for ci, h in enumerate(hdrs4b, 1):
            hdr(ws4.cell(row=gap_start, column=ci, value=h))
        ws4.row_dimensions[gap_start].height = 22
        for i, g in enumerate(perm_gaps, start=gap_start + 1):
            bg = WHITE if i % 2 == 0 else GRAY
            vals = [g.get("android_perm", ""), g.get("suggested_hmos", ""), (g.get("confidence") or "").capitalize()]
            for ci, v in enumerate(vals, 1):
                c = ws4.cell(row=i, column=ci, value=v)
                dat(c)
                c.fill = PatternFill("solid", start_color=bg)
                if ci == 3:
                    c.font      = Font(bold=True, color=conf_clr.get(g.get("confidence"), "000000"), name="Arial", size=9)
                    c.alignment = Alignment(horizontal="center", vertical="center")
            ws4.row_dimensions[i].height = 16

    wb.save(output_path)
    _print_ok(f"Excel report: {output_path}")


def export_excel_exe(result: dict, output_path: Path):
    hdr, dat, bdr, RED, GRAY, WHITE, GRN, AMB, RED_C = _excel_styles()
    conf_clr = {"high": GRN, "medium": AMB, "low": RED_C}

    wb = Workbook()


    ws1 = wb.active
    ws1.title = "Overview"
    ws1.sheet_view.showGridLines = False
    ws1.merge_cells("A1:B1")
    ws1["A1"] = "EXE → HarmonyOS NEXT Migration Report"
    ws1["A1"].font      = Font(bold=True, size=14, color=RED, name="Arial")
    ws1["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws1.row_dimensions[1].height = 30

    ws1.merge_cells("A3:B3")
    ws1["A3"] = "PE Metadata"
    hdr(ws1["A3"])
    vi = result["version_info"]
    subsystem_label = "N/A (library)" if result["is_dll"] else result["subsystem"]
    meta_rows = [
        ("File",          result["file_name"]),
        ("Architecture",  result["machine"]),
        ("Subsystem",     subsystem_label),
        ("Entry Point",   result["entry_point"]),
        ("Image Base",    result["image_base"]),
        ("Image Size",    f"{result['image_size']:,} bytes"),
        ("Compile Time",  result["timestamp"]),
        ("Is DLL",        "Yes" if result["is_dll"] else "No"),
        ("Is .NET / CLR", "Yes" if result["is_dotnet"] else "No"),
        ("Company",       vi.get("CompanyName", "—")),
        ("Product",       vi.get("ProductName", "—")),
        ("File Version",  vi.get("FileVersion", "—")),
        ("Description",   vi.get("FileDescription", "—")),
        ("Date",          datetime.now().strftime("%Y-%m-%d %H:%M")),
        ("Analysis (s)",  result["analysis_time_sec"]),
    ]
    for i, (k, v) in enumerate(meta_rows, start=4):
        bg = GRAY if i % 2 == 0 else WHITE
        ws1[f"A{i}"] = k
        ws1[f"B{i}"] = v
        ws1[f"A{i}"].font = Font(bold=True, name="Arial", size=9, color="4B5270")
        ws1[f"A{i}"].fill = ws1[f"B{i}"].fill = PatternFill("solid", start_color=bg)
        dat(ws1[f"B{i}"])

    r = 4 + len(meta_rows) + 1
    ws1.merge_cells(f"A{r}:B{r}")
    ws1[f"A{r}"] = "Summary"
    hdr(ws1[f"A{r}"])
    total_funcs = sum(len(v) for v in result["imports"].values())
    for i, (k, v) in enumerate([
        ("Kit Matches",         len(result["kit_matches"])),
        ("Imported DLLs",       len(result["imports"])),
        ("Total Import Funcs",  total_funcs),
        ("Delay Import DLLs",   len(result["delay_imports"])),
        ("Exported Symbols",    len(result["exports"])),
        ("Unmapped DLLs",       len(result["unmapped_dlls"])),
    ], start=r + 1):
        bg = GRAY if i % 2 == 0 else WHITE
        ws1[f"A{i}"] = k
        ws1[f"B{i}"] = v
        ws1[f"A{i}"].font   = Font(bold=True, name="Arial", size=9, color="4B5270")
        ws1[f"A{i}"].fill   = ws1[f"B{i}"].fill = PatternFill("solid", start_color=bg)
        ws1[f"B{i}"].font   = Font(bold=True, size=11, color=RED, name="Arial")
        ws1[f"B{i}"].alignment = Alignment(horizontal="center", vertical="center")
        ws1[f"A{i}"].border = ws1[f"B{i}"].border = bdr
    ws1.column_dimensions["A"].width = 28
    ws1.column_dimensions["B"].width = 46


    ws2 = wb.create_sheet("Kit Matches")
    ws2.sheet_view.showGridLines = False
    hdrs2 = ["DLL Name", "DLL Description", "HarmonyOS Kit", "Import Path", "Coverage", "Recommendation", "Delay"]
    for ci, h in enumerate(hdrs2, 1):
        hdr(ws2.cell(row=1, column=ci, value=h))
    ws2.row_dimensions[1].height = 22
    row = 2
    for km in result["kit_matches"]:
        for src in km["dll_sources"]:
            bg   = WHITE if row % 2 == 0 else GRAY
            vals = [src.get("dll_name", ""), src.get("dll_display", ""),
                    km.get("kit_name", ""), km.get("harmony_import") or "",
                    (km.get("confidence") or "").capitalize(), km.get("note") or "",
                    "Yes" if src.get("is_delay") else "No"]
            for ci, v in enumerate(vals, 1):
                c = ws2.cell(row=row, column=ci, value=v)
                dat(c, wrap=(ci == 6))
                c.fill = PatternFill("solid", start_color=bg)
                if ci == 5:
                    c.font      = Font(bold=True, color=conf_clr.get(km.get("confidence"), "000000"), name="Arial", size=9)
                    c.alignment = Alignment(horizontal="center", vertical="center")
                if ci == 7:
                    c.alignment = Alignment(horizontal="center", vertical="center")
            ws2.row_dimensions[row].height = 18
            row += 1
    for ci, w in enumerate([28, 36, 32, 28, 12, 55, 8], 1):
        ws2.column_dimensions[get_column_letter(ci)].width = w
    ws2.freeze_panes = "A2"
    ws2.auto_filter.ref = f"A1:{get_column_letter(len(hdrs2))}1"


    ws3 = wb.create_sheet("Imports")
    ws3.sheet_view.showGridLines = False
    for ci, h in enumerate(["DLL", "Function", "Type"], 1):
        hdr(ws3.cell(row=1, column=ci, value=h))
    row = 2
    for dll, funcs in sorted(result["imports"].items()):
        for f in funcs:
            bg = WHITE if row % 2 == 0 else GRAY
            for ci, v in enumerate([dll, f, "Import"], 1):
                c = ws3.cell(row=row, column=ci, value=v)
                dat(c)
                c.fill = PatternFill("solid", start_color=bg)
            row += 1
    for dll, funcs in sorted(result["delay_imports"].items()):
        for f in funcs:
            bg = WHITE if row % 2 == 0 else GRAY
            for ci, v in enumerate([dll, f, "Delay Import"], 1):
                c = ws3.cell(row=row, column=ci, value=v)
                dat(c)
                c.fill = PatternFill("solid", start_color=bg)
            row += 1
    for ci, w in enumerate([36, 52, 14], 1):
        ws3.column_dimensions[get_column_letter(ci)].width = w
    ws3.freeze_panes = "A2"


    ws4 = wb.create_sheet("Unmapped")
    ws4.sheet_view.showGridLines = False
    for ci, h in enumerate(["DLL Name", "Function Count", "Sample Functions", "Delay"], 1):
        hdr(ws4.cell(row=1, column=ci, value=h))
    row = 2
    for u in result["unmapped_dlls"]:
        bg   = WHITE if row % 2 == 0 else GRAY
        vals = [u["dll_name"], u["func_count"], ", ".join(u["sample_funcs"]),
                "Yes" if u["is_delay"] else "No"]
        for ci, v in enumerate(vals, 1):
            c = ws4.cell(row=row, column=ci, value=v)
            dat(c, wrap=(ci == 3))
            c.fill = PatternFill("solid", start_color=bg)
        row += 1
    for ci, w in enumerate([34, 14, 60, 8], 1):
        ws4.column_dimensions[get_column_letter(ci)].width = w
    ws4.freeze_panes = "A2"
    ws4.auto_filter.ref = "A1:D1"

    wb.save(output_path)
    _print_ok(f"Excel report: {output_path}")


def export_excel_ipa(result: dict, output_path: Path):
    hdr, dat, bdr, RED, GRAY, WHITE, GRN, AMB, RED_C = _excel_styles()
    conf_clr = {"high": GRN, "medium": AMB, "low": RED_C}

    wb = Workbook()


    ws1 = wb.active
    ws1.title = "Overview"
    ws1.sheet_view.showGridLines = False
    ws1.merge_cells("A1:B1")
    ws1["A1"] = "IPA → HarmonyOS NEXT Migration Report"
    ws1["A1"].font      = Font(bold=True, size=14, color=RED, name="Arial")
    ws1["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws1.row_dimensions[1].height = 30

    ws1.merge_cells("A3:B3")
    ws1["A3"] = "App Info"
    hdr(ws1["A3"])
    meta_rows = [
        ("File",            result["file_name"]),
        ("Bundle ID",       result.get("bundle_id") or "—"),
        ("App Name",        result.get("app_name") or "—"),
        ("Version",         result.get("version") or "—"),
        ("Min iOS Version", result.get("min_ios_version") or "—"),
        ("Date",            datetime.now().strftime("%Y-%m-%d %H:%M")),
        ("Analysis (s)",    result["analysis_time_sec"]),
    ]
    for i, (k, v) in enumerate(meta_rows, start=4):
        bg = GRAY if i % 2 == 0 else WHITE
        ws1[f"A{i}"] = k
        ws1[f"B{i}"] = v
        ws1[f"A{i}"].font = Font(bold=True, name="Arial", size=9, color="4B5270")
        ws1[f"A{i}"].fill = ws1[f"B{i}"].fill = PatternFill("solid", start_color=bg)
        dat(ws1[f"B{i}"])

    r = 4 + len(meta_rows) + 1
    ws1.merge_cells(f"A{r}:B{r}")
    ws1[f"A{r}"] = "Summary"
    hdr(ws1[f"A{r}"])
    for i, (k, v) in enumerate([
        ("Kit Matches",          len(result["kit_matches"])),
        ("Frameworks (total)",   len(result["frameworks"])),
        ("Unmapped Frameworks",  len(result["unmapped_frameworks"])),
        ("Permissions (total)",  len(result["permissions"])),
        ("Permission Matches",   len(result["permission_matches"])),
        ("App Extensions",       len(result["extensions"])),
    ], start=r + 1):
        bg = GRAY if i % 2 == 0 else WHITE
        ws1[f"A{i}"] = k
        ws1[f"B{i}"] = v
        ws1[f"A{i}"].font   = Font(bold=True, name="Arial", size=9, color="4B5270")
        ws1[f"A{i}"].fill   = ws1[f"B{i}"].fill = PatternFill("solid", start_color=bg)
        ws1[f"B{i}"].font   = Font(bold=True, size=11, color=RED, name="Arial")
        ws1[f"B{i}"].alignment = Alignment(horizontal="center", vertical="center")
        ws1[f"A{i}"].border = ws1[f"B{i}"].border = bdr
    ws1.column_dimensions["A"].width = 28
    ws1.column_dimensions["B"].width = 46


    ws2 = wb.create_sheet("Kit Matches")
    ws2.sheet_view.showGridLines = False
    hdrs2 = ["Framework Name", "Framework Display", "HarmonyOS Kit", "Import Path", "Coverage", "Recommendation"]
    for ci, h in enumerate(hdrs2, 1):
        hdr(ws2.cell(row=1, column=ci, value=h))
    ws2.row_dimensions[1].height = 22
    row = 2
    for km in result["kit_matches"]:
        for src in km["framework_sources"]:
            bg   = WHITE if row % 2 == 0 else GRAY
            vals = [src.get("framework_name", ""), src.get("framework_display", ""),
                    km.get("kit_name", ""), km.get("harmony_import") or "",
                    (km.get("confidence") or "").capitalize(), km.get("note") or ""]
            for ci, v in enumerate(vals, 1):
                c = ws2.cell(row=row, column=ci, value=v)
                dat(c, wrap=(ci == 6))
                c.fill = PatternFill("solid", start_color=bg)
                if ci == 5:
                    c.font      = Font(bold=True, color=conf_clr.get(km.get("confidence"), "000000"), name="Arial", size=9)
                    c.alignment = Alignment(horizontal="center", vertical="center")
            ws2.row_dimensions[row].height = 18
            row += 1
    for ci, w in enumerate([28, 36, 32, 28, 12, 55], 1):
        ws2.column_dimensions[get_column_letter(ci)].width = w
    ws2.freeze_panes = "A2"
    ws2.auto_filter.ref = f"A1:{get_column_letter(len(hdrs2))}1"


    ws3 = wb.create_sheet("Permissions")
    ws3.sheet_view.showGridLines = False
    hdrs3 = ["iOS Key", "iOS Display", "HarmonyOS Permission", "HarmonyOS Kit"]
    for ci, h in enumerate(hdrs3, 1):
        hdr(ws3.cell(row=1, column=ci, value=h))
    ws3.row_dimensions[1].height = 22
    matched_keys = {pm["ios_key"] for pm in result["permission_matches"]}
    row = 2
    for pm in result["permission_matches"]:
        bg   = WHITE if row % 2 == 0 else GRAY
        vals = [pm["ios_key"], pm.get("ios_display", ""), pm.get("harmony", ""), pm.get("kit", "")]
        for ci, v in enumerate(vals, 1):
            c = ws3.cell(row=row, column=ci, value=v)
            dat(c)
            c.fill = PatternFill("solid", start_color=bg)
            if ci == 4:
                c.font = Font(bold=True, color=GRN, name="Arial", size=9)
        ws3.row_dimensions[row].height = 16
        row += 1
    for perm in result["permissions"]:
        if perm in matched_keys:
            continue
        bg   = WHITE if row % 2 == 0 else GRAY
        vals = [perm, "—", "—", "—"]
        for ci, v in enumerate(vals, 1):
            c = ws3.cell(row=row, column=ci, value=v)
            dat(c)
            c.fill = PatternFill("solid", start_color=bg)
            if ci == 4:
                c.font = Font(bold=True, color=AMB, name="Arial", size=9)
        ws3.row_dimensions[row].height = 16
        row += 1
    for ci, w in enumerate([50, 32, 50, 28], 1):
        ws3.column_dimensions[get_column_letter(ci)].width = w
    ws3.freeze_panes = "A2"
    ws3.auto_filter.ref = f"A1:{get_column_letter(len(hdrs3))}1"

    wb.save(output_path)
    _print_ok(f"Excel report: {output_path}")


def _rel_link(html_path, output_path) -> str:
    """Hyperlink target for a report, relative to the workbook that points at it.

    An absolute `file:///C:/...` URI resolves only on the machine that produced
    the workbook. Excel resolves a relative target against the workbook's own
    location, and the reports sit beside it in `result/`, so a bare filename
    travels with the folder.

    Forward slashes on purpose: the OOXML relationship target is a URI, not a
    Windows path. Falls back to the absolute URI only when no relative path
    exists at all -- a different drive, where os.path.relpath raises.
    """
    src = Path(html_path).resolve()
    try:
        rel = os.path.relpath(src, Path(output_path).resolve().parent)
    except ValueError:
        return src.as_uri()
    return rel.replace("\\", "/")


def export_excel_batch(
    rows: list,
    output_path: Path,
    unmapped_dlls: list | None = None,
    unmapped_frameworks: list | None = None,
    mapped_ns_apps: dict | None = None,
    mapped_ns_kit: dict | None = None,
    unmapped_ns_apps: dict | None = None,
    play_metadata: dict | None = None,
    ohpm_ns_apps: dict | None = None,
    ohpm_ns_meta: dict | None = None,
    frameworks: dict | None = None,
) -> None:
    hdr, dat, bdr, RED, GRAY, WHITE, GRN, AMB, RED_C = _excel_styles()
    DKBLUE = "1F3864"

    wb = Workbook()
    ws = wb.active
    ws.title = "Batch Summary"
    ws.sheet_view.showGridLines = False

    ws.merge_cells("A1:G1")
    ws["A1"] = "Migration Analyzer — Batch Summary"
    ws["A1"].font      = Font(bold=True, size=14, color=RED, name="Arial")
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 30

    headers = ["File", "App Name", "Platform", "Coverage %", "Kit Count", "Unmapped", "Permissions"]
    for ci, h in enumerate(headers, 1):
        hdr(ws.cell(row=2, column=ci, value=h), bg=DKBLUE)
    ws.row_dimensions[2].height = 22

    for ri, row in enumerate(rows, start=3):
        bg = GRAY if ri % 2 != 0 else WHITE

        cell = ws.cell(row=ri, column=1, value=row["file_name"])
        if row.get("html_path"):
            cell.hyperlink = _rel_link(row["html_path"], output_path)
            cell.font = Font(name="Arial", size=9, color="0563C1", underline="single")
        else:
            dat(cell)
        cell.fill = PatternFill("solid", start_color=bg)
        cell.border = bdr

        # Platform reads off the row's own framework dict, NOT the `frameworks`
        # argument: that one is keyed by package_name, which this sheet does not
        # carry. The "(+ secondary)" form matches the Framework column on App
        # Info. EXE/IPA rows have no framework and stay blank.
        fw   = row.get("framework") or {}
        plat = fw.get("framework") or ""
        hyb  = ", ".join(h["framework"] for h in (fw.get("hybrid") or []))
        if plat and hyb:
            plat = f"{plat} (+ {hyb})"
        # A packed app's Kit Count / Unmapped columns are single digits and look
        # like an analysis failure. Naming the packer here turns a mystery into
        # a finding.
        _fd = fw.get("detail") or {}
        if plat and "packed" in (_fd.get("note") or "").lower():
            plat = f"{plat} — DEX packed: {_fd.get('packer') or 'unknown'}"

        # Same rule as the report's stat card, via the same function, so the
        # sheet and the HTML cannot disagree. Not measurable -> an em-dash; the
        # Platform cell alongside already says why.
        cov_pct, cov_state = coverage_status(row)
        cov_val = cov_pct if cov_pct is not None else "—"

        # Coverage sits next to Platform, not next to the counts: the two are
        # read together (a packed platform is exactly why a coverage cell is
        # blank), and it is the headline number a reader scans for.
        vals = [row.get("app_name", ""), plat, cov_val, row.get("kit_count", ""),
                row.get("unmapped_count", ""), row.get("permission_count", "")]
        for ci, v in enumerate(vals, start=2):
            c = ws.cell(row=ri, column=ci, value=v)
            dat(c, align=("center" if ci >= 4 else "left"))
            c.fill = PatternFill("solid", start_color=bg)
            # Colour-coded at the same 70 / 40 thresholds the report uses.
            if ci == 4 and cov_pct is not None:
                c.font = Font(name="Arial", size=9, bold=True,
                              color=(GRN if cov_pct >= 70 else AMB if cov_pct >= 40 else RED_C))
            elif ci == 4:
                c.font = Font(name="Arial", size=9, color="9AA0AE")

        ws.row_dimensions[ri].height = 18

    for ci, w in enumerate([40, 32, 38, 13, 12, 13, 14], 1):
        ws.column_dimensions[get_column_letter(ci)].width = w
    ws.freeze_panes = "A3"
    ws.auto_filter.ref = f"A2:{get_column_letter(7)}2"

    # Play Store metadata -- inserted at index 0 so it lands FIRST in tab order.
    # APK-only; omitted entirely when there is nothing to show. Cells may carry
    # the placeholders produced by core.play_meta. No Size column by design:
    # Play no longer exposes an app size field.
    if play_metadata:
        ws_ai = wb.create_sheet("App Info", 0)
        ws_ai.sheet_view.showGridLines = False
        # Framework columns ride on App Info rather than a sheet of their own.
        # "Framework Version" is spelled out because "Version" here already means
        # the Play release. Store Region / Data Fetched / Source are provenance:
        # the scraper is an unofficial HTML scrape, so without them a stale row
        # and a live row look identical.
        hdrs_ai = ["Package Name", "App Name", "Category", "Installs", "Rating",
                   "Rating Count", "Developer", "Last Updated", "Version",
                   "Store Region", "Data Fetched", "Source",
                   "Framework", "Engine", "Framework Version", "Confidence",
                   "Packer", "Evidence"]
        for ci, h in enumerate(hdrs_ai, 1):
            hdr(ws_ai.cell(row=1, column=ci, value=h), bg=DKBLUE)
        ws_ai.row_dimensions[1].height = 22

        for ri, (pkg, meta) in enumerate(play_metadata.items(), start=2):
            bg   = WHITE if ri % 2 == 0 else GRAY
            meta = meta or {}
            fw   = (frameworks or {}).get(pkg) or {}
            fdet = fw.get("detail") or {}
            hyb  = ", ".join(h["framework"] for h in (fw.get("hybrid") or []))
            fname = fw.get("framework", "") or ""
            if hyb:
                fname = f"{fname} (+ {hyb})"
            vals = [
                pkg,
                meta.get("app_name", ""),     meta.get("category", ""),
                meta.get("installs", ""),     meta.get("rating", ""),
                meta.get("rating_count", ""), meta.get("developer", ""),
                meta.get("last_updated", ""), meta.get("version", ""),
                meta.get("store_region", ""), meta.get("fetched_on", ""),
                meta.get("data_source", ""),
                fname,
                fw.get("engine", "") or "",
                fw.get("version", "") or "",
                fw.get("confidence", "") or "",
                fdet.get("packer", "") or "",
                ", ".join(fw.get("evidence", []) or []),
            ]
            for ci, v in enumerate(vals, 1):
                c = ws_ai.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci in (4, 5, 6, 10, 11, 14, 16) else "left"),
                    wrap=(ci == 18))
                c.fill = PatternFill("solid", start_color=bg)
            ws_ai.row_dimensions[ri].height = 16

        for ci, w in enumerate([34, 30, 20, 18, 10, 14, 30, 16, 20,
                                13, 14, 15,
                                22, 10, 16, 12, 16, 46], 1):
            ws_ai.column_dimensions[get_column_letter(ci)].width = w
        ws_ai.freeze_panes = "A2"
        ws_ai.auto_filter.ref = f"A1:{get_column_letter(len(hdrs_ai))}1"

    # Batch rollup: one row per framework. Its own sheet rather than a block on
    # App Info, which would break that sheet's freeze pane and auto-filter.
    if frameworks:
        counts, examples = {}, {}
        for pkg, fw in frameworks.items():
            key = (fw or {}).get("framework") or "Unknown"
            counts[key] = counts.get(key, 0) + 1
            examples.setdefault(key, []).append(pkg)
        total_fw = sum(counts.values()) or 1
        idx = 1 if play_metadata else 0
        ws_fr = wb.create_sheet("Framework Rollup", idx)
        ws_fr.sheet_view.showGridLines = False
        ws_fr.merge_cells("A1:D1")
        ws_fr["A1"] = f"Built-with breakdown — {total_fw} app(s)"
        ws_fr["A1"].font = Font(bold=True, size=13, color=RED, name="Arial")
        ws_fr["A1"].alignment = Alignment(horizontal="left", vertical="center")
        ws_fr.row_dimensions[1].height = 26
        hdrs_fr = ["Framework", "Apps", "Share", "Example apps"]
        for ci, h in enumerate(hdrs_fr, 1):
            hdr(ws_fr.cell(row=2, column=ci, value=h), bg=DKBLUE)
        ws_fr.row_dimensions[2].height = 22
        for ri, (name, n) in enumerate(
                sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])), start=3):
            bg = WHITE if ri % 2 == 0 else GRAY
            vals = [name, n, round(100.0 * n / total_fw, 1),
                    ", ".join(sorted(examples[name])[:4])]
            for ci, v in enumerate(vals, 1):
                c = ws_fr.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci in (2, 3) else "left"), wrap=(ci == 4))
                c.fill = PatternFill("solid", start_color=bg)
            ws_fr.row_dimensions[ri].height = 16
        for ci, w in enumerate([26, 9, 9, 70], 1):
            ws_fr.column_dimensions[get_column_letter(ci)].width = w
        ws_fr.freeze_panes = "A3"

    def _common_rows(freq: dict) -> list:
        return sorted(
            ((ns, apps) for ns, apps in freq.items() if len(apps) >= _COMMON_MIN_APPS),
            key=lambda kv: (-len(kv[1]), kv[0]),
        )

    def _empty_note(sheet):
        c = sheet.cell(row=2, column=1,
                       value=f"No namespace appeared in {_COMMON_MIN_APPS} or more APKs.")
        c.font = Font(italic=True, name="Arial", size=9, color="4B5270")

    if mapped_ns_apps is not None:
        ws_cm = wb.create_sheet("Common Mapped")
        ws_cm.sheet_view.showGridLines = False
        hdrs_cm = ["Android Namespace", "Mapped Kit", "App Count", "Apps"]
        for ci, h in enumerate(hdrs_cm, 1):
            hdr(ws_cm.cell(row=1, column=ci, value=h), bg=DKBLUE)
        ws_cm.row_dimensions[1].height = 22

        common_mapped = _common_rows(mapped_ns_apps)
        for ri, (ns, apps) in enumerate(common_mapped, start=2):
            bg = WHITE if ri % 2 == 0 else GRAY
            vals = [ns, (mapped_ns_kit or {}).get(ns, ""), len(apps), ", ".join(sorted(apps))]
            for ci, v in enumerate(vals, 1):
                c = ws_cm.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci == 3 else "left"), wrap=(ci == 4))
                c.fill = PatternFill("solid", start_color=bg)
            ws_cm.row_dimensions[ri].height = 16
        if not common_mapped:
            _empty_note(ws_cm)
        for ci, w in enumerate([46, 30, 11, 60], 1):
            ws_cm.column_dimensions[get_column_letter(ci)].width = w
        ws_cm.freeze_panes = "A2"
        ws_cm.auto_filter.ref = f"A1:{get_column_letter(len(hdrs_cm))}1"

    if unmapped_ns_apps is not None:
        ws_cu = wb.create_sheet("Common Unmapped")
        ws_cu.sheet_view.showGridLines = False
        hdrs_cu = ["Android Namespace", "App Count", "Apps"]
        for ci, h in enumerate(hdrs_cu, 1):
            hdr(ws_cu.cell(row=1, column=ci, value=h), bg=DKBLUE)
        ws_cu.row_dimensions[1].height = 22

        common_unmapped = _common_rows(unmapped_ns_apps)
        for ri, (ns, apps) in enumerate(common_unmapped, start=2):
            bg = WHITE if ri % 2 == 0 else GRAY
            vals = [ns, len(apps), ", ".join(sorted(apps))]
            for ci, v in enumerate(vals, 1):
                c = ws_cu.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci == 2 else "left"), wrap=(ci == 3))
                c.fill = PatternFill("solid", start_color=bg)
            ws_cu.row_dimensions[ri].height = 16
        if not common_unmapped:
            _empty_note(ws_cu)
        for ci, w in enumerate([50, 11, 60], 1):
            ws_cu.column_dimensions[get_column_letter(ci)].width = w
        ws_cu.freeze_panes = "A2"
        ws_cu.auto_filter.ref = f"A1:{get_column_letter(len(hdrs_cu))}1"

    if ohpm_ns_apps:
        # Second tier. No _COMMON_MIN_APPS threshold here, unlike the Common
        # sheets: the whole OHPM tier is small enough that a single-app hit is
        # still a real finding. Omitted entirely when empty.
        ws_oh = wb.create_sheet("OHPM Matches")
        ws_oh.sheet_view.showGridLines = False
        hdrs_oh = ["Android Namespace", "OHPM Package", "Install", "Category",
                   "Confidence", "App Count", "Apps"]
        for ci, h in enumerate(hdrs_oh, 1):
            hdr(ws_oh.cell(row=1, column=ci, value=h), bg=DKBLUE)
        ws_oh.row_dimensions[1].height = 22

        meta = ohpm_ns_meta or {}
        ohpm_rows = sorted(
            ohpm_ns_apps.items(),
            key=lambda kv: (-len(kv[1]), -(meta.get(kv[0], {}).get("method_count") or 0), kv[0]),
        )
        for ri, ((ns, pkg), apps) in enumerate(ohpm_rows, start=2):
            bg = WHITE if ri % 2 == 0 else GRAY
            m  = meta.get((ns, pkg), {})
            vals = [ns, pkg, m.get("install_cmd") or f"ohpm install {pkg}",
                    m.get("category") or "", m.get("confidence") or "",
                    len(apps), ", ".join(sorted(apps))]
            for ci, v in enumerate(vals, 1):
                c = ws_oh.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci in (5, 6) else "left"), wrap=(ci == 7))
                c.fill = PatternFill("solid", start_color=bg)
            ws_oh.row_dimensions[ri].height = 16
        for ci, w in enumerate([46, 30, 38, 34, 12, 11, 60], 1):
            ws_oh.column_dimensions[get_column_letter(ci)].width = w
        ws_oh.freeze_panes = "A2"
        ws_oh.auto_filter.ref = f"A1:{get_column_letter(len(hdrs_oh))}1"

    if unmapped_dlls:
        ws2 = wb.create_sheet("Unmapped DLLs")
        ws2.sheet_view.showGridLines = False
        hdrs2 = ["DLL Name", "App Count", "Total Func Count", "Apps", "Sample Functions"]
        for ci, h in enumerate(hdrs2, 1):
            hdr(ws2.cell(row=1, column=ci, value=h), bg=DKBLUE)
        ws2.row_dimensions[1].height = 22
        for ri, u in enumerate(unmapped_dlls, start=2):
            bg = WHITE if ri % 2 == 0 else GRAY
            vals = [
                u["dll_name"], len(u["apps"]), u["func_count"],
                ", ".join(u["apps"]), ", ".join(u["sample_funcs"]),
            ]
            for ci, v in enumerate(vals, 1):
                c = ws2.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci in (2, 3) else "left"), wrap=(ci in (4, 5)))
                c.fill = PatternFill("solid", start_color=bg)
            ws2.row_dimensions[ri].height = 16
        for ci, w in enumerate([40, 11, 16, 40, 55], 1):
            ws2.column_dimensions[get_column_letter(ci)].width = w
        ws2.freeze_panes = "A2"
        ws2.auto_filter.ref = f"A1:{get_column_letter(len(hdrs2))}1"

    if unmapped_frameworks:
        ws3 = wb.create_sheet("Unmapped Frameworks")
        ws3.sheet_view.showGridLines = False
        hdrs3 = ["Framework", "App Count", "Apps"]
        for ci, h in enumerate(hdrs3, 1):
            hdr(ws3.cell(row=1, column=ci, value=h), bg=DKBLUE)
        ws3.row_dimensions[1].height = 22
        for ri, u in enumerate(unmapped_frameworks, start=2):
            bg = WHITE if ri % 2 == 0 else GRAY
            vals = [u["framework"], len(u["apps"]), ", ".join(u["apps"])]
            for ci, v in enumerate(vals, 1):
                c = ws3.cell(row=ri, column=ci, value=v)
                dat(c, align=("center" if ci == 2 else "left"), wrap=(ci == 3))
                c.fill = PatternFill("solid", start_color=bg)
            ws3.row_dimensions[ri].height = 16
        for ci, w in enumerate([45, 11, 55], 1):
            ws3.column_dimensions[get_column_letter(ci)].width = w
        ws3.freeze_panes = "A2"
        ws3.auto_filter.ref = f"A1:{get_column_letter(len(hdrs3))}1"

    # Tab order is asserted here rather than left to the order the code happens
    # to build sheets in. The order tells a story: what the portfolio IS, then
    # per-app results, then what DID map, then what did NOT. Any sheet not
    # listed keeps its relative position at the end.
    _TAB_ORDER = ["App Info", "Framework Rollup", "Batch Summary", "Common Mapped",
                  "OHPM Matches", "Common Unmapped", "Unmapped DLLs",
                  "Unmapped Frameworks"]
    for name in reversed(_TAB_ORDER):
        if name in wb.sheetnames:
            sheet = wb[name]
            wb.move_sheet(sheet, offset=-wb.index(sheet))   # to the front
    wb.active = 0

    wb.save(output_path)
    _print_ok(f"Batch Excel: {output_path}")


def export_excel_batch_unmapped(per_file_unmapped: dict, output_path: Path) -> None:
    hdr, dat, bdr, RED, GRAY, WHITE, GRN, AMB, RED_C = _excel_styles()

    wb = Workbook()
    ws0 = wb.active
    used_names: set = set()
    sheets_written = False

    for file_stem, unmapped in per_file_unmapped.items():
        if not unmapped:
            continue

        raw_name = re.sub(r'[\[\]:*?/\\]', "_", file_stem)[:31]
        sheet_name, n = raw_name, 1
        while sheet_name in used_names:
            suffix = f"_{n}"
            sheet_name = raw_name[:31 - len(suffix)] + suffix
            n += 1
        used_names.add(sheet_name)

        ws = ws0 if not sheets_written else wb.create_sheet(sheet_name)
        if not sheets_written:
            ws.title = sheet_name
        sheets_written = True

        ws.sheet_view.showGridLines = False
        hdrs = ["Namespace", "Class Count", "Method Count", "Sample Methods"]
        for ci, h in enumerate(hdrs, 1):
            hdr(ws.cell(row=1, column=ci, value=h))
        ws.row_dimensions[1].height = 22
        row = 2
        for u in unmapped:
            bg = WHITE if row % 2 == 0 else GRAY
            vals = [u["namespace"], u["class_count"], u["method_count"],
                    ", ".join(u["sample_methods"])]
            for ci, v in enumerate(vals, 1):
                c = ws.cell(row=row, column=ci, value=v)
                dat(c, wrap=(ci == 4))
                c.fill = PatternFill("solid", start_color=bg)
            ws.row_dimensions[row].height = 16
            row += 1
        for ci, w in enumerate([50, 12, 14, 60], 1):
            ws.column_dimensions[get_column_letter(ci)].width = w
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = f"A1:{get_column_letter(len(hdrs))}1"

    if not sheets_written:
        ws0.title = "No Unmapped"
        ws0["A1"] = "No unmapped namespaces found in any analyzed file."
        ws0["A1"].font = Font(italic=True, name="Arial", size=10, color="4B5270")
        ws0.column_dimensions["A"].width = 55

    wb.save(output_path)
    _print_ok(f"Batch unmapped Excel: {output_path}")


# Emitted once at the top of agent_summary.json, never per app. The per-app
# files carry tier:"ohpm" on every row, which is self-describing; this is the
# prose form for a human or LLM reading the batch summary.
OHPM_SCHEMA_NOTE = (
    "ohpm_matches are second-tier third-party OHPM packages, NOT native "
    "HarmonyOS kits — treat them as external dependencies with their own "
    "license and maintenance implications, and prefer a native kit from "
    "kit_list where one exists."
)


def build_agent_json(result: dict) -> dict:
    mode = result["mode"]
    now  = datetime.now().isoformat(timespec="seconds")

    kit_list = []
    for km in result["kit_matches"]:
        entry = {
            "kit_name":    km["kit_name"],
            # Explicit, so a consumer can positively confirm these are native
            # kits rather than only inferring it from the absence of an OHPM tag.
            # kit_list is rebuilt field-by-field here, so the engine's km["tier"]
            # would otherwise be dropped.
            "tier":        km.get("tier", "native"),
            "confidence":  km["confidence"],
            "note":        km["note"],
            "doc_url":     get_doc_url(km["kit_name"], result.get("target", "hmos")),
            "sample_url":  km.get("sample_url"),
            "codelab_url": km.get("codelab_url"),
        }
        if mode == "apk":
            entry["source_namespaces"] = [s["android_namespace"] for s in km["android_sources"]]
        elif mode == "ipa":
            entry["source_frameworks"] = [s["framework_name"] for s in km["framework_sources"]]
        else:
            entry["source_dlls"] = [s["dll_name"] for s in km["dll_sources"]]
        kit_list.append(entry)

    counts = {"high": 0, "medium": 0, "low": 0}
    for km in result["kit_matches"]:
        counts[km["confidence"]] = counts.get(km["confidence"], 0) + 1
    total = sum(counts.values())
    confidence_scores = {
        **counts,
        "total":    total,
        "high_pct": round(counts["high"] / total, 3) if total else 0.0,
    }

    if mode == "apk":
        app_metadata = {
            "package_name":      result["package_name"],
            "app_name":          result["app_name"],
            "version_name":      result["version_name"],
            "version_code":      result["version_code"],
            "min_sdk":           result["min_sdk"],
            "target_sdk":        result["target_sdk"],
            "permission_count":  len(result["permissions"]),
            "obfuscated_count":  result.get("obfuscated_count", 0),
            "analysis_time_sec": result["analysis_time_sec"],
        }
    elif mode == "ipa":
        app_metadata = {
            "file_name":          result["file_name"],
            "bundle_id":          result.get("bundle_id"),
            "app_name":           result.get("app_name"),
            "version":            result.get("version"),
            "min_ios_version":    result.get("min_ios_version"),
            "framework_count":    len(result["frameworks"]),
            "permission_count":   len(result["permissions"]),
            "analysis_time_sec":  result["analysis_time_sec"],
        }
    elif mode == "exe_folder":
        app_metadata = {
            "folder_name":       result["folder_name"],
            "file_count":        result["file_count"],
            "files":             [f["file_name"] for f in result["files"]],
            "dll_count":         len(result["imports"]),
            "analysis_time_sec": result["analysis_time_sec"],
        }
    else:
        app_metadata = {
            "file_name":         result["file_name"],
            "machine":           result["machine"],
            "subsystem":         result["subsystem"],
            "is_dotnet":         result["is_dotnet"],
            "is_packed":         result["is_packed"],
            "dll_count":         len(result["imports"]),
            "analysis_time_sec": result["analysis_time_sec"],
        }

    agent = {
        "schema_version":    "1.0",
        "generated_at":      now,
        "mode":              mode,
        "target":            result.get("target", "hmos"),
        "app_metadata":      app_metadata,
        "kit_list":          kit_list,
        "confidence_scores": confidence_scores,
    }
    if mode == "apk":
        agent["api_matches"]     = result.get("api_matches", [])
        agent["permission_gaps"] = result.get("permission_gaps", [])
        # Passed through verbatim, exactly like api_matches above, so each row
        # keeps the engine's tier:"ohpm" tag. No per-app schema note: the prose
        # explanation lives ONCE at the top of agent_summary.json.
        agent["ohpm_matches"]    = result.get("ohpm_matches", [])
        # Top level and tier-independent: this describes what the app was BUILT
        # with, which is orthogonal to the native/OHPM mapping tiers. Passed
        # through verbatim so the packer name and both confidence values survive.
        agent["framework"]       = result.get("framework") or {}
    agent["device_matrix"] = result.get("device_matrix", {})
    return agent


def write_agent_json(result: dict, output_path: Path) -> None:
    output_path.parent.mkdir(exist_ok=True)
    data = build_agent_json(result)
    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    _print_ok(f"Agent JSON: {output_path}")


def _print_summary_apk(result: dict):
    conf_colors = {"high": (C.BOLD, C.GREEN), "medium": (C.BOLD, C.YELLOW), "low": (C.BOLD, C.RED)}
    conf_labels = {"high": "HIGH", "medium": "MED ", "low": "LOW "}
