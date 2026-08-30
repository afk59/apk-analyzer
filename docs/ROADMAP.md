# v2 Roadmap

Status: `todo` · `wip` · `done`. Update the status line when a milestone closes, and record what
was measured — not what was intended.

---

## M0 — Skeleton `done` (2026-08-28)

Branch `v2` and a separate working folder; `src/` → `engine/` with behaviour verified unchanged;
v1's history archived under `docs/v1/`; short root `CLAUDE.md`; ADRs for the four decisions taken.

**Verified:** `python engine/analyzer.py <apk>` produces a report from the new location.

---

## M1 — App shell `done` (2026-08-29)

The window opens, the backend answers, nothing analyses yet.

- `python -m app` launches uvicorn on a free loopback port and a pywebview window onto it
- Graceful fallback: if pywebview is unavailable, open the default browser and say so
- Native pickers: `POST /api/pick?kind=file|folder` returns a real absolute path
- `POST /api/open` → `os.startfile` on a path **inside the result tree only** (path check, so a
  crafted request cannot open an arbitrary file)
- Design tokens + shell layout, light and dark

**Acceptance:** window opens, a file picked through the dialog round-trips its path to the UI, an
existing v1 report opens in the browser from a click.

**Met.** Window reports `MainWindowTitle 'Migration Analyzer'`, `Responding=True`. The `/api/open`
guard was verified against three cases: an outside path and `engine/result/../../../Windows/…`
both 403, a missing path inside 404, a real report 200 and opens.

---

## M2 — Run an analysis with real progress `done` (2026-08-29)

- `app/worker.py`: analyse ONE file in its own process, emit JSONL progress to stdout
- Progress stages come from the engine's real phases, not a fake timer:
  `loading → dex scan → kit matching → api matching → rendering → done`
- `JobRunner`: queue, one subprocess at a time, cancel, per-file failure isolation
- SSE `/api/runs/{id}/events`; UI shows current file, stage, elapsed, and n/total
- Batch = folder pick → every supported file in it, sequentially

**Acceptance:** a 5-APK folder runs end to end; killing one file does not stop the run; the
produced HTML/XLSX are byte-identical to what the v1 CLI produces for the same inputs.

> The last clause is the real test. If output differs, the UI has started doing the engine's job.

**Met, and extended.** Per-app HTML and agent JSON hash identical to the CLI's; the XLSX differs
in exactly two entries, both timestamps (`docProps/core.xml`, one digit of the analysis-time cell).
A 4-file folder run: corrupt `.apk` failed and the run continued, `.apkm` never picked up, an
already-analysed file skipped, packed app's coverage suppressed. Cancel terminates the file in
flight and stops the queue.

The batch workbooks were added on top, because a folder run that does not produce them is not
equivalent to `--batch`. `app/aggregate.py` replays run_batch's aggregation over the side-cars and
calls the REAL exporters. Verified cell by cell against v1's own `run_batch` over identical
inputs: **all 6 sheets of `batch_summary.xlsx` and both sheets of `batch_unmapped.xlsx`
identical**.

---

## M3 — Results library `done` (2026-08-29)

- SQLite schema + migration-on-open; rescan rebuilds it from `result/` alone
- Run list → app cards: name, package, framework badge, coverage, kit/unmapped counts
- Click a card → open HTML; a second action → open the Excel
- Packed-DEX and low-sample apps carry the same honesty the report already has: no percentage,
  the reason shown instead

**Acceptance:** delete `analyzer.db`, reopen, the library is identical.

**Met.** Two things were needed to make it literally true: run grouping exists nowhere on disk, so
a finished run writes a manifest to `engine/result/.runs/`; and coverage would have been lost,
because the agent JSON has no namespace counts — they are read back from the report's own
`report_data` block and handed to the engine's `coverage_status()`. Schema changes rebuild rather
than ALTER, since every column is derivable from disk.

---

## M4 — APK search & download `done` (2026-08-29)

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

**Met.** `d.apkpure.com`'s direct endpoint — no HTML parsing, and a missing package answers a
clean 404. Verified against the local corpus: the bytes served match the sizes of files already
on disk.

Two things the testing changed:

* **`/b/APK/` does not always serve a single APK.** `com.foodgulu` came back as a 143.9 MB App
  Bundle at that path. Since App Bundle is the Play default, rejecting it would have failed for
  a large share of modern apps, so `fetch()` unwraps it and analyses `base.apk`, reporting that
  the config splits were dropped. Not a degraded case — 27 of the 43 corpus apps are base
  splits too — but native libraries are genuinely missing and the log says so.
* **Two defects fixed:** `file_count` double-counted a downloaded package (it is appended to
  `paths` while staying in `packages`), and `run.status` was set *before* the manifest write and
  the `run_finished` event, so an SSE reader waking in that window closed the stream early and
  the UI's Start button would never re-enable. Status is now set last.

> Scope note: only for apps the team is authorised to analyse. Sources are third-party mirrors
> with their own terms; treat availability as best-effort and never as a guarantee.

---

## M5 — Mapping re-grounding against `docs-ref` `wip`

**Round 1 landed 2026-08-30 — `mapping.json` v1.11.0**, 279 → 311 namespaces and
38 → 67 permissions. Expo (the corpus's largest gap, 223 unmapped namespaces),
the HMS SDK, and the three gaps the documentation corpus closed. Write-up in
`docs/MAPPING_ROUND_2026-08-30.md`. All 60 kit tokens now resolve to a doc URL.


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

**First pass done, awaiting review — `docs/MAPPING_CANDIDATES_2026-08-29.md`.** The six recorded
gaps were re-tested: three have a documented counterpart (`@kit.OnlineAuthenticationKit`,
`@kit.DeviceSecurityKit`, `@kit.CoreVisionKit`), two are confirmed as real gaps, one unchanged.
`rcp` is real but the recommendation is to change nothing — Huawei documents both kits as valid
for HTTP, and `mapping.json` is append-only. **Nothing has been written to `mapping.json`.**

The finding that shapes the rest of M5: all three kits found above have **no `.d.ts` in `kits/`**,
so a `.d.ts`-only rule would have reproduced v1's index mistake in a new form.

Still to do: re-rank the 1,771-row `Common Unmapped` pool, the kit↔module table, the `-V5` URL
audit.

---

## M5b — Test suite `done` (2026-08-30)

Not originally a milestone; it became one because the absence of tests was the
standing risk flagged before v2 started. 162 tests, ~2.5 min, plain `unittest`, no
new dependency. See `tests/README.md`.

**Five real bugs found on first runs:** the reap timeout was unreachable in the exact
case it was written for; the worker ignored the configured result directory; a
file-handle leak per run; a `SystemExit` from the engine reaching the UI as
"worker exited 1"; and the permission suggester recommending four permissions that do
not exist.

---

## M5c — Mapping audit + i18n `done` (2026-08-30)

Not planned as a milestone; added because the maintainer asked for proof that no
mapping is a hallucination, and for Turkish and Chinese.

**Nine hallucinated values found and corrected** across the mapping files —
`@kit.AnalyticsKit` (13 rows, a kit that appears NOWHERE in the 110 MB corpus),
`@kit.RelationalStoreKit` (3 rows), and five iOS permission targets carrying
Android names. Write-up in `docs/MAPPING_AUDIT_2026-08-30.md`; the audit is now
five permanent tests.

**EN / TR / 中文.** UI chrome only — kit tokens, permission names and the reports
stay as the engine produced them, and a test asserts identifiers never change
across languages.

---

## M6 — Packaging `todo`

- `requirements.txt` pinned; first-run install keeps v1's XGATE proxy-stripping behaviour
- `run.bat` unchanged in spirit: one double-click
- A short operator README: what to do when a download source dies, when Play metadata goes `N/A`

---

## Carried over from v1, unresolved

| Item | Where it is written up |
|---|---|
| ~~No automated tests anywhere~~ | **CLOSED 2026-08-30** — 162 tests, `tests/README.md`. Found 5 real bugs on their first runs. |
| Per-process batch runner never committed | v1 log §1, §16 — M2 supersedes it |
| `device_matrix` always `{}` in agent JSON | v1 Known gaps |
| 50 legacy `-V5` doc URLs unaudited | M5 |
| No `export_excel_exe_folder` | v1 Known gaps |
| Two corpus files are the wrong app (Aptoide, Uptodown) | v1 log, BUG X — maintainer's call |
