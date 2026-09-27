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

In a sprawling subterranean data center, an engineer is tasked with monitoring a network of $2011 \times 2011$ interconnected servers. Each server is assigned a unique identification code from the set of integers $\{1, 2, 3, \dots, 2011^2\}$, such that every code is used exactly once.

The server racks are arranged in a seamless grid that wraps around both horizontally and vertically. Specifically, the server at the end of any row is directly connected to the server at the beginning of that same row, and the server at the top of any column is directly connected to the server at the bottom of that same column. Two servers are considered "adjacent" if they are next to each other in the same row or the same column, accounting for this wrap-around connectivity.

The engineer is concerned about the "voltage leap" between adjacent units, defined as the absolute difference between their identification codes. They wish to determine the most significant guaranteed leap.

Determine the largest positive integer $M$ such that, regardless of how the identification codes are distributed across the grid, there must exist at least two adjacent servers whose codes differ by at least $M$.

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
