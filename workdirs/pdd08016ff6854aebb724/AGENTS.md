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

In a specialized chemical processing plant, three catalysts—**Alpha (a)**, **Beta (b)**, and **Gamma (c)**—are used in varying positive concentrations to stabilize a reaction.

The efficiency of the reaction is determined by the sum of three relative concentration ratios. For each pair of catalysts, the plant monitors the cubic efficiency of the first relative to the total mass of the pair: 
$(\frac{a}{a+b})^3 + (\frac{b}{b+c})^3 + (\frac{c}{c+a})^3$.

To improve stability, a safety engineer introduces a "Synergy Factor," represented by a constant **k**. This factor is multiplied by the product of all three concentrations and then divided by the product of the three pairwise mass sums: 
$\frac{k \cdot a \cdot b \cdot c}{(a+b)(b+c)(c+a)}$.

The plant’s safety protocol dictates that the sum of the cubic efficiencies plus this Synergy Factor must always be greater than or equal to a baseline threshold defined by the formula $\frac{3+k}{8}$, regardless of the specific positive concentrations of $a, b,$ and $c$.

What is the best (largest) constant **k** that ensures this safety inequality holds true for all possible positive concentrations of the three catalysts?

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
