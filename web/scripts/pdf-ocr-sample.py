# -*- coding: utf-8 -*-
import fitz
import easyocr
from pathlib import Path

p = Path(r"E:\BaiduNetdiskDownload\2.0 雅思词汇胜经.pdf")
doc = fitz.open(p)
reader = easyocr.Reader(["ch_sim", "en"], gpu=False)

for page_no in [15, 20, 30, 50, 80]:
    if page_no >= doc.page_count:
        continue
    page = doc[page_no]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    img_path = Path(__file__).parent / f"_ocr_p{page_no}.png"
    pix.save(img_path)
    result = reader.readtext(str(img_path), detail=0, paragraph=True)
    text = "\n".join(result)
    print(f"\n=== page {page_no + 1} ===\n{text[:2500]}")
    img_path.unlink(missing_ok=True)

doc.close()
