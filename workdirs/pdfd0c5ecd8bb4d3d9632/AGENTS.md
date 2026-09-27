# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

# Problem

In a remote desert, three observation outposts—Alpha, Bravo, and Charlie—form a triangle. At outpost Alpha, the surveyor measures the angle between the lines of sight to Bravo and Charlie to be exactly $50^\circ$.

A central communications hub, Station P, is located inside the triangular region formed by the three outposts. The logistics team notes that Station P is positioned such that its distance to outpost Bravo is exactly equal to its distance to outpost Charlie.

To coordinate signals, two linear cables are laid down: one connects Bravo to Station P and extends to meet the perimeter road between Alpha and Charlie at a junction point called East-Gate; the other connects Charlie to Station P and extends to meet the perimeter road between Alpha and Bravo at a junction point called Frost-Gate.

An engineer at the communications hub measures the internal alignment of these junctions. They find that the angle formed at East-Gate between Station P and Frost-Gate is $50^\circ$. Furthermore, the angle formed at Frost-Gate between Station P and East-Gate is $30^\circ$.

Based on this surveying data, determine the measure of the angle at outpost Charlie (the angle formed between the lines of sight to outposts Alpha and Bravo).

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
