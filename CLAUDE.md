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

## Known gaps / warts (as of 2026-08-07)

- **`device_matrix` is always `{}`** — `build_agent_json:2592` unconditionally emits `result.get("device_matrix", {})`, but no engine ever sets the key. Every agent JSON in every mode carries an empty dict.
- **No CLI flag for `exe_folder`** — `--mode` is `choices=["apk","exe","ipa"]`. The `mode == "exe_folder"` branch at `analyzer.py:318` is reachable only through the interactive TUI, so the mode cannot be scripted or automated.
- **No `export_excel_exe_folder`** — folder mode has no Python Excel export. Only the in-browser XLSX.js button produces a spreadsheet, and it needs a CDN fetch.
- **`.apkm` files are not batched** — `run_batch` globs `*.apk`, `*.exe`, `*.dll`, `*.ipa`. There is at least one `.apkm` in `src/input/` that is silently skipped. Split-APK bundles are not handled at all.
- **`hmos_api.xlsx` is untracked while its generated index is tracked** — `.gitignore` has `*.xlsx`, so `src/data/reference/hmos_api.xlsx` is not in git, but `hmos_api_index.json` (3.9 MB) is. Re-running `python src/core/api_index.py` on a fresh clone fails; the source-of-truth spreadsheet must be obtained out-of-band.
- **`src/data/permissions/*.txt` and `src/data/reference/package_names.txt` are unreferenced** — grep across all `.py` returns zero hits. They are inert reference material. If they were meant to drive `grant_level` assignment or the private-lib heuristic, that wiring was never built.
- **APK stat card 1 counts namespaces, not kits** — the label reads "Number of Libraries Mapped" and the value is `len(flat_ns_rows)`. It is NOT `len(kit_matches)`, which is what the TUI summary and agent JSON report. The two numbers will differ, usually substantially.
- **`api-ms-win-*` / `ext-ms-win-*` beyond the 11 CRT stubs vanish silently** — they match no mapping entry and are then filtered out of `unmapped_dlls`, so they appear in neither the kit table nor the unmapped list.

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

---

## Bugfix Round — 2026-06-30

Four post-Sprint-7 fixes: `dfd76da` added `grant_level` to all 38 `permission_mappings` entries and fixed the Permission Coverage stat-card sublabel in `renderer.py` to display real system/user/restricted tier counts instead of always showing zero. `2daca8a` restructured the namespace-matching loop in `apk_engine.py` so `namespace_mappings` is tried first for all namespaces — the blanket androidx→ArkUI fallback had been running before the loop with a `continue`, making 20 specific androidx entries (camera, media3, biometric, room, etc.) permanently unreachable. `f6bcc99` replaced hard key accesses with `.get()` fallbacks throughout `export_excel_apk()`, `export_excel_exe()`, and `export_excel_ipa()` to prevent intermittent `AttributeError` when a mapping entry has a null `confidence` or `note` field. `e208272` corrected six semantic errors in `mapping.json`: `android.hardware.sensor` → `android.hardware.Sensor` (capital S, so `SensorManager`/`Sensor`/`SensorEvent` now match), recaptcha → `@kit.UserAuthenticationKit`, protobuf → `@kit.ArkData`, freshchat → `@kit.ArkWeb`, xposed `harmony_kit` → `null` (engine now routes null-kit matches to `unmapped_namespaces` instead of crashing), and commons.lang3 kit label tightened to `"HarmonyOS NDK (libc++)"` / low confidence.
