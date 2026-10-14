@echo off
cd /d "%~dp0"
if not exist "data\overnight.pid" ( echo not running & exit /b 0 )
set /p PID=<"data\overnight.pid"
echo stopping pid %PID% gracefully (finishes current chunk, writes report)...
taskkill /PID %PID% >nul 2>&1
timeout /t 20 /nobreak >nul
tasklist /FI "PID eq %PID%" | find "%PID%" >nul && ( echo still running - forcing & taskkill /F /PID %PID% ) || echo stopped
