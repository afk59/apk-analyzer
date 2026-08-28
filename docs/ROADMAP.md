# v2 Roadmap

Status: `todo` · `wip` · `done`. Update the status line when a milestone closes, and record what
was measured — not what was intended.

---

## M0 — Skeleton `done` (2026-08-28)

Branch `v2` and a separate working folder; `src/` → `engine/` with behaviour verified unchanged;
v1's history archived under `docs/v1/`; short root `CLAUDE.md`; ADRs for the four decisions taken.

**Verified:** `python engine/analyzer.py <apk>` produces a report from the new location.

---

## M1 — App shell `todo`

The window opens, the backend answers, nothing analyses yet.

- `python -m app` launches uvicorn on a free loopback port and a pywebview window onto it
- Graceful fallback: if pywebview is unavailable, open the default browser and say so
- Native pickers: `POST /api/pick?kind=file|folder` returns a real absolute path
- `POST /api/open` → `os.startfile` on a path **inside the result tree only** (path check, so a
  crafted request cannot open an arbitrary file)
- Design tokens + shell layout, light and dark

**Acceptance:** window opens, a file picked through the dialog round-trips its path to the UI, an
existing v1 report opens in the browser from a click.

---

## M2 — Run an analysis with real progress `todo`

- `app/worker.py`: analyse ONE file in its own process, emit JSONL progress to stdout
- Progress stages come from the engine's real phases, not a fake timer:
  `loading → dex scan → kit matching → api matching → rendering → done`
- `JobRunner`: queue, one subprocess at a time, cancel, per-file failure isolation
- SSE `/api/runs/{id}/events`; UI shows current file, stage, elapsed, and n/total
- Batch = folder pick → every supported file in it, sequentially

**Acceptance:** a 5-APK folder runs end to end; killing one file does not stop the run; the
produced HTML/XLSX are byte-identical to what the v1 CLI produces for the same inputs.

> The last clause is the real test. If output differs, the UI has started doing the engine's job.

---

## M3 — Results library `todo`

- SQLite schema + migration-on-open; rescan rebuilds it from `result/` alone
- Run list → app cards: name, package, framework badge, coverage, kit/unmapped counts
- Click a card → open HTML; a second action → open the Excel
- Packed-DEX and low-sample apps carry the same honesty the report already has: no percentage,
  the reason shown instead

**Acceptance:** delete `analyzer.db`, reopen, the library is identical.

---

## M4 — APK search & download `todo`

Enter a package name, fetch the APK, then analyse it.

- `app/services/downloader.py` — the only new network code; isolated like `play_meta.py`
- Source adapters behind one interface, tried in order; every one of them is HTML scraping and
  will break without notice, so failures must be legible, not silent
- Verify what arrived: it must be a real APK (`classes.dex` + `AndroidManifest.xml` present) and
  its manifest package must match what was asked for — the corpus already contains two files
  that are the wrong app entirely, and that cost real analysis time
- Download → `input/`, then hand straight to the JobRunner

**Acceptance:** a known package downloads, verifies, and analyses in one flow; a nonexistent one
fails with a message naming which sources were tried.

> Scope note: only for apps the team is authorised to analyse. Sources are third-party mirrors
> with their own terms; treat availability as best-effort and never as a guarantee.

---

## M5 — Mapping re-grounding against `docs-ref` `todo`

The reason v2 exists at all, alongside the UI. See `MAPPING_DISCIPLINE.md` and `DOCS_REF_GUIDE.md`.

- Re-test every **rejected** candidate in `docs/v1/MAPPING_CANDIDATES_2026-08-20.md` and the six
  recorded genuine gaps against the SDK `.d.ts` corpus — v1's rejections rested on
  `hmos_api_index.json`, where NOT FOUND meant *unconfirmed*, and two such cuts were already
  reversed once
- Rank the ~1,771 `Common Unmapped` rows again with the declaration corpus available
- Build a `kit ↔ module` table straight from `docs-ref/ArkTS-*/kits/@kit.*.d.ts` (47 kits) and
  reconcile it against `KIT_DOC_URLS` and every `harmony_kit` value in use
- Audit the 50 legacy `-V5` doc URLs, which HTTP status cannot verify

**Acceptance:** each new row cites a `.d.ts` path or a doc path; absorption predicted before the
run and confirmed after; shadowing measured and zero.

---

## M6 — Packaging `todo`

- `requirements.txt` pinned; first-run install keeps v1's XGATE proxy-stripping behaviour
- `run.bat` unchanged in spirit: one double-click
- A short operator README: what to do when a download source dies, when Play metadata goes `N/A`

---

## Carried over from v1, unresolved

| Item | Where it is written up |
|---|---|
| No automated tests anywhere | `docs/v1/ENGINE_REFERENCE.md`, housekeeping round |
| Per-process batch runner never committed | v1 log §1, §16 — M2 supersedes it |
| `device_matrix` always `{}` in agent JSON | v1 Known gaps |
| 50 legacy `-V5` doc URLs unaudited | M5 |
| No `export_excel_exe_folder` | v1 Known gaps |
| Two corpus files are the wrong app (Aptoide, Uptodown) | v1 log, BUG X — maintainer's call |
