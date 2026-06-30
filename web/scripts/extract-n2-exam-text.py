#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 N2 历年真题 PDF 提取文本（可复制文本优先，扫描件用 EasyOCR），写入缓存。"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import fitz

ROOT_CANDIDATES = list(Path(r"E:/BaiduNetdiskDownload").glob("N2*1991*"))
EXAM_ROOT = ROOT_CANDIDATES[0] if ROOT_CANDIDATES else None
CACHE_DIR = Path(__file__).resolve().parent / "_n2_exam_cache"
INDEX_FILE = CACHE_DIR / "index.json"

SKIP_NAME = (
    "解析", "答案", "听力原文", "解说", "解答", "讲解", "记解", "高清扫描",
    "沪江", "网校", "记解", "阅读", "语法", "听力音频",
)
MIN_JP_PER_PAGE = 40


def exam_id_from_path(p: Path) -> str:
    for text in (p.name, p.stem):
        m = re.search(r"(20\d{2})[\.\年](\d{1,2})", text)
        if m:
            return f"{m.group(1)}.{int(m.group(2)):02d}"
        m = re.search(r"(20\d{2})(\d{2})", text)  # 201007
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


def extract_text_native(doc: fitz.Document) -> str:
    return "".join(page.get_text() for page in doc)


def extract_text_ocr(doc: fitz.Document, reader) -> str:
    parts: list[str] = []
    for i in range(doc.page_count):
        page = doc[i]
        native = page.get_text()
        if len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", native)) >= MIN_JP_PER_PAGE:
            parts.append(native)
            continue
        pix = page.get_pixmap(matrix=fitz.Matrix(1.8, 1.8))
        img = pix.tobytes("png")
        import tempfile

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp.write(img)
            tmp_path = tmp.name
        try:
            lines = reader.readtext(tmp_path, detail=0, paragraph=True)
            parts.append("\n".join(lines))
        finally:
            Path(tmp_path).unlink(missing_ok=True)
    return "\n".join(parts)


def should_skip(p: Path) -> bool:
    n = p.name
    if "词汇" in n and "解析" in str(p.parent):
        return False  # 保留词汇解析卷
    return any(k in n for k in SKIP_NAME) or any(k in str(p.parent) for k in ("阅读", "语法") if "词汇" not in n)


def main() -> None:
    native_only = "--native-only" in sys.argv or "-n" in sys.argv
    full_ocr = "--full" in sys.argv
    if not native_only and not full_ocr:
        native_only = True  # 默认仅提取可复制文本，避免误跑 OCR
    if not EXAM_ROOT or not EXAM_ROOT.exists():
        print("未找到真题目录 E:/BaiduNetdiskDownload/N2历年真题合集1991-2025", file=sys.stderr)
        sys.exit(1)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    index: dict = {}
    if INDEX_FILE.exists():
        index = json.loads(INDEX_FILE.read_text(encoding="utf-8"))

    pdfs = sorted(p for p in EXAM_ROOT.rglob("*.pdf") if not should_skip(p))
    print(f"[extract] {len(pdfs)} 个 PDF，缓存目录 {CACHE_DIR}")

    reader = None
    for i, pdf in enumerate(pdfs, 1):
        eid = exam_id_from_path(pdf)
        ph = pdf_hash(pdf)
        entry = index.get(str(pdf))
        if entry and entry.get("hash") == ph and (CACHE_DIR / entry["file"]).exists():
            continue

        print(f"  [{i}/{len(pdfs)}] {eid} {pdf.name[:50]}…")
        doc = fitz.open(pdf)
        text = extract_text_native(doc)
        jp = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", text))
        if jp < 800 and full_ocr:
            if reader is None:
                import easyocr

                print("    初始化 EasyOCR（首次较慢）…")
                reader = easyocr.Reader(["ja", "en"], gpu=False)
            print(f"    文本过少({jp})，OCR {doc.page_count} 页…")
            text = extract_text_ocr(doc, reader)
            jp = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", text))
        elif jp < 800 and native_only:
            print(f"    文本过少({jp})，跳过（用 --full 开启 OCR）")
        doc.close()

        out_name = f"{ph}_{eid.replace('.', '-')}.txt"
        (CACHE_DIR / out_name).write_text(text, encoding="utf-8")
        index[str(pdf)] = {
            "hash": ph,
            "file": out_name,
            "exam_id": eid,
            "jp_chars": jp,
            "name": pdf.name,
        }
        INDEX_FILE.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"    → {jp} 日文假名/汉字")

    print(f"[extract] 完成，共缓存 {len(index)} 份")
    if native_only:
        print("提示：扫描版试卷需运行 python extract-n2-exam-text.py --full 进行 OCR（耗时较长）")


if __name__ == "__main__":
    main()
