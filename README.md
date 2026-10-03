# Migration Analyzer

Scans Android APKs, Windows EXE/DLLs and iOS IPAs and matches what they use against
HarmonyOS NEXT / HMS Core kits. Produces an HTML report and an Excel workbook for every
app, showing what maps directly, what needs work, and what has no equivalent yet.

## Requirements

- Windows 10 or 11
- Python 3.10 or newer, on PATH
- Internet access **once**, for the first start (it installs its own packages)

## Starting

Double-click **`run.bat`**.

The first start installs everything it needs and says what it is doing; this happens once.
After that, `run.bat` opens the app window directly. If a window cannot be opened, the app
opens in your default browser instead.

> On a corporate network, if the first start cannot install its packages: disconnect from
> the company proxy/VPN, start once, then reconnect. The app itself needs no internet
> afterwards, except for downloading APKs by package name.

## Using it

**Analyze** — choose what to analyse:

- **A file** — one `.apk`, `.exe`, `.dll` or `.ipa`.
- **A folder** — every supported file in it, as one batch. Files that already have a report
  are skipped unless you untick *skip existing*.
- **A program folder** (EXE/DLL only) — every binary gets its own report (*batch*), or the
  whole program gets one merged report (*combined*). Subfolders are included by default.
- **Download by package name** — fetches APKs from a public mirror and analyses them as they
  arrive. Separate several package names with commas or new lines.

Pick the target (HarmonyOS NEXT or HMS Core) and press **Start**.

**Progress** — live stages, per-file results and, for a batch, the two summary workbooks.
A run can be cancelled; closing or reloading the window does not stop it.

**Results** — every past run and app. Click a row to open its report; the Excel button opens
its workbook. Rows can be deleted one by one (× twice), several at once, or all together.

The interface is available in English, Türkçe and 中文, with light, dark or system theme.

## Where the outputs are

```
engine/result/
  <app>_<type>_<target>_report.html    one report per app
  <app>_<type>_<target>_report.xlsx    its workbook
  batch_summary.xlsx                   cross-app summary of the last batch
  batch_unmapped.xlsx                  unmapped namespaces per app (APK batches)
engine/input/                          APKs downloaded by package name
```

The report opens in any browser and works offline; its *Excel* button hands over the same
workbook that sits beside it.
