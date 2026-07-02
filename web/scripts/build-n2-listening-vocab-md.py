#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 N2 听力原文统计高频词汇，输出 Markdown。"""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
LISTEN_DIR = Path(r"d:\Study\日语\N2\听力")
CSV_PATH = SCRIPTS / "_n2_jamsin.csv"
FREQ_JSON = SCRIPTS / "_n2_freq.json"
OUT = ROOT / "content" / "posts" / "N2听力高频词汇.md"

# 指令/旁白，不计入词汇匹配语料
SKIP_PATTERNS = [
    r"^\[音声\]$",
    r"^問題\d",
    r"^例\s",
    r"最も良いもの",
    r"問題用紙",
    r"日本語能力試験",
    r"常会|聴解|超解",
    r"メモをとって",
    r"手を挙げて",
    r"では始めます|では練習|いつでもいい",
    r"回答用紙",
    r"天気がいいから散歩",
    r"^\d+番$",
    r"^[1-4]番です",
    r"^[はいん]+$",
    r"^女の人$",
    r"^男の人$",
    r"^女$",
    r"^男$",
]

CACHE_FILE = SCRIPTS / "_n2_meaning_zh_cache.json"

# 旁白/指令词，不计入听力高频统计
STOP_EXPR = {
    "する", "なる", "女の人", "男の人", "お願いします", "お願い", "質問", "問題", "番号",
    "正しい", "間違い", "選択", "答え", "例", "次", "以下", "以上", "構いません", "かまいません",
    "いいえ", "はい", "ええ", "うん", "そう", "そうです", "そうですね", "そうですか",
}

_trans_cache: dict[str, str] = {}


def load_trans_cache() -> None:
    global _trans_cache
    if CACHE_FILE.exists():
        _trans_cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))


def en_to_zh(en: str, expr: str = "") -> str:
    if expr and expr in ZH_OVERRIDE:
        return ZH_OVERRIDE[expr]
    if not en:
        return "（释义待补）"
    if en in _trans_cache:
        return _trans_cache[en]
    zh = en.replace(",", "；").replace(" to ", "；").strip()
    _trans_cache[en] = zh
    return zh


def resolve_vocab(expr: str, merged: dict[str, dict]) -> dict | None:
    if expr in merged:
        it = merged[expr].copy()
        it["zh"] = en_to_zh(it["meaning_en"], expr)
        it["manual"] = False
        return it
    if expr in MANUAL_SCENE_VOCAB:
        reading, zh = MANUAL_SCENE_VOCAB[expr]
        return {
            "expr": expr,
            "reading": reading,
            "meaning_en": "",
            "zh": zh,
            "exam_count": 0,
            "occurrence": 0,
            "exam_sessions": [],
            "rank": None,
            "manual": True,
        }
    return None


def vocab_badge(it: dict) -> str:
    if it.get("exam_count", 0) > 0:
        return f"真题 **{it['exam_count']}** 套"
    if it.get("manual"):
        return "扩展·听高频"
    return "扩展·N2词表"


LISTENING_SCENE = {
    "案内", "伝える", "連絡", "確認", "予約", "届く", "遅れる", "割引", "点検", "故障",
    "相談", "説明", "紹介", "乗り換え", "遅延", "欠席", "出席", "延期", "中止", "変更",
    "届ける", "配達", "受付", "申し込む", "送料", "返品", "交換", "領収書", "症状", "診察",
    "会議", "資料", "締め切り", "提出", "報告", "満席", "空席", "キャンセル", "定員",
    "お知らせ", "通知", "掲示", "振込", "口座", "発送", "配送", "手続き", "営業時間", "定休日",
    "アルバイト", "研修", "実習", "ボランティア", "インタビュー", "発表", "企画", "清掃",
    "チケット", "ホテル", "宿題", "授業", "研究室", "病院", "避難", "地震",
}

# 语料未收录、但 N2 听力各场景极常见（多为 N3 或口语高频，标为听高频扩展）
MANUAL_SCENE_VOCAB: dict[str, tuple[str, str]] = {
    "連絡": ("れんらく", "联系、联络"),
    "予約": ("よやく", "预约"),
    "遅延": ("ちえん", "延误（电车等）"),
    "欠席": ("けっせき", "缺席"),
    "出席": ("しゅっせき", "出席"),
    "延期": ("えんき", "延期"),
    "中止": ("ちゅうし", "取消、中止"),
    "変更": ("へんこう", "变更"),
    "案内": ("あんない", "引导、介绍、告知"),
    "説明": ("せつめい", "说明"),
    "紹介": ("しょうかい", "介绍"),
    "相談": ("そうだん", "商量、咨询"),
    "確認": ("かくにん", "确认"),
    "届く": ("とどく", "送到、收到"),
    "遅れる": ("おくれる", "迟到、延误"),
    "アルバイト": ("アルバイト", "打工、兼职"),
    "キャンセル": ("キャンセル", "取消预约"),
    "掲示": ("けいじ", "张贴告示"),
    "お知らせ": ("おしらせ", "通知、公告"),
    "満席": ("まんせき", "满座"),
    "空席": ("くうせき", "空位"),
    "配達": ("はいたつ", "配送"),
    "受付": ("うけつけ", "受理、前台"),
    "返品": ("へんぴん", "退货"),
    "交換": ("こうかん", "换货、交换"),
    "領収書": ("りょうしゅうしょ", "收据"),
    "症状": ("しょうじょう", "症状"),
    "診察": ("しんさつ", "诊察"),
    "会議": ("かいぎ", "会议"),
    "提出": ("ていしゅつ", "提交"),
    "報告": ("ほうこく", "报告"),
    "営業時間": ("えいぎょうじかん", "营业时间"),
    "故障": ("こしょう", "故障"),
    "点検": ("てんけん", "检修、点检"),
    "発表": ("はっぴょう", "发表、发布会"),
    "企画": ("きかく", "策划"),
    "ボランティア": ("ボランティア", "志愿者"),
    "会場": ("かいじょう", "会场"),
    "参加者": ("さんかしゃ", "参加者"),
    "部活": ("ぶかつ", "社团活动"),
    "文化祭": ("ぶんかさい", "文化节"),
    "終電": ("しゅうでん", "末班车"),
    "試着": ("しちゃく", "试穿"),
    "担当": ("たんとう", "负责（人）"),
    "承認": ("しょうにん", "承认、批准"),
    "病院": ("びょういん", "医院"),
    "薬": ("くすり", "药"),
    "ところで": ("ところで", "对了、顺便说"),
    "ちなみに": ("ちなみに", "顺便一提"),
    "実は": ("じつは", "其实"),
    "もしかして": ("もしかして", "难道、说不定"),
    "せっかく": ("せっかく", "好不容易"),
    "申し込む": ("もうしこむ", "报名、申请"),
    "伝える": ("つたえる", "传达、告诉"),
    "避難": ("ひなん", "避难"),
    "地震": ("じしん", "地震"),
    "満員": ("まんいん", "满员（电车等）"),
    "片道": ("かたみち", "单程"),
    "往復": ("おうふく", "往返"),
}

# 场景词包：真题语料归纳 + 同类场景可能考到的词
SCENE_PACKS: list[dict] = [
    {
        "title": "校园·社团·志愿",
        "hint": "サークル募集、ボランティア、小学生向け活動",
        "words": [
            "サークル", "募集", "活躍", "テーマ", "きっかけ", "ボランティア", "清掃", "研修", "実習",
            "小学生", "発表", "企画", "参加者", "部活", "文化祭", "定員", "締め切り", "当日", "会場", "案内",
        ],
    },
    {
        "title": "通知·说明会·广播",
        "hint": "ポスター、お知らせ、日程変更",
        "words": [
            "資料", "ポスター", "通知", "お知らせ", "掲示", "日時", "当日", "締め切り", "案内", "説明",
            "連絡", "確認", "変更", "延期", "中止", "参加者", "会場",
        ],
    },
    {
        "title": "交通·出行",
        "hint": "電車遅延、乗り換え、出張",
        "words": [
            "コース", "乗り換え", "出張", "平日", "各地", "遅延", "遅れる", "終電", "片道", "往復", "満員",
            "空席", "案内", "変更", "中止",
        ],
    },
    {
        "title": "购物·服务·店铺",
        "hint": "割引、返品、営業時間",
        "words": [
            "割引", "配る", "返品", "交換", "送料", "領収書", "定休日", "営業時間", "受付", "試着",
            "キャンセル", "予約", "確認",
        ],
    },
    {
        "title": "工作·办事·商务",
        "hint": "申請、会議、手続き",
        "words": [
            "申請", "作成", "調整", "手続き", "年度", "出張", "会議", "報告", "提出", "資料", "締め切り",
            "担当", "承認", "相談", "確認",
        ],
    },
    {
        "title": "医疗·健康",
        "hint": "病院予約、症状、診察",
        "words": [
            "病院", "予約", "症状", "診察", "薬", "相談", "確認", "変更", "キャンセル", "連絡",
        ],
    },
    {
        "title": "口语衔接·应答",
        "hint": "对话理解、说话人意图",
        "words": [
            "やっぱり", "そういえば", "それなら", "おかげさまで", "そのため", "ところで", "ちなみに",
            "実は", "もしかして", "せっかく", "きっかけ", "工夫",
        ],
    },
    {
        "title": "灾害·紧急",
        "hint": "地震、避難案内（N2 即时应答常见）",
        "words": [
            "地震", "避難", "案内", "確認", "連絡", "中止", "変更", "お知らせ", "通知",
        ],
    },
]

# 常用词中文覆盖（优先于机翻缓存）
ZH_OVERRIDE: dict[str, str] = {
    "やっぱり": "毕竟、还是",
    "サークル": "社团",
    "工夫": "想办法、下功夫",
    "資料": "资料",
    "テーマ": "主题、课题",
    "小学生": "小学生",
    "当日": "当天、活动当天",
    "きっかけ": "契机、起因",
    "コース": "课程、路线",
    "ポスター": "海报",
    "募集": "招募",
    "活躍": "活跃、大展身手",
    "対策": "对策",
    "主人": "丈夫（自称）",
    "出張": "出差",
    "年度": "年度、财年",
    "平日": "工作日",
    "割引": "折扣",
    "配る": "分发、发放",
    "申請": "申请",
    "日時": "日期和时间",
    "そういえば": "说起来",
    "それなら": "那样的话",
    "そのため": "因此",
    "おかげさまで": "托您的福、多亏",
    "各地": "各地",
    "作成": "制作、编写",
    "調整": "调整",
    "締め切り": "截止日期",
    "手続き": "手续",
    "通知": "通知",
    "乗り換え": "换乘",
    "送料": "运费",
    "定休日": "定休日",
    "研修": "培训",
    "実習": "实习、实操",
    "清掃": "清扫",
    "定員": "定员、名额上限",
    "片道": "单程",
    "往復": "往返",
    "満員": "满员（电车拥挤）",
}


def load_csv() -> list[dict]:
    rows = []
    with CSV_PATH.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if "JLPT_2" in r.get("tags", ""):
                rows.append(r)
    return rows


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


def exam_id_from_name(name: str) -> str:
    n = name.lower().replace(".txt", "")
    if n.startswith("201007"):
        return "2010.07"
    m = re.match(r"(\d{4})-(\d{2})", n)
    if m:
        return f"{m.group(1)}.{m.group(2)}"
    m = re.match(r"(\d{4})-(\d)", n)
    if m:
        return f"{m.group(1)}.0{m.group(2)}"
    return n


def clean_line(line: str) -> str:
    line = re.sub(r"^\[\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}\]\s*", "", line)
    return line.strip()


def is_skip_line(s: str) -> bool:
    if not s or len(s) < 2:
        return True
    for pat in SKIP_PATTERNS:
        if re.search(pat, s):
            return True
    return False


def load_listening_corpus() -> list[dict]:
    by_exam: dict[str, list[str]] = defaultdict(list)
    for f in sorted(LISTEN_DIR.glob("*.txt")):
        eid = exam_id_from_name(f.stem)
        lines = []
        for raw in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            s = clean_line(raw)
            if is_skip_line(s):
                continue
            lines.append(s)
        by_exam[eid].extend(lines)
    out = []
    for eid in sorted(by_exam):
        text = "\n".join(by_exam[eid])
        jp = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", text))
        out.append({"exam_id": eid, "text": text, "jp_chars": jp, "files": list(LISTEN_DIR.glob(f"*{eid.replace('.', '-')}*"))})
    return out


def word_in_text(expr: str, reading: str, text: str) -> int:
    count = 0
    if expr and len(expr) >= 2:
        count += len(re.findall(re.escape(expr), text))
    if reading and len(reading) >= 2:
        pat = r"(?<![ぁ-んァ-ヶ一-龥ー])" + re.escape(reading) + r"(?![ぁ-んァ-ヶ一-龥ー])"
        count += len(re.findall(pat, text))
    return count


def main() -> None:
    load_trans_cache()
    corpus = load_listening_corpus()
    exam_ids = [c["exam_id"] for c in corpus]
    print(f"[listen] 语料 {len(corpus)} 套: {', '.join(exam_ids)}")

    freq = load_freq()
    merged: dict[str, dict] = {}
    for r in load_csv():
        expr = r["expression"]
        if expr in STOP_EXPR:
            continue
        if expr not in merged:
            merged[expr] = {
                "expr": expr,
                "reading": r["reading"],
                "meaning_en": re.sub(r"\s+", " ", r["meaning"].strip().strip('"')),
                "rank": freq.get((expr, r["reading"])),
            }

    for expr, it in merged.items():
        sessions: list[str] = []
        total = 0
        for c in corpus:
            n = word_in_text(expr, it["reading"], c["text"])
            if n:
                sessions.append(c["exam_id"])
                total += n
        it["exam_count"] = len(sessions)
        it["occurrence"] = total
        it["exam_sessions"] = sessions

    matched = [it for it in merged.values() if it["exam_count"] > 0]
    matched.sort(key=lambda x: (-x["exam_count"], -x["occurrence"], x.get("rank") or 99999))

    # 场景扩充词（去重）
    scene_all: list[str] = []
    seen_scene: set[str] = set()
    for pack in SCENE_PACKS:
        for w in pack["words"]:
            if w not in seen_scene:
                seen_scene.add(w)
                scene_all.append(w)
    scene_resolved = [resolve_vocab(w, merged) for w in scene_all]
    scene_resolved = [it for it in scene_resolved if it]
    corpus_in_scene = sum(1 for it in scene_resolved if it["exam_count"] > 0)
    expand_in_scene = sum(1 for it in scene_resolved if it["exam_count"] == 0)

    lines = [
        "---",
        "title: N2 听力 · 真题高频词汇",
        "date: 2026-06-30",
        "tags: 学习/日语/JLPT/N2",
        "column: 学习笔记",
        "toc: true",
        "---",
        "",
        "# N2 听力 · 真题高频词汇",
        "",
        f"> **语料**：`d:/Study/日语/N2/听力` 内 **{len(corpus)}** 套听力原文（{', '.join(exam_ids)}）。",
        f"> **词条**：N2 词表 **{len(merged)}** 词；听力语料中命中 **{len(matched)}** 词；场景扩充 **{len(scene_resolved)}** 词（其中语料未命中 **{expand_in_scene}**）。",
        "> **排序**：真题部分按 **出现套数** → **出现次数**；扩充部分按场景归类。",
        "",
        "## 考频分级",
        "",
        "| 级别 | 出现套数 | 建议 |",
        "|------|----------|------|",
        "| **S** | ≥6 套 | 听力必背场景词 |",
        "| **A** | 4–5 套 | 高频 |",
        "| **B** | 2–3 套 | 重点复习 |",
        "| **C** | 1 套 | 考过需认识 |",
        "",
        "## 速览 Top 30",
        "",
    ]

    top30 = matched[:30]
    lines.append("| 词 | 中文 | 套数 | 次数 |")
    lines.append("|----|------|------|------|")
    for it in top30:
        mark = "🎧 " if it["expr"] in LISTENING_SCENE else ""
        lines.append(
            f"| {mark}{it['expr']} | {en_to_zh(it['meaning_en'], it['expr'])[:24]} | {it['exam_count']} | {it['occurrence']} |"
        )
    lines += ["", "## 按级别展开", ""]

    def tier(n: int) -> str:
        if n >= 6:
            return "S"
        if n >= 4:
            return "A"
        if n >= 2:
            return "B"
        return "C"

    current_tier = None
    for it in matched:
        t = tier(it["exam_count"])
        if t != current_tier:
            current_tier = t
            label = {"S": "S级·≥6套", "A": "A级·4–5套", "B": "B级·2–3套", "C": "C级·1套"}[t]
            lines += ["", f"## {label}", ""]

        scene = " 🎧" if it["expr"] in LISTENING_SCENE else ""
        zh = en_to_zh(it["meaning_en"], it["expr"])
        sess = "、".join(it["exam_sessions"])
        lines.append(f"#### {it['expr']}：{zh}{scene}")
        lines.append("")
        lines.append(
            f"> 読み {it['reading']} · 听力 **{it['exam_count']}** 套（共 **{it['occurrence']}** 次｜{sess}）"
            + (f" · 词表序 #{it['rank'] + 1}" if it.get("rank") is not None else "")
            + f" · 英：{it['meaning_en'][:80]}"
        )
        lines.append("")

    # 场景扩充
    lines += [
        "",
        "## 按场景扩充（真题 + 可能高频）",
        "",
        f"> 共 **{len(scene_resolved)}** 词：语料已命中 **{corpus_in_scene}** · 扩展补充 **{expand_in_scene}**（标 *扩展* 者未在本批 8 套原文出现，但同场景极高频）。",
        "",
    ]
    for pack in SCENE_PACKS:
        lines += [f"### {pack['title']}", "", f"> {pack['hint']}", ""]
        lines.append("| 词 | 読み | 中文 | 来源 |")
        lines.append("|----|------|------|------|")
        for w in pack["words"]:
            it = resolve_vocab(w, merged)
            if not it:
                continue
            zh = it["zh"] if it.get("manual") or it["expr"] in ZH_OVERRIDE else en_to_zh(it["meaning_en"], it["expr"])
            src = vocab_badge(it)
            if it["exam_count"] > 0:
                src += f"（{it['occurrence']}次）"
            mark = "🎧 " if w in LISTENING_SCENE or it.get("manual") else ""
            lines.append(f"| {mark}{w} | {it['reading']} | {zh} | {src} |")
        lines.append("")

        # 场景要点（仅扩充词）
        extras = []
        for w in pack["words"]:
            it = resolve_vocab(w, merged)
            if it and it["exam_count"] == 0:
                extras.append(w)
        if extras:
            lines.append("**本场景建议额外背诵**：" + "、".join(f"**{w}**" for w in extras[:12]) + "。")
            lines.append("")

    # 场景词速记
    top_scene = [it for it in matched if it["expr"] in LISTENING_SCENE][:40]
    lines += [
        "",
        "## 听力场景词速记（命中语料）",
        "",
        " · ".join(f"**{it['expr']}**（{it['exam_count']}套）" for it in top_scene[:25]),
        "",
        "---",
        "",
        "## 说明",
        "",
        "- 语料为字幕/听写文本，已剔除「問題用紙を開けて」等考场指令。",
        "- 标 🎧 者为听力场景词；**扩展·听高频** 多为 N3/口语词，但 N2 听力对话中极常见。",
        "- **扩展·N2词表** 为 N2 词表内词，本批语料未出现，同类真题仍可能考到。",
        "- 可与 [`N2词汇.md`](N2词汇.md) 文字語彙真题对照复习。",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[listen] → {OUT}")
    print(f"  命中 {len(matched)} 词，S级 {sum(1 for it in matched if tier(it['exam_count'])=='S')} 个")


if __name__ == "__main__":
    main()
