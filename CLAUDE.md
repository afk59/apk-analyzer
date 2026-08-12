## Sprints 1–10: COMPLETED (verified against code, 2026-08-07)

> **Doc hygiene:** `CLAUDE.md` was untracked until 2026-08-07 — `.gitignore` line 3 read
> `claude.md`, which matched `CLAUDE.md` on Windows' case-insensitive FS. That line has
> been removed and the doc is now tracked. Keep it updated in the same commit as code changes.

---

### Sprint 1–2 — APK Engine + HTML Report

**Core engine:** `src/core/apk_engine.py`
- `androguard.misc.AnalyzeAPK` for DEX bytecode analysis
- Scans all method cross-references, builds `detected_namespaces` dict keyed by 4-segment prefix
- Obfuscation filter: `_is_obfuscated(class_name, method_name)` — two regexes:
  - `_OBFUS_SIMPLE = ^[A-Za-z]{1,2}[0-9]{0,2}$` — 1–2 letter names with optional trailing digits
  - `_OBFUS_SHORT  = ^[A-Z]\.[A-Za-z0-9]{2,5}$` — single-letter package prefixes
  - Obfuscated refs are counted in `obfuscated_count` and skipped entirely
- Unresolvable filter: `_is_unresolvable(ns)` — skips namespaces containing `__`, `._`, `$`, or starting with `kotlinx.`; these go to `result["unresolvable_namespaces"]` (NOT unmapped)
- `androidx.*` auto-mapping: all `ns.startswith("androidx.")` → hard-coded to `@kit.ArkUI`, note "AndroidX compatibility library → ArkUI component system" — runs AFTER the `namespace_mappings` loop as a fallback (see Bugfix Round `2daca8a`), aggregates all androidx classes/methods
- Namespace matching: longest-prefix-first against `namespace_mappings`
- Result dict fields: `mode`, `apk_path`, `target`, `package_name`, `app_name`, `version_name`, `version_code`, `min_sdk`, `target_sdk`, `permissions`, `activities`, `services`, `receivers`, `providers`, `native_libs`, `manifest_xml`, `detected_namespaces`, `kit_matches`, `permission_matches`, `unmapped_namespaces`, `unresolvable_namespaces`, `private_libs`, `api_matches`, `permission_gaps`, `missed_match_count`, `obfuscated_count`, `analysis_time_sec`, `total_detected_ns`, `total_3p_ns`

**Mapping:** `src/data/mappings/mapping.json` v1.3.0 (`last_updated: 2026-07`)
- **168** `namespace_mappings` entries (Android namespace → HarmonyOS NEXT kit); fields: `android_namespace`, `android_display`, `harmony_kit`, `harmony_import`, `confidence`, `note`
- 38 `permission_mappings` entries: fields `android`, `harmony`, `kit`, **`grant_level`**
  (`system_grant` | `user_grant` | `restricted` | `unknown`; current spread: 13 user / 12 unknown / 10 system / 3 restricted)
- Field `harmony_kit` used for HMOS target, `hms_kit` for HMS target
- No `category` field on APK namespace entries (all 168 are `null`) — APK status is confidence-derived only

**HTML report:** `src/core/renderer.py` — `render_html_apk(result, mapping=None)`
- Shared base template `_HTML_BASE` with `%%PLACEHOLDER%%` substitution
- Stat cards: see Sprint 8 (restructured — 4 cards)
- Sections: Kit Matches, Permission Mapping, Unmatched Permissions, Permission Gaps, Native Libraries, Unrecognized Third-Party Libraries, Private Libs, AndroidManifest.xml, Manifest Components
- Built-in JS `exportExcel()` → loads XLSX.js from CDN → builds Excel in-browser (mode-aware: apk/exe/exe_folder/ipa branches)

---

### Sprint 3 — HMS Core Target + Obfuscation + Permission Gaps

**HMS Core target:**
- `src/data/mappings/hms_mapping.json` v1.2.0: **135** `namespace_mappings`, 27 `permission_mappings`
- Namespace entry fields: `android_namespace`, `android_display`, `hms_kit`, `confidence`, `note` (no `harmony_import`)
- Permission entry fields: `android`, `hms_note` only — no `harmony`/`kit`/`grant_level`
- `--target hms` flag selects `hms_kit` field from mapping; `--target hmos` selects `harmony_kit`
- `perm_lookup` built from mapping's `permission_mappings`; for HMS, renderer shows `hms_note` field instead of `harmony`/`kit`

**Permission gap engine:**
- `_suggest_hmos_perm(android_perm)` — keyword intersection against 46-entry `_OHOS_PERM_CATALOGUE`
- Noise words filtered: `ACCESS, GET, USE, SET, MANAGE, REQUEST, CHANGE, RECEIVE, READ, WRITE, SEND`
- Returns `(suggested_ohos_perm, confidence)` where confidence is `"high"` (exact match or ≥2 keywords), `"medium"` (single meaningful word ≥4 chars), `"low"` (short single word)
- Results stored in `result["permission_gaps"]`

**TUI:** `src/ui/terminal.py` — `interactive_session()`
- Arrow-key TUI (`tty`/`termios` on Linux, `msvcrt` on Windows, numbered fallback)
- **5-item menu** — see Sprint 9 for the current list

---

### Sprint 4 — Excel Export + "Couldn't Resolve" Sheet

**Excel export:** `export_excel_apk(result, output_path)` — see Sprint 8 for the current 6-sheet structure.

All sheets: frozen header row, auto-filter, no gridlines, alternating row shading.

---

### Sprint 5 — Windows EXE/DLL Analysis

**Engine:** `src/core/exe_engine.py`
- Library: `pefile` (pip-installed on first run)
- Extracts: architecture (`_MACHINE` dict), subsystem (`_SUBSYSTEM` dict), is_dll, is_dotnet (checks CLR header via DATA_DIRECTORY[14]), entry_point, image_base, timestamp, image_size, version_info (StringFileInfo), sections (name/vsize/raw_size/entropy/exec flag)
- Import table: regular + delay imports (per-DLL function lists)
- Export table: all named symbols
- Entropy: `_section_entropy()` — per-section Shannon entropy, averaged
- Packer detection: `_detect_packer()` — named sections (UPX, ASPack, MPRESS, Themida, Enigma, NsPack, VMProtect, PELock, Petite) + high-entropy fallback (≥7.0); sets `is_packed`, `packer_hint`, `avg_entropy`
- String-scan fallback: when import table empty → `_string_scan_imports()` — section-aware (skips high-entropy sections), extracts ASCII + wide-char strings, matches against 14 API pattern groups + known DLL set; sets `string_scan_mode=True`
- Kit matching via `win_mapping.json` (**92** `dll_mappings`); stem-prefix fallback for versioned DLL names (e.g. `vcruntime140_1.dll` matches `vcruntime140.dll`)
- **Skip filter for `api-ms-win-*`, `ext-ms-win-*`, `_codegen*` now lives INSIDE the unmatched (`else`) branch of `_match_kits` (`exe_engine.py:265`)** — it only applies to DLLs that found no mapping entry. The 11 explicit `api-ms-win-crt-*` entries added in Sprint 9 therefore match first and are never skipped; all other `api-ms-win-*` / `ext-ms-win-*` are still dropped from `unmapped_dlls`.
- Status/color: `_match_kits` prefers a mapping entry's `category` field if present, else derives from `confidence` (high→"Supported"/green, medium→"Replaceable"/amber, low→"Should Confirm"/blue)

**Result dict fields:** `mode`, `exe_path`, `target`, `file_name`, `machine`, `subsystem`, `is_dll`, `is_dotnet`, `entry_point`, `image_base`, `timestamp`, `image_size`, `version_info`, `sections`, `imports`, `delay_imports`, `exports`, `kit_matches`, `unmapped_dlls`, `qt6_dlls`, `is_packed`, `packer_hint`, `avg_entropy`, `string_scan_mode`, `analysis_time_sec`

**Mapping:** `src/data/mappings/win_mapping.json` v1.1.0 (`last_updated: 2026-07-13`) — **92** `dll_mappings`
- Fields: `dll_name`, `dll_display`, `harmony_kit`, `harmony_import`, `confidence`, `note`, `sample_url`, optional **`category`**
- `category` is currently set on exactly 3 entries (`Qt6Core/Gui/Widgets.dll` → `"Should Confirm"`), overriding their `medium` confidence

**HTML:** `render_html_exe(result)` — sections: packed/string-scan warning banner, PE Metadata grid, PE Sections table, Kit Matches (with Qt6 banner), Import Table, Exports, Unmapped DLLs.
Stat cards (5): Kit Matches · Imported DLLs · Imported Functions · Exported Symbols · **"Mapped DLLs" `{mapped}/{total}`** with a `{pct}% coverage` sublabel colored at 70 / 40 thresholds.
`mapped = Σ len(km["dll_sources"])`, `total = mapped + len(unmapped_dlls)`. "Unmapped DLLs" survives only as a body section and sidebar link, not a stat card.

**Excel:** `export_excel_exe(result, output_path)` — 4 sheets: Overview, Kit Matches, Imports (DLL/Function/Type with delay flag), Unmapped (DLL Name, Function Count, Sample Functions, Delay).

---

### Sprint 6 — IPA (iOS) Analysis + Encryption Detection

**Engine:** `src/core/ipa_engine.py`
- Libraries: `zipfile` + `plistlib` (stdlib); `macholib` for encryption detection
- Extracts from IPA (ZIP archive):
  - `Payload/<App>.app/Info.plist` → `bundle_id`, `app_name`, `version`, `min_ios_version`, `executable_name`
  - All `*UsageDescription` keys → `permissions` list
  - `CFBundleURLTypes[].CFBundleURLSchemes` → `url_schemes`
  - `Payload/<App>.app/Frameworks/*.framework` → strip `.framework` → `frameworks` list
  - `Payload/<App>.app/PlugIns/*.appex` → strip `.appex` → `extensions` list
- Encryption detection: `_is_binary_encrypted()` — macholib checks LC_ENCRYPTION_INFO (0x21) / LC_ENCRYPTION_INFO_64 (0x2C); `cryptid != 0` → encrypted
- `static_linking_likely` flag: set when `len(frameworks) < 3 AND is_encrypted`; triggers yellow info banner in HTML
- Permission matching: `_load_permission_map()` loads `src/data/mappings/ios_permission_mapping.json` internally (`ipa_engine.py:107`, NOT passed via `mapping` param); `mapping` param carries only `ios_mapping.json` framework data
- Framework matching: case-insensitive lookup in `mapping["framework_mappings"]` by `framework_name`

**Result dict fields:** `mode`, `target`, `file_name`, `bundle_id`, `app_name`, `version`, `min_ios_version`, `permissions`, `frameworks`, `extensions`, `url_schemes`, `kit_matches`, `unmapped_frameworks`, `permission_matches`, `is_encrypted`, `is_encrypted_warning`, `static_linking_likely`, `analysis_time_sec`

**NOTE — drift from Sprint 6 spec:** The spec described an `is_encrypted` HTML warning banner. What was actually implemented is a `static_linking_likely` banner (shown when few frameworks + encrypted). There is no standalone encryption-only banner.

**Mapping files:**
- `src/data/mappings/ios_mapping.json` v1.0.0 — 54 `framework_mappings`; fields: `framework_name`, `framework_display`, `harmony_kit`, `harmony_import`, `confidence`, `note`
- `src/data/mappings/ios_permission_mapping.json` v1.0.0 — 22 `permission_mappings`; fields: `ios_key`, `ios_display`, `harmony`, `kit`

**HTML:** `render_html_ipa(result)` — sections: static-linking banner (conditional), App Metadata grid, Kit Matches, Permission Mapping, Unmatched Permissions, URL Schemes, App Extensions, Unmapped Frameworks. Stat cards: Kit Matches, Frameworks, Unmapped, Permissions (N/total), Extensions.

**Excel:** `export_excel_ipa(result, output_path)` — 3 sheets: Overview, Kit Matches, Permissions.

**Dependency bootstrap (`_ensure_deps` in analyzer.py):** `androguard`, `openpyxl`, `pefile`, `macholib` — all four checked and auto-installed on first run. The installer strips `HTTP_PROXY`/`HTTPS_PROXY`/`http_proxy`/`https_proxy` from the subprocess env and forces `NO_PROXY=*` (`analyzer.py:29-33`) — this is the XGATE workaround described in README.

**Log suppression (`_silence_androguard_logs` in analyzer.py):** called immediately after
`_ensure_deps()` and **before** the `core.apk_engine` import. androguard logs every DEX
`map_item` it parses at DEBUG through loguru; left on, one APK writes ~31 MB and a 42-app batch
exceeds 10 GB (a batch run was killed at 3/42 having already produced 1 GB). The function drops
loguru's default sink via `logger.remove()`, wrapped in `try/except ImportError` so a missing
loguru is a silent no-op.

Ordering is load-bearing:
- **after `_ensure_deps()`** — loguru arrives as an androguard dependency, so on a cold first
  run it does not exist until the pip install has completed;
- **before any `AnalyzeAPK`** — `apk_engine.py:147` imports androguard lazily *inside*
  `analyze_apk`, so placing the call at module scope in `analyzer.py` reliably precedes it.

Two caveats worth knowing before changing this:
- `logger.remove()` removes **all** loguru sinks, not just androguard's. That is fine today
  because androguard is the only loguru consumer in the dependency tree — revisit if project
  code ever adopts loguru for its own logging.
- androguard re-adds a sink at import time in `decompiler/decompile.py` (module level), but it
  is scoped `filter="dad", level="INFO"` and does not reintroduce the `androguard.core.dex`
  DEBUG flood. The other `logger.add()` call site (`util.py:39`) lives inside a function and
  only fires if called.

Measured effect: single APK **31,332,761 → 1,747 bytes**; 2-APK batch **4,067 bytes** (was
~62 MB). Reports, Excel, and agent JSON are byte-for-byte unaffected — only log noise is gone.

---

### Sprint 7 — API Matching, Batch Mode, Agent JSON Output

**HarmonyOS API matching:**
- `src/data/reference/hmos_api.xlsx` — "API Device Matrix" sheet; columns: API/Method, Kit, Import Statement, URL
- `src/core/api_index.py` — one-shot builder script; run manually after updating xlsx; normalizes method names (lowercase, strips trailing version numbers), writes `src/data/reference/hmos_api_index.json`
- `src/data/reference/hmos_api_index.json` — 16,167 entries indexed by normalized simple method name
- `src/core/api_matcher.py` — `match_methods(android_methods: list) -> list`; loads index lazily on first call; deduplicates by normalized simple name; returns hits with `android_method`, `import_statement`, `doc_url`, `kit`, `match_type="exact"`, `score=1.0`
- Called from `apk_engine.py` after kit matching; results stored in `result["api_matches"]`
- **Kit confidence boosting:** if an API match's `kit` field matches a matched kit, that kit's confidence is bumped one level up (`low→medium`, `medium→high`); applied in-place on `result["kit_matches"]`

**Batch mode:**
- `run_batch(input_dir, result_dir, script_dir, target)` in `analyzer.py`
- Scans `input/` for `*.apk`, `*.exe`, **`*.dll`**, `*.ipa` (`.dll` added in Sprint 9); processes all in sequence. Does NOT recurse into `input/pc/`.
- Per-file: runs full analysis, writes HTML report to `result/`, writes agent JSON to `result/agent_outputs/`
- Outputs two workbooks — see Sprint 9 ("Batch output split")
- Aggregate agent JSON: `result/agent_outputs/agent_summary.json` (schema_version, generated_at, file_count, files array)
- Accessible via `--batch` / `-b` CLI flag OR TUI "Batch" option (4th item)

**Agent JSON output:**
- `build_agent_json(result) -> dict` — mode-aware; fields: `schema_version`, `generated_at`, `mode`, `target`, `app_metadata`, `kit_list`, `confidence_scores`
- APK-specific fields: `api_matches`, `permission_gaps`; `device_matrix` is emitted for every mode (see Known gaps)
- `write_agent_json(result, output_path)` — always called after every analysis (single, batch, and exe_folder)
- `kit_list` entries include `source_namespaces` (apk), `source_frameworks` (ipa), or `source_dlls` (exe / exe_folder)
- `app_metadata` has four branches: apk, ipa, **exe_folder** (`folder_name`, `file_count`, `files`, `dll_count`), and exe

**CLI flags (analyzer.py):**
`input`, `--mode/-M` (apk/exe/ipa), `--target/-t` (hmos/hms), `--output/-o`, `--json/-j`, `--excel/-e`, `--mapping/-m`, `--no-open`, `--batch/-b`

---

### Sprint 8 — Report Restructure

**Concept:** Four-tier namespace classification for APK analysis. Every detected namespace is classified into exactly one bucket: MATCHED (has a kit mapping), UNMAPPED (real 3rd-party, no current mapping), PRIVATE/CUSTOM (derived from the app's own bundle root — first 2 segments of package_name), or FILTERED (obfuscated via `_is_obfuscated` or unresolvable via `_is_unresolvable`). PRIVATE and FILTERED namespaces NEVER affect any ratio, count, or matching percentage; they are informational only.

**Engine changes (`src/core/apk_engine.py`):**
- `_is_private_lib(ns, package_name, ns_mappings) -> bool` — extracts bundle_root (first 2 package segments), returns True if ns starts with bundle_root AND does not match any ns_mappings entry; checked AFTER unresolvable filter, BEFORE namespace_mappings loop
- `result["private_libs"]` — list of dicts matching unmapped_namespaces structure
- `status` / `status_color` added to each kit_matches entry after confidence boosting
- `inner_methods` added to each android_source when corroborating api_matches exist for that namespace prefix

**HTML report (`src/core/renderer.py` — `render_html_apk`):** 4 stat cards
1. **"Number of Libraries Mapped"** — value is `len(flat_ns_rows)`, i.e. the count of matched **namespace rows**, not `len(kit_matches)`. Clickable to `#kit-matches-section`. HMOS-only sublabel `{pct}% coverage` where `pct = total_detected_ns / total_3p_ns`, colored at 70 / 40 thresholds. HMS reports omit the sublabel entirely (coverage % is an HMOS-only concept).
2. **"Private Libs"** — single number, onclick reveals/scrolls to collapsible `#private-libs-section`; sublabel "Custom app-internal classes — excluded from matching"
3. **"Permission Coverage"** — `{matched}/{total}`, sublabel shows real `grant_level` tier counts (`System: N · User: N · Restricted: N`)
4. **"Native .so Libs"** — count

- Kit Matches section: 3-level collapsible TABLE (all rows start collapsed); Level 1 = group root (`_group_root`), Level 2 = namespace rows, Level 3 = inner method matches
- `_render_kit_table_apk(flat_rows, ns_lookup, is_hmos)` for APK mode; IPA still uses `_render_kit_cards`; EXE/EXE-folder use `_render_kit_table_exe`
- `_HTML_BASE` additions: CSS for `.kit-table`, `.badge.status-{green,amber,blue}`, chevrons; JS for `revealSection(id)`, `toggleKitRow`, `toggleNsRow`, `toggleGroupRow`, `toggleDllRow`, `toggleSidebar`

**Excel export (`export_excel_apk`):** 6 sheets — Overview · Kit Matches (with Status column) · Permissions · Unmapped Libraries · Filtered Libraries · Custom Private Libs

**JS in-browser Excel** mirrors the same 6-sheet structure; `report_data` includes `private_libs`, `unresolvable_namespaces`, `obfuscated_count`.

---

## Sprint 9 — 2026-07-14 (commits `805fe80`, `53fd823`, `fd2efae`, `1259b7f`)

> Note: `805fe80` is self-titled "Sprint 8" and landed 2026-07-12; the other three landed
> 2026-07-14. Its contents were never documented, so it is folded in here.

### Data-file reorganization (`53fd823`)

All data files moved out of flat `src/` into `src/data/`:

```
src/data/mappings/     mapping.json  hms_mapping.json  win_mapping.json
                       ios_mapping.json  ios_permission_mapping.json
src/data/reference/    hmos_api.xlsx  hmos_api_index.json  package_names.txt
src/data/permissions/  open_system_grant_permissions.txt
                       open_user_grant_permissions.txt
                       restricted_permissions.txt
```

Path resolution: `analyzer.py:69,319,327-333` → `script_dir/"data"/"mappings"`;
`api_matcher.py:7` and `api_index.py:5-6` → `data/reference/`;
`ipa_engine.py:107` → `data/mappings/ios_permission_mapping.json`.

### EXE Folder mode (`53fd823`)

Analyzes a whole `input/pc/<app>/` directory as one logical application.

**Engine — `analyze_exe_folder(folder_path, mapping)` (`exe_engine.py:390-458`):**
- Globs `*.exe` + `*.dll` in the folder, calls `analyze_exe()` per file
- Per-file failures are caught (`SystemExit` from an invalid PE, or any `Exception`) and recorded as `{"file_name", "error"}` in `files_meta` — one bad file does not abort the run
- **Merge/dedup:** `merged_imports: defaultdict(set)` — function names are `set.update()`d per DLL across all files, so cross-file duplicates collapse. Delay imports fold into the *same* `merged_imports` dict; the DLL name is additionally tracked in `merged_delay`.
- **`source_map`:** `defaultdict(set)` mapping `dll_name → {files that import it}`. Passed into `_match_kits(..., source_map)`, which attaches a sorted `source_files` list to every matched `dll_sources` entry and every `unmapped_dlls` entry. Surfaces as "Found in: a.exe, b.dll" rows in HTML.
- Result keys: `mode:"exe_folder"`, `folder_path`, `folder_name`, `file_count`, `files`, `imports`, `delay_dlls`, `import_sources`, `kit_matches`, `unmapped_dlls`, `qt6_dlls`, `analysis_time_sec`

**Self-import exclusion (`renderer.py:1550-1557`):** the folder-mode "Mapped DLLs" stat builds `self_names` from the analyzed files and excludes those from BOTH numerator and denominator — so `app-core.dll` importing from `app.exe` doesn't inflate coverage. Single-file `render_html_exe` has no such adjustment.

**Driver:** `run_exe_folder()` (`analyzer.py:227-252`), dispatched at `analyzer.py:318-321`.
**Renderer:** `render_html_exe_folder()` (`renderer.py:1468-1638`) — Analyzed Files table (arch/subsystem/type/packer per file, red row on parse failure), Kit Matches + Qt6 banner, Merged Import Table, Unmapped DLLs. Stat cards: Kit Matches · Files Analyzed · Imported DLLs · Imported Functions · Mapped DLLs X/Y.
**TUI:** menu item 5, then a second picker listing subfolders of `input/pc/`.

**Reachable via TUI ONLY** — `--mode` is `choices=["apk","exe","ipa"]`, so there is no CLI flag for `exe_folder`. There is also **no `export_excel_exe_folder`**; only the in-browser JS export button covers this mode.

### `api-ms-win-crt-*` → NDK libc, plus render-time grouping (`53fd823`)

- `win_mapping.json` gained **11 explicit `api-ms-win-crt-*.dll` entries**, all → `HarmonyOS NDK (libc)`, `confidence: high`:
  `convert`, `environment`, `filesystem`, `heap`, `locale`, `math`, `runtime`, `stdio`, `string`, `time`, `utility` (each `-l1-1-0.dll`).
- The `api-ms-win` / `ext-ms-win` / `_codegen` skip filter moved inside the `else` branch of `_match_kits`, so these 11 match before the filter can drop them.
- **Grouping is render-time and generic — there is no `group` field in the mapping file** (all 92 entries have `group: null`). `_group_dll_families(dll_names, min_group_size=3)` (`renderer.py:799-819`) splits DLL stems on `-` and collapses any prefix of ≥2 tokens shared by ≥3 DLLs into a parent row labeled `<prefix>-*` (e.g. `api-ms-win-crt-*`). `_render_kit_table_exe` emits a clickable `group-row` with a member count; children are hidden behind `toggleGroupRow()`.

### Qt5 / Qt6 mapping split + warning banner (`53fd823`)

- `Qt5Core/Gui/Widgets.dll` → `Qt for HarmonyOS (official port)`, `confidence: high`
- `Qt6Core/Gui/Widgets.dll` → `Qt for HarmonyOS (pending Qt 6.12 release)`, `confidence: medium`, **`category: "Should Confirm"`** (the `category` field overrides confidence-derived status in `_match_kits`)
- `Qt5Network.dll` / `Qt6Network.dll` → `@kit.NetworkKit`, medium
- Detection: `_QT_VERSION_RE = ^qt(\d)`; `_detect_qt6_dlls()` (`exe_engine.py:213-220`) returns sorted DLLs whose stem starts `qt6`, stored as `result["qt6_dlls"]` by both `analyze_exe` and `analyze_exe_folder`
- Banner: `_qt6_banner()` (`renderer.py:32-45`) — amber, *"Qt6 — HarmonyOS support not yet available"*, lists detected DLLs, states Qt 6.x has no official HarmonyOS port and Qt 6.12 formal release is expected ~Q4 2026. Injected **inside the Kit Matches section, above the table**, in `render_html_exe` (`:1312`) and `render_html_exe_folder` (`:1501`). Renders only when `qt6_dlls` is non-empty.

### Batch output split (`805fe80`)

Batch mode now writes **two** workbooks instead of one:

**`result/batch_summary.xlsx`** — `export_excel_batch(rows, path, unmapped_dlls, unmapped_frameworks)` (`renderer.py:2354`):
1. "Batch Summary" — File (hyperlinked to the HTML report), App Name, Kit Count, Permissions
2. "Unmapped DLLs" *(conditional)* — DLL Name, App Count, Total Func Count, Apps, Sample Functions — cross-app aggregated, sorted by app count then func count
3. "Unmapped Frameworks" *(conditional)* — Framework, App Count, Apps

**`result/batch_unmapped.xlsx`** — `export_excel_batch_unmapped(per_file_unmapped, path)` (`renderer.py:2450`):
- **One sheet per APK**, named after the file stem (sanitized of `[]:*?/\`, truncated to 31 chars, de-duplicated with `_1`/`_2` suffixes)
- Columns: Namespace, Class Count, Method Count, Sample Methods
- Falls back to a single "No Unmapped" sheet when nothing was found

### HMS target fixes (`805fe80`)

- HMS reports no longer render a coverage-percentage sublabel — it is an HMOS-only concept (`renderer.py:1094-1097`, gated on `is_hmos`)
- HMS target skips `android.` / `androidx.` from `unmapped_namespaces` (natively supported in Android-based HMS development): `skip_prefixes` is extended when `target == "hms"` (`apk_engine.py:255-256`)
- `skip_prefixes` was **hoisted above** the matching loop (`apk_engine.py:249`), fixing a latent `NameError` when the loop's first namespace hit the null-kit branch before the list was assigned

### Flutter / cross-platform mappings (`805fe80`)

Added to both mapping files — `io.flutter`, `io.flutter.plugins`, and per-plugin entries for
`googlemaps`, `googlesignin`, `sharedpreferences`, `pathprovider`, `urllauncher`, `camera`,
`videoplayer`, `imagepicker`, plus `com.dexterous.flutterlocalnotifications` and
`com.google.maps.flutter`.

- `mapping.json` (v1.3.0): **14** Flutter-related entries — e.g. `io.flutter.plugins.googlemaps` → `@kit.MapKit` (high), `io.flutter.plugins.camera` → `@kit.CameraKit` (high), bare `io.flutter` / `io.flutter.plugins` → `@kit.ArkUI` (medium)
- `hms_mapping.json` (v1.2.0): **11** entries — e.g. `io.flutter.plugins.googlemaps` → `Map Kit` (high), `com.dexterous.flutterlocalnotifications` → `Push Kit` (medium), bare `io.flutter` → `Network Kit` (low)

### Test-fixture ignores + README (`fd2efae`, `1259b7f`)

- `.gitignore` gained `*.dll`, `*.exe`, `*.ipa` (joining the existing `*.apk`, `*.xlsx`, `*.html`)
- `README.md` rewritten for developer onboarding: `run.bat` entry point, the XGATE/wlanaccess disconnect step for first-run pip install, the `input/pc/<app>/` convention for EXE Folder mode, and the 5-mode menu. It is currently the most accurate prose description of EXE Folder mode.

### TUI menu — 5 options (`terminal.py:160-193`)

1. APK (Android → HarmonyOS NEXT / HMS)
2. EXE (Windows → HarmonyOS NEXT)
3. IPA (iOS → HarmonyOS NEXT) [limited: App Store binaries are encrypted]
4. Batch (all APK + EXE + IPA files in input/)
5. **EXE Folder (analyze all .exe/.dll in an input/pc/<folder>/)**

`interactive_session` returns a 3-tuple; for option 5 it is `(folder_path, "exe_folder", "hmos")`.
Also added: `print_summary_exe_folder()`.

> **Load-bearing `min`/`max` order in `tui_select`:** the viewport is
> `view = min(len(options), max(3, _rows - 4))` — floor the *terminal height* at 3 for tiny
> windows FIRST, then cap by the option count. Written the other way round
> (`max(3, min(len(options), _rows - 4))`) it yields `view = 3` for any menu with fewer than
> 3 options, and `_render` walks past the end of `options` with an `IndexError`. That crashed
> the 2-item migration-target picker on every APK run. Do not "simplify" the nesting.

> Naming wart: `interactive_session(script_dir)` is called as `interactive_session(input_dir)`
> (`analyzer.py:299`), so the parameter name is misleading — `pc_dir = script_dir/"pc"`
> actually resolves to `input/pc/`.

---

## Sprint 10 — Report Chrome + Batch Aggregate Sheets

### Shared report chrome (sidebar / header / toggle)

Frontend-only. Every change lives in `_HTML_BASE` (`renderer.py`), so it applies uniformly to
the **apk**, **exe**, and **exe_folder** reports. **IPA is structurally unaffected** —
`render_html_ipa` sets `SIDEBAR_HTML`, `SIDEBAR_TOGGLE_HTML`, `CONTAINER_EXTRA_CLASS` and
`HEADER_EXTRA_CLASS` all to `""`, so it has no sidebar, no toggle button, and no
`.with-toggle` class for the new rules to bind to.

### Sidebar now starts CLOSED

- `<body>` → `<body class="sidebar-closed">`. The initial state is set in markup, not by JS on
  load, so there is no flash-of-open-sidebar before script execution.
- `toggleSidebar()` rewritten to keep `sidebar-closed` (desktop) and `sidebar-open` (≤768px
  overlay) **mutually exclusive** — it now removes the counterpart class before toggling.
  Previously a viewport resize across the 768/769px boundary could leave both classes on
  `<body>` simultaneously, leaving the toggle a no-op until resized back.

### Header shift fix

Previously `.header.with-toggle` had only `padding-left:74px` and never moved; the header sat
at `margin-left:0` at full width while `.sidebar` (`position:fixed`, `z-index:100`) painted
straight over it. The sidebar overlapped the red top bar instead of pushing it.

```css
.header.with-toggle { padding-left:74px; margin-left:200px; transition:margin-left .2s ease; }
body.sidebar-closed .header.with-toggle { margin-left:0; }
@media(max-width:768px){ .header.with-toggle { margin-left:0; } }
```

Offset (`200px`) and transition (`margin-left .2s ease`) deliberately mirror
`.container.with-sidebar` exactly, so header and body move in tandem.

**Specificity note (do not "simplify" these selectors):** `body.sidebar-closed
.header.with-toggle` is `(0,3,0)` and beats the `(0,2,0)` base rule when closed. Inside the
≤768px block the override is also `(0,2,0)` but sits *later in source order*, so it wins
whenever the sidebar is in overlay mode (`sidebar-open`, no `sidebar-closed` on body). Both
paths resolve to `margin-left:0` below 768px — the header stays full-width and fully usable
while the sidebar overlays it, never clipped or pushed off-screen.

### Toggle button neon glow

- `@keyframes toggle-glow` — 3.2s `ease-in-out infinite` box-shadow pulse in accent red
  `rgba(200,0,42,…)` (= `--accent` `#c8002a`), cycling opacity `.16 → .36`. Deliberately slow
  and low-opacity: locatable in peripheral vision, not attention-grabbing.
- `:hover` pauses the animation (`animation-play-state:paused`) and settles on a brighter
  static glow.
- Added `:focus-visible` outline for keyboard users.
- **`@media (prefers-reduced-motion: reduce)`** sets `animation:none` and substitutes a
  constant low-opacity shadow — the button stays findable with zero motion.

> **Drive-by fix:** `.sidebar-toggle` had `background:rgba(0, 0, 0)` — invalid, `rgba()` needs
> four arguments, so browsers dropped the declaration and the button rendered with no
> background at all. Corrected to `rgba(0,0,0,.85)`. Without this the glow would have been
> haloing an invisible button.

### Batch aggregate sheets — "Common Mapped" / "Common Unmapped"

`batch_summary.xlsx` gained two cross-app frequency sheets, inserted **after "Batch Summary"
and before** the conditional "Unmapped DLLs" / "Unmapped Frameworks" sheets. **APK results
only** — EXE and IPA contribute nothing to them.

| Sheet | Columns |
|---|---|
| **Common Mapped** | Android Namespace · Mapped Kit · App Count · Apps |
| **Common Unmapped** | Android Namespace · App Count · Apps |

**Threshold:** `_COMMON_MIN_APPS = 2` at the top of `renderer.py` — a namespace must appear in
at least this many distinct APKs to be listed. Set to `1` to list everything. Filtering and
sorting both happen in `export_excel_batch`, so the constant is the single source of truth.
Sort is app-count descending, then namespace ascending for stable ordering.

**Collection (`run_batch`, `analyzer.py`):** three accumulators —
`mapped_ns_apps: {namespace: set(app names)}`, `mapped_ns_kit: {namespace: kit_name}` (first
seen), and `unmapped_ns_apps: {namespace: set(app names)}` — populated inside the APK branch
and passed to `export_excel_batch` as keyword args. Values are **sets**, so App Count is the
number of distinct APKs, never total occurrences.

**Aggregation key is the namespace, matching how the engine buckets** — class-level counts are
not tracked anywhere. Two consequences worth knowing:

- Mapped rows key on `kit_matches[].android_sources[].android_namespace`, which is the
  **mapping pattern** (`best_match["android_namespace"]`), not the raw detected namespace.
  Several detected namespaces collapse onto one canonical row — that pattern *is* the mapped
  library's identity, which is what makes it the right key.
- The AndroidX fallback branch emits a literal `"androidx."` pseudo-pattern, so expect a single
  high-count `androidx.` row rather than per-artifact rows.

Pattern→kit is 1:1 within a run (one mapping file, one target), so the single "Mapped Kit"
column is unambiguous. It is labelled "Mapped Kit" rather than "HarmonyOS Kit" because
`export_excel_batch` receives no `target` and the values are HMS kit names under `--target hms`.

**Edge cases:** both sheets are omitted entirely when the batch contains no APKs. When APKs
were processed but nothing clears the threshold (e.g. a single-APK batch), the sheets are still
created with an italic note naming the threshold — a silently missing sheet reads as a bug.

**Also wired:** `rows["unmapped_count"]` was collected by `run_batch` but never written. The
"Batch Summary" sheet now has an **Unmapped** column between Kit Count and Permissions
(header row, merge range `A1:E1`, widths, and auto-filter range all widened by one column).

### Mapping expansion from the 42-app batch

Driven by the Common Unmapped output above. Candidates were ranked by how many of the 42 APKs
each namespace appeared in, then grounded against `hmos_api_index.json` before being proposed —
distinctive method names were looked up in the index to confirm which kit actually owns the API
(e.g. `getAttributeCount` → `xml` from `@kit.ArkTS`, `getCalendar`/`getTimeZone` → `i18n` from
`@kit.LocalizationKit`, `createAccount`/`getAllAccounts` → `appAccount` from
`@kit.BasicServicesKit`). Nothing was mapped on vibes.

| File | Version | `namespace_mappings` | Added |
|---|---|---|---|
| `mapping.json` | 1.3.0 → **1.4.0** | 168 → **188** | **+20** |
| `hms_mapping.json` | 1.2.0 → **1.3.0** | 135 → **136** | **+1** |

`last_updated` bumped to `2026-08` on both. Append-only — no existing entry was modified.
`permission_mappings` untouched (38 / 27).

**Why HMS got one row and HMOS got twenty.** Under `--target hms` the engine adds `android.`
and `androidx.` to `skip_prefixes` (`apk_engine.py:255-256`), so no `android.*` namespace can
ever reach the HMS unmapped list. More fundamentally, HMS apps are still Android apps — Android
platform APIs and platform-neutral Java libraries (okio, bolts, xmlpull, conscrypt, Fresco,
React Native) run unchanged and need no migration. Mapping them to an HMS kit would falsely
imply migration work. Only `com.android.installreferrer` (a Google Play service with a real
Huawei counterpart) qualified.

**Deliberately left unmapped** — a wrong mapping is worse than an honest gap:
`org.conscrypt` (35/42, JSSE provider internals — TLS is platform-managed),
`android.security.NetworkSecurityPolicy` (28/42, expressed as app config on HarmonyOS, not an
API), `com.facebook.common` (26/42, heterogeneous utility grab-bag), `android.system` (19/42,
POSIX errno wrappers), `android.service.media` (17/42, AVSession is the likely target but the
exact kit token could not be confirmed against the index), Fresco cache/datasource/
binaryresource plumbing, `com.facebook.jni` / `soloader` / `hermes` (build and runtime
infrastructure), and `com.facebook.infer` / `com.google.errorprone` (compile-time annotations,
zero runtime). Three further candidates were proposed and cut during review:
`com.google.firebase` (root catch-all over SDK plumbing), `okio`, and `bolts`.

**Pending follow-up:** `@kit.LocalizationKit` and `@kit.ArkTS` are **not** in `KIT_DOC_URLS`
(`core/mapping.py`), so those rows render without an "Official Docs" link. Both are attested
verbatim in `hmos_api_index.json` import statements, so the kit tokens are correct — only the
doc-URL table is incomplete. Adding them is a separate change; `KIT_DOC_URLS` was deliberately
not touched here. Precedent for kits outside that table already exists (`@kit.AnalyticsKit`,
`@kit.PaymentKit`, `HarmonyOS NDK (libc++)`).

### Known pre-existing issues in this area (NOT fixed — read before touching the breakpoints)

- **Conflicting breakpoints:** `@media(max-width:768px)` establishes the overlay behaviour via
  `body.sidebar-open`, but a separate `@media (max-width:767px)` block sets
  `.sidebar { display:none }`, which kills it. The overlay path is only live in a one-pixel
  window at exactly 768px. Consolidating these two blocks is the real fix.
- **Dead rule:** the ≤767px block styles `.main-content`, a class that appears nowhere in the
  template.

---

## Sprint 11 — 2026-08-10 — Play Store App-Metadata Sheet (first online capability)

`batch_summary.xlsx` gained an **"App Info"** sheet fetched from Google Play. This is the
**only** part of the tool that touches the network. Everything about its design exists to
guarantee that fact stays invisible to an offline run.

### The non-negotiable: offline must not degrade

The batch's HTML reports, agent JSON, `batch_unmapped.xlsx`, and the other three sheets of
`batch_summary.xlsx` are produced **byte-identically** whether the fetch succeeds, finds no
internet, or never manages to import its dependency. Metadata is purely additive — it is
collected *after* the per-file analysis loop has fully finished (`analyzer.py`, between the
loop and `if rows:`), so every report and JSON is already written to disk before a single
socket opens.

Two placeholder strings can reach the sheet, and they mean different things:

| String | Meaning | Cached? |
|---|---|---|
| `No internet connection` | The connectivity probe failed; the whole phase was skipped. | **No** — retries next run |
| `N/A` | Internet is up, but this one app could not be resolved (delisted, region-locked). | **No** — retries next run |

Neither is ever written to the cache, so a bad network day never poisons future runs.

### `src/core/play_meta.py` (new, isolated)

All network code lives here and nowhere else — no engine imports it. `fetch_metadata(apps,
cache_path, ensure_dep=None)` takes `(package_name, apk_app_name)` pairs and returns an ordered
`{package_name: {field: value}}` dict **covering every input app**, so the sheet always has one
row per APK. It never raises.

**Probe-once, then commit to a mode.** The first uncached app decides the phase:

- `GooglePlayScraperException` (`NotFoundError` / `ExtraHTTPError`) → internet is *up*, this one
  app is unresolvable → that row is `N/A`, **keep going**. Expected for HK/Macau titles.
- Any other exception (DNS, timeout, TLS, proxy) → **no internet** → one warning line, every
  remaining row is `No internet connection`, and **no further requests are attempted**. With 42
  APKs this is the difference between one 5s timeout and 42 of them.

A connection-level failure *after* the probe (link dropped mid-run, e.g. XGATE reconnecting)
flips the same switch for the remainder rather than grinding through dead sockets.

**Timeout.** `google_play_scraper.app()` accepts **no timeout parameter** — it calls
`urllib.request.urlopen` bare, inheriting the global socket default of `None` (block forever).
The 5s bound is therefore imposed with `socket.setdefaulttimeout(_PROBE_TIMEOUT_SEC)` around
the phase and **restored in a `finally`**, so an exception cannot leave the global socket
timeout mutated for the rest of the process. Do not "simplify" this into the `try` body.

### Optional dependency — never in the hard-exit list

`google-play-scraper` (PyPI, unofficial) is bootstrapped by **`_ensure_play_scraper()`**, which
is deliberately **separate from `_ensure_deps()`**. `_ensure_deps()` calls `sys.exit(1)` when an
install fails — correct for androguard/openpyxl/pefile/macholib, fatal for an optional online
extra whose install failure is the *normal* offline outcome. `_ensure_play_scraper()` swallows
every failure, prints one line, and returns.

It is invoked **lazily**, through the `ensure_dep` hook passed into `fetch_metadata`, and only
when something actually needs fetching — a fully-cached run (or a run with no APKs) never
attempts a pip install. Install uses `--timeout 10 --retries 1` plus a 120s subprocess timeout
so an offline attempt fails fast instead of hanging on pip's own retry backoff.

### Region fallback — `hk` → `mo` → `us`

Each uncached app is tried against `_REGIONS = ("hk", "mo", "us")` in order with `lang="en"`,
stopping at the first storefront that has it. `us` is **last** on purpose: it is the library's
default, and this corpus is Hong Kong / Macau titles.

**The fallback cannot widen the offline probe cost.** A `NotFoundError` is the store *answering*
— it is itself proof of connectivity — so the region loop can only ever advance past its first
iteration once the internet question is already settled. An offline run therefore makes exactly
**one** call total, no matter how many APKs are in the batch (measured: 42 apps → 1 call, only
`hk` attempted). A miss in all three regions is **not** a connectivity failure and never flips
the offline switch; it lands as `N/A` for that app and the phase continues.

The winning region is cached as a sibling of `fetched_at` (`{"fetched_at", "region", "data"}`),
so a cached hit never re-probes. Entries written before this field existed are still valid — a
missing `region` is tolerated.

> **Measured on the 43-app corpus — the fallback does NOT improve coverage.** Both `us`-only and
> `hk`→`mo`→`us` resolve **41/43**. The same two apps fail either way (`com.mtr.mobile`,
> `com.huayuan.namkwong`) and they are simply not on Google Play in any region — not
> region-locked. An earlier version of this document claimed region-locking was the main cause
> of `N/A`; that was wrong and has been corrected in Known gaps.
>
> What the fallback *does* change is **which numbers you get** for apps that resolve in both.
> Across a sample of 11: `score` differed for **10**, and `ratings` / `version` /
> `lastUpdatedOn` each differed for **3**. The HK storefront returns the rating and shipped
> version actually seen by HK users, which is the relevant figure for a HK/Macau migration
> assessment. That accuracy — not coverage — is the reason to keep it.

### Cache — `src/data/reference/play_metadata_cache.json`

Chosen over `result/.metadata_cache.json` on purpose: it **survives clearing `result/`**, which
is the entire point (re-running a batch on XGATE should reuse data, not show "No internet
connection"). Shape: `{schema_version, generated_at, apps: {pkg: {fetched_at, data}}}`.
Entries older than **30 days** (`_CACHE_TTL_DAYS`) are treated as stale and refetched when
online. A corrupt or unreadable cache degrades to `{}`, never an exception.
Gitignored explicitly, alongside a `*.metadata` line.

### The sheet

Inserted with `wb.create_sheet("App Info", 0)` — index 0, so it is **first in tab order** and
the workbook opens on it. Final order: **App Info** → Batch Summary → Common Mapped → Common
Unmapped → [Unmapped DLLs] → [Unmapped Frameworks].

Passed as the keyword arg `play_metadata=None` on `export_excel_batch`, matching the existing
`mapped_ns_apps` / `unmapped_ns_apps` pattern — **existing positional callers are unaffected**
and the sheet is omitted entirely when the value is falsy (EXE/IPA-only batches have no Play
package, so they never get one).

Nine columns: `Package Name · App Name · Category · Installs · Rating · Rating Count ·
Developer · Last Updated · Version`, from `appId / title / genre / installs / score / ratings /
developer / lastUpdatedOn / version`. Styling matches the other sheets exactly (frozen header,
auto-filter, no gridlines, DKBLUE header, alternating fill).

> **A Size column was deliberately omitted — do not add it back.** Google removed app size from
> the Play detail page; `ElementSpecs.Detail` has 40 keys and `size` is not among them, and the
> library exposes no equivalent. The column would be permanently `N/A` for every app.

`Last Updated` prefers `lastUpdatedOn` (pre-formatted, `'Aug 4, 2026'`) and falls back to
formatting the `updated` Unix timestamp. Note `score`/`ratings`/`updated` are all genuinely
`None` upstream for low-traffic apps — an `N/A` there is Play's answer, not a parsing bug.

### Verified

| Scenario | Result |
|---|---|
| Online, 2-APK batch | 1 app populated, 1 `N/A` (not on Play), cache written with only the success |
| Offline (DNS forced to fail), no cache | One `[!]` line, all 8 metadata cells `No internet connection`, **no cache written**, batch completed, other 3 sheets intact |
| Offline, fully cached | `1 app(s) from cache — no network needed` — no probe attempted at all |
| Offline, partially cached | Cached row fully populated, uncached row `No internet connection` |
| Full 43-package corpus, online | 41 resolved, all via `hk`; 2 `N/A` (not on Play anywhere) |
| Offline, 42 pending apps | **1** network call total, only `hk` attempted — the ladder never runs |
| All 3 regions miss | 3 calls/app, `N/A`, offline switch **not** flipped, nothing cached |
| `hk` hits immediately | 1 call/app — no wasted `mo`/`us` probes; region cached |
| Link drops after 2 successes | 2 rows kept, one `[!]` line, remaining rows `No internet connection` |

Also confirmed: App Info first in tab order, `Batch Summary` columns
(File/App Name/Kit Count/Unmapped/Permissions) unchanged, `socket.getdefaulttimeout()` back to
`None` after a failed phase, and a legacy positional `export_excel_batch(rows, path, [], [])`
call still produces exactly `['Batch Summary']`.

---

## Sprint 12 — 2026-08-12 — Mapping expansion, round 2 (41-app batch)

Second pass over the `Common Unmapped` sheet, same discipline as the round-1 expansion in
Sprint 10 (`61f7c42`): rank candidates by how many APKs each namespace appears in, then ground
every one against `hmos_api_index.json` by looking up distinctive method names before proposing
it. Nothing was mapped on vibes, and two proposed rows were cut in review for failing exactly
that test (below).

| File | Version | `namespace_mappings` | Added |
|---|---|---|---|
| `mapping.json` | 1.4.0 → **1.5.0** | 188 → **206** | **+18** |
| `hms_mapping.json` | 1.3.0 → **1.4.0** | 136 → **137** | **+1** |

`last_updated` already read `2026-08` on both and stays there — the field is `YYYY-MM` and this
round landed in the same month as round 1. Append-only; no existing entry modified or reordered.
`permission_mappings` untouched (38 / 27). `harmony_import == harmony_kit` on all 18 HMOS rows
(the single file-wide exception, `android.renderscript`, is pre-existing and was not touched).

> **The batch is 41 APKs, not 43.** `Batch Summary` has `max_row = 43` = 1 title + 1 header +
> 41 app rows, and that arithmetic is where the "43" in circulation comes from. Cross-checked
> against 41 `_agent.json` files, 41 `_report.html` files, and 39 sheets in
> `batch_unmapped.xlsx`. Unrelated to the 43-package Play corpus in Sprint 11, which counts
> *packages queried*, not APKs analysed. All frequencies below are **N of 41**.

### What was added

Three groups, by what made them findable:

- **React Native community modules (11 rows)** — `rnscreens`, `gesturehandler`, `reanimated`,
  `safeareacontext`, `horcrux.svg`, `reactnativecommunity.webview` / `picker` / `clipboard`,
  `reactnativepagerview`, `BV.LinearGradient`, `me.leolin.shortcutbadger`. These dominate by
  *row* count because RN libraries are extremely granular — `com.horcrux.svg` alone is 52
  distinct unmapped namespaces and `com.swmansion.rnscreens` is 45, each absorbed by one prefix
  rule. Precedent already existed (`com.rnmaps.maps`, `com.agontuk.RNFusedLocation`,
  `com.reactnativecommunity.asyncstorage`).
- **Alias / breadth completion (4 rows)** — `org.apache.http` broadens the existing
  `org.apache.http.client` to the sibling sub-packages (same kit, so no behaviour change for
  already-matched namespaces); `org.w3c.dom` and `org.xml.sax` join the existing `org.xmlpull`
  → `@kit.ArkTS` family; `com.google.maps.android` joins `com.google.android.gms.maps` →
  `@kit.MapKit`.
- **Single-target libraries (3 rows)** — `com.pichillilorenzo.flutter_inappwebview_android` →
  `@kit.ArkWeb` (follows the `io.flutter.plugins.*` per-plugin precedent),
  `com.yalantis.ucrop` → `@kit.ImageKit`, `android.provider.MediaStore` →
  `@kit.MediaLibraryKit`.

`com.horcrux.svg` carries an explicit ambiguity note: `@kit.ArkGraphics2D` is also plausible for
the canvas-backed rendering path. It is recorded in the entry rather than resolved, because the
index confirms ArkUI owns `createPath2D` but does not settle which kit a full SVG renderer
should target.

**HMS gets one row again, for the same structural reason as round 1** — HMS apps are still
Android apps, so RN/Flutter/Java libraries run unchanged there and mapping them would falsely
imply migration work. `com.google.maps.android` → `Map Kit` (medium) qualifies on the same
grounds as `com.android.installreferrer` did: a Google service with a real Huawei counterpart.

### Cut in review — both had frequency but failed grounding

- **`com.learnium.RNDeviceInfo`** (12/41). Grounding did not merely come back weak, it came
  back **empty**: `@ohos.deviceInfo` is absent from `hmos_api_index.json` entirely —
  `osFullName`, `productModel`, `udid`, `buildVersion` all return nothing, and a search for
  `deviceinfo` surfaces only `remoteDevice` from `@kit.NearLinkKit`, a different API. Same
  disposition as `android.service.media` in round 1: the target is probably right, the kit
  token cannot be confirmed. Note the index is not exhaustive, so NOT FOUND means *unconfirmed*,
  not *nonexistent*.
- **`android.preference`** (13/41). Half-true rather than unconfirmed. `PreferenceActivity` is a
  *UI* class; `@kit.ArkData` is the *storage* half, and HarmonyOS has no preference-screen
  abstraction at all. Sibling precedent cuts both ways — `android.content.SharedPreferences` →
  `@kit.ArkData` is correct because it really is storage, while
  `android.security.NetworkSecurityPolicy` was left unmapped for being config-not-API.

### Left unmapped on purpose (beyond the round-1 list, which still stands)

- **Firebase core plumbing** — `datatransport` (21/41), `events`, `heartbeatinfo`, `inject`,
  `platforminfo`, `FirebaseApp`, `FirebaseOptions`, `tracing`, `StartupTime`, `logger`
  (≈130 rows). DI-container and telemetry-transport internals, the same category as the Fresco
  plumbing left in round 1. `FirebaseApp` / `FirebaseOptions` *do* have a real counterpart, but
  it is **AGConnect — an ohpm package (`@hw-agconnect/core`), not a `@kit.*`**. Same for
  `io.invertase.firebase.*` and `com.airbnb.lottie` (→ `@ohos/lottie`). These are the intended
  catch for the OHPM second tier and were deliberately not forced into a native kit.
- **`org.openjsse.javax.net`** (12/41) — JSSE provider internals, identical in kind to
  `org.conscrypt`, which round 1 left unmapped. Consistency.
- **Vendor SDKs** — `com.alipay.*` (8/41), `com.tencent.mm.opensdk` (8/41). Third-party
  HarmonyOS SDKs exist but are not native kits.
- **`com.google.android.libraries`** (9/41) — too vague to attribute to any kit.

### Verified against real engine output

Two passes, because they measure different things and the row-count units are easy to conflate.

**Analytical** — the real match loop (`apk_engine.py:312-316`, `break`-on-first-match in file
order) replayed over all 41 per-app sheets of `batch_unmapped.xlsx`:

| Metric | Result |
|---|---|
| Distinct namespaces in `Common Unmapped` (≥2 apps) now matched | **255** of 2,180 |
| Predicted at proposal time | 260 |
| Delta | exactly the 2 cut rows — `android.preference` (1) + `com.learnium.RNDeviceInfo` (4) |
| Per-app row instances absorbed | 1,823 of 15,011 (12.1%) |
| Distinct namespaces incl. 1-app-only (not in the sheet) | 284 |
| **Rows absorbed by a pre-existing entry (shadowing)** | **0** |

The shadowing count is the load-bearing one: every absorbed row resolves to one of the 18 new
entries, so appending could not have changed the result for any namespace that already matched.

**Empirical** — full `analyze_apk` runs, old unmapped count vs new:

| APK | Before | After | Drop | Predicted |
|---|---|---|---|---|
| `com.hph.odt.stacks` | 71 | 23 | **48** | 48 ✓ |
| `com.polyulife` | 371 | 216 | **155** | 155 ✓ |

Both exact, and no namespace covered by a new rule leaked back into `unmapped_namespaces`.

### Pending follow-up (deliberately NOT done here)

`@kit.MediaLibraryKit` joins `@kit.ArkTS` and `@kit.LocalizationKit` as kit tokens absent from
`KIT_DOC_URLS` (`core/mapping.py`, 50 entries), so rows using them render with no "Official
Docs" anchor. `get_doc_url` returns `None` and the renderer omits the `<a>` cleanly, so this is
cosmetic, not a broken link — but it now affects four of the new rows (`org.w3c.dom`,
`org.xml.sax`, `android.provider.MediaStore`). `KIT_DOC_URLS` was left untouched in this commit;
fixing all three tokens together is a separate change.

### OHPM second-tier mapping — Phase 2B: registry fetcher (2026-08-12)

Groundwork for an **OHPM second tier**: native `@kit.*` / HMS kits stay the priority, and OHPM
is only a second-pass filter over what native leaves unmapped. Sprint 12 already named the
intended catches — Firebase core and `com.airbnb.lottie` are the rows that want an ohpm package
rather than a kit. This phase builds only the data source; **no mapping file exists yet** and
nothing in the analysis pipeline reads any of it.

**`src/core/ohpm_fetch.py` (new, isolated, stdlib-only).** Same containment rule as
`play_meta.py`: no engine, renderer or mapping code opens a socket. Unlike `play_meta.py` it
needs **no third-party dependency** — the API is plain JSON over `urllib` — so there is no
`_ensure_*` hook and nothing that can fail to pip-install. It is a manually-run builder in the
mould of `api_index.py`, not part of any analysis run:

```
python src/core/ohpm_fetch.py            # resume/refresh the sweep
python src/core/ohpm_fetch.py --force    # discard and re-sweep from page 1
python src/core/ohpm_fetch.py --check @ohos/lottie
```

Because it runs standalone it deliberately does **not** import `ui.terminal` (that would need
`src/` on `sys.path`); it prints plain ASCII-prefixed lines like `api_index.py`. The em-dashes
used everywhere else in this project mojibake on the Windows console, so printed strings here
use ASCII hyphens — docstrings and comments still use em-dashes.

#### Endpoints

Found by reading the SPA bundle `/assets/index-*.js`, which inlines the base-URL table
(`mP="/ohpmweb/registry"`, `la="/ohpm/console/api"`, `Loe="/ohpm"`). The site is a JS-only Vite
SPA — there is no HTML to scrape.

| Purpose | Route |
|---|---|
| Search / enumerate | `GET /ohpmweb/registry/oh-package/openapi/v1/search` |
| Detail (one package) | `GET /ohpmweb/registry/oh-package/openapi/v1/detail/{urlencoded}[/{ver}]` |
| Category tree | `GET /ohpm/tech-map` — note `/ohpm/`, **not** `/ohpmweb/` |

Search takes five **required** params: `condition`, `pageNum`, `pageSize`, `sortedType`,
`isHomePage`. `sortedType` must be the literal **`relevancy`** — `relevance` returns
`HTTP 400 {"message":"参数异常"}`. An empty `condition` enumerates the whole registry.
`pageSize` caps at **100**; 200 is rejected with HTTP 400. The sibling `business/v1` prefix is
auth-gated (`401 {"code":204030,"message":"The request source is abnormal"}`) — `openapi/v1` is
the public one.

#### Four API behaviours that are load-bearing

- **A missing package returns HTTP 200, not 404.** `body` degrades from an object to the literal
  string `"success"`. Existence is `isinstance(body, dict)` and nothing else — neither the HTTP
  status nor the `code` field distinguishes a real package from a typo. This is not academic:
  `@hw-agconnect/core`, the package Sprint 12 named as the Firebase target, **does not exist**
  and returns exactly this sentinel. The real ids are `@hw-agconnect/hmcore` (HarmonyOS NEXT
  generation) and `@hw-agconnect/core-ohos` (legacy OpenHarmony v1.1.x); the org has 69
  packages across those two generations. Existence-check before writing any mapping row.
- **A Huawei WAF fronts the site.** `GET /` sets `HWWAFSESID` + `HWWAFSESTIME`; those cookies
  plus a `Referer` header must ride on every request or repeats get challenged. Hence the
  CookieJar seeded on first use in `_Session`. Measured: **zero challenges** across the sweep.
- **Responses are gzip and urllib does not decompress**, so `Content-Encoding` is honoured by
  hand. A 2xx body that will not parse as JSON is treated as a WAF interstitial and stops the
  sweep (error kind `"parse"`), rather than being mistaken for a per-package miss.
- **There is no import statement anywhere in the API.** An OHPM package is consumed via
  `ohpm install <name>`, which `install_cmd()` builds. OHPM mapping rows must therefore carry a
  package id + install command, **not** a `harmony_import` — this is the structural difference
  from `@kit.*` rows, whose imports come from `hmos_api_index.json`.

#### Sweep strategy — search rows, not details

The sweep harvests **search rows only**: 3499 packages in 35 requests. It deliberately does not
call detail per package, because the fields split cleanly and search carries the ones that
matter for capability matching:

- **search-only:** `description` — the single most useful field for matching, and *absent from
  the detail response entirely*
- **detail-only:** `repository`, `downloads`, `fileSize`, `readme*Url`, `changelog*Url`,
  `compatibleSdkVersion`, `dependencies`/`dependent`, `versions`, `pointDetail`

So detail is reserved for the Phase-2D shortlist (where `repository` drives README
verification) instead of 3499 extra calls. `_PKG_FIELDS` is the search→cache field map.

`/ohpm/tech-map` is fetched once and flattened to `{packageName: "L1 > L2 > L3"}` — 19 top-level
categories nested to L4, 1062 packages, each in exactly one category (verified 1:1, no
duplicates). Only ~30% of the registry is categorised, so an uncategorised package is normal,
not an error. Two tech-map names are absent from the search sweep (1060/1062 overlap).

#### Cache — `src/data/reference/ohpm_registry_cache.json`

Sits beside `play_metadata_cache.json` and is **gitignored** the same way (1.8 MB).
Shape: `{schema_version, fetched_at, sweep:{complete,pages_done,total_pages,total,page_size},
packages:{name:{…}}, tech_map:{name:"cat > path"}}`. `load_registry()` is the offline accessor
for downstream phases.

**Resumable.** The cache is written after *every* page and `sweep.pages_done` records the
highest contiguous page, so a kill mid-sweep resumes at the next page rather than restarting.
Writes go to a `.tmp` sibling and are then `replace()`d, so a kill *during* a write cannot
truncate an already-good cache. Packages are keyed by name, which makes re-fetching a partially
written page idempotent — and also absorbs the pagination drift from publishes landing during
the sweep (empty-condition ordering is newest-first). A cache written at a different
`_PAGE_SIZE` cannot be resumed (its `pages_done` counts differently sized pages) and is
discarded rather than continued.

Politeness: `_PAGE_DELAY_SEC = 0.4` between pages, `_PAGE_RETRIES = 2` per page with a short
backoff before the sweep parks itself for resume. Full sweep ≈ 77s wall-clock.

#### Verified

| Scenario | Result |
|---|---|
| Fresh full sweep | **3499** packages, 1062 categorised, 35 pages, **37 requests** (1 seed + 1 tech-map + 35), zero WAF challenges |
| Kill mid-sweep, re-run | Resumed at the next page and completed; proved twice (killed at page 1, and a SIGPIPE kill at page 4 → resumed at 5 in 31 requests) |
| Re-run when complete | `[=] Sweep already complete` — no pages re-fetched |
| `validate_package_exists("@ohos/lottie")` | `True`, served from cache with **0** network requests |
| `validate_package_exists` garbage / `""` | `False` (garbage costs 1 request; empty string short-circuits) |
| `@hw-agconnect/core` vs `/hmcore` | `NOT FOUND` vs `EXISTS` — the `isinstance` gotcha caught a real error |
| Offline (unresolvable host) | One `[!]` line, `packages=0`, `complete=False`, **no exception**; `validate_package_exists` → `None` (indeterminate, not `False`), `fetch_tech_map` → `{}` |

Field coverage across the 3499: `name`/`popularity`/`points`/`likes`/`latest_version` 100%,
`description` 3496 (99.9%), `license` 3495, `org` 69%, `keywords` 63%.

### OHPM Phase 2D: `ohpm_mapping.json` exists — slice 1 (2026-08-12)

`src/data/mappings/ohpm_mapping.json` v1.0.0 — **11 namespace rows / 8 distinct packages**,
the first OHPM second-tier mappings. Nothing in the analysis pipeline reads it yet; it is data
only, built slice by slice from the batch pool with per-slice review.

**Schema** — deliberately *not* the `mapping.json` shape:

```json
{"version":"1.0.0","last_updated":"2026-08","tier":"ohpm",
 "ohpm_mappings":[{"android_namespace","android_display","ohpm_package","install_cmd",
                   "category","description","confidence","source_repo","popularity","note"}]}
```

- The list key is **`ohpm_mappings`**, not `namespace_mappings`, and there is a `tier` field —
  so OHPM rows can never be loaded into the native matcher by accident.
- **No `harmony_import`.** The API has no import statement; `install_cmd`
  (`ohpm install <name>`) takes its place. It is derivable from `ohpm_package` via
  `ohpm_fetch.install_cmd()` and is stored redundantly for readability.
- `category` comes from `/ohpm/tech-map` and is **nullable** — only ~30% of the registry is
  categorised (2 of the 11 rows are `null`). `source_repo` is nullable too and is `null` for 7
  of 11: vendor packages (`@hw-agconnect/*`, `@tencent/wechat_open_sdk`,
  `@cashier_alipay/cashiersdk`) are closed-source and publish no repository. README
  verification for those used the registry's own `readmeEnUrl` CDN copy instead, which is
  better evidence anyway — it is the package's own documentation.
- `popularity` is stored because it is the tiebreak that justified the pick, which makes a
  stale row auditable later.

**Native-first is the dominant rule, and it routes most of the pool AWAY from OHPM.** Before
any OHPM package may be proposed, the capability is checked against `hmos_api_index.json`; if a
native `@kit.*` genuinely covers it, **no OHPM row is written**. In slice 1 this disqualified
**12 of 21** reviewed capabilities — including several that look like obvious third-party
libraries (permissions, connectivity, zip, EventBus, share, notifications, image picker). OHPM
is only for what native cannot cover, exactly as the native kits stay the priority tier.

Those 12 are not lost: they accumulate in **`NATIVE_CANDIDATES.md`** (repo root, tracked) as a
backlog for a dedicated native mapping round. Two of them **correct earlier cuts** and must not
be re-cut — `android.service.media` → `@kit.AVSessionKit` (Sprint 10 could not confirm the kit
token; now attested) and `com.learnium.RNDeviceInfo` → `@kit.BasicServicesKit` (Sprint 12
searched for the wrong token — `import { deviceInfo } from '@kit.BasicServicesKit'` is attested
verbatim).

**Verification discipline per proposed row** — unchanged in spirit from the Sprint 10/12 native
rounds, plus one addition:

1. native-first check against `hmos_api_index.json` (above);
2. match on **function** — description + keywords + tech-map category, never on name alone;
3. rank competing candidates by popularity/points/likes, propose the top one, record the
   runners-up in `note`;
4. **fetch and read the package README** (repository, or the registry `readmeEnUrl` for
   closed-source vendor packages) and confirm it does what the Android library did;
5. **existence-check against the cache** before the row may be written — this is where the
   `isinstance(body, dict)` gotcha earns its keep.

Popularity does **not** override function. `com.github.chrisbanes.photoview` →
`@ohos/photoview` (popularity 364) was chosen over `@rv/image-preview` (1300) because the
latter is a Swiper-based lightbox gallery, not a zoomable ImageView.

> **Vendor SaaS SDKs must be checked, not assumed absent.** Phase 2C initially classified
> WeChat/Alipay/Stripe/Braze/Xiaomi/Amazon as "vendor SDK → skip" on the assumption that a
> vendor's own SDK would not be an ohpm package. That was wrong for two of the six, and they
> are high-frequency: `@tencent/wechat_open_sdk` (popularity 13301) and
> `@cashier_alipay/cashiersdk` (13325) are official, first-party, and matched
> `com.tencent.mm.opensdk` / `com.alipay.sdk.app` exactly. Stripe, Braze and Xiaomi push
> genuinely return **zero** hits. The registry also carries `@tencent/mmkv`, `@umeng/apm`,
> `@volcengine/apmplus`, `@growingio/analytics`. Always query the cache — it is local and free.

#### Slice 2 (2026-08-12) — and the pool is now exhausted

`ohpm_mapping.json` → **v1.1.0, 15 namespace rows / 11 distinct packages**. Slice 2 added 3
approved mappings over 4 namespace rows:

| Android namespace | OHPM package | Conf |
|---|---|---|
| `org.mozilla.universalchardet` | `@ohos/juniversalchardet` | high |
| `pl.droidsonroids.gif` | `@ohos/gif-drawable` | medium |
| `com.drew` · `com.adobe.xmp` | `@ohos/metadata-extractor` | medium |

Both `medium`s are medium for the same reason — **native partly covers them**, so the row is a
migrator's choice rather than a required dependency, the shape first used for `com.tencent.mmkv`:
`@kit.ImageKit` decodes GIF frames but has no play/pause/seek/speed control (`ImageAnimator` is
absent from the index), and `@kit.ImageKit`'s `getImageProperty`/`modifyImageProperty` already
covers image EXIF — metadata-extractor earns its row only on the IPTC/XMP/ICC and audio/video
superset.

**One row was cut on function mismatch:** `org.javamoney.moneta` → `bignumber.js` (popularity
6088, 98k downloads) was rejected despite being the obvious search hit. JavaMoney `Money` is
amount + currency + rounding policy; `bignumber.js` supplies only the arithmetic half and is not
a Money type, while native `intl.NumberFormat` (`@kit.LocalizationKit`) covers currency
*formatting*. Left unmapped — a wrong mapping is worse than a gap. Popularity never overrides
function; the same principle picked `@ohos/photoview` (364) over `@rv/image-preview` (1300) in
slice 1.

**Native-first routed 24 of 29 capabilities in slice 2** (vs 12 of 21 in slice 1), including six
that were confidently expected to be third-party ports and are not:

| Expected OHPM | Actually native |
|---|---|
| barcode → a zxing port | **`@kit.ScanKit`** (`import { detectBarcode } from '@kit.ScanKit'`) |
| fastjson → a JSON lib | **`@kit.ArkTS`** + the JS builtin `JSON` |
| SLF4J → a logback port | **`@kit.PerformanceAnalysisKit`** (`hilog`) |
| PDF → a pdfium port | **`@kit.PDFKit`** (`import { pdfService } from '@kit.PDFKit'`) |
| icon fonts → a vector-icons port | **`@kit.ArkUI`** (`registerFont` + `SymbolGlyph`) |
| cookies → `@kit.NetworkKit` | **`@kit.ArkWeb`** (webview cookie manager) |

> **Method-name lookups can produce false negatives — check import statements too.** `@kit.ScanKit`
> returned NOT FOUND for `scanBarcode`/`generateBarcode`/`customScan` against the index keys, and
> was nearly written off as having no native path. Scanning the index's *`import_statement`
> values* for `ScanKit` immediately produced three verbatim imports. `hmos_api_index.json` keys on
> normalized simple method names, so a kit whose methods are indexed under other names is
> invisible to a key lookup. Always fall back to an import-statement grep before concluding a
> capability has no native kit.

**The pool is exhausted.** Of the 87 capabilities the Phase-2C pool consolidated into (50 MAP /
37 SKIP), **all 50 MAP capabilities have now been reviewed** — 14 in slice 1, 34 in slice 2, and
the final 2 (`wakelock`, `packageinfo`, 2 apps each) resolved to `@kit.BasicServicesKit`
(`runningLock`) and `@kit.AbilityKit` (`bundleManager`). **There is no slice 3.** What remains
below the capability rollup is the 567-namespace residual, all ≤3 apps and dominated by
`cn.jiguang.*` (JPush, vendor) plus obfuscation leakage — nothing mappable.

Final tally for the OHPM tier: **15 OHPM rows** against **38 native candidates** banked in
`NATIVE_CANDIDATES.md`. The tier converged small and sharp, exactly as the native-first rule
intends — the headline is that the batch pool's real answer was overwhelmingly *native kits*, and
OHPM was only ever needed for vendor SDKs (WeChat, Alipay, AGConnect, MMKV) and a handful of
genuine library ports (Lottie, PhotoView, SubsamplingScaleImageView, juniversalchardet,
gif-drawable, metadata-extractor).

**Genuine gaps recorded, deliberately unmapped:** `net.openid.appauth` / `com.rnappauth` (4 apps —
native Account Kit is Huawei-ID-only; generic OAuth2/OIDC against arbitrary providers has no
equivalent and the registry has only provider-specific SDKs, so it must be hand-rolled over
`@kit.NetworkKit` + `@kit.ArkWeb`), `com.scottyab.rootbeer` (4 — zero registry hits, no native
attestation API), and `org.reactnative.facedetector` (3 — best candidate `hfacedetect` is
popularity 74 / 289 downloads, and `@kit.VisionKit` offers only `interactiveLiveness` /
`visionImageAnalyzer`, not face landmarks).

The Firebase bullet became **three** rows (`com.google.firebase.FirebaseApp`,
`.FirebaseOptions`, `io.invertase.firebase.app`) rather than one: the engine matches by
namespace prefix, and a shared `com.google.firebase.Firebase` prefix would also swallow
`FirebaseCommonRegistrar`, which is deliberately left unmapped. Firebase's other halves route
to **native** kits — `.messaging` → `@kit.PushKit`, `.analytics` → `@kit.AnalyticsKit` — and
its DI/telemetry plumbing (`datatransport` 21/41, `events` 18/41, `heartbeatinfo`, `inject`,
`platforminfo`, `tracing`) stays unmapped, as Sprint 12 already decided.

---

## Known gaps / warts (as of 2026-08-07)

- **`device_matrix` is always `{}`** — `build_agent_json:2592` unconditionally emits `result.get("device_matrix", {})`, but no engine ever sets the key. Every agent JSON in every mode carries an empty dict.
- **No CLI flag for `exe_folder`** — `--mode` is `choices=["apk","exe","ipa"]`. The `mode == "exe_folder"` branch at `analyzer.py:318` is reachable only through the interactive TUI, so the mode cannot be scripted or automated.
- **No `export_excel_exe_folder`** — folder mode has no Python Excel export. Only the in-browser XLSX.js button produces a spreadsheet, and it needs a CDN fetch.
- **`.apkm` files are not batched** — `run_batch` globs `*.apk`, `*.exe`, `*.dll`, `*.ipa`. There is at least one `.apkm` in `src/input/` that is silently skipped. Split-APK bundles are not handled at all.
- **`hmos_api.xlsx` is untracked while its generated index is tracked** — `.gitignore` has `*.xlsx`, so `src/data/reference/hmos_api.xlsx` is not in git, but `hmos_api_index.json` (3.9 MB) is. Re-running `python src/core/api_index.py` on a fresh clone fails; the source-of-truth spreadsheet must be obtained out-of-band.
- **`src/data/permissions/*.txt` and `src/data/reference/package_names.txt` are unreferenced** — grep across all `.py` returns zero hits. They are inert reference material. If they were meant to drive `grant_level` assignment or the private-lib heuristic, that wiring was never built.
- **APK stat card 1 counts namespaces, not kits** — the label reads "Number of Libraries Mapped" and the value is `len(flat_ns_rows)`. It is NOT `len(kit_matches)`, which is what the TUI summary and agent JSON report. The two numbers will differ, usually substantially.
- **`api-ms-win-*` / `ext-ms-win-*` beyond the 11 CRT stubs vanish silently** — they match no mapping entry and are then filtered out of `unmapped_dlls`, so they appear in neither the kit table nor the unmapped list.
- **`google-play-scraper` is unofficial and scrapes HTML** — it parses embedded JSON out of the Play detail page via regex (`Regex.SCRIPT` / `KEY` / `VALUE` in `constants/element.py`). Google can change that page's structure at any time with no notice, and when they do the library returns `None` for some or all fields (surfacing as `N/A`) or stops working entirely until upstream patches it. The failure is contained — every path degrades to `N/A` and the rest of the batch is untouched — but do not treat the App Info sheet as a reliable data source, and check for a library update before investigating a sudden wave of `N/A`.
- **Apps absent from Google Play return `N/A`, and region fallback does not help** — measured across the 43-app corpus, `us`-only and the `hk`→`mo`→`us` ladder both resolve 41/43. The two failures (`com.mtr.mobile`, `com.huayuan.namkwong`) are not listed on Play in any of the three storefronts, so no region setting recovers them; enterprise/internal builds and delisted apps simply have no Play page. `NotFoundError` for these is **expected, not an error**. (A previous revision of this file asserted that region-locking was the common cause of `N/A` and that region support "would likely recover some of them" — both claims were wrong, and the measurement above supersedes them. The ladder was kept for data accuracy, not coverage; see Sprint 11.)
- **`updated` / `score` / `ratings` are genuinely `None` for low-traffic apps** — Play itself omits them, so `Last Updated`, `Rating`, and `Rating Count` show `N/A` even for a successfully fetched app. Not a parsing bug; there is nothing to fix.

---

## Implementation Notes (current)

- Read each file before editing
- `mapping.json` / `hms_mapping.json`: append `namespace_mappings` and `permission_mappings`, never overwrite; bump the `version` field when adding entries
- `ios_mapping.json`: only append `framework_mappings`, never overwrite
- `win_mapping.json`: append `dll_mappings`; use the optional `category` field to override confidence-derived status (as done for Qt6)
- `hmos_api_index.json` is generated by `python src/core/api_index.py` — re-run after updating `hmos_api.xlsx` (note the xlsx is untracked; see Known gaps)
- DLL family grouping in the EXE report is derived at render time from DLL name shape — do NOT add a `group` field to `win_mapping.json` expecting it to be read
- IPA binary (Mach-O) is often encrypted from App Store — framework folder is always readable; `static_linking_likely` is set when encrypted AND fewer than 3 frameworks visible
- `plistlib` handles both XML and binary plist formats automatically
- Test with real `.ipa` from TestFlight or developer build for full analysis; App Store builds will show static-linking banner
- EXE Folder mode expects `input/pc/<app-name>/` containing the `.exe` plus all its `.dll` files
- Network code belongs in `src/core/play_meta.py` and nowhere else — no engine or renderer may open a socket. Anything added there must degrade to a placeholder string, never raise, and never block past the socket timeout
- Never add `google-play-scraper` (or any optional dep) to `_ensure_deps()` — that list `sys.exit(1)`s on install failure. Use the `_ensure_play_scraper()` soft pattern
- Delete `src/data/reference/play_metadata_cache.json` to force a full refetch; it is gitignored and safe to remove at any time

---

## Bugfix Round — 2026-06-30

Four post-Sprint-7 fixes: `dfd76da` added `grant_level` to all 38 `permission_mappings` entries and fixed the Permission Coverage stat-card sublabel in `renderer.py` to display real system/user/restricted tier counts instead of always showing zero. `2daca8a` restructured the namespace-matching loop in `apk_engine.py` so `namespace_mappings` is tried first for all namespaces — the blanket androidx→ArkUI fallback had been running before the loop with a `continue`, making 20 specific androidx entries (camera, media3, biometric, room, etc.) permanently unreachable. `f6bcc99` replaced hard key accesses with `.get()` fallbacks throughout `export_excel_apk()`, `export_excel_exe()`, and `export_excel_ipa()` to prevent intermittent `AttributeError` when a mapping entry has a null `confidence` or `note` field. `e208272` corrected six semantic errors in `mapping.json`: `android.hardware.sensor` → `android.hardware.Sensor` (capital S, so `SensorManager`/`Sensor`/`SensorEvent` now match), recaptcha → `@kit.UserAuthenticationKit`, protobuf → `@kit.ArkData`, freshchat → `@kit.ArkWeb`, xposed `harmony_kit` → `null` (engine now routes null-kit matches to `unmapped_namespaces` instead of crashing), and commons.lang3 kit label tightened to `"HarmonyOS NDK (libc++)"` / low confidence.
