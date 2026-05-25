@echo off
chcp 65001 >nul
cd /d "%~dp0..\.."
set SHENGJING_PDF=E:\BaiduNetdiskDownload\2.0 雅思词汇胜经.pdf
echo === 2.0 雅思词汇胜经 全书 OCR ===
echo PDF: %SHENGJING_PDF%
python -u web\scripts\build-shengjing-vocab.py --no-copy --from 0 --to -1 --ocr-only
if errorlevel 1 exit /b 1
python -u web\scripts\build-shengjing-from-cache.py
echo === 完成 ===
pause
