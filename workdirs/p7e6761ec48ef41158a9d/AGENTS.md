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

Consider a chess board, with the numbers $1$ through $64$ placed in the squares as in the diagram below.

\[\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline
9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 \\
\hline
17 & 18 & 19 & 20 & 21 & 22 & 23 & 24 \\
\hline
25 & 26 & 27 & 28 & 29 & 30 & 31 & 32 \\
\hline
33 & 34 & 35 & 36 & 37 & 38 & 39 & 40 \\
\hline
41 & 42 & 43 & 44 & 45 & 46 & 47 & 48 \\
\hline
49 & 50 & 51 & 52 & 53 & 54 & 55 & 56 \\
\hline
57 & 58 & 59 & 60 & 61 & 62 & 63 & 64 \\
\hline
\end{tabular}\]

Assume we have an infinite supply of knights. We place knights in the chess board squares such that no two knights attack one another and compute the sum of the numbers of the cells on which the knights are placed. What is the maximum sum that we can attain?

Note. For any $2\times3$ or $3\times2$ rectangle that has the knight in its corner square, the knight can attack the square in the opposite corner.

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
