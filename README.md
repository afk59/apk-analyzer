# App-Analyzer

Scans Android APKs, Windows EXE/DLLs, and iOS IPAs, and matches what they use against HarmonyOS NEXT / HMS Core kits. Gives you an HTML report showing what maps directly, what needs work, and what has no equivalent yet.

## What a clone needs

Everything required to **run** an analysis is in this repository. Nothing has to be
fetched out of band:

| File | Why it is tracked |
|---|---|
| `src/data/mappings/*.json` | The mapping rules themselves — Android/iOS/Windows namespace → HarmonyOS kit, plus the OHPM second tier. |
| `src/data/reference/hmos_api_index.json` | The generated HarmonyOS API index the matcher reads at runtime. |
| `src/data/reference/hmos_api.xlsx` | Its source spreadsheet, so `python src/core/api_index.py` can regenerate the index. |
| `src/data/reference/ohpm_registry_cache.json` | The full OHPM registry sweep (3,499 packages). Rebuilding it needs internet and a working session against Huawei's WAF. |
| `src/data/reference/play_metadata_cache.json` | Cached Google Play metadata. Without it an offline batch shows "No internet connection" instead of real data. |
| `docs-ref/` | The HarmonyOS documentation and ArkTS API corpus used to ground every mapping decision. Read-only reference, not used at runtime. |

Only two things are deliberately **not** in the repository, and neither is needed to run
the tool: the APK/EXE/IPA test corpus (large binaries, not ours to redistribute) and
generated output (`src/result/`, reports, workbooks).

> **Windows: enable long paths before cloning.** The documentation corpus nests deeply —
> the longest path inside the repo is 212 characters, and Windows' default limit is 260
> for the *whole* path including where you cloned it. Clone into a short directory and
> run this once, or the checkout will fail partway with "Filename too long":
>
> ```
> git config --global core.longpaths true
> ```

## Requirements

Before using this tool, make sure **Python** is installed on your computer.

## How to Run

Simply run the `run.bat` file.

The first time you run the tool, `run.bat` will automatically install the required Python dependencies using `pip`.

Since these dependencies are downloaded from the internet, you must:

* Disconnect from **wlanaccess** network and **XGATE**.
* Connect to a personal internet connection (such as a mobile hotspot or home Wi-Fi).
* Run `run.bat` once to download and install the required dependencies.

After the initial installation is complete, you can reconnect to **XGATE** and use the tool normally. The dependency installation is only required once.

## Adding Files to Analyze

Everything you want to analyze goes in the `input/` folder (inside `src/`).

* **APK** — copy the `.apk` file straight into `input/`.
* **IPA** — copy the `.ipa` file straight into `input/`.
* **EXE / DLL** — these need their own subfolder, since a Windows app is usually more than one file. Create a folder under `input/pc/` named after the app, and put the `.exe` together with all its `.dll` files in there.

  ```
  input/
    pc/
      cppcheck/
        cppcheck.exe
        cppcheck-core.dll
        Qt6Core.dll
        ...
  ```

  You can have multiple app folders under `input/pc/` — the tool will ask you which one to analyze.

## Modes

Run `run.bat` and pick a mode from the menu:

* **APK** — analyze one Android APK. You'll also be asked to pick a target: **HarmonyOS NEXT** or **HMS Core**.
* **EXE** — analyze a single Windows `.exe` (or `.dll`) file from `input/`.
* **IPA** — analyze one iOS IPA. Note: App Store builds are encrypted, so results are limited to what's visible without decrypting the binary (frameworks folder, Info.plist, permissions).
* **Batch** — analyze every APK, EXE, and IPA file sitting directly in `input/` in one go, and produce a combined summary.
* **EXE Folder** — analyze a whole `input/pc/<app-name>/` folder as one app: imports from every `.exe`/`.dll` in it are merged into a single report.

## Output

Everything gets saved in `result/` (inside `src/`):

* An **HTML report** per analysis — opens automatically in your browser when the run finishes. Shows matched kits, unmapped libraries, permissions, and (for EXE) DLL details. There's an **Export to Excel** button at the top of the report if you want a spreadsheet copy.
* A matching **JSON file** in `result/agent_outputs/` — a machine-readable summary of the same result, meant for feeding into other tools/agents rather than reading directly.
* **Batch** mode additionally produces `result/batch_summary.xlsx`, a one-row-per-file overview of everything analyzed in that run.

Reports are named after the input file/folder, so re-running an analysis overwrites the previous report for that same file.
