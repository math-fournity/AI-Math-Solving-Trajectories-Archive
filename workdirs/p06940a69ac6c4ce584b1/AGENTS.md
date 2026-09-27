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

In a remote high-tech research facility, six power stations are arranged in a perfect circle, indexed clockwise from 1 to 6. Initially, Station 1 contains a stockpile of $n$ fuel cells, where $n$ is an integer such that $1 \le n \le 100$. All other stations (2 through 6) begin with zero fuel cells.

The facility operates under a specific redistribution protocol: if any station contains at least 4 fuel cells, it can trigger a "discharge cycle." During one cycle, that station consumes 1 fuel cell to power its internal systems, transmits 1 fuel cell to its clockwise neighbor, transmits 1 fuel cell to its counter-clockwise neighbor, and transmits 1 fuel cell to the station directly across the circle.

A configuration is defined as "balanced" if there exists a finite sequence of these discharge cycles that results in every station holding exactly the same number of fuel cells. 

Let $S$ be the set of all possible initial values of $n \in \{1, 2, \dots, 100\}$ for which a balanced configuration can be achieved. Find the sum of all elements in $S$.

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
