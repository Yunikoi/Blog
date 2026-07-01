# -*- coding: utf-8 -*-
from pathlib import Path

base = Path(__file__).resolve().parent
parts = [
    base / "_n2_2021_2024_insert.md",
    base / "_n2_2021_2024_part3.md",
    base / "_n2_2021_2024_part4.md",
]
out = "".join(p.read_text(encoding="utf-8") for p in parts if p.exists())
md = base.parent.parent / "content/posts/N2词汇.md"
text = md.read_text(encoding="utf-8")
marker = "\n---\n\n# 2012～2013 年（文字・語彙）"
if marker not in text:
    raise SystemExit("marker not found")
new_text = text.replace(marker, "\n---\n" + out + marker, 1)
md.write_text(new_text, encoding="utf-8")
print(f"inserted {len(out)} chars before 2012 section")
