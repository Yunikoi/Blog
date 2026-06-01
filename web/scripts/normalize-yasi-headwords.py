# -*- coding: utf-8 -*-
"""将 Yasi.md 词条标题规范为动词原形 / 名词单数 / 形容词原形等。"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YASI = ROOT / "content" / "posts" / "Yasi.md"

# 标题保持不变的短语 / 固定搭配 / 本身即词典原形
KEEP: set[str] = {
    "civil war",
    "take on",
    "take shape",
    "stem from",
    "split off",
    "provide insight into",
    "is given to",
    "run-off",
    "shot up",
    "clouds of dust",
    "eye blink",
    "rift valley",
    "division of labour",
    "set up shop",
    "knock out",
    "sum up",
    "seek to",
    "dedicated to",
    "export-oriented",
    "ringbark",
    "no-frills",
    "ill-equipped",
    "groundbreaking",
    "worsted",
    "melancholy",
    "anomaly",
    "assembly",
    "tally",
    "embed",
    "data",
    "species",
    "series",
    "headquarters",
    "means",
    "physics",
    "economics",
    "cactus moth",
    "gaining control",
    "cane toad",
    "argentina",
    "radical",
    "backlash",
    "vacuum",
    "grey",
    "seaweed",
    "dumpling",
    "sapling",
    "bell",
    "tidy",
    "silly",
    "breathtaking",
    "sprinkling",
    "swelling",
    "hypothesis",
    "tuberculosis",
    "foetus",
    "prospectus",
    "religious",
    "nervous",
    "indigenous",
    "prestigious",
    "inglorious",
    "boisterous",
    "fibrous",
    "herbivorous",
    "fineness",
    "photosynthesis",
}

# 不规则 / 明确映射（小写键 -> 原形；None 表示不改）
LEMMA: dict[str, str | None] = {
    "sought": "seek",
    "sought to": "seek to",
    "intellectuals": "intellectual",
    "submerged": "submerge",
    "corrupted": "corrupt",
    "paralysed": "paralyse",
    "mystified": "mystify",
    "discoloured": "discolour",
    "curated": "curate",
    "bewildering": "bewilder",
    "billowing": "billow",
    "condescending": "condescend",
    "unfulfilling": "fulfill",
    "nagging": "nag",
    "scorching": "scorch",
    "crossbreeding": "crossbreed",
    "preceding": "precede",
    "underlying": "underlie",
    "unparalleled": "parallel",
    "untapped": "tap",
    "barbed": "barb",
    "prevailing": "prevail",
    "photosynthesis": "photosynthesis",
}


def is_phrase(w: str) -> bool:
    return " " in w.strip()


def to_lemma(word: str) -> str | None:
    w = word.strip()
    low = w.lower()
    if low in KEEP or w in KEEP:
        return None
    if is_phrase(w):
        if low in LEMMA:
            v = LEMMA[low]
            return v if v else None
        return None
    if low in LEMMA:
        v = LEMMA[low]
        return v if v else None

    # 副词 -> 形容词 / 名词
    adv_map = {
        "consequently": "consequent",
        "acoustically": "acoustic",
        "alternatively": "alternative",
        "briefly": "brief",
        "coincidentally": "coincidental",
        "correctly": "correct",
        "decidedly": "decided",
        "diagonally": "diagonal",
        "fairly": "fair",
        "intimately": "intimate",
        "masterfully": "masterful",
        "mildly": "mild",
        "perversely": "perverse",
        "plainly": "plain",
        "presumably": "presumable",
        "rarely": "rare",
        "rigidly": "rigid",
        "ruthlessly": "ruthless",
        "specifically": "specific",
    }
    if low in adv_map:
        return adv_map[low]

    # -ies -> -y
    if re.fullmatch(r"[a-z]{4,}ies", low):
        return low[:-3] + "y"

    # -ves -> -f / -fe
    if re.fullmatch(r"[a-z]{4,}ves", low):
        return low[:-3] + "f"

    # -ing verb/noun
    if low.endswith("ing") and len(low) > 5:
        ing_map = {
            "billowing": "billow",
            "condescending": "condescend",
            "bewildering": "bewilder",
            "unfulfilling": "fulfill",
            "nagging": "nag",
            "scorching": "scorch",
            "crossbreeding": "crossbreed",
        }
        if low in ing_map:
            return ing_map[low]
        # skip noun -ing: building, learning, etc.
        if low in {
            "building",
            "learning",
            "hearing",
            "training",
            "marketing",
            "engineering",
            "reasoning",
            "funding",
            "setting",
            "clothing",
            "groundbreaking",
            "sprinkling",
            "swelling",
            "billing",
            "rating",
            "fishing",
            "nothing",
            "something",
            "everything",
            "during",
            "morning",
            "evening",
            "ceiling",
            "feeling",
            "meeting",
            "writing",
            "reading",
            "heating",
            "lighting",
            "painting",
            "printing",
            "gardening",
            "filtering",
            "clustering",
            "monitoring",
        }:
            return None
        base = low[:-3]
        if base.endswith("e"):
            return base  # make -> making
        # doubling: running -> run
        if len(base) > 2 and base[-1] == base[-2]:
            return base[:-1]
        return base

    # -ed
    if low.endswith("ed") and len(low) > 3:
        ed_map = {
            "submerged": "submerge",
            "corrupted": "corrupt",
            "paralysed": "paralyse",
            "mystified": "mystify",
            "discoloured": "discolour",
            "curated": "curate",
            "barbed": None,
            "unparalleled": None,
            "untapped": None,
            "ill-equipped": None,
            "alarmed": "alarm",
            "concerned": "concern",
            "related": "relate",
            "located": "locate",
            "estimated": "estimate",
            "dominated": "dominate",
            "isolated": "isolate",
            "motivated": "motivate",
            "anticipated": "anticipate",
            "complicated": "complicate",
            "integrated": "integrate",
            "separated": "separate",
            "dedicated": "dedicate",
        }
        if low in ed_map:
            return ed_map[low]
        if low.endswith("ied"):
            return low[:-3] + "y"
        if low.endswith("ated"):
            stem = low[:-4]
            return stem + "e" if stem.endswith(("at", "it", "ut")) else stem + "ate"
        # -ed regular: leaked -> leak
        if low.endswith("ed") and not low.endswith(("eed", "red", "bed", "led", "wed", "fed")):
            if low.endswith("ted"):
                return low[:-2]  # limited -> limit
            if low.endswith("sed"):
                return low[:-2]
            if low.endswith("ced"):
                return low[:-2]
            if low.endswith("ged"):
                return low[:-2]
            if low.endswith("ned"):
                return low[:-2]
            if low.endswith("med"):
                return low[:-2]
            if low.endswith("ped"):
                return low[:-2]
            if low.endswith("ded"):
                return low[:-2]
            if low.endswith("ked"):
                return low[:-2]
            if low.endswith("led") and low != "led":
                return low[:-2]
            if low.endswith("ved"):
                return low[:-2]
            if low.endswith("zed"):
                return low[:-2]
            if low.endswith("xed"):
                return low[:-2]
            # stopped -> stop (double p)
            if len(low) > 4 and low[-3] == low[-4]:
                return low[:-3]
            return low[:-2] if low.endswith("ed") else None

    # 复数（仅 -ies / -ves / 显式映射，避免 words→word 误伤）
    if low in LEMMA:
        return LEMMA[low]
    if low.endswith("ies") and len(low) > 4:
        return low[:-3] + "y"
    if low.endswith("ves") and len(low) > 4:
        return low[:-3] + "f"

    return None


def preserve_case(old: str, new: str) -> str:
    if old[0].isupper() and new[0].islower():
        return new[0].upper() + new[1:]
    return new


def main() -> None:
    text = YASI.read_text(encoding="utf-8")
    pattern = re.compile(r"^(#### )(.+?)(：)", re.M)
    changes: list[tuple[str, str]] = []
    seen_new: dict[str, int] = {}

    def repl(m: re.Match) -> str:
        prefix, head, colon = m.group(1), m.group(2), m.group(3)
        lemma = to_lemma(head)
        if not lemma or lemma.lower() == head.lower():
            return m.group(0)
        new_head = preserve_case(head, lemma)
        changes.append((head, new_head))
        key = new_head.lower()
        seen_new[key] = seen_new.get(key, 0) + 1
        return f"{prefix}{new_head}{colon}"

    new_text = pattern.sub(repl, text)
    if changes:
        YASI.write_text(new_text, encoding="utf-8")
    print(f"已修改 {len(changes)} 个标题")
    for a, b in changes:
        print(f"  {a} → {b}")
    dups = {k: v for k, v in seen_new.items() if v > 1}
    if dups:
        print(f"注意：以下标题出现重复 {len(dups)} 个，请人工合并：")
        for k, v in sorted(dups.items())[:30]:
            print(f"  {k} ({v}次)")


if __name__ == "__main__":
    main()
