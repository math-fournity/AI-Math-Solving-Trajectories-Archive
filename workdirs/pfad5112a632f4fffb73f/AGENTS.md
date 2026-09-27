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

In a specialized laboratory, three energy-conducting liquids are stored in a pressurized spherical containment unit. The quantities of these liquids, represented by the variables $x$, $y$, and $z$, are constrained by the physical capacity of the unit such that the sum of their squares, $x^2 + y^2 + z^2$, is exactly equal to 1.

The laboratory aims to measure the total "Stability Index" of this mixture. The index is calculated through a specific interaction of their densities. The first two liquids contribute positively to the index at a power of four ($x^4 + y^4$). However, the third liquid, due to its volatile nature, reduces the index by twice its quantity raised to the fourth power ($-2z^4$). Additionally, there is a complex interference factor created by the interaction of all three liquids, which further reduces the stability by a factor of $3\sqrt{2}$ times the product of the three quantities ($-3\sqrt{2}xyz$).

Given that $x, y,$ and $z$ are any real numbers satisfying the containment constraint, determine the maximum possible Stability Index defined by the expression $x^4 + y^4 - 2z^4 - 3\sqrt{2}xyz$.

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
