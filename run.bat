@echo off
REM Migration Analyzer v2 -- desktop app.
REM The v1 CLI is still here and still supported:  python engine\analyzer.py <file>
cd /d "%~dp0"
python -m app %*
pause
