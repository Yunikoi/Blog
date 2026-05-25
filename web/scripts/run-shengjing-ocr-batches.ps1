# 分批 OCR《雅思词汇胜经》，每批 40 页，跑完合并 markdown
$ErrorActionPreference = "Stop"
$root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
Set-Location $root
$py = "python"
$pdfCheck = & $py -c "from pathlib import Path; p=Path(r'e:/BaiduNetdiskDownload'); fs=sorted(p.glob('2.0*胜经*.pdf')); f=next((x for x in fs if '(1)' not in x.name), fs[0] if fs else None); print(f or '')"
if (-not $pdfCheck) {
    Write-Error "找不到 PDF: e:\BaiduNetdiskDownload\2.0*胜经*.pdf"
    exit 1
}
$env:SHENGJING_PDF = $pdfCheck.Trim()
Write-Host "PDF: $($env:SHENGJING_PDF)" -ForegroundColor Green
$py = "python"
$script = "web\scripts\build-shengjing-vocab.py"
$batch = 40
$total = 407
for ($from = 0; $from -lt $total; $from += $batch) {
    $to = [Math]::Min($from + $batch, $total)
    Write-Host "=== OCR pages $from .. $to ===" -ForegroundColor Cyan
    & $py -u $script --no-copy --from $from --to $to --ocr-only
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
Write-Host "=== merge markdown ===" -ForegroundColor Green
& $py "web\scripts\build-shengjing-from-cache.py"
