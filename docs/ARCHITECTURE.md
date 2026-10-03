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
│    data/mappings     THE PRODUCT: see MAPPING_DISCIPLINE.md     │
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

**Downloads overlap analysis; analyses never overlap each other.** A package list is fetched on
its own thread (`fetch-<run>`) that appends each verified APK to the run's input list and wakes
the analysis loop, so the first APK is being analysed while the rest download. Downloading holds
no androguard heap, so this does not weaken the one-worker-at-a-time rule. A cancel raises from
the download's progress callback, which aborts the body in flight and deletes the partial file.

## Inputs a run can be given

| Picked | Becomes |
|---|---|
| one file | one input, never skipped |
| a folder of APK/IPA (or mixed with EXE/DLL) | every supported file at the top level — one level, as the CLI's batch |
| a **program folder** — EXE/DLL at the top level, no APK/IPA | **batch** by default: every EXE/DLL, subfolders included, each with its own report, plus the two batch workbooks. `*.resources.dll` (.NET language packs, no code) are left out unless asked for. `pc_mode: "combined"` is the engine's `exe_folder` mode instead: one merged report |
| package names (comma, `;` or newline separated, repeats dropped) | downloaded and analysed in one run |

**Output names never collide within a run.** Two inputs that would write the same report —
`ShareX.exe` beside `ShareX.dll`, or `x.dll` in two subfolders — get a `--stem` override built
from their path relative to the picked folder (`ShareX.dll_exe_hmos_report.html`,
`plugins__x.dll_exe_hmos_report.html`). Anything that collides with nothing keeps the CLI's name.
`jobs.plan_names()` decides; it is deterministic, which is what `skip_existing` relies on.

## Data flow — analysing

```
UI: "Select APK"        → POST /api/pick        → native dialog (real path)
UI: "Analyze"           → POST /api/runs        → run_id
                                                → JobRunner spawns worker(s)
worker stdout (JSONL)   → SSE /api/runs/{id}/events
                        → UI progress bar + per-stage animation
worker finishes         → HTML + XLSX + agent JSON written to result/  (unchanged)
run finishes            → manifest in result/.runs/ → SQLite rebuilt from disk
UI: results list        → GET /api/results      → app cards with coverage/framework
UI: page reloaded       → GET /api/runs/latest  → re-attach to the run's event stream
UI: click a card        → POST /api/open        → os.startfile(path)   → Excel/browser opens
UI: × on a card (twice) → POST /api/results/delete → files + manifest entries removed → rescan
UI: tick + Delete selected → POST /api/results/delete-many → same, one manifest sweep, ONE rescan
```

**Deleting edits the manifests, not just the database.** The index is rebuilt from them, so a row
removed only from SQLite would come back on the next rescan. A delete is keyed by the report's
path — never by row id, which is reassigned on every rescan — and removes the report, its
workbook, its agent JSON and its side-car, then drops that report from **every** manifest that
lists it (re-analysing an input overwrites one report that several runs point at). A manifest
left with nothing to show is removed. The batch workbooks are not touched: they record the batch
they summarise. Same guard as `/api/open` — resolved path inside `result/`, and it must be a
`*_report.html`.

`os.startfile` is why this is a local app and not a web page: a browser cannot open a local
workbook, and `<input type=file>` never yields a real path. Both are solved by the native side.

## SQLite — an index, not a replacement

`app/store/analyzer.db`. The HTML and Excel files remain the deliverable; the database exists so
the UI can list, filter and compare without re-reading every file on disk.

```sql
-- SCHEMA_VERSION 4. The authoritative definition is app/store/db.py.
runs      (id, started_at, finished_at, mode, target, status, input_path, file_count,
           skipped_count, manifest)               -- manifest: file name in result/.runs/
apps      (id, run_id, source_file, package_name, app_name, version, framework,
           engine_name, packer, coverage_pct, coverage_status, kit_count,
           unmapped_count, ohpm_count, permission_count, analysis_time_sec,
           status, error)
artifacts (id, app_id, kind, path)            -- kind: html | xlsx | agent_json
downloads (id, run_id, package_name, source, state, file_path, version, size,
           requested_at, error, note)         -- one row per fetch attempt (ADR 0006)
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
- Run manifests still hold the **absolute** report path the worker wrote. Rescan and delete
  resolve it by file name against the current `RESULT_DIR` first (`index._locate`), since
  every report lives directly there -- that is what makes a moved or copied result folder
  work, including for manifests written before the fix (audit 2026-10-03, BUG-05).

## Side-cars

`result/.sidecars/` holds what the batch workbooks need from each analysed input, so a resumed
batch can rebuild them for files it skipped. APK: `<stem>_<target>.json` (namespaces, framework,
counts — the name it has always had). EXE / IPA / exe_folder: `<stem>_<mode>_<target>.json`,
carrying the batch row's counts. Before 2026-10-02 only APKs had one, and a resumed batch silently
dropped every EXE/DLL/IPA it skipped from `batch_summary.xlsx`.

## Frontend

Vanilla HTML/CSS/JS on purpose: no npm, no build step, no toolchain to install behind XGATE, and
the same skill the team already uses for `renderer.py`'s report CSS. State is small enough that a
framework would cost more than it saves.

- `app/web/index.html` — shell, one page, panel-based navigation
- `app/web/css/` — design tokens first, then components; light/dark both defined
- `app/web/js/` — `main.js` (panels, pickers, results), `run.js` (a run and its SSE
  stream), `api.js` (fetch wrapper), `i18n.js`, `theme.js`

The SSE stream gives every event its position as `id:`, and the endpoint honours
`Last-Event-ID`, so EventSource's own reconnect resumes instead of replaying.

The report's visual language (accent red `#c8002a` for HarmonyOS chrome, slate for third-party,
green/amber/blue status badges) carries over, so a report opened from the app does not look like
a different product.

## What the UI must never do

- Re-implement matching, coverage or confidence. Call the engine.
- Write HTML or Excel itself. `engine/core/renderer.py` owns both.
- Block on an analysis in the request thread. Everything long-running goes through the JobRunner.
- Treat a database row as authoritative over the file it indexes.
