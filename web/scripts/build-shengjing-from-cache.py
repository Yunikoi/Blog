# -*- coding: utf-8 -*-
"""仅用已缓存 OCR 页生成 雅思词汇胜经.md（不重新 OCR）"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "b", Path(__file__).parent / "build-shengjing-vocab.py"
)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

CACHE = b.CACHE_DIR / "pages"
pages = []
for f in sorted(CACHE.glob("*.txt")):
    i = int(f.stem)
    pages.append((i, f.read_text(encoding="utf-8", errors="ignore")))

md = b.build_markdown(pages)
b.OUT.write_text(md, encoding="utf-8")
print(f"#### 词条: {md.count('#### ')} → {b.OUT}")
