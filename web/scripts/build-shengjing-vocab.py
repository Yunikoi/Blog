# -*- coding: utf-8 -*-
"""
从《2.0 雅思词汇胜经》PDF（扫描版）OCR 提取词表 → content/posts/雅思词汇胜经.md
默认 PDF：E:\\BaiduNetdiskDownload\\2.0 雅思词汇胜经.pdf
"""
from __future__ import annotations

import gc
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
PDF_USER = Path(r"E:\BaiduNetdiskDownload\2.0 雅思词汇胜经.pdf")
PDF_LOCAL = ROOT / "web" / "data" / "shengjing.pdf"
OUT = ROOT / "content" / "posts" / "雅思词汇胜经.md"
CACHE_DIR = ROOT / "web" / "data" / "shengjing-ocr"
PROGRESS = CACHE_DIR / "progress.json"

ENTRY_RE = re.compile(
    r"(?:^|\n)\s*([A-Za-z][A-Za-z' -]{0,40}?)\s*\[(?:[^\]\n]|\n){1,80}?\]",
    re.MULTILINE,
)
WORD_LIST_RE = re.compile(r"Word\s*List\s*(\d+)", re.I)
SECTION_RE = re.compile(
    r"6\s*分\s*词\s*汇|7\s*分\s*词\s*汇|6分词汇|7分词汇|#?\s*6\s*分|#?\s*7\s*分",
    re.I,
)
CJK_RE = re.compile(r"[\u4e00-\u9fff]{2,}")
SKIP_WORDS = frozenset(
    {"adj", "n", "v", "vt", "vi", "adv", "prep", "conj", "the", "and", "for"}
)


def resolve_pdf() -> Path:
    import os

    env = os.environ.get("SHENGJING_PDF")
    if env and Path(env).is_file():
        return Path(env)
    if PDF_LOCAL.is_file() and PDF_LOCAL.stat().st_size > 500_000:
        return PDF_LOCAL
    if PDF_USER.is_file():
        return PDF_USER
    return PDF_USER


def ensure_local_pdf() -> Path:
    if PDF_LOCAL.is_file() and PDF_LOCAL.stat().st_size > 500_000:
        return PDF_LOCAL
    src = resolve_pdf()
    if not src.is_file():
        return src
    if src.resolve() == PDF_LOCAL.resolve():
        return src
    PDF_LOCAL.parent.mkdir(parents=True, exist_ok=True)
    print(f"复制 PDF → {PDF_LOCAL} …", flush=True)
    shutil.copyfile(src, PDF_LOCAL)
    print("复制完成", flush=True)
    return PDF_LOCAL


def ocr_tesseract_png(img: Path) -> str | None:
    exe = shutil.which("tesseract")
    if not exe:
        return None
    for lang in ("eng+chi_sim", "eng"):
        try:
            r = subprocess.run(
                [exe, str(img), "stdout", "-l", lang, "--psm", "6"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
                timeout=120,
            )
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout
        except (subprocess.TimeoutExpired, OSError):
            continue
    return None


def ocr_fitz_tesseract(page: fitz.Page) -> str | None:
    try:
        tp = page.get_textpage_ocr(language="eng", dpi=150, full=False)
        t = tp.extractText() or ""
        return t if len(t.strip()) > 20 else None
    except Exception:
        return None


def ocr_page(doc: fitz.Document, i: int, reader) -> str:
    cache = CACHE_DIR / "pages" / f"{i:04d}.txt"
    if cache.is_file():
        return cache.read_text(encoding="utf-8", errors="ignore")

    page = doc[i]
    text = ocr_fitz_tesseract(page)
    img = CACHE_DIR / "_tmp.png"

    if not text:
        pix = page.get_pixmap(matrix=fitz.Matrix(1.15, 1.15))
        pix.save(img)
        del pix
        text = ocr_tesseract_png(img) or ""
        if not text and reader is not None:
            lines = reader.readtext(
                str(img), detail=0, paragraph=True, batch_size=1, width_ths=0.8
            )
            text = "\n".join(lines)
        img.unlink(missing_ok=True)

    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text, encoding="utf-8")
    gc.collect()
    return text


def extract_chinese_snippets(block: str, max_len: int = 120) -> str:
    parts = CJK_RE.findall(block)
    if not parts:
        return ""
    joined = "".join(parts[:10])
    joined = re.sub(r"\s+", "", joined)
    return joined[:max_len]


def guess_derivatives(word: str) -> list[str]:
    w = word.lower().strip()
    out: list[str] = []
    if w.endswith("ive"):
        out.append(f"{w[:-3]}ion n. …")
    elif w.endswith("al") and len(w) > 4:
        out.append(f"{w}ly adv. …地")
    elif w.endswith("ic") and len(w) > 4:
        out.append(f"{w}ally adv. …地")
    elif w.endswith("ion"):
        out.append(f"{w[:-3]}e v. …")
    elif w.endswith("ly"):
        out.append(f"{w[:-2]} adj. …")
    elif w.endswith("ness"):
        out.append(f"{w[:-4]} adj. …")
    elif w.endswith("ment"):
        out.append(f"{w[:-4]} v. …")
    return out[:3]


def parse_entries(text: str) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    matches = list(ENTRY_RE.finditer(text))
    for i, m in enumerate(matches):
        word = m.group(1).strip().lower()
        if len(word) < 2 or word in SKIP_WORDS:
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        cn = extract_chinese_snippets(block)
        en_bits = re.findall(r"[a-z]+\.\s*[^[\n]{8,80}", block[:400], re.I)
        en_hint = en_bits[0][:80] if en_bits else ""
        if cn and en_hint:
            defn = f"{cn}（{en_hint.strip()}）"
        elif cn:
            defn = cn
        elif en_hint:
            defn = en_hint.strip()
        else:
            defn = "见原书词条"
        entries.append((word, defn))
    return entries


def format_entry(word: str, defn: str) -> list[str]:
    lines = [f"#### {word}：{defn}"]
    derivs = guess_derivatives(word)
    if derivs:
        lines.append("")
        lines.append("> " + " | ".join(derivs))
    lines.append("")
    return lines


def build_markdown(pages_data: list[tuple[int, str]], pdf_path: Path) -> str:
    out: list[str] = [
        "---",
        "title: 雅思词汇胜经",
        "toc: true",
        "date: 2026-05-22",
        "tags: 学习",
        "column: 学习笔记",
        "---",
        "",
        f"> 来源：`{pdf_path}`（《2.0 雅思词汇胜经》全书 OCR）。格式同 `Yasi.md`。",
        "",
    ]
    current_section = "6分词汇"
    current_list = 0
    seen: set[str] = set()

    out.append(f"## {current_section}")
    out.append("")

    for _page_idx, text in pages_data:
        wl = WORD_LIST_RE.search(text)
        if wl:
            current_list = int(wl.group(1))
            out.append(f"### Word List {current_list}")
            out.append("")

        sec = SECTION_RE.search(text)
        if sec:
            current_section = "7分词汇" if "7" in sec.group(0) else "6分词汇"
            out.append(f"## {current_section}")
            out.append("")

        for word, defn in parse_entries(text):
            key = f"{current_section}:{word}"
            if key in seen:
                continue
            seen.add(key)
            out.extend(format_entry(word, defn))

    return "\n".join(out) + "\n"


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="page_from", type=int, default=0)
    ap.add_argument("--to", dest="page_to", type=int, default=-1)
    ap.add_argument("--ocr-only", action="store_true")
    ap.add_argument("--no-copy", action="store_true", help="不复制到 web/data，直接用 E 盘 PDF")
    args = ap.parse_args()

    PDF = resolve_pdf() if args.no_copy else ensure_local_pdf()
    if not PDF.is_file():
        print(f"找不到 PDF: {PDF_USER}", file=sys.stderr)
        sys.exit(1)
    print(f"PDF: {PDF} ({PDF.stat().st_size // 1024} KB)", flush=True)

    reader = None
    tess = shutil.which("tesseract")
    if tess:
        print(f"Tesseract: {tess}", flush=True)
    else:
        print("未检测到 Tesseract，将使用 EasyOCR（较慢）", flush=True)
        try:
            import easyocr

            print("加载 EasyOCR…", flush=True)
            reader = easyocr.Reader(["en", "ch_sim"], gpu=False, verbose=False)
        except ImportError:
            print("请安装: pip install easyocr  或安装 Tesseract OCR", file=sys.stderr)
            sys.exit(1)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    total = doc.page_count
    p_end = total if args.page_to < 0 else min(args.page_to, total)
    p_start = max(0, args.page_from)
    prog = {"done": [], "total": total, "pdf": str(PDF)}
    if PROGRESS.is_file():
        prog = json.loads(PROGRESS.read_text(encoding="utf-8"))

    pages_data: list[tuple[int, str]] = []
    for i in range(total):
        cache = CACHE_DIR / "pages" / f"{i:04d}.txt"
        if cache.is_file():
            pages_data.append((i, cache.read_text(encoding="utf-8", errors="ignore")))

    for i in range(p_start, p_end):
        cache = CACHE_DIR / "pages" / f"{i:04d}.txt"
        if cache.is_file():
            continue
        if i % 3 == 0:
            print(f"OCR {i + 1}/{total}", flush=True)
        text = ocr_page(doc, i, reader)
        pages_data.append((i, text))
        if i not in prog.get("done", []):
            prog.setdefault("done", []).append(i)
            PROGRESS.write_text(json.dumps(prog), encoding="utf-8")

    doc.close()
    cached = len(list((CACHE_DIR / "pages").glob("*.txt")))
    print(f"缓存 {cached}/{total} 页", flush=True)
    if args.ocr_only:
        return

    by_page = {p: t for p, t in pages_data}
    pages_data = sorted(by_page.items(), key=lambda x: x[0])
    md = build_markdown(pages_data, PDF)
    OUT.write_text(md, encoding="utf-8")
    print(f"词条 {md.count('#### ')} → {OUT}", flush=True)


if __name__ == "__main__":
    main()
