@echo off
setlocal
cd /d "%~dp0"
echo ==================================================================
echo  GEV corpus - night 2:  repairs -^> checks -^> overnight run
echo ==================================================================
echo.

echo [1/6] packages for spreadsheets and PDF fallback
pip install -q openpyxl pdfplumber pyxlsb xlrd || ( echo pip failed & exit /b 1 )

echo.
echo [2/6] syntax check every module
python -c "import ast,glob,sys; [ast.parse(open(f,encoding='utf-8').read(),f) for f in glob.glob('src/*.py')]; print('   all modules parse')" || ( echo SYNTAX ERROR - stop & exit /b 1 )

echo.
echo [3/6] import check (schema migrations run here)
python -c "import sys; sys.path.insert(0,'src'); import common, extract, build_index, embed, ingest_web, ingest_primary, ingest_tabular, thesis, repair, overnight; con=common.connect(); print('   imports + schema OK,', con.execute('SELECT COUNT(*) FROM chunks').fetchone()[0], 'chunks'); con.close()" || ( echo IMPORT ERROR - stop & exit /b 1 )

echo.
echo [4/6] repair - check, then apply
python src\repair.py --check || exit /b 1
python src\repair.py || ( echo REPAIR FAILED - stop & exit /b 1 )

echo.
echo [5/6] probe the new sources (no downloads)
python src\ingest_tabular.py --check
python src\ingest_primary.py --check --only ir operators

echo.
echo [6/6] launch the overnight run (9h, detached)
powershell -NoProfile -Command "$p = Start-Process -FilePath python -ArgumentList 'overnight.py','--hours','9' -WorkingDirectory 'src' -RedirectStandardOutput 'data\overnight.log' -RedirectStandardError 'data\overnight.err' -WindowStyle Hidden -PassThru; Start-Sleep 8; Write-Host ('   launched pid ' + $p.Id + ', alive: ' + (-not $p.HasExited))"
echo.
echo Done. Morning: night-status.cmd, then data\NIGHT_REPORT.md and data\INSIGHTS.md
endlocal
