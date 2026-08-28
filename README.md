# Migration Analyzer — v2

Scans Android APKs, Windows EXE/DLLs and iOS IPAs and matches what they use against
HarmonyOS NEXT / HMS Core kits. Produces an HTML report and Excel workbooks showing what maps
directly, what needs work, and what has no equivalent yet.

**v2 adds a desktop UI, an APK downloader, a run library, and a documentation-grounded mapping
expansion.** v1's analysis engine is inherited unchanged and its CLI still works.

> Status: skeleton. The app shell lands in M1 — see `docs/ROADMAP.md`.
> Until then use the CLI below; it is fully functional.

## Layout

```
engine/     v1 analysis engine — inherited and behaviour-frozen (decisions/0003)
  data/mappings/    THE PRODUCT: 279 native + 15 OHPM mapping rows
  analyzer.py       the v1 CLI, still supported
app/        v2 shell: FastAPI + pywebview + frontend + SQLite + downloader
docs/       architecture, roadmap, mapping rules, decisions, session log
  v1/       v1's full history — engine reference, work log, mapping candidates
docs-ref/   HarmonyOS SDK .d.ts + official docs corpus (read-only, mapping-time)
```

## Running

```
run.bat                                       # v2 desktop app  (M1)
python engine/analyzer.py <file> --no-open    # v1 CLI, works today
python engine/analyzer.py --batch             # every file in engine/input/
python engine/analyzer.py engine/input/pc/<app>   # a folder of .exe/.dll
```

First run installs `androguard`, `openpyxl`, `pefile` and `macholib` via pip. On a corporate
network that install is the one step that needs real internet — disconnect from XGATE /
wlanaccess, run once, then reconnect.

## What a clone needs

Everything required to **run** an analysis is here. Two files are read during an analysis —
`engine/data/mappings/*.json` and `engine/data/reference/hmos_api_index.json`, plus
`play_metadata_cache.json` in batch mode. Nothing has to be fetched out of band.

Three further things are tracked but **not** read at runtime, and are here for mapping work:
`hmos_api.xlsx` (regenerates the API index), `ohpm_registry_cache.json` (answers OHPM
package-existence queries without a fresh 3,499-package sweep) and `docs-ref/`.

> **`docs-ref/` exists on this branch only.** It is 110 MB of HarmonyOS SDK declarations and
> crawled documentation, used to ground mappings — see `docs/DOCS_REF_GUIDE.md`. `main` is the
> product branch and deliberately does not carry it, which is also what keeps `main` free of the
> Windows long-path problem below.

Deliberately absent, and not needed to run the tool: the APK/EXE/IPA test corpus (large
binaries, not ours to redistribute) and generated output.

> **Windows: enable long paths before cloning.** The deepest path in `docs-ref/` is 212
> characters against a 260-character limit that includes wherever you cloned it. Run this once,
> or the checkout fails partway with "Filename too long" — and it fails as a *checkout* error,
> leaving a repo that looks fine until files turn up missing.
>
> ```
> git config --global core.longpaths true
> ```

## Contributing

Read `CLAUDE.md` first — it is short and points at the rest. Before touching a mapping file,
read `docs/MAPPING_DISCIPLINE.md` and `docs/DOCS_REF_GUIDE.md`; those rules are why the mappings
can be trusted.
