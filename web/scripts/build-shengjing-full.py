# -*- coding: utf-8 -*-
"""从《2.0 雅思词汇胜经》词序 + 释义生成 content/posts/雅思词汇胜经.md（格式同 Yasi.md）"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PDF_GLOB = Path(r"e:/BaiduNetdiskDownload")
LIST_URL_NAME = "2018雅思词汇胜经"  # 与 2.0 胜经同书 Word List
DATA = ROOT / "web" / "data" / "shengjing-source"
LIST_FILE = DATA / "word-list.txt"
CSV_FILE = DATA / "translations.csv"
OUT = ROOT / "content" / "posts" / "雅思词汇胜经.md"

HEAD_RE = re.compile(r"^#?\s*(6分词汇|7分词汇)\s*Word\s*List\s*(\d+)\s*$", re.I)
WORD_RE = re.compile(r"^[a-z][a-z'-]{1,39}$")


def find_pdf() -> Path | None:
    if not PDF_GLOB.is_dir():
        return None
    cands = sorted(PDF_GLOB.glob("2.0*胜经*.pdf"), key=lambda p: len(p.name))
    for p in cands:
        if "(1)" not in p.name and p.is_file():
            return p
    for p in PDF_GLOB.glob("2.0*胜经*.pdf"):
        if p.is_file():
            return p
    return None


def load_translations() -> dict[str, str]:
    trans: dict[str, str] = {}
    if not CSV_FILE.is_file():
        return trans
    with CSV_FILE.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            word = row[0].strip().lower()
            if not word or word in trans:
                continue
            defn = row[1].strip().replace("\n", "；") if len(row) > 1 else ""
            trans[word] = defn[:200] if defn else "见原书"
    return trans


def guess_derivatives(word: str) -> str:
    w = word.lower()
    bits: list[str] = []
    if w.endswith("ive"):
        bits.append(f"{w[:-3]}ion n. …")
    elif w.endswith("al") and len(w) > 4:
        bits.append(f"{w}ly adv. …地")
    elif w.endswith("tion") and len(w) > 5:
        bits.append(f"{w[:-4]}t v. …")
    elif w.endswith("ion") and len(w) > 4:
        bits.append(f"{w[:-3]} v. …")
    elif w.endswith("ly"):
        bits.append(f"{w[:-2]} adj. …")
    return " | ".join(bits[:2])


def main() -> None:
    if not LIST_FILE.is_file():
        print(f"缺少 {LIST_FILE}", file=sys.stderr)
        sys.exit(1)

    pdf = find_pdf()
    pdf_note = str(pdf) if pdf else r"e:\BaiduNetdiskDownload\2.0 雅思词汇胜经.pdf"
    trans = load_translations()

    lines_out: list[str] = [
        "---",
        "title: 雅思词汇胜经",
        "toc: true",
        "date: 2026-05-22",
        "tags: 学习",
        "column: 学习笔记",
        "---",
        "",
        f"> 来源：《2.0 雅思词汇胜经》· 6分/7分 Word List（与 `{pdf_note}` 同书）。",
        "",
    ]

    section = ""
    last_list = ""
    seen: set[str] = set()
    count = 0

    for raw in LIST_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        hm = HEAD_RE.match(line) or re.match(
            r"^#?\s*(6分词汇|7分词汇)\s*Word\s*List\s*(\d+)", line, re.I
        )
        if hm:
            sec, wl = hm.group(1), hm.group(2)
            if sec != section:
                section = sec
                lines_out.append(f"## {section}")
                lines_out.append("")
            if wl != last_list:
                last_list = wl
                lines_out.append(f"### Word List {wl}")
                lines_out.append("")
            continue

        word = line.lower().strip()
        if not WORD_RE.match(word):
            continue
        key = f"{section}:{word}"
        if key in seen:
            continue
        seen.add(key)
        defn = trans.get(word, "见原书词条")
        lines_out.append(f"#### {word}：{defn}")
        deriv = guess_derivatives(word)
        if deriv:
            lines_out.append("")
            lines_out.append(f"> {deriv}")
        lines_out.append("")
        count += 1

    OUT.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(f"词条 {count} → {OUT}", flush=True)


if __name__ == "__main__":
    main()
