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

Consider a $6 \times 8$ grid. Let $(R_i, C_j)$ denote the square in row $i$ and column $j$ for $1 \le i \le 6$ and $1 \le j \le 8$. Some unit squares in the grid are filled with numbers such that:
(i) exactly four squares in each row and four squares in each column contain a number,
(ii) each of the numbers 1 through 12 appears exactly twice, and
(iii) for $n=1,2, \ldots, 12$, the shortest path (Manhattan distance) between the pair of $n$'s has length exactly $n$.

The following numbers are already placed in the grid:
- 6 is at $(R_1, C_5)$
- 10 is at $(R_2, C_2)$
- 1 is at $(R_2, C_3)$
- 2 is at $(R_3, C_4)$
- 8 is at $(R_3, C_8)$
- 5 is at $(R_4, C_2)$
- 2 is at $(R_4, C_5)$
- 7 is at $(R_5, C_6)$
- 9 is at $(R_5, C_7)$
- 3 is at $(R_6, C_5)$

Let $(r_n, c_n)$ and $(r_n', c_n')$ be the coordinates of the two squares containing the number $n$. Find the value of the sum $\sum_{n=1}^{12} (r_n + r_n' + c_n + c_n')$.

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
