# App-Analyzer

Scans Android APKs, Windows EXE/DLLs, and iOS IPAs, and matches what they use against HarmonyOS NEXT / HMS Core kits. Gives you an HTML report showing what maps directly, what needs work, and what has no equivalent yet.

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
