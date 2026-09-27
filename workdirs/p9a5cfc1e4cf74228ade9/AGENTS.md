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

A specialized deep-sea research station is testing the stability of two pressure-regulating ballast tanks, represented by the variables $x$ and $y$. The energy output of the primary hydraulic system is defined by the cubic combination $x^3 + x^2y + xy^2 + y^3$. For the station to maintain equilibrium, this energy output must exactly equal a calibrated safety threshold. This threshold is calculated as 8 times the sum of the system’s quadratic surface tension $(x^2 + xy + y^2)$ and a constant unit of atmospheric pressure (1).

The station’s computer identifies all possible real-number pairs $(x, y)$ that satisfy this equilibrium equation:
\[ x^3 + x^2y + xy^2 + y^3 = 8(x^2 + xy + y^2 + 1) \]

Let $S$ be the set of all such coordinate pairs $(x, y)$ that balance the system. To calibrate the final safety protocol, the lead engineer needs to aggregate all data points. Calculate the total sum of every $x$-value and every $y$-value found across all valid pairs in $S$. That is, compute:
\[ \sum_{(x,y) \in S} (x + y) \]

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
