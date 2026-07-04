#!/usr/bin/env python3
"""Extract 文字語彙 考点词 from N2词汇.md, grouped by 問題1～6."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "content" / "posts" / "N2词汇.md"

GROUP_LABELS = {
    "p1": "問題1 · 读音",
    "p2": "問題2 · 汉字书写",
    "p3": "問題3 · 填空（语法搭配）",
    "p4": "問題4 · 填空（词义/用法）",
    "p5": "問題5 · 近义替换",
    "p6": "問題6 · 用法",
    "sokuha": "2012～2013 速查",
    "freq": "跨套高频（≥2 次）",
}

SKIP_P1 = {
    "新聞", "新入生", "大学", "学生", "先生", "学校", "今日", "明日", "昨日", "自分",
    "会社", "仕事", "時間", "問題", "生活", "世界", "日本", "中国", "電話", "家族",
    "友達", "子供", "彼女", "彼", "教師", "生徒", "模範", "行動", "大会", "決勝",
    "レストラン", "親子", "部屋", "食器", "当日", "資料", "連絡", "海外", "市場",
    "進出", "販売", "部門", "必要", "世", "中", "動", "親", "子", "客", "日当",
    "悪", "昼", "風邪", "詰", "箱", "駅前", "歩", "突然", "午前", "午後", "予定",
    "司会", "話", "合", "転校", "クラス", "分", "涙", "止", "評価", "試験", "近",
    "勉強", "卒業", "行", "青木", "握", "空気", "入", "閉", "線", "対", "池",
    "今朝", "寒", "議論", "団体", "傷", "動物", "活動", "機械",
}


def normalize(word: str) -> str:
    w = word.strip().strip("・")
    w = re.sub(r"^[*]+|[*]+$", "", w)
    w = re.sub(r"（[^）]*）", "", w)
    return w.strip()


def is_valid_token(w: str) -> bool:
    if not w or len(w) < 2 or len(w) > 8:
        return False
    if any(c in w for c in "。、・（）()「」『』…"):
        return False
    if re.search(r"[をがにはでとのもへや]", w):
        return False
    junk_suffix = ("て", "で", "さ", "く", "ま", "ん", "い", "れ", "せ")
    if len(w) > 4 and w.endswith(junk_suffix):
        return False
    junk_part = ("くださ", "てい", "して", "ます", "ません", "でした", "である", "決まり")
    if any(j in w for j in junk_part):
        return False
    if re.match(r"^[\u3040-\u309f]+$", w) and len(w) > 6:
        return False
    if w.endswith("さん") or w.endswith("ほう") or "したほう" in w:
        return False
    if w in ("さん", "ある", "いる", "ない", "する", "した", "して", "ため", "たち"):
        return False
    junk = ("仍为", "未提供", "考点速查", "N2", "文字", "語彙", "文法", "见下", "ばかり")
    return not any(j in w for j in junk)


def pick_p1_target(sent: str) -> str | None:
    cands = [w for w in re.findall(r"[\u4e00-\u9fff]{2,}", sent) if w not in SKIP_P1]
    if not cands:
        return None
    preferred = [w for w in cands if 2 <= len(w) <= 4]
    pool = preferred or cands
    pool.sort(key=lambda x: (abs(len(x) - 3), x))
    return pool[0]


def pick_p2_target(sent: str) -> str | None:
    patterns = [
        r"([\u3040-\u309f]{2,7})(?:った|って|た|て|だ|る|り|っ|う|く|ん|が|は|を|に|の|で|ま|せ)",
        r"(?:が|を|は|に|の|で)([\u3040-\u309f]{2,7})(?:[。、]|$)",
    ]
    for pat in patterns:
        for m in re.finditer(pat, sent):
            w = m.group(1)
            if is_valid_token(w):
                return w
    return None


def pick_p5_target(sent: str) -> str | None:
    sent = sent.rstrip("。").split("\u3000")[0]
    patterns = [
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})である",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})だった",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})で、",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})なの",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})なら",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})した",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})して",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})する",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})いる",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})いました",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})ました",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})ません",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})だ",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})と",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})を",
        r"([\u4e00-\u9fff\u3040-\u309f]{2,6})が",
    ]
    for pat in patterns:
        m = re.search(pat, sent)
        if m:
            w = m.group(1)
            if is_valid_token(w):
                return w
    return None


def sort_key(word: str) -> tuple:
    if re.match(r"^[\u3040-\u309f\u30a0-\u30ff〜～]", word):
        return (0, word)
    if re.match(r"^[A-Za-z]", word):
        return (1, word.lower())
    return (2, word)


def fmt_word(w: str, c: int) -> str:
    return f"{w}（{c}）" if c > 1 else w


def format_word_block(words: list[str], counter: Counter[str], per_line: int = 12) -> list[str]:
    lines: list[str] = []
    chunk: list[str] = []
    for w in words:
        chunk.append(fmt_word(w, counter[w]))
        if len(chunk) >= per_line:
            lines.append(" · ".join(chunk))
            chunk = []
    if chunk:
        lines.append(" · ".join(chunk))
    return lines


def extract_grouped(text: str) -> tuple[dict[str, Counter[str]], Counter[str]]:
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for i, ln in enumerate(lines[1:], 1):
            if ln.strip() == "---":
                start = i + 1
                break
    lines = lines[start:]

    groups: dict[str, Counter[str]] = defaultdict(Counter)
    total: Counter[str] = Counter()
    in_vocab = False
    problem: int | None = None

    def add(raw: str, group: str) -> None:
        w = normalize(raw)
        if is_valid_token(w):
            groups[group][w] += 1
            total[w] += 1

    def parse_sokuha(line: str) -> None:
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        for part in re.split(r"[｜|]", line):
            for w in re.split(r"[・、，,/\s]+", part):
                if w and not re.match(r"^\d{4}", w):
                    add(w, "sokuha")

    i = 0
    while i < len(lines):
        ln = lines[i]

        if ln.strip() == "## 文字・語彙":
            in_vocab, problem = True, None
            i += 1
            continue
        if ln.startswith("## 文法"):
            in_vocab, problem = False, None
            i += 1
            continue
        if "2012～2013" in ln or ln.startswith("# 2012"):
            in_vocab = True

        if "考点词速查" in ln:
            in_vocab = True
            i += 1
            continue

        if in_vocab and not ln.startswith(("#", "|", ">")) and "・" in ln and len(ln) < 180:
            if ln.startswith(("装置", "抽象", "清潔")) or re.search(r"\d{4}年", ln):
                parse_sokuha(ln)
            i += 1
            continue

        pm = re.match(r"^### 問題(\d+)", ln)
        if pm and in_vocab:
            n = int(pm.group(1))
            problem = n if n <= 6 else None
            i += 1
            continue

        if not in_vocab or problem is None:
            i += 1
            continue

        qm = re.match(r"^(\d+)\.\s*(.+)$", ln)
        if not qm:
            i += 1
            continue

        qtext = qm.group(2).strip()
        gkey = f"p{problem}"

        if problem == 6 and "。" not in qtext and len(qtext) <= 20:
            if not re.match(r"^[1-4]\.", qtext):
                add(qtext, gkey)
                i += 1
                continue

        if problem in (3, 4) and re.match(r"^[1-4]\.\s", qtext) and "（" not in qtext:
            opts = re.findall(r"[1-4]\.\s*([^\u3000\d]+?)(?=\s*[1-4]\.\s*|\s*$)", qtext)
            for o in opts:
                add(o.strip(), gkey)
            i += 1
            continue

        sent = qtext.split("\u3000")[0]

        if problem == 1:
            w = pick_p1_target(sent)
            if w:
                add(w, gkey)
        elif problem == 2:
            w = pick_p2_target(sent)
            if w:
                add(w, gkey)
        elif problem in (3, 4):
            combined = qtext
            j = i + 1
            while j < len(lines) and lines[j].startswith("   "):
                combined += " " + lines[j].strip()
                j += 1
            opts = re.findall(
                r"[1-4]\.\s*([^\u3000\d]+?)(?=\s*[1-4]\.\s*|\s*$)", combined
            )
            for o in opts:
                add(o.strip(), gkey)
        elif problem == 5:
            w = pick_p5_target(sent)
            if w:
                add(w, gkey)

        i += 1

    for ln in lines[:80]:
        m = re.match(r"^\| \*\*\d+\*\* \| (.+?) \|", ln)
        if m:
            for w in re.split(r"[／/・、，,（）()\s]+", m.group(1)):
                add(w, "freq")

    return dict(groups), total


def build_summary_section(groups: dict[str, Counter[str]], total: Counter[str]) -> str:
    n_total = len(total)
    n_multi = sum(1 for c in total.values() if c >= 2)

    out = [
        "## 全部考点词汇总",
        "",
        f"> 从本页 **文字・語彙 問題1～6** 及 2012～2013 速查区提取，**按题型分组**。"
        f"去重合计 **{n_total}** 词（跨题型重复计 1 次）；其中出现 ≥2 次 **{n_multi}** 词。",
        f"問題1/5 为规则识别，个别词以各套正文为准。",
        "",
    ]

    order = ["p1", "p2", "p3", "p4", "p5", "p6", "sokuha", "freq"]
    for key in order:
        counter = groups.get(key, Counter())
        if not counter:
            continue
        label = GROUP_LABELS[key]
        words = sorted(counter.keys(), key=sort_key)
        out.append(f"### {label}（{len(words)} 词）")
        out.append("")
        out.extend(format_word_block(words, counter))
        out.append("")

    out.append(f"### 全部单词一览（去重 {n_total} 词）")
    out.append("")
    all_words = sorted(total.keys(), key=sort_key)
    out.extend(format_word_block(all_words, total))
    out.append("")

    out.append("### 按出现次数（≥2 次）")
    out.append("")
    for freq in sorted({c for c in total.values() if c >= 2}, reverse=True):
        words = sorted((w for w, c in total.items() if c == freq), key=sort_key)
        out.append(f"**{freq} 次**（{len(words)}）：{' · '.join(words)}")
        out.append("")

    return "\n".join(out)


def main() -> None:
    text = MD.read_text(encoding="utf-8")
    text = re.sub(
        r"\n## 全部考点词汇总[\s\S]*?(?=\n---\n|\n# 2015|\Z)",
        "\n",
        text,
        count=1,
    )
    groups, total = extract_grouped(text)
    section = build_summary_section(groups, total)
    insert_after = "其余考点词各考 **1 次**，见各套真题正文。"
    text = text.replace(insert_after, insert_after + "\n\n" + section, 1)
    MD.write_text(text, encoding="utf-8")

    for k in ["p1", "p2", "p3", "p4", "p5", "p6", "sokuha", "freq"]:
        c = groups.get(k, Counter())
        print(f"{GROUP_LABELS[k]}: {len(c)}")
    print(f"TOTAL unique: {len(total)}")


if __name__ == "__main__":
    main()
