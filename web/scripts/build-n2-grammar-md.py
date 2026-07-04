#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 N2词汇.md 提取历年真题文法题，汇总考点并生成 Markdown。"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from _n2_grammar_notes import explain, explain_body

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "posts" / "N2词汇.md"
OUT = ROOT / "content" / "posts" / "N2文法考点总表.md"

SKIP_EXAMS = {"2016.12", "2022.12"}

# (regex on option/stem, 考点名, 分类)
GRAMMAR_RULES: list[tuple[str, str, str]] = [
    (r"の末", "〜の末に", "时间・经过"),
    (r"をめぐ", "〜をめぐって", "话题"),
    (r"を込め", "〜を込めて", "方式"),
    (r"なくなり次第|なり次第", "〜次第（一…就）", "时间"),
    (r"以上", "〜以上", "理由"),
    (r"うちに|ないうちに|たたないうちに", "〜うちに", "时间"),
    (r"ばかり", "〜ばかり", "限定"),
    (r"だけの|だけで|きり|っきり|抜き", "〜だけ／きり／抜き", "限定"),
    (r"わけにはいかない|わけがない|わけではない|わけでも", "〜わけ", "理由"),
    (r"ほかない|しかない|よりほか", "〜しかない／ほかない", "限定"),
    (r"にあたって|にあたり", "〜にあたって", "时间"),
    (r"に際", "〜に際して", "时间"),
    (r"に限り|に限って|に限ら", "〜に限り", "限定"),
    (r"にわた", "〜にわたって", "范围"),
    (r"一方だ|一方で", "〜一方だ", "变化"),
    (r"次第だ|次第で|なり次第|なくなり次第", "〜次第", "时间"),
    (r"ほどだ|ほどの|ほどに|ほどで", "〜ほどだ", "程度"),
    (r"べき", "〜べき", "应该"),
    (r"はず", "〜はず", "理应"),
    (r"に違いない|に決まって|に相違", "〜に違いない 等", "确信"),
    (r"かのよう|まるで", "〜かのようだ", "比喻"),
    (r"くらい|ぐらい", "〜くらい", "程度"),
    (r"ものなら|ものだ|ものでは|ものか|ものの|ものを|ものだから", "〜もの", "语气"),
    (r"ことになっている|ことになった|ことにな|ことにする|ことに感|ことに驚|ことに気|ことだから|ことではない|ことか\b", "〜ことになる／ことに", "形式名词"),
    (r"ところがある|ところだ|ところで|ところだった|ところを", "〜ところ", "时点"),
    (r"がち", "〜がち", "倾向"),
    (r"っぽい|気味|づらい|にくい|がたい", "〜がち／づらい 等", "倾向・难易"),
    (r"得る|得ない|かねない|かねる", "〜得る／かねない", "可能"),
    (r"てたまらない|てしょうがない|てならない|て当然", "〜てたまらない 等", "程度"),
    (r"ずにはいられない|ないではいられない|ないことはない", "双重否定・抑制", "语气"),
    (r"ないわけにはいかない|てもおかしくない|てもかまわ", "义务・许可", "语气"),
    (r"申し上げ|おっしゃ|いただ|くださ|うけたまわ|お越し|参り|伺い|差し上げ", "敬语", "敬语"),
    (r"からには|ながらも|どころか|どころでは|わりには", "接续・逆接", "接续"),
    (r"に対して|にとって|として|にしたが|につれ|に伴", "〜に対して／につれて", "关系"),
    (r"をきっかけ|を契機|を機に|をはじめ|を除|を問わ|を通じ|を踏まえ|を前提", "范围・契机", "关系"),
    (r"ばかりか|だけでなく|のみならず|さえ|こそ|すら", "强调・递进", "强调"),
    (r"にしては|としては|にしても|としても|であれ|であっても|にしろ|にせよ|とはいえ", "让步", "让步"),
    (r"てからでないと|てからで|てからでなく|なければなら|なくては|ないと", "条件・义务", "条件"),
    (r"ずに済|ないで済|なくて済|て済|で済", "〜ずに済む", "结果"),
    (r"ように|ような|ために|ため|おかげ|せい", "目的・原因", "原因"),
    (r"のに|くせに", "〜のに", "逆接"),
    (r"とおり|通り|どおり|まま", "〜とおり／まま", "方式"),
    (r"最中|途中|たところ|たばかり|ところだった", "时点", "时间"),
    (r"か何|や何", "〜か何か", "举例"),
    (r"に欠かせ|に越した|にほかなら|にすぎ|に反して|に基づ|に沿|に応|に先立", "固定表达", "固定"),
    (r"つもり|たらいい|ばいい|といい|がる|てほし|てみ|てしま|ておく|てくる|ていく", "补助动词", "补助"),
    (r"とすると|としたら|とすれば|なら|ならば", "假设", "条件"),
    (r"というと|といえば|というのは|というより|とは限|かどうか", "引用・是否", "引用"),
    (r"いったい|おそらく|かえって|どうしても|つい|いつのまにか|まもなく", "副词", "副词"),
    (r"から言|から見|からす|に見え|ように見え|ようにして|ようにな", "看法・变化", "变化"),
    (r"っこない|っぱなし|もんか|もん", "口语・否定", "口语"),
    (r"考えていない|考えようとし|乗るしか|待たずに済|待たなければ", "语境型", "语境"),
    (r"入れても|入れること|口に", "〜ように（目的）", "目的"),
    (r"からには|決まった|演奏家", "〜からには／として", "语境"),
]

PARTICLE_STEMS = [
    (r"上った|上る|達|超", "数量＋に（达到）", "助词"),
    (r"議論|会議|協議", "をめぐる／の末", "助词"),
    (r"強.*ばかり|増.*ばかり", "ばかり（越来越）", "助词"),
    (r"取得|卒業|完成|終", "てからでないと", "助词"),
    (r"なくな.*終了|無くな", "なくなり次第", "助词"),
    (r"調味料|欠.*", "に欠かせない", "助词"),
    (r"雑誌|新聞", "か何か／や何か", "助词"),
    (r"熱|病気|大事", "わけにはいかない", "助词"),
    (r"敬语|報告|お越し|参り", "敬语", "敬语"),
    (r"★", "语序题", "语序"),
]


@dataclass
class GrammarQ:
    exam: str
    qtype: str  # fill / order
    num: int
    stem: str
    options: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)


def exam_id_from_heading(line: str) -> str | None:
    m = re.match(r"#\s*(\d{4})年(\d{1,2})月", line)
    if m:
        return f"{m.group(1)}.{int(m.group(2)):02d}"
    return None


def parse_options(text: str) -> list[str]:
    opts = re.findall(r"[1-4１-４]\.\s*([^1-4１-４]+?)(?=\s*[1-4１-４]\.\s*|\s*$)", text)
    if not opts:
        opts = re.findall(r"[1-4１-４]\.\s*(.+?)(?=\s*[1-4１-４]\.|$)", text)
    return [o.strip().strip("　") for o in opts if o.strip()]


def best_tag(text: str, qtype: str) -> tuple[str, str]:
    if qtype == "order" or "★" in text:
        return "★语序题", "语序"

    scored: list[tuple[int, str, str]] = []
    all_rules = GRAMMAR_RULES + PARTICLE_STEMS
    for pat, name, cat in all_rules:
        m = re.search(pat, text)
        if m:
            score = len(m.group(0)) * 2 + len(name)
            scored.append((score, name, cat))

    # 选项仅为助词时，优先看题干
    opts = parse_options(text)
    if opts and all(len(o) <= 4 for o in opts):
        stem_only = re.sub(r"\s*[1-4１-４]\.\s*.+$", "", text)
        for pat, name, cat in all_rules:
            m = re.search(pat, stem_only)
            if m:
                score = len(m.group(0)) * 3 + len(name) + 10
                scored.append((score, name, cat))

    if scored:
        scored.sort(key=lambda x: (-x[0], x[1]))
        return scored[0][1], scored[0][2]

    if opts:
        joined = "／".join(opts[:4])
        return joined[:28], "选项辨析"
    return "（待归类）", "其他"


def classify_question(q: GrammarQ) -> None:
    blob = q.stem + " " + " ".join(q.options)
    tag, cat = best_tag(blob, q.qtype)
    q.tags = [tag]
    q.categories = [cat]


def parse_questions(text: str) -> list[GrammarQ]:
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for i, ln in enumerate(lines[1:], 1):
            if ln.strip() == "---":
                start = i + 1
                break
    lines = lines[start:]

    questions: list[GrammarQ] = []
    exam: str | None = None
    in_grammar = False
    qtype: str | None = None  # fill / order
    section_num: int | None = None

    i = 0
    while i < len(lines):
        ln = lines[i]
        eid = exam_id_from_heading(ln)
        if eid:
            exam = eid
            in_grammar = False
            qtype = None
            i += 1
            continue

        if ln.startswith("## 文法"):
            in_grammar = True
            qtype = None
            i += 1
            continue

        if ln.startswith("## ") and "文法" not in ln:
            in_grammar = False
            qtype = None
            i += 1
            continue

        if not in_grammar or not exam:
            i += 1
            continue

        if ln.startswith(">") and ("串卷" in ln or "相同" in ln or "见该节" in ln):
            i += 1
            continue

        if "（問題例）" in ln or ln.strip().startswith("（問題例）"):
            i += 1
            continue

        sm = re.match(r"^###\s*問題(\d+)", ln)
        if sm:
            section_num = int(sm.group(1))
            heading = ln
            if section_num == 8 or ("★" in heading or "语序" in heading):
                qtype = "order"
            elif section_num in (6, 7):
                qtype = "fill"
            i += 1
            continue

        qm = re.match(r"^(\d+)\.\s*(.+)$", ln.strip())
        if qm and qtype:
            num = int(qm.group(1))
            body = qm.group(2).strip()
            min_order = 43 if section_num == 7 else 42

            if qtype == "fill" and num < 31:
                i += 1
                continue
            if qtype == "order" and num < min_order:
                i += 1
                continue
            if qtype == "order" and num <= 4:
                i += 1
                continue

            combined = body
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                nxt_stripped = nxt.strip()
                if nxt.startswith("#") or nxt.startswith("---"):
                    break
                nm = re.match(r"^(\d+)\.\s*", nxt_stripped)
                if nm:
                    nnum = int(nm.group(1))
                    if qtype == "fill" and nnum >= 31:
                        break
                    if qtype == "order" and nnum >= min_order:
                        break
                    if nnum <= 4:
                        combined += " " + nxt_stripped
                        j += 1
                        continue
                    break
                if nxt_stripped:
                    combined += " " + nxt_stripped
                j += 1

            opts = parse_options(combined)
            stem = re.sub(r"\s*[1-4１-４]\.\s*.+$", "", combined).strip()
            qt = "order" if qtype == "order" or "★" in stem else "fill"

            if not opts and qt == "fill":
                i = j
                continue

            gq = GrammarQ(exam=exam, qtype=qt, num=num, stem=stem, options=opts)
            classify_question(gq)
            questions.append(gq)
            i = j
            continue

        i += 1

    return questions


def build_guide_section(tag_count: Counter[str], tag_exams: dict[str, set[str]]) -> list[str]:
    """按频次生成语法讲解章节（详细版）。"""
    out = [
        "## 语法讲解",
        "",
        "> 按真题出现频次排列。每条含：**核心义、接续、例句、辨析表、真题提示**。",
        "",
    ]
    tags_sorted = [t for t, _ in tag_count.most_common() if t != "（待归类）"]
    if "（待归类）" in tag_count:
        tags_sorted.append("（待归类）")

    for tag in tags_sorted:
        cnt = tag_count[tag]
        exs = "、".join(sorted(tag_exams[tag]))
        body = explain_body(tag)
        out.append(f"### {tag}（真题 **{cnt}** 次 · {exs}）")
        out.append("")
        out.append(body)
        out.append("")

    return out


def build_md(questions: list[GrammarQ]) -> str:
    counted = [q for q in questions if q.exam not in SKIP_EXAMS]
    fill_qs = [q for q in counted if q.qtype == "fill"]
    order_qs = [q for q in counted if q.qtype == "order"]

    tag_exams: dict[str, set[str]] = defaultdict(set)
    tag_count: Counter[str] = Counter()
    cat_tags: dict[str, set[str]] = defaultdict(set)

    for q in counted:
        primary = q.tags[0]
        tag_count[primary] += 1
        tag_exams[primary].add(q.exam)
        cat_tags[q.categories[0]].add(primary)

    exams = sorted({q.exam for q in questions})
    valid_exams = sorted({q.exam for q in counted})

    out: list[str] = [
        "---",
        "title: N2 文法 · 历年真题考点总表",
        "date: 2026-07-04",
        "tags: 学习/日语/JLPT/N2",
        "column: 学习笔记",
        "toc: true",
        "---",
        "",
        "# N2 文法 · 历年真题考点总表",
        "",
        "> **来源**：`试题集锦` 文件夹真题，正文数据取自 [N2词汇.md](./N2词汇.md) 已收录部分。",
        f"> **套数**：文法 **{len(valid_exams)}** 套有效（2015.07～2025.12；排除串卷 2016.12／2022.12；**2020.07** 取消、**2023.07** 未提供）。",
        f"> **题量**：填空题 **{len(fill_qs)}** 道 ＋ ★语序题 **{len(order_qs)}** 道（去重后统计）。",
        "> **说明**：考点由题干＋选项模式自动归类；「≥2 次」为跨套出现频次。下方 **语法讲解** 含各考点用法与辨析。",
        "",
        "## 跨套高频考点（≥2 次）",
        "",
        "| 次数 | 考点 | 出现考次 |",
        "|:----:|------|----------|",
    ]

    for tag, cnt in tag_count.most_common():
        if tag == "★语序题":
            continue
        if cnt < 2:
            break
        exs = "、".join(sorted(tag_exams[tag]))
        out.append(f"| **{cnt}** | {tag} | {exs} |")

    order_cnt = tag_count.get("★语序题", 0)
    order_exams = len(tag_exams.get("★语序题", set()))
    out += [
        "",
        f"> **★语序题**：共 **{order_cnt}** 道，覆盖 **{order_exams}** 套（每套通常 5 题，不与其他语法点混排频次）。",
        "",
    ]

    out += build_guide_section(tag_count, tag_exams)

    out += ["## 按分类汇总", ""]
    cat_order = [
        "敬语", "授受", "条件", "原因", "逆接", "时间", "限定", "程度", "确信",
        "变化", "关系", "强调", "让步", "语气", "形式名词", "时点", "倾向", "可能",
        "固定", "补助", "假设", "引用", "副词", "语序", "助词", "接续", "其他", "语境",
    ]
    seen_cats = set()
    for cat in cat_order:
        if cat not in cat_tags:
            continue
        seen_cats.add(cat)
        tags = sorted(cat_tags[cat], key=lambda t: (-tag_count[t], t))
        out.append(f"### {cat}（{len(tags)} 项）")
        out.append("")
        for t in tags:
            exs = "、".join(sorted(tag_exams[t]))
            out.append(f"- **{t}** ×{tag_count[t]} — {exs}")
        out.append("")

    for cat in sorted(set(cat_tags) - seen_cats):
        tags = sorted(cat_tags[cat], key=lambda t: (-tag_count[t], t))
        out.append(f"### {cat}（{len(tags)} 项）")
        out.append("")
        for t in tags:
            exs = "、".join(sorted(tag_exams[t]))
            out.append(f"- **{t}** ×{tag_count[t]} — {exs}")
        out.append("")

    out += ["## 全部考点一览（按频次）", ""]
    for tag, cnt in tag_count.most_common():
        exs = "、".join(sorted(tag_exams[tag]))
        out.append(f"- **{cnt}** · {tag} — {exs}")
    out.append("")

    out += ["## 分套真题文法题", ""]
    by_exam: dict[str, list[GrammarQ]] = defaultdict(list)
    for q in questions:
        by_exam[q.exam].append(q)

    for eid in exams:
        qs = by_exam.get(eid, [])
        if not qs:
            continue
        note = ""
        if eid in SKIP_EXAMS:
            note = "（串卷，频次未计入）"
        elif eid in {"2025.12"}:
            note = "（★ 语序与 2015.07 重复）"
        out.append(f"### {eid.replace('.', '年')}月{note}")
        out.append("")
        for q in sorted(qs, key=lambda x: x.num):
            label = "★语序" if q.qtype == "order" else "填空"
            tag_str = q.tags[0]
            summary, full_body, example, tip = explain(tag_str)
            stem_short = q.stem[:100] + ("…" if len(q.stem) > 100 else "")
            out.append(f"**{q.num}** [{label}] **{tag_str}**")
            out.append(f"- **要点**：{summary}")
            out.append(f"- **题干**：{stem_short}")
            if q.options:
                opts = "　".join(f"{i+1}.{o}" for i, o in enumerate(q.options[:4]))
                out.append(f"- **选项**：{opts}")
            if example and example != "—":
                out.append(f"- **例句**：{example}")
            if tip and tip not in ("—", "注意与形近语法区分。"):
                out.append(f"- **做题**：{tip[:300]}")
            out.append("")

    out += [
        "## 收录说明",
        "",
        "- 2011～2014 年真题在 `试题集锦` 中为 PDF/DOC，尚未全文提取；本表基于 **2015.07～2025.12** 已整理正文。",
        "- **2016.12 ≈ 2015.12**、**2022.12 ≈ 2021.12**、**2025.12 文法★ ≈ 2015.07 問題8**。",
        "- 需要把 2011～2014 文法也纳入时，可先运行 `web/scripts/extract-n2-exam-text.py` 提取文本后再更新。",
        "",
    ]
    return "\n".join(out)


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    questions = parse_questions(text)
    md = build_md(questions)
    OUT.write_text(md, encoding="utf-8")
    counted = [q for q in questions if q.exam not in SKIP_EXAMS]
    print(f"parsed {len(questions)} grammar questions")
    print(f"counted {len(counted)} (excl duplicates)")
    print(f"unique tags {len({t for q in counted for t in q.tags})}")
    print(f"written {OUT}")


if __name__ == "__main__":
    main()
