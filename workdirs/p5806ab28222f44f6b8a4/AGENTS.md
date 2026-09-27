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

In a vast desert, three specialized communication outposts—Alpha, Bravo, and Charlie—form a triangular network. The distance between Alpha and Bravo is exactly 13 kilometers, the distance between Bravo and Charlie is 14 kilometers, and the distance between Charlie and Alpha is 15 kilometers.

A specialized signal beam is projected from Alpha. The transmission protocol follows a rigid geometric sequence:
1. The beam is first projected from Alpha in a direction perpendicular to the straight line connecting Bravo and Charlie.
2. Upon reaching the Bravo-Charlie line, the signal is instantaneously retransmitted in a direction perpendicular to the straight line connecting Charlie and Alpha.
3. Upon reaching the Charlie-Alpha line, the signal is retransmitted in a direction perpendicular to the straight line connecting Alpha and Bravo.
4. Upon reaching the Alpha-Bravo line, the signal is retransmitted in a direction perpendicular to the Bravo-Charlie line again.

This cyclic sequence (perpendicular to $BC$, then $CA$, then $AB$) repeats indefinitely. As the signal continues this process, its path eventually converges toward a stable, finite closed polygonal loop, which we denote as $T_{\infty}$.

Determine the ratio of the perimeter of this final polygonal loop $T_{\infty}$ to the perimeter of the triangle formed by outposts Alpha, Bravo, and Charlie. If this ratio is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a+b$?

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
