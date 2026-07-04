#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""N2 文字词汇常考词：真题考点 × 考纲词表（_n2_jamsin.csv）交叉分析。"""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
SRC = ROOT / "content" / "posts" / "N2词汇.md"
CSV_PATH = SCRIPTS / "_n2_jamsin.csv"
FREQ_JSON = SCRIPTS / "_n2_freq.json"
CACHE = SCRIPTS / "_n2_meaning_zh_cache.json"
CACHE_DIR = SCRIPTS / "_n2_exam_cache"
INDEX_FILE = CACHE_DIR / "index.json"
OUT = ROOT / "content" / "posts" / "N2文字词汇常考词.md"

KANJI = re.compile(r"[一-龥]")
KATA = re.compile(r"^[ァ-ヶー・]+$")
HIRAGANA = re.compile(r"^[ぁ-んー]+$")

# 真题高频词中文补充（优先于机翻）
ZH: dict[str, str] = {
    "湿る": "潮湿；淋湿", "しめる": "潮湿", "湿って": "潮湿（连用）",
    "略す": "省略；简略", "略く": "简略", "省く": "省去；省略",
    "破片": "碎片", "着々": "逐步；稳步", "でたらめ": "胡乱；乱来",
    "諸": "各；诸多（諸国）", "抱える": "抱着；承担（难题）",
    "廃止": "废止", "仕上げる": "完成；做好", "生じる": "产生",
    "普及": "普及", "劣る": "不如；逊色", "幼い": "幼稚；年幼（おさない）",
    "削除": "删除", "うつむく": "低头", "帰省": "回乡探亲",
    "討論": "讨论", "豊富": "丰富", "敏感": "敏感",
    "飛び散る": "飞溅；散开", "節約": "节约", "拡充": "扩充",
    "傾く": "倾斜；倾向", "豊か": "丰富；富裕", "競う": "竞争",
    "抽象": "抽象", "垂直": "垂直", "苦情": "投诉；怨言",
    "ぎっしり": "紧密；满满", "一転": "一转；骤变",
    "警備": "警卫", "役目": "任务；职责", "収穫": "收获",
    "あいまい": "模糊", "企画": "策划", "独特": "独特",
    "引退": "引退", "快い": "爽快；痛快", "快く": "痛快地",
    "活発": "活泼", "提供": "提供", "延長": "延长",
    "さびる": "生锈", "再〜": "再…（再開等）", "〜風": "…风格",
    "〜順": "…顺序", "真": "真；纯正（真っ白）",
    "ぐっすり": "熟睡", "ショック": "冲击", "付き": "附带（付き合い）",
    "到達": "到达", "連れ": "带领", "かすか": "微弱",
    "異": "不同；异（異文化）", "諸": "各；诸多",
    "さびる": "生锈", "じめじめ": "闷热潮湿", "すっきり": "清爽",
    "づらい": "难…的（〜づらい）", "アピール": "呼吁；吸引",
    "インパクト": "冲击", "ステージ": "舞台", "スペース": "空间",
    "チャージ": "收费；充电", "デザイン": "设计", "プレッシャー": "压力",
    "不都合": "不方便", "付属": "附属", "伴い": "伴随",
    "制作": "制作", "取り払った": "清除", "大まかな": "粗略的",
    "寄付": "捐赠", "打ち消した": "否定", "栽培": "栽培",
    "減量": "减重", "発揮": "发挥", "解散": "解散",
    "転勤": "调职", "限定": "限定", "面倒": "麻烦",
    "きっかけ": "契机", "分解": "分解", "分野": "领域",
    "反省": "反省", "大げさ": "夸张", "掲示": "张贴告示",
    "散らかす": "弄乱", "生き生き": "生动", "発達": "发达",
    "目上": "长辈", "破れる": "破裂", "覆う": "覆盖",
    "論争": "争论", "隔てる": "隔开", "頂上": "山顶", "順調": "顺利",
    "圧倒的": "压倒性的", "応募": "应征；报名", "抽象的": "抽象的",
    "破綻": "破裂；破产", "貴重": "贵重", "激怒": "激怒",
    "勧誘": "劝诱", "善良": "善良", "密閉": "密闭",
    "偶然": "偶然", "実践": "实践", "心配": "担心",
    "平等": "平等", "状況": "状况", "現象": "现象",
    "負担": "负担", "飛行機": "飞机", "特別": "特别",
    "比較的": "比较的", "派手": "花哨", "機嫌": "心情",
    "入学金": "入学费", "受信拒否": "拒收", "処理": "处理",
    "分析": "分析", "刺激": "刺激", "冷蔵庫": "冰箱",
    "危険": "危险", "品質": "品质", "係員": "工作人员",
    "優秀": "优秀", "体操": "体操", "声援": "声援",
    "夕方": "傍晚", "夕日": "夕阳", "学年": "学年",
    "家具": "家具", "山道": "山路", "強火": "大火",
    "当時": "当时", "情景": "情景", "才能": "才能",
    "記者": "记者", "科学技術": "科学技术",
    "器用": "灵巧", "要約": "摘要", "裏づける": "证实；支持",
    "短気": "急躁", "縮小": "缩小", "自衛": "自卫",
    "宛て": "寄给", "届け": "送达", "持ち上げる": "举起",
    "抜け": "脱落；漏洞", "寄り": "靠近", "守衛": "警卫",
    "始まり": "开始", "向き": "朝向", "含み": "包含",
    "取り上げる": "拿起；讨论", "別れ": "分别", "出かけ": "出门",
    "具合": "情况；状态", "便り": "消息", "予備": "预备",
    "予防": "预防", "マーケット": "市场", "ホール": "大厅",
    "きつい": "紧；辛苦", "ぐるしい": "痛苦", "いたい": "疼",
    "おそい": "慢；迟", "よわい": "弱；年幼", "わるい": "坏",
    "過ごし": "度过", "集まり": "聚集", "離れ": "离开",
    "近づける": "靠近", "込み": "包含", "載せ": "放上",
    "足し": "添加", "詳細": "详细", "逃げ": "逃跑",
    "気味": "倾向（〜気味）",
}

PROBLEM_HINT = {
    "問題1": "読み（读音）— 选正确假名",
    "問題2": "表記（汉字）— 选正确汉字",
    "問題3": "語彙（搭配填空）— 语法搭配・接辞",
    "問題4": "意味（词义）— 选最接近义项",
    "問題5": "用法（近义句）— 选用法正确的句子",
    "問題6": "用法（词用法）— 选正确用例",
    "2012": "2012～2013 速查",
    "跨套": "跨套高频",
}

MOJI_TYPE_HINT = {
    "読み": "問題1 向け：汉字音训读、特殊读音",
    "表記": "問題2 向け：同音异字、假名书写",
    "接辞": "問題3 向け：〜付き、〜づらい、〜気味",
    "意味": "問題4 向け：词义辨析、搭配",
    "外来語": "問題4 向け：片假名外来语",
    "用法": "問題5・6 向け：近义句、正确用例",
}


def load_zh_cache() -> dict[str, str]:
    if CACHE.is_file():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def load_freq_rank() -> dict[str, int]:
    if not FREQ_JSON.is_file():
        return {}
    data = json.loads(FREQ_JSON.read_text(encoding="utf-8"))
    start = next(i for i, row in enumerate(data) if row[0] == "N2")
    out: dict[str, int] = {}
    rank = 0
    for row in data[start + 1 :]:
        if len(row) != 2 or row[0] in ("N1", "N2", "N3", "N4", "N5"):
            continue
        out[row[0]] = rank
        rank += 1
    return out


def load_syllabus() -> list[dict]:
    rows: list[dict] = []
    if not CSV_PATH.is_file():
        return rows
    with CSV_PATH.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if "JLPT_2" not in r.get("tags", ""):
                continue
            expr = r["expression"].strip()
            rows.append({
                "expr": expr,
                "reading": r["reading"].strip(),
                "meaning_en": re.sub(r"\s+", " ", r["meaning"].strip().strip('"')),
            })
    return rows


def build_syllabus_index(syllabus: list[dict]) -> tuple[dict[str, dict], dict[str, list[dict]]]:
    by_expr: dict[str, dict] = {}
    by_reading: dict[str, list[dict]] = defaultdict(list)
    for it in syllabus:
        by_expr[it["expr"]] = it
        if it["reading"]:
            by_reading[it["reading"]].append(it)
    return by_expr, dict(by_reading)


def is_content_vocab(expr: str) -> bool:
    if not expr or len(expr) < 2:
        return False
    if expr.startswith(("～", "〜", "~", "(", "（")):
        return False
    if re.match(r"^[～〜~]", expr):
        return False
    if re.search(r"～|〜", expr[:5]):
        return False
    if "MediaMissing" in expr:
        return False
    return True


def classify_moji_type(expr: str, reading: str) -> str:
    if KATA.match(expr) or re.match(r"^[A-Za-z]", expr):
        return "外来語"
    if HIRAGANA.match(expr) and not KANJI.search(expr):
        return "表記"
    if any(expr.endswith(s) for s in ("付き", "気味", "づらい", "がち", "っぽい")):
        return "接辞"
    if expr.startswith("再") or expr in ("〜風", "〜順", "再〜"):
        return "接辞"
    if KANJI.search(expr):
        return "読み"
    return "意味"


def zh_for(word: str, csv_idx: dict, en_cache: dict[str, str]) -> str:
    w = word.strip()
    if w in ZH:
        return ZH[w]
    if w in csv_idx:
        en = csv_idx[w]["meaning_en"]
        if en in en_cache:
            return en_cache[en].replace(",", "；")[:56]
        return en.replace(",", "；").replace(" to ", "；")[:56]
    return "（待补）"


def normalize_token(tok: str) -> str:
    tok = tok.strip()
    tok = re.sub(r"（\d+）$", "", tok)
    tok = re.sub(r"（[^）]+）$", "", tok)
    if re.search(r"[\*\|次：]", tok) or len(tok) < 1:
        return ""
    return tok.strip()


def is_valid_word(w: str) -> bool:
    if not w or w.isdigit():
        return False
    if re.search(r"[\*\|次：・]", w):
        return False
    if " 等" in w or w.endswith("等"):
        return False
    if " " in w:
        return False
    return True


def extract_summary_block(text: str) -> str:
    m = re.search(
        r"## 全部考点词汇总.*?\n\n(.*?)(?:\n\n### 按出现次数|\n\n---\n\n# )",
        text,
        re.S,
    )
    return m.group(1) if m else ""


def parse_exam_vocab(text: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    """仅从词汇汇总区解析，不含各套真题正文。"""
    freq_words: dict[str, int] = {}

    # 跨套表
    for m in re.finditer(r"\|\s*\*\*(\d+)\*\*\s*\|\s*([^|]+)\|", text[:2500]):
        count = int(m.group(1))
        body = m.group(2).strip()
        for part in re.split(r"、|，", body):
            part = part.strip()
            if not part or part.startswith("20"):
                continue
            main = re.sub(r"（[^）]+）", "", part).strip()
            for w in re.split(r"[／/、·・]", main):
                w = normalize_token(w.strip())
                if is_valid_word(w):
                    freq_words[w] = max(freq_words.get(w, 0), count)

    sec = re.search(r"### 按出现次数.*?\n\n(.*?)(?:\n\n---|\n\n# )", text, re.S)
    if sec:
        for m in re.finditer(r"\*\*(\d+)\s*次\*\*[^：\n]*：([^\n]+)", sec.group(1)):
            count = int(m.group(1))
            for w in re.split(r"[·\s]+", m.group(2).strip()):
                w = normalize_token(w)
                if is_valid_word(w):
                    freq_words[w] = max(freq_words.get(w, 0), count)

    by_problem: dict[str, list[str]] = defaultdict(list)
    current = None
    for line in extract_summary_block(text).splitlines():
        m = re.match(r"^### (問題\d|2012～2013|跨套高频)", line)
        if m:
            key = m.group(1)
            if "問題" in key:
                current = key.split()[0]
            elif "2012" in key:
                current = "2012"
            else:
                current = "跨套"
            continue
        if current and line.strip():
            for chunk in re.split(r"[\s·]+", line.strip()):
                tok = normalize_token(chunk.strip())
                if is_valid_word(tok):
                    by_problem[current].append(tok)

    for k in by_problem:
        seen: set[str] = set()
        out: list[str] = []
        for t in by_problem[k]:
            if t not in seen:
                seen.add(t)
                out.append(t)
        by_problem[k] = out

    return freq_words, dict(by_problem)


def match_to_syllabus(
    word: str,
    by_expr: dict[str, dict],
    by_reading: dict[str, list[dict]],
) -> dict | None:
    if word in by_expr:
        return by_expr[word]
    if word in by_reading and len(by_reading[word]) == 1:
        return by_reading[word][0]
    # 去掉常见活用尾再试
    for suf in ("した", "って", "った", "ない", "ます", "ている", "な"):
        if word.endswith(suf) and len(word) > len(suf) + 1:
            base = word[: -len(suf)]
            if base in by_expr:
                return by_expr[base]
    return None


def load_exam_corpus() -> list[dict]:
    if not INDEX_FILE.is_file():
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
            by_exam[eid] = {"exam_id": eid, "text": text}
    return sorted(by_exam.values(), key=lambda x: x["exam_id"])


def corpus_hits(expr: str, reading: str, corpus: list[dict]) -> int:
    n = 0
    for c in corpus:
        t = c["text"]
        if expr and len(expr) >= 2:
            n += len(re.findall(re.escape(expr), t))
        if reading and len(reading) >= 2:
            pat = r"(?<![ぁ-んァ-ヶ一-龥ー])" + re.escape(reading) + r"(?![ぁ-んァ-ヶ一-龥ー])"
            n += len(re.findall(pat, t))
    return n


def exam_tier(n: int) -> str:
    if n >= 4:
        return "S"
    if n >= 3:
        return "A"
    if n >= 2:
        return "B"
    return "C"


def predict_tier(score: int, in_moji: bool, moji_n: int) -> str:
    if in_moji and moji_n >= 2:
        return "S"
    if in_moji or score >= 400:
        return "A"
    if score >= 250:
        return "B"
    if score >= 120:
        return "C"
    return "D"


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    freq_words, by_problem = parse_exam_vocab(text)
    exam_all = set()
    for words in by_problem.values():
        exam_all.update(words)

    syllabus = load_syllabus()
    by_expr, by_reading = build_syllabus_index(syllabus)
    csv_idx = {it["expr"]: it for it in syllabus}
    en_cache = load_zh_cache()
    freq_rank = load_freq_rank()
    corpus = load_exam_corpus()

    content_syll = [it for it in syllabus if is_content_vocab(it["expr"])]
    ranked_exam = sorted(freq_words.items(), key=lambda x: (-x[1], x[0]))
    high_exam = [(w, c) for w, c in ranked_exam if c >= 2]

    # 考纲词分析
    analyzed: list[dict] = []
    for it in content_syll:
        expr = it["expr"]
        moji_n = freq_words.get(expr, 0)
        in_moji = expr in exam_all or moji_n > 0
        # 活用形出现在真题汇总
        if not in_moji:
            for ew in exam_all:
                if ew == expr or ew.startswith(expr):
                    in_moji = True
                    moji_n = max(moji_n, freq_words.get(ew, 1))
                    break
        rank = freq_rank.get(expr)
        corp = corpus_hits(expr, it["reading"], corpus) if corpus else 0
        mtype = classify_moji_type(expr, it["reading"])
        score = 0
        if moji_n:
            score += 500 + moji_n * 100
        if rank is not None:
            score += max(0, 450 - rank)
        if corp:
            score += min(corp, 30) * 5
        if mtype == "読み" and KANJI.search(expr):
            score += 40
        elif mtype in ("意味", "外来語"):
            score += 25
        elif mtype == "表記":
            score += 20
        analyzed.append({
            **it,
            "moji_n": moji_n,
            "in_moji": in_moji,
            "rank": rank,
            "corp": corp,
            "mtype": mtype,
            "score": score,
            "ptier": predict_tier(score, in_moji, moji_n),
        })

    analyzed.sort(key=lambda x: (-x["score"], x["rank"] is None, x["rank"] or 99999, x["expr"]))

    # 考纲对标：真题词命中考纲
    matched_exam = 0
    for w in exam_all:
        if match_to_syllabus(w, by_expr, by_reading):
            matched_exam += 1

    predict_unexam = [a for a in analyzed if not a["in_moji"] and a["ptier"] in ("A", "B", "C")]
    by_type: dict[str, list[dict]] = defaultdict(list)
    for a in analyzed:
        if a["ptier"] in ("S", "A", "B"):
            by_type[a["mtype"]].append(a)

    lines = [
        "---",
        "title: N2 文字词汇 · 考纲+真题常考词",
        "date: 2026-07-04",
        "tags: 学习/日语/JLPT/N2",
        "column: 学习笔记",
        "toc: true",
        "---",
        "",
        "# N2 文字词汇 · 考纲+真题常考词",
        "",
        f"> **考纲**：open-anki / tanos **N2 词表** [`_n2_jamsin.csv`](../../web/scripts/_n2_jamsin.csv) 共 **{len(syllabus)}** 词（内容词 **{len(content_syll)}**）。",
        f"> **真题**：[`N2词汇.md`](N2词汇.md) 文字・語彙 **23 套**汇总 **{len(exam_all)}** 考点词；与考纲精确/读音匹配 **{matched_exam}** 词。",
        f"> **分析**：考纲通用频率（`_n2_freq.json`）+ 真题文字語彙命中 + 历年卷面语料共 **{len(corpus)}** 套，按题型特征（読み/表記/意味/外来語）加权排序。",
        "> **2025.12 起**：文字語彙 問題1～5（30 题）；此前为 問題1～6。",
        "",
        "## 怎么用",
        "",
        "1. **先背** [一、真题已考高频](#一真题已考高频≥2-次)（确定会考）。",
        "2. **再补** [二、考纲重点·按题型](#二考纲重点按文字词汇题型)（考纲核心 + 未考但易考）。",
        "3. **冲刺** [三、考纲预测·尚未考过](#三考纲预测尚未在文字語彙考过)（高频考纲词，防新题）。",
        "4. 完整题干见 [`N2词汇.md`](N2词汇.md)；全库统计见 [`JLPT-N2词汇考频总表.md`](JLPT-N2词汇考频总表.md)。",
        "",
        "## 题型与备考要点",
        "",
        "| 题型 | 考什么 | 技巧 |",
        "|------|--------|------|",
        "| **問題1 読み** | 汉字正确读音 | 音读训读、特殊读（一人→ひとり）|",
        "| **問題2 表記** | 假名→正确汉字 | 同音异字、惯用书写 |",
        "| **問題3 語彙** | 句中搭配填空 | 接辞・慣用（〜付き、〜気味）|",
        "| **問題4 意味** | 词义选择 | 名词动词形容词、外来语 |",
        "| **問題5 用法** | 近义句选正确句 | 语感、搭配、敬语 |",
        "| **問題6 用法** | 词的正确用例 | 多义词、书面语 |",
        "",
        "## 考频分级",
        "",
        "| 级别 | 真题文字語彙 | 考纲预测 |",
        "|------|-------------|----------|",
        "| **S** | 跨套 ≥4 次 | 真题≥2 次 或 考纲 Top50 且语料高频 |",
        "| **A** | 3 次 | 考纲 Top200 / 真题考过 1 次 |",
        "| **B** | 2 次 | 考纲 Top500 |",
        "| **C** | 1 次 | 考纲 Top800，尚未考过 |",
        "",
        "---",
        "",
        "## 一、真题已考高频（≥2 次）",
        "",
        f"> 共 **{len(high_exam)}** 词（23 套文字語彙汇总）。",
        "",
        "| 词 | 中文 | 読み | 次数 | 考纲 |",
        "|----|------|------|------|------|",
    ]

    for w, c in ranked_exam:
        if c < 2:
            break
        sy = match_to_syllabus(w, by_expr, by_reading)
        reading = sy["reading"] if sy else csv_idx.get(w, {}).get("reading", "")
        in_syll = "✓" if sy else "—"
        lines.append(
            f"| {w} | {zh_for(w, csv_idx, en_cache)[:18]} | {reading or '—'} | **{c}** | {in_syll} |"
        )

    lines += ["", "### 按考频展开", ""]
    current_t = None
    for w, c in ranked_exam:
        if c < 2:
            break
        t = exam_tier(c)
        if t != current_t:
            current_t = t
            lines += ["", f"#### {t}级", ""]
        sy = match_to_syllabus(w, by_expr, by_reading)
        reading = sy["reading"] if sy else ""
        zh = zh_for(w, csv_idx, en_cache)
        extra = f" · 読み {reading}" if reading else ""
        syll_note = " · **考纲收录**" if sy else " · 考纲未收录（活用/短语）"
        lines += [f"**{w}**（{zh}）", "", f"> 真题 **{c}** 次{extra}{syll_note}", ""]

    lines += [
        "",
        "## 二、考纲重点·按文字词汇题型",
        "",
        "> 从考纲 **内容词** 中按题型特征筛选；**真题** 列标文字語彙出现次数（0=未考过）。",
        "",
    ]

    type_limits = {"読み": 180, "意味": 120, "外来語": 80, "表記": 60, "接辞": 40, "用法": 40}
    for mtype in ("読み", "表記", "接辞", "意味", "外来語"):
        items = sorted(
            [a for a in analyzed if a["mtype"] == mtype],
            key=lambda x: (-x["score"], x["rank"] is None, x["rank"] or 99999),
        )[: type_limits.get(mtype, 100)]
        if not items:
            continue
        lines += [
            f"### {mtype}向け · {MOJI_TYPE_HINT.get(mtype, '')}",
            "",
            f"> 考纲 **{mtype}** 类 Top **{len(items)}**（按预测分排序）",
            "",
            "| 词 | 読み | 中文 | 考纲序 | 真题 | 预测 |",
            "|----|------|------|--------|------|------|",
        ]
        for a in items:
            rank_s = f"#{a['rank'] + 1}" if a["rank"] is not None else "—"
            moji_s = f"**{a['moji_n']}**" if a["moji_n"] >= 2 else (str(a["moji_n"]) if a["moji_n"] else "0")
            lines.append(
                f"| {a['expr']} | {a['reading']} | {zh_for(a['expr'], csv_idx, en_cache)[:16]} "
                f"| {rank_s} | {moji_s} | {a['ptier']} |"
            )
        lines.append("")

    lines += [
        "## 三、考纲预测·尚未在文字語彙考过",
        "",
        f"> 考纲高频、题型适配、但 **23 套文字語彙汇总未出现** 的词，共 **{len(predict_unexam)}** 个；",
        "下表列预测 **A/B** 前 **120** 个（防新题抽查）。",
        "",
        "| 词 | 読み | 中文 | 考纲序 | 语料 | 题型 | 预测 |",
        "|----|------|------|--------|------|------|------|",
    ]
    shown = 0
    for a in predict_unexam:
        if a["ptier"] not in ("A", "B"):
            continue
        if shown >= 120:
            break
        rank_s = f"#{a['rank'] + 1}" if a["rank"] is not None else "—"
        lines.append(
            f"| {a['expr']} | {a['reading']} | {zh_for(a['expr'], csv_idx, en_cache)[:14]} "
            f"| {rank_s} | {a['corp'] or '—'} | {a['mtype']} | {a['ptier']} |"
        )
        shown += 1

    lines += ["", "## 四、真题考点·按题型速查", ""]
    for prob in ["問題1", "問題2", "問題3", "問題4", "問題5", "問題6", "2012", "跨套"]:
        words = by_problem.get(prob, [])
        if not words:
            continue
        hint = PROBLEM_HINT.get(prob, "")
        lines += [f"### {prob}", "", f"> {hint} · 共 **{len(words)}** 词", ""]
        show = words
        if prob == "問題4" and len(words) > 100:
            hi = {w for w, c in ranked_exam if c >= 2}
            show = [w for w in words if w in hi][:80]
            show += [w for w in words if w not in show][:40]
            lines.append("> 問題4 共 {} 词；下表为高频 + 部分常考。".format(len(words)))
            lines.append("")
        lines.append("| 词 | 中文 | 読み | 真题频次 | 考纲 |")
        lines.append("|----|------|------|----------|------|")
        for w in show[:100]:
            c = freq_words.get(w, 1)
            sy = match_to_syllabus(w, by_expr, by_reading)
            reading = sy["reading"] if sy else ""
            mark = f"**{c}**" if c >= 2 else str(c)
            lines.append(
                f"| {w} | {zh_for(w, csv_idx, en_cache)[:20]} | {reading or '—'} | {mark} | {'✓' if sy else '—'} |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        "## 说明",
        "",
        "- **考纲词表**：JLPT N2 标准词汇（1906 条），含语法接辞词条；本表「内容词」已过滤 `～位` `～化` 等纯语法后缀。",
        "- **预测分**：考纲频率序 + 文字語彙真题命中 + 全卷语料出现 + 题型权重；非官方泄题，仅供备考优先级参考。",
        "- **考纲未收录**：真题中的活用形（如 取り払った）、复合短语、听力干扰项等，仍以真题为准背诵。",
        "- 重新生成：`python web/scripts/build-n2-moji-vocab-md.py`",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[moji] -> {OUT}")
    print(f"  exam>={2}: {len(high_exam)}  syllabus: {len(content_syll)}  predict: {len(predict_unexam)}")


if __name__ == "__main__":
    main()
