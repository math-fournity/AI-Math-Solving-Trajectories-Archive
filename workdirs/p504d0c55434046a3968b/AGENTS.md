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

A high-tech server farm is organized into a massive circular structure consisting of 2011 horizontal rings, where each ring contains 2011 individual server nodes. This configuration forms a seamless data torus: every node is connected to a neighbor above, below, to its left, and to its right. Specifically, if we index the nodes as $(x, y)$ where $x, y \in \{0, 1, \dots, 2010\}$, node $(x, y)$ is adjacent to nodes $(x, y \pm 1 \pmod{2011})$ and $(x \pm 1 \pmod{2011}, y)$.

A technician must assign a unique security ID number to each of the $2011^2$ nodes, using every integer from the set $\{1, 2, \dots, 2011^2\}$ exactly once. The "stress" on a connection between two adjacent nodes is defined as the absolute difference between their assigned ID numbers.

The network's stability depends on the maximum stress found between any two adjacent nodes in the entire system. What is the largest possible integer $M$ such that, no matter how the technician assigns the ID numbers, there will always be at least one pair of adjacent nodes whose ID difference is $M$ or greater?

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
