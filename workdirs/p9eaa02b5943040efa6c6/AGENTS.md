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

A logistics company manages two types of supply chains: a "Steady-Rate" line (represented by the sequence $a_n$) and an "Exponential-Growth" line (represented by the sequence $b_n$). 

The Steady-Rate line follows a linear progression where each day ($n$) the quantity $a_n$ increases or decreases by a fixed constant. Simultaneously, the Exponential-Growth line follows a geometric progression where each day the quantity $b_n$ is multiplied by a constant ratio.

The company tracks the "Integrated Output" of these two lines by calculating the product of their daily quantities ($a_n \times b_n$). The records for the first three days show the following total outputs:
- On Day 1, the output $a_1 b_1$ was exactly 20 units.
- On Day 2, the output $a_2 b_2$ was exactly 19 units.
- On Day 3, the output $a_3 b_3$ was exactly 14 units.

Based on the mathematical constraints of these two sequences, find the greatest possible value for the Integrated Output on Day 4 ($a_4 b_4$).

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
