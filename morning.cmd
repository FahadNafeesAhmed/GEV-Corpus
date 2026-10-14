@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"
echo ==================================================================
echo  GEV corpus - status, derived tables, report
echo ==================================================================
echo.
echo [1/3] is a run going?
set RUNNING=0
if exist "data\overnight.pid" (
  set /p PID=<"data\overnight.pid"
  tasklist /FI "PID eq !PID!" 2>nul | find "!PID!" >nul && set RUNNING=1
)
if "!RUNNING!"=="1" (
  echo   RUNNING pid !PID! - derived tables still refresh; the report below is from the LAST finished run
  powershell -NoProfile -Command "Get-Content 'data\overnight.log' -Tail 6"
) else ( echo   no run in progress )

echo.
echo [2/3] derived tables (seconds, no GPU)
python src\derive.py

echo.
echo [2b] write INSIGHTS.md from the cards already in the database (no model calls)
python src\thesis.py --report-only

echo.
echo [3/3] extraction status
python src\extract.py --status

echo.
echo ------------------------------------------------------------------
if exist "data\NIGHT_REPORT.md" ( type "data\NIGHT_REPORT.md" ) else ( echo no NIGHT_REPORT.md yet )
echo ------------------------------------------------------------------
echo.
echo Read next:  data\INSIGHTS.md   (the argument)     data\validation_sample.csv   (your human pass)
echo Explore:    python src\ask.py comps ^| backlog ^| generators ^| insights ^| catalysts ^| search "..."
endlocal
