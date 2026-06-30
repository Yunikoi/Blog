#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计 N2 词汇在历年真题中的出现次数，并生成按真题考频排序的 Markdown。"""
from __future__ import annotations

import csv
import json
import re
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
OUT = ROOT / "content" / "posts" / "JLPT-N2词汇考频总表.md"
CACHE_DIR = SCRIPTS / "_n2_exam_cache"
INDEX_FILE = CACHE_DIR / "index.json"
FREQ_JSON = SCRIPTS / "_n2_freq.json"
CSV_PATH = SCRIPTS / "_n2_jamsin.csv"
CACHE_FILE = SCRIPTS / "_n2_meaning_zh_cache.json"

# 听力稿常见短语，不计入词汇题统计
STOP_EXPR = {
    "する", "なる", "女の人", "男の人", "お願いします", "お願い", "質問", "問題", "番号",
    "正しい", "間違い", "選択", "答え", "例", "次", "以下", "以上",
}

LISTENING_HINTS = {
    "案内", "伝える", "連絡", "確認", "予約", "届く", "遅れる", "割引", "点検", "故障",
    "相談", "説明", "紹介", "乗り換え", "遅延", "欠席", "出席", "延期", "中止", "変更",
    "届ける", "配達", "受付", "申し込む", "送料", "返品", "交換", "領収書", "症状", "診察",
    "会議", "資料", "締め切り", "提出", "報告", "満席", "空席", "キャンセル", "定員",
    "お知らせ", "通知", "掲示", "振込", "口座", "発送", "配送", "手続き", "営業時間", "定休日",
}

_trans_cache: dict[str, str] = {}


def load_trans_cache() -> None:
    global _trans_cache
    if CACHE_FILE.exists():
        _trans_cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))


def save_trans_cache() -> None:
    CACHE_FILE.write_text(json.dumps(_trans_cache, ensure_ascii=False, indent=0), encoding="utf-8")


def clean_meaning(en: str) -> str:
    return re.sub(r"\s+", " ", en.strip().strip('"'))


def en_to_zh(en: str) -> str:
    if not en:
        return "（释义待补）"
    if en in _trans_cache:
        return _trans_cache[en]
    # 离线优先：保留英文释义，避免批量联网翻译卡住
    zh = en.replace(",", "；").replace(" to ", "；").strip()
    _trans_cache[en] = zh
    return zh


def load_freq() -> dict[tuple[str, str], int]:
    if not FREQ_JSON.exists():
        return {}
    data = json.loads(FREQ_JSON.read_text(encoding="utf-8"))
    start = next(i for i, row in enumerate(data) if row[0] == "N2")
    out: dict[tuple[str, str], int] = {}
    rank = 0
    for row in data[start + 1 :]:
        if len(row) != 2 or row[0] in ("N1", "N2", "N3", "N4", "N5"):
            continue
        out[(row[0], row[1])] = rank
        rank += 1
    return out


def load_csv() -> list[dict]:
    rows: list[dict] = []
    with CSV_PATH.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if "JLPT_2" in r.get("tags", ""):
                rows.append(r)
    return rows


def load_exam_corpus() -> list[dict]:
    """返回 [{exam_id, text, source}]；仅保留日文文本充足的考次。"""
    if not INDEX_FILE.exists():
        return []
    index = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    by_exam: dict[str, dict] = {}
    for _path, meta in index.items():
        if meta.get("jp_chars", 0) < 800:
            continue
        eid = meta.get("exam_id", "?")
        f = CACHE_DIR / meta["file"]
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        if eid not in by_exam or meta.get("jp_chars", 0) > by_exam[eid].get("jp_chars", 0):
            by_exam[eid] = {
                "exam_id": eid,
                "text": text,
                "source": meta.get("name", ""),
                "jp_chars": meta.get("jp_chars", 0),
            }
    return sorted(by_exam.values(), key=lambda x: x["exam_id"])


def word_in_text(expr: str, reading: str, text: str) -> int:
    """返回出现次数（0=未出现）。单字汉字易误匹配，仅计读音。"""
    count = 0
    if expr and len(expr) >= 2:
        count += len(re.findall(re.escape(expr), text))
    if reading and len(reading) >= 2:
        pat = r"(?<![ぁ-んァ-ヶ一-龥ー])" + re.escape(reading) + r"(?![ぁ-んァ-ヶ一-龥ー])"
        count += len(re.findall(pat, text))
    return count


def exam_tier(exam_count: int) -> str:
    if exam_count >= 5:
        return "S"
    if exam_count >= 3:
        return "A"
    if exam_count == 2:
        return "B"
    if exam_count == 1:
        return "C"
    return "D"


def tier_label(t: str) -> str:
    return {
        "S": "S级·真题5次及以上",
        "A": "A级·真题3–4次",
        "B": "B级·真题2次",
        "C": "C级·真题1次",
        "D": "D级·未在本库真题文本中出现",
    }[t]


def is_listening(expr: str, meaning_en: str) -> bool:
    if expr in LISTENING_HINTS:
        return True
    keys = ("announce", "reserv", "deliver", "contact", "guide", "delay", "cancel", "receipt", "symptom")
    return any(k in meaning_en.lower() for k in keys)


def main() -> None:
    load_trans_cache()
    corpus = load_exam_corpus()
    exam_ids = [c["exam_id"] for c in corpus]
    print(f"[build] 真题语料 {len(corpus)} 套（来自 {len(exam_ids)} 个考次）")

    freq = load_freq()
    merged: dict[str, dict] = {}
    for r in load_csv():
        expr = r["expression"]
        if expr not in merged:
            merged[expr] = {
                "expr": expr,
                "reading": r["reading"],
                "meaning_en": clean_meaning(r["meaning"]),
                "rank": freq.get((r["expression"], r["reading"])),
            }

    # 真题统计
    for expr, it in merged.items():
        if expr in STOP_EXPR:
            it["exam_count"] = 0
            it["occurrence"] = 0
            it["exam_sessions"] = []
            continue
        sessions: list[str] = []
        total = 0
        for c in corpus:
            n = word_in_text(expr, it["reading"], c["text"])
            if n > 0:
                sessions.append(c["exam_id"])
                total += n
        it["exam_count"] = len(sessions)
        it["occurrence"] = total
        it["exam_sessions"] = sessions

    items = list(merged.values())
    items.sort(
        key=lambda x: (
            -x["exam_count"],
            -x["occurrence"],
            x["rank"] is None,
            x["rank"] if x["rank"] is not None else 99999,
            x["expr"],
        )
    )

    # 翻译（仅未缓存）
    for en in sorted({it["meaning_en"] for it in items if it["meaning_en"]}):
        if en not in _trans_cache:
            en_to_zh(en)
    save_trans_cache()

    for it in items:
        it["meaning_zh"] = en_to_zh(it["meaning_en"]) if it["meaning_en"] else "（释义待补）"
        it["tier"] = exam_tier(it["exam_count"])
        it["listen"] = is_listening(it["expr"], it["meaning_en"])

    exam_range = f"{min(exam_ids)}–{max(exam_ids)}" if exam_ids else "—"
    appeared = sum(1 for it in items if it["exam_count"] > 0)

    lines: list[str] = [
        "---",
        "title: JLPT N2 词汇考频总表（真题统计·文字词汇·听力）",
        "date: 2026-06-28",
        "tags: 学习/日语/JLPT/N2",
        "column: 学习笔记",
        "toc: true",
        "---",
        "",
        "# JLPT N2 词汇考频总表（真题优先）",
        "",
        f"> **语料**：本地 `N2历年真题合集1991-2025` 中提取文本，当前覆盖 **{len(corpus)}** 套考次（{exam_range}）。",
        f"> **词条**：tanos / open-anki **N2 词表** 共 **{len(items)}** 词；其中 **{appeared}** 词在已提取真题中出现。",
        "> **排序**：先按 **真题出现套数**（考过几套卷）降序，再按卷内 **出现次数** 降序；未出现者排最后（按通用频率序）。",
        "> **说明**：2010 年后大量试卷为扫描版，需 OCR 补全；运行 `web/scripts/extract-n2-exam-text.py` 可增量更新缓存。",
        "",
        "## 考频分级（按真题套数）",
        "",
        "| 级别 | 真题出现套数 | 建议 |",
        "|------|-------------|------|",
        "| **S** | ≥5 套 | 必背，反复考到 |",
        "| **A** | 3–4 套 | 高频真题词 |",
        "| **B** | 2 套 | 中频，重点复习 |",
        "| **C** | 1 套 | 考过，需认识 |",
        "| **D** | 0 套（本库未检出） | 词表覆盖，考前浏览 |",
        "",
    ]

    current_tier = ""
    for it in items:
        if it["tier"] != current_tier:
            current_tier = it["tier"]
            lines += ["", f"## {tier_label(current_tier)}", ""]
        listen_tag = " [听力]" if it["listen"] else ""
        ec = it["exam_count"]
        oc = it["occurrence"]
        sessions = it["exam_sessions"]
        sess_s = "、".join(sessions[:8]) + ("…" if len(sessions) > 8 else "")
        lines.append(f"#### {it['expr']}{listen_tag}：{it['meaning_zh']}")
        lines.append("")
        exam_part = f"真题 **{ec}** 套" if ec else "真题 **0** 套"
        if ec:
            exam_part += f"（共 **{oc}** 次"
            if sess_s:
                exam_part += f"｜{sess_s}"
            exam_part += "）"
        rank_s = f"#{it['rank'] + 1}" if it["rank"] is not None else "—"
        lines.append(
            f"> 読み {it['reading']} · {exam_part} · 词表序 {rank_s}"
            + (f" · 英：{it['meaning_en']}" if it["meaning_en"] else "")
        )
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[build] → {OUT}")
    print(f"  真题命中 {appeared}/{len(items)}，S级 {sum(1 for i in items if i['tier']=='S')} 词")


if __name__ == "__main__":
    main()
