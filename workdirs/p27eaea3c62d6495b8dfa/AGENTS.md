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

A specialized chemical refinery operates using two catalysts, $x$ and $y$, measured in positive real-valued concentrations. The efficiency of a specific refining process is governed by a continuous performance function $f: \mathbb{R}^+ \to \mathbb{R}^+$.

The plant’s total energy output is determined by a complex interaction between these catalysts. On one side of the equilibrium equation, the engineers combine the performance of the net yield—calculated as the function of the product of the concentrations minus the product itself—with the weighted performance contributions of each individual catalyst (concentration $x$ times the performance of $y$, plus concentration $y$ times the performance of $x$).

This sum is found to be perfectly balanced by the sum of the performance of the product of the concentrations and the product of the individual performance values of $x$ and $y$. Mathematically, for all $x, y \in \mathbb{R}^+$, the system follows the rule:
\[ f(f(xy) - xy) + xf(y) + yf(x) = f(xy) + f(x)f(y) \]

Let $S$ be the set of all continuous functions that satisfy this equilibrium. For every valid function $f$ in $S$, calculate the specific performance value when the catalyst concentration is exactly $2$ units (i.e., $f(2)$). 

Determine the sum of all possible values of $f(2)$ that result in an integer within the range $[2, 10]$.

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
