# Architecture — v2

## Layers

```
┌─────────────────────────────────────────────────────────────────┐
│  app/web/            frontend: HTML + CSS + vanilla JS          │
│                      no build step, no npm, no framework        │
├─────────────────────────────────────────────────────────────────┤
│  app/api/            FastAPI: REST + SSE progress stream        │
│  app/services/       job runner · downloader · native dialogs   │
│  app/store/          SQLite index over the file outputs         │
├─────────────────────────────────────────────────────────────────┤
│  engine/             v1 analysis code — FROZEN                  │
│    core/apk_engine   androguard → namespaces → kits             │
│    core/renderer     HTML report + Excel workbooks              │
│    data/mappings     THE PRODUCT: 279 native + 15 OHPM rows     │
│    data/reference    API index, OHPM registry, Play cache       │
├─────────────────────────────────────────────────────────────────┤
│  docs-ref/           HarmonyOS SDK .d.ts + official docs        │
│                      read-only, mapping-time only, never runtime│
└─────────────────────────────────────────────────────────────────┘
```

`app/` imports `engine/`. **`engine/` imports nothing from `app/`** — that one-way rule is what
keeps "the engine is unchanged" true by construction rather than by testing, exactly as v1 kept
`play_meta` / `ohpm_fetch` / `framework_detect` isolated.

## Process model

The window, the web server and the analysis all have different failure modes, so they do not
share a process.

```
run.bat
 └─ python -m app                          [main process]
     ├─ uvicorn on 127.0.0.1:<free port>   [background thread]
     ├─ pywebview window                   [main thread — must own it]
     └─ JobRunner
         └─ subprocess: python -m app.worker <file>   [one per input file]
```

**Why a subprocess per file, not a thread or a loop:** androguard holds the whole DEX xref graph
in memory and does not give it back. v1 measured this repeatedly — a single-process batch over
the 43-app corpus died four times at three different points, while one fresh process per APK did
the same corpus in 27 minutes with zero failures. The worker exits, the OS reclaims the memory,
and a crash costs only the file in flight. See `decisions/0005-process-isolation.md`.

The worker prints progress as one JSON object per line on stdout; the JobRunner parses those and
pushes them to the browser over SSE. Nothing is shared but the pipe.

## Data flow — analysing

```
UI: "Select APK"        → POST /api/pick        → native dialog (real path)
UI: "Analyze"           → POST /api/runs        → run_id
                                                → JobRunner spawns worker(s)
worker stdout (JSONL)   → SSE /api/runs/{id}/events
                        → UI progress bar + per-stage animation
worker finishes         → HTML + XLSX + agent JSON written to result/  (unchanged)
                        → row inserted into SQLite
UI: results list        → GET /api/runs/{id}    → app cards with coverage/framework
UI: click a card        → POST /api/open        → os.startfile(path)   → Excel/browser opens
```

`os.startfile` is why this is a local app and not a web page: a browser cannot open a local
workbook, and `<input type=file>` never yields a real path. Both are solved by the native side.

## SQLite — an index, not a replacement

`app/store/analyzer.db`. The HTML and Excel files remain the deliverable; the database exists so
the UI can list, filter and compare without re-reading every file on disk.

```sql
runs      (id, started_at, finished_at, mode, target, status, input_path, file_count)
apps      (id, run_id, package_name, app_name, version, framework, engine_name,
           coverage_pct, coverage_status, kit_count, unmapped_count, ohpm_count,
           permission_count, packer, analysis_time_sec)
artifacts (id, app_id, kind, path)            -- kind: html | xlsx | agent_json
downloads (package_name, source, state, file_path, requested_at, error)
```

Rules:
- **Every column is derivable from an artifact on disk.** Delete the DB and a rescan rebuilds it.
  Nothing that only exists in the database may ever be a business output.
- `coverage_pct` / `coverage_status` come from `engine.core.renderer.coverage_status()` — the
  same single source of truth the report and the workbook already share. Never recompute.
  Since 2026-09-24 the formula is `(total_detected_ns + total_ohpm_ns) / total_3p_ns` — a
  namespace with an OHPM port counts as covered. A report without `total_ohpm_ns` (written
  earlier) keeps the kit-only figure it was published with.
- Paths are stored **relative to the repo root** so a moved or shared folder still resolves.

## Frontend

Vanilla HTML/CSS/JS on purpose: no npm, no build step, no toolchain to install behind XGATE, and
the same skill the team already uses for `renderer.py`'s report CSS. State is small enough that a
framework would cost more than it saves.

- `app/web/index.html` — shell, one page, panel-based navigation
- `app/web/css/` — design tokens first, then components; light/dark both defined
- `app/web/js/` — one module per panel, plus `sse.js` and `api.js`

The report's visual language (accent red `#c8002a` for HarmonyOS chrome, slate for third-party,
green/amber/blue status badges) carries over, so a report opened from the app does not look like
a different product.

## What the UI must never do

- Re-implement matching, coverage or confidence. Call the engine.
- Write HTML or Excel itself. `engine/core/renderer.py` owns both.
- Block on an analysis in the request thread. Everything long-running goes through the JobRunner.
- Treat a database row as authoritative over the file it indexes.
