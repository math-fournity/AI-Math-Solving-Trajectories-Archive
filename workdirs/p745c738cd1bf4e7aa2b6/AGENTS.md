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

In a remote logistics hub, two rival managers, Max and Mini, are tasked with configuring the final weight distribution for a two-stage rocket delivery. The control panel displays two rows of four empty slots, representing two 4-digit integers:

Top Row: $[A][B][C][D]$
Bottom Row: $[E][F][G][H]$

The final payload weight is calculated by subtracting the total value of the bottom row from the total value of the top row (Top Row − Bottom Row).

The process follows a strict protocol:
1. Max (the first player) selects a single digit from the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$. 
2. Immediately after a digit is called, Mini (the second player) must decide which of the eight empty slots ($A$ through $H$) to lock that digit into.
3. This sequence repeats 8 times until every slot is filled. 

Note that Max may choose the same digit multiple times; he is not restricted to unique numbers. Max’s objective is to coordinate his calls so that the final calculated difference is as large as possible. Conversely, Mini’s objective is to place those digits in a way that makes the final difference as small as possible.

Assuming both managers play with perfect mathematical strategy to achieve their respective goals, find the value of the final difference.

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
