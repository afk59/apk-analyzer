# Handoff — start here

Last updated **2026-08-30**, end of session. Read this, then `CLAUDE.md`.

---

## Where things stand

| | |
|---|---|
| Branch | `v2` (this folder), pushed. `main` is the product branch, frozen except bug fixes. |
| App | Working. `run.bat` → window, pickers, analysis with live progress, results library, APK download by package name. |
| Languages | EN / TR / 中文, remembered. UI chrome only — analysis output is never translated. |
| Theme | system / light / dark, remembered. |
| Tests | **169**, `python -m unittest discover -s tests -t .`, ~2.5 min when nothing else is running. |
| `mapping.json` | **v1.11.1** — 311 namespaces, 67 permissions. Fully audited. |
| Corpus | 43 apps in `../apk-analyzer-side/src/input/`. Full run ≈ 55 min including HSBC. |

## THE ONE THING THAT IS UNFINISHED

**The corpus results are in a mixed state and must be re-run.**

A v1.11.1 re-run was cancelled at 26 of 43 to allow a shutdown. So:

- **26 apps** carry v1.11.1 reports
- **18 apps** still carry v1.11.0 reports — listed in `RESUME.txt` at the repo root
- **`batch_summary.xlsx` and `batch_unmapped.xlsx` are from the earlier v1.11.0 run**, because the aggregate step is skipped when a run is cancelled

The only difference between the two versions is that `@kit.AnalyticsKit` (a kit
that does not exist) became `@kit.PerformanceAnalysisKit` in 3 namespace rows —
so the mixed state is cosmetically small but it means **two apps in the same
workbook can name different kits for the same library**. That is exactly the
kind of inconsistency this project does not tolerate.

### How to finish it

```
run.bat                        # or: python -m app
```
Pick the corpus folder, **turn skip_existing OFF** (a folder run defaults to ON,
and every app already has a report so nothing would be re-analysed). Or drive it
headlessly the way the last two runs were driven:

```
python -m app --no-window                       # note the port it prints
POST /api/runs {"input": "<corpus>", "target": "hmos", "skip_existing": false}
```

Budget ~55 min. HSBC (`hk.com.hsbc.hsbchkmobilebanking.apk`, 328 MB) is last in
sort order and takes ~20 min on its own; that is normal, not a hang.

**Afterwards, confirm the absorption** — the numbers to reproduce are in
`docs/MAPPING_ROUND_2026-08-30.md` §6: 161 distinct namespaces, 251 row
instances, 0 shadowed, 0 leak-back.

> **Read `batch_unmapped.xlsx` from row 2.** Header on row 1, data from row 2.
> Reading from row 3 silently drops the first row of every sheet and produced a
> phantom one-namespace disagreement last time.

## What was done this session

1. **Dark/light/system theme**, and **EN/TR/中文**. The i18n boundary is the
   decision worth remembering: chrome yes, analysis output never — kit tokens,
   permission names and the reports are identifiers and deliverables.
2. **A test suite from nothing to 169 tests**, which found **six real bugs** on
   its first runs (see `tests/README.md` and the session log).
3. **`mapping.json` v1.10.0 → v1.11.1**: +32 namespaces (Expo was the corpus's
   largest gap at 223 unmapped namespaces and had nothing mapped), +29
   permissions, and the corrections below.
4. **A full audit of every mapping row against four reference corpora**, which
   found **nine hallucinated values** — including `@kit.AnalyticsKit`, a kit
   that appears nowhere in the 110 MB documentation corpus and was used by 13
   rows. All corrected; the audit is now five permanent tests.

## What is deliberately still open

| Item | Note |
|---|---|
| **The 18-app re-run above** | The only blocking item |
| `expo.modules.updates` unmapped | OTA JS bundle delivery; AppGallery Kit's in-app update is store-driven and a different thing |
| HMS SDK plumbing unmapped | 7,144 methods. On HarmonyOS NEXT that layer disappears; there is no kit to point at |
| 6 genuine gaps from v1 | 3 were closed this round; `net.openid.appauth` and `org.altbeacon` were re-tested and CONFIRMED as gaps; `com.google.android.odml` untouched |
| 50 legacy `-V5` doc URLs | Unaudited. `developer.huawei.com` returns an identical 200 shell for any slug, so they must be checked through the docs search index, not by fetching |
| `device_matrix` always `{}` | Removing an always-empty key changes the agent JSON schema — a product decision |
| No `export_excel_exe_folder` | Folder mode has no Python Excel export, only the in-browser button |
| Two wrong corpus files | `com.macauwynn.android.apk` is Aptoide, `hk.edu.cityu.mobile.apk` is Uptodown. Maintainer's call; untouched |
| `main` is 20+ commits behind | Deliberate. v2 merges forward when stable — and **that merge must delete `docs-ref/` again**, since v2 tracks it and `main` does not |

## Rules that keep being re-learned

Written here because each cost real time:

- **NOT FOUND means unconfirmed, not nonexistent.** Four sources exist and none
  is complete: 47 kit barrels, the api `.d.ts`, the crawled docs, the generated
  index. Search by **capability**, then read which kit owns the path.
- **`kits/` holds only the 47 OPEN SDK kits.** ScanKit, PushKit, MapKit,
  PaymentKit are real and have no `.d.ts` there.
- **A permission name needs three sources** (`data/permissions/*.txt`, the docs,
  the `.d.ts` `@permission` annotations — 748 names between them). Several real
  names are in only one of them.
- **A wrong row is worse than a gap.** Popularity never overrides function.
- **Predict absorption, then confirm it.** Every round has landed exactly.
- **Output-changing commits stay separate** from ones claiming to be neutral.

## Environment

- `PYTHONIOENCODING` is no longer required — the CLI forces UTF-8 itself.
- The corpus needs AC power. Sleep-on-battery killed a v1 run; the DC timeouts
  are currently 0, but check `PowerLineStatus` before starting anything long.
- Scratch scripts from this session (`audit_mappings.py`, `predict.py`,
  `confirm.py`, `run_batch.py`, `compare_v1_v2.py`) live in the session
  scratchpad and **do not survive**. The procedures they implement are described
  in `docs/MAPPING_ROUND_2026-08-30.md` and `docs/MAPPING_AUDIT_2026-08-30.md`;
  rebuild from those if needed.
