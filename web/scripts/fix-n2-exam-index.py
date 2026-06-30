#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import json
import re
from pathlib import Path

import fitz

SCRIPTS = Path(__file__).resolve().parent
CACHE = SCRIPTS / "_n2_exam_cache"
INDEX = CACHE / "index.json"
ROOT = next(p for p in Path(r"E:/BaiduNetdiskDownload").iterdir() if "N2" in p.name and "1991" in p.name)


def exam_id(p: Path) -> str:
    for text in (p.name, p.stem):
        m = re.search(r"(20\d{2})[\.\年](\d{1,2})", text)
        if m:
            return f"{m.group(1)}.{int(m.group(2)):02d}"
    m = re.search(r"(19\d{2})", p.name)
    if m:
        return m.group(1)
    return p.stem[:24]


def pdf_hash(p: Path) -> str:
    h = hashlib.md5()
    h.update(str(p.stat().st_mtime).encode())
    h.update(str(p.stat().st_size).encode())
    return h.hexdigest()[:12]


def main() -> None:
    index = json.loads(INDEX.read_text(encoding="utf-8")) if INDEX.exists() else {}
    for path, meta in list(index.items()):
        meta["exam_id"] = exam_id(Path(path))

    for pdf in ROOT.rglob("*.pdf"):
        if any(k in pdf.name for k in ("解析", "解说", "讲解", "沪江", "网校")):
            continue
        if "答案" in pdf.name and "真题" not in pdf.name:
            continue
        if str(pdf) in index and index[str(pdf)].get("jp_chars", 0) >= 800:
            continue
        doc = fitz.open(pdf)
        text = "".join(page.get_text() for page in doc)
        doc.close()
        jp = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", text))
        if jp < 800:
            continue
        h = pdf_hash(pdf)
        e = exam_id(pdf)
        fn = f"{h}_{e.replace('.', '-')}.txt"
        (CACHE / fn).write_text(text, encoding="utf-8")
        index[str(pdf)] = {"hash": h, "file": fn, "exam_id": e, "jp_chars": jp, "name": pdf.name}
        print(f"added {e} jp={jp} {pdf.name[:40]}")

    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    good = sorted({v["exam_id"] for v in index.values() if v.get("jp_chars", 0) >= 800})
    print("usable exams:", good)


if __name__ == "__main__":
    main()
