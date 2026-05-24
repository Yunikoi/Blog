# -*- coding: utf-8 -*-
"""从 ZXZ 阅读 PDF 为 Yasi 词条补充例句，生成 Yasi-ZXZ-阅读例句.md（不含词根/衍生批量块）。"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import fitz
except ImportError:
    print("需要 pymupdf: pip install pymupdf", file=sys.stderr)
    sys.exit(1)

PDF_DIR = Path(r"D:\Study\英语\雅思\ZXZ阅读")
SRC = Path(__file__).resolve().parents[2] / "content" / "posts" / "Yasi.md"
OUT = Path(__file__).resolve().parents[2] / "content" / "posts" / "Yasi-ZXZ-阅读例句.md"

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")


def load_corpus() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        doc = fitz.open(pdf)
        parts: list[str] = []
        for page in doc:
            parts.append(page.get_text())
        doc.close()
        text = re.sub(r"\s+", " ", " ".join(parts))
        out.append((pdf.name, text))
    return out


def term_from_heading(line: str) -> str | None:
    m = re.match(r"^####\s+(.+)$", line.strip())
    if not m:
        return None
    body = m.group(1).strip()
    for sep in ("：", ":"):
        if sep in body:
            return body.split(sep, 1)[0].strip()
    return body


def word_pattern(term: str) -> re.Pattern[str]:
    t = re.escape(term.strip())
    if " " in term:
        return re.compile(t, re.IGNORECASE)
    return re.compile(rf"\b{t}\b", re.IGNORECASE)


def find_sentences(term: str, corpus: list[tuple[str, str]], max_per_pdf: int = 1, max_total: int = 3) -> list[tuple[str, str]]:
    patterns = [word_pattern(term)]
    if " " not in term and not term.endswith("s"):
        patterns.append(word_pattern(term + "s"))

    found: list[tuple[str, str]] = []
    seen: set[str] = set()
    for pdf_name, text in corpus:
        count = 0
        for raw in SENT_SPLIT.split(text):
            s = raw.strip()
            if len(s) < 20 or len(s) > 600 or s in seen:
                continue
            if any(p.search(s) for p in patterns):
                found.append((pdf_name, s))
                seen.add(s)
                count += 1
                if count >= max_per_pdf:
                    break
        if len(found) >= max_total:
            break
    return found[:max_total]


def enrich_content(lines: list[str], corpus: list[tuple[str, str]]) -> tuple[list[str], int]:
    out: list[str] = []
    i = 0
    matched = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        term = term_from_heading(line)
        if term:
            hits = find_sentences(term, corpus)
            if hits:
                matched += 1
                out.append("")
                out.append("> ##### ZXZ 阅读例句")
                for pdf_name, sent in hits:
                    short = pdf_name.replace(".pdf", "")
                    out.append(">")
                    out.append(f"> - **{short}**：{sent}")
                out.append("")
        i += 1
    return out, matched


def main() -> None:
    if not PDF_DIR.is_dir():
        print(f"PDF 目录不存在: {PDF_DIR}", file=sys.stderr)
        sys.exit(1)
    if not SRC.is_file():
        print(f"源文件不存在: {SRC}", file=sys.stderr)
        sys.exit(1)

    corpus = load_corpus()
    print(f"已加载 {len(corpus)} 个 PDF")

    raw = SRC.read_text(encoding="utf-8")
    lines = raw.splitlines()
    new_lines: list[str] = []
    for line in lines:
        if line.startswith("title:"):
            new_lines.append("title: Yasi-ZXZ 阅读例句")
        elif line.startswith("date:"):
            new_lines.append("date: 2026-05-22")
        else:
            new_lines.append(line)

    intro = [
        "",
        "> 本文件由 `Yasi.md` 复制生成，并与 `D:\\Study\\英语\\雅思\\ZXZ阅读` 下 PDF 对照：在原文中找到该词的，在词条下补充 **ZXZ 阅读例句**（摘自对应 PDF 正文）。",
        "",
    ]
    body, matched = enrich_content(new_lines, corpus)
    out_lines: list[str] = []
    inserted = False
    for line in body:
        if not inserted and line.startswith("## "):
            out_lines.extend(intro)
            inserted = True
        out_lines.append(line)
    if not inserted:
        out_lines = body + intro

    OUT.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"匹配到例句的词条: {matched}")
    print(f"已写入: {OUT}")


if __name__ == "__main__":
    main()
