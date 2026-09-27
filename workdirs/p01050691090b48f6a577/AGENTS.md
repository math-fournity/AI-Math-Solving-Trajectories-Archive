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

An experimental laboratory has 8 specialized storage canisters, each assigned a unique temperature setting (in Celsius) from the following set: $\{-3, -2, -1, 0, 1, 2, 3, 4\}$.

A technician must arrange these 8 canisters in a single row, creating a sequence of positions designated as $x_1$ through $x_8$. The safety protocol for the facility requires that the product of the temperatures of any two adjacent canisters must not decrease as one moves from the beginning of the row to the end.

Specifically, the arrangement must satisfy this safety chain: the product of the temperatures at positions 1 and 2 must be less than or equal to the product of positions 2 and 3, which must be less than or equal to the product of positions 3 and 4, and so on, continuing through the product of positions 7 and 8.

How many distinct permutations of these temperature settings satisfy the requirement $x_1x_2 \le x_2x_3 \le x_3x_4 \le x_4x_5 \le x_5x_6 \le x_6x_7 \le x_7x_8$?

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
