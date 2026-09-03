@echo off
REM Migration Analyzer v2 -- desktop app. The first run installs what it needs.
REM The v1 CLI is still supported:  python engine\analyzer.py <file>
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
  echo [!] Python was not found.
  echo     Install Python 3.10 or newer from https://www.python.org/downloads/
  echo     and tick "Add python.exe to PATH" in the installer.
  echo.
  pause
  exit /b 1
)

python -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if errorlevel 1 (
  echo [!] This app needs Python 3.10 or newer. Found:
  python --version
  echo.
  pause
  exit /b 1
)

python -m app %*
pause
