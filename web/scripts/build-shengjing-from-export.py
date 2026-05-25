# -*- coding: utf-8 -*-
"""从《雅思词汇胜经》词表 list + 释义 CSV 生成 雅思词汇胜经.md（与 2.0 PDF 同书 Word List）"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "web" / "data" / "shengjing-source"
LIST_FILE = SRC / "list.txt"
CSV_FILE = SRC / "translations.csv"
OUT = ROOT / "content" / "posts" / "雅思词汇胜经.md"
PDF_NOTE = r"E:\BaiduNetdiskDownload\2.0 雅思词汇胜经.pdf"

HEADER_RE = re.compile(r"#(6分词汇|7分词汇)\s*Word\s*List\s*(\d+)", re.I)


def load_translations() -> dict[str, str]:
    trans: dict[str, str] = {}
    with CSV_FILE.open(encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if not row or not row[0].strip():
                continue
            word = row[0].strip().lower()
            defn = (row[1] if len(row) > 1 else "").strip().replace("\n", "；")
            if word and defn:
                trans[word] = defn
    return trans


def guess_derivatives(word: str) -> str:
    w = word.lower()
    hints: list[str] = []
    if w.endswith("ive"):
        hints.append(f"{w[:-3]}ion n. …")
    elif w.endswith("al") and len(w) > 4:
        hints.append(f"{w}ly adv. …地")
    elif w.endswith("ion"):
        hints.append(f"{w[:-3]}e v. …")
    elif w.endswith("ly"):
        hints.append(f"{w[:-2]} adj. …")
    return " | ".join(hints[:2])


def build() -> str:
    trans = load_translations()
    lines_in = LIST_FILE.read_text(encoding="utf-8").splitlines()
    out: list[str] = [
        "---",
        "title: 雅思词汇胜经",
        "toc: true",
        "date: 2026-05-22",
        "tags: 学习",
        "column: 学习笔记",
        "---",
        "",
        f"> 来源：《2.0 雅思词汇胜经》（`{PDF_NOTE}`）全书 6 分 / 7 分 Word List + 释义。",
        "> 与纸质/PDF 版词序一致；若你本机 PDF 已就绪，可用 `web/scripts/run-shengjing-full.cmd` 重新 OCR 校对释义。",
        "",
    ]
    section = "6分词汇"
    list_no = 0
    seen: set[str] = set()
    count = 0

    def ensure_section():
        nonlocal out
        if not out or out[-1] != f"## {section}":
            out.append(f"## {section}")
            out.append("")

    for raw in lines_in:
        line = raw.strip()
        if not line:
            continue
        hm = HEADER_RE.match(line)
        if hm:
            section = hm.group(1)
            list_no = int(hm.group(2))
            ensure_section()
            out.append(f"### Word List {list_no}")
            out.append("")
            continue
        word = line.lower()
        if not re.match(r"^[a-z][a-z'-]*$", word):
            continue
        key = f"{section}:{word}"
        if key in seen:
            continue
        seen.add(key)
        defn = trans.get(word, "见原书词条")
        defn = defn.replace('"', "'")[:200]
        out.append(f"#### {word}：{defn}")
        hint = guess_derivatives(word)
        if hint:
            out.append("")
            out.append(f"> {hint}")
        out.append("")
        count += 1

    print(f"词条 {count}", flush=True)
    return "\n".join(out) + "\n"


def main() -> None:
    if not LIST_FILE.is_file() or not CSV_FILE.is_file():
        print(f"缺少数据文件，请先放到:\n  {LIST_FILE}\n  {CSV_FILE}", file=sys.stderr)
        sys.exit(1)
    md = build()
    OUT.write_text(md, encoding="utf-8")
    print(f"→ {OUT} ({md.count('#### ')} 条)", flush=True)


if __name__ == "__main__":
    main()
