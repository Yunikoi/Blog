# -*- coding: utf-8 -*-
"""Reformat 高考数学复习专项.md for KaTeX + clean example layout."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "content/posts/高考数学复习专项.md"
lines = MD.read_text(encoding="utf-8").splitlines()

out = []
i = 0
while i < len(lines):
    line = lines[i]

    # Math normalization
    line = line.replace(r"\subsetneqq", r"\subsetneq")
    line = line.replace(r"\varnothing", r"\emptyset")

    if line.startswith("### 通俗解释"):
        out.append("### 核心概念")
        i += 1
        continue
    if line.startswith("### 符号速查"):
        out.append("### 符号一览")
        i += 1
        continue
    if line.startswith("### 例题"):
        num = line.replace("### 例题", "").strip()
        out.append(f"#### 例 {num}")
        out.append("")
        i += 1
        continue

    if line.startswith("**题**"):
        out.append("> **题目**  ")
        out.append("> " + line.replace("**题**　", "").replace("**题** ", ""))
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("**解**") and not lines[i].startswith("**答**") and not lines[i].startswith("> **易错"):
            if lines[i].strip():
                out.append("> " + lines[i].strip())
            i += 1
        out.append("")
        continue

    if line.startswith("**解**"):
        out.append("> **解答**  ")
        rest = line.replace("**解**　", "").replace("**解** ", "").strip()
        if rest:
            out.append("> " + rest)
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("**答**") and not lines[i].startswith("> **易错") and not lines[i].startswith("---") and not lines[i].startswith("#### ") and not lines[i].startswith("### ") and not lines[i].startswith("## "):
            out.append("> " + lines[i].strip())
            i += 1
        out.append("")
        continue

    if line.startswith("**答**"):
        out.append("> **答案**  ")
        out.append("> " + line.replace("**答**　", "").replace("**答** ", ""))
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("> **易错") and not lines[i].startswith("---") and not lines[i].startswith("#### ") and not lines[i].startswith("### ") and not lines[i].startswith("## "):
            out.append("> " + lines[i].strip())
            i += 1
        out.append("")
        continue

    if line.startswith("> **易错**"):
        out.append(line.replace("> **易错**：", "> **易错提醒**  "))
        i += 1
        continue

    if "B  entirely 在 A 右侧之外" in line:
        line = line.replace("B  entirely 在 A 右侧之外", "B 完全在 A 的右侧之外")

    out.append(line)
    i += 1

text = "\n".join(out)
text = text.replace(
    "| **描述法** | `{ x ∈ 某范围 | 满足某条件 }` | 元素 **很多或无穷** |",
    "| **描述法** | $\\{ x \\in \\text{范围} \\mid \\text{条件} \\}$ | 元素 **很多或无穷** |",
)

# Display formula for subset count
marker = "**为什么？** 每个元素在子集中"
if marker in text and "2^n" not in text.split(marker)[0][-200:]:
    text = text.replace(
        marker,
        "$$|A|=n \\text{ 时，子集个数 }=2^n$$\n\n" + marker,
    )

MD.write_text(text + "\n", encoding="utf-8")
print("OK", len(out), "lines")
