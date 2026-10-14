@echo off
setlocal
cd /d "%~dp0"
echo ==================================================================
echo  GEV corpus - build the insight cards NOW on what is already there
echo  (safe to run while an overnight job is going; the GPU is shared)
echo ==================================================================
echo.
echo [1/4] syntax check
python -c "import ast,glob; [ast.parse(open(f,encoding='utf-8').read(),f) for f in glob.glob('src/*.py')]; print('   ok')" || ( echo SYNTAX ERROR - fix before continuing & exit /b 1 )

echo.
echo [2/4] derived tables: forward-flag backfill, guidance revisions, comps, XBRL backlog spine, catalysts
python src\derive.py || exit /b 1

echo.
echo [3/4] insight cards - 16 hypotheses, both sides of the evidence, falsification condition each
echo       (~2-4 min per card on the 5060; ~45 min total. Ctrl-C keeps what is done.)
python src\thesis.py --limit 16 %*

echo.
echo [4/4] summary
python src\ask.py insights
echo.
echo Full cards:  data\INSIGHTS.md
echo Also try:    python src\ask.py comps      python src\ask.py generators      python src\ask.py backlog
echo              python src\embed.py --search "your question" --all -k 10
endlocal
