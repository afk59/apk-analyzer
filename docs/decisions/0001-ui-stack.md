# 0001 — UI stack: pywebview + FastAPI + hand-written frontend

**Date:** 2026-08-28 · **Status:** accepted · **Decided by:** maintainer

## Context

v1 is a CLI with an arrow-key TUI. v2 needs file and folder pickers, live progress, a results
library, and clicking a result to open its HTML or Excel. The analysis engine is Python
(androguard) and cannot move. The target machines are corporate Windows behind XGATE, where
installing a toolchain is the expensive part — v1's whole deployment story is `run.bat` plus a
first-run `pip install`.

## Decision

A pywebview desktop window over a local FastAPI server, with a hand-written HTML/CSS/JS frontend.
No Node, no npm, no build step.

## Why not the others

- **Electron / Tauri** gives the best-looking result and the richest ecosystem, but adds a Node
  toolchain, a build pipeline and Python-as-a-sidecar packaging. Behind XGATE, `npm install` is
  the single most likely thing to fail on a machine we do not control, and it would replace a
  one-double-click deployment with a build artefact.
- **PySide6 / Qt** is a real native app in one `pip install` and would be a defensible choice.
  Rejected because a modern, designed UI costs meaningfully more in QSS than in CSS, and because
  the team already writes the report's CSS — the same skill and the same visual language.
- **Plain local web in the browser** is the cheapest install and fails the requirements outright:
  `<input type="file">` never yields a real path, there is no folder picker, and a page cannot
  ask the OS to open a local workbook. Two of the three UI requirements would be unmet.

## Consequences

- Native file/folder dialogs come from the Python side (pywebview's, or `tkinter.filedialog` as a
  stdlib fallback) and return real absolute paths.
- `os.startfile()` opens reports and workbooks in whatever the user has associated. This is the
  capability that made a local app necessary, so it must stay guarded: only paths inside the
  result tree may be opened, checked server-side.
- Windows 11 ships Edge WebView2, so pywebview has a renderer with no extra install. If it is
  missing, fall back to opening the default browser and say so rather than failing.
- It will not feel as "app-like" as Electron. Accepted.
