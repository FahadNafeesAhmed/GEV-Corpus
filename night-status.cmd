@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0src"
echo === overnight process ===
if exist "..\data\overnight.pid" (
  set /p PID=<"..\data\overnight.pid"
  tasklist /FI "PID eq !PID!" 2>nul | find "!PID!" >nul && ( echo   RUNNING pid !PID! ) || ( echo   pid !PID! not running - finished or died )
) else ( echo   no pid file - not running )
echo.
echo === last 12 log lines ===
powershell -NoProfile -Command "Get-Content '..\data\overnight.log' -Tail 12"
echo.
echo === live counts ===
python extract.py --status
echo.
if exist "..\data\NIGHT_REPORT.md" ( echo === NIGHT_REPORT.md exists === ) else ( echo === no report yet === )
endlocal
