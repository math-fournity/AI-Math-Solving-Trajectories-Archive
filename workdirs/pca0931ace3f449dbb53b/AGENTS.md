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

In a specialized manufacturing facility, three high-precision chemical catalysts—Alpha ($a$), Beta ($b$), and Gamma ($c$)—are used to stabilize a reaction. The concentrations of these catalysts, measured in parts per million, are all strictly positive values.

The chemical stability of the system is governed by a precise equilibrium equation. Specifically, the sum of the reciprocals of the Alpha and Beta concentrations, reduced by the reciprocal of the Gamma concentration, must exactly equal the value of 4 divided by the combined net concentration of the three (calculated as the sum of Alpha and Beta minus Gamma). This relationship is expressed as:
$$\frac{1}{a} + \frac{1}{b} - \frac{1}{c} = \frac{4}{a+b-c}$$

The efficiency index of the entire production cycle, denoted as $P$, is determined by multiplying two distinct factors. The first factor is the sum of the fifth powers of the three catalyst concentrations ($a^5 + b^5 + c^5$). The second factor is the sum of the reciprocals of those same fifth powers ($\frac{1}{a^5} + \frac{1}{b^5} + \frac{1}{c^5}$).

Based on the required equilibrium constraint, find the minimum possible value for the efficiency index $P$.

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
