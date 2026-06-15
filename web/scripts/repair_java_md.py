# -*- coding: utf-8 -*-
"""Remove duplicate content accidentally inserted in Java guide."""
from pathlib import Path

MD = Path(__file__).resolve().parents[2] / "content/posts/Java期末复习满分攻略.md"
text = MD.read_text(encoding="utf-8")

prog = "# 三、编程题（2 道）"
tail_marker = (
    "## 官方样例题\n\n"
    "![编程题样例：Person / Job / Life / Student](/java-exam/sample-programming.png)\n\n"
    "**题目要求摘要**"
)

i_prog = text.index(prog)
i_step6 = text.index("### 第六步：官方样例 · 对照表（写完打勾）", i_prog)
i_end = text.index("**10 项对 8 项 ≈ 基本分**；全对 ≈ 满分。", i_step6)
i_end = text.index("\n\n---", i_end) + len("\n\n---")

i_tail = text.rindex(tail_marker)

if i_tail <= i_end:
    raise SystemExit(f"repair failed: tail {i_tail} <= end {i_end}")

new_text = text[:i_end] + "\n" + text[i_tail:]
MD.write_text(new_text, encoding="utf-8")
print("OK repaired, lines", new_text.count("\n"), "removed", text.count("\n") - new_text.count("\n"))
