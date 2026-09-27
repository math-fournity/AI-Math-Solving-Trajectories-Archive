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

Find the inverse of 1/839 times the matrix and calculate the trace (sum of diagonal elements) of the inverse. Round your answer to the nearest integer:
[[23, 8, -27, 1, 0, -8, 6, 7, 6, 30, 19, 12],
 [0, -9, 31, -23, 9, -26, -27, 18, -9, -2, -35, -4],
 [0, 0, -16, -1, -19, -18, 9, 17, 32, 29, -35, 22],
 [0, 0, 0, 23, 5, -31, 29, -19, -14, 5, 32, 33],
 [0, 0, 0, 0, -10, -17, 24, 35, 11, 35, -10, 4],
 [0, 0, 0, 0, 0, -28, 5, -17, 10, -8, 32, -21],
 [0, 0, 0, 0, 0, 0, 27, 25, 0, -12, -12, -32],
 [0, 0, 0, 0, 0, 0, 0, 17, 26, 5, 21, 24],
 [0, 0, 0, 0, 0, 0, 0, 0, -33, 15, 11, 32],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, -11, -9, 15],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, -4],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29]]

Present the answer in LaTex format: \boxed{Your answer}

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
