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

In a remote digital archipelago, two data grids have been constructed: a square server farm of size $100 \times 100$ and a rectangular logistics hub of size $100 \times 101$. Within these grids, individual processing units are arranged in rows and columns.

Security firewalls are installed in the form of specialized "dual-node blocks." Each block occupies exactly two horizontally or vertically adjacent units. To prevent interference, these blocks are positioned such that no two blocks ever touch, not even at a single corner. Furthermore, the designated entry point at the bottom-left corner $(1,1)$ and the exit point at the top-right corner $(m, n)$ of each grid are always kept clear of blocks.

A signal packet begins at $(1,1)$. Its protocol only allows it to move one unit at a time, and only in two specific directions: East (increasing the first coordinate) or North (increasing the second coordinate). 

We define a stability function $f(m, n)$ for a grid of dimensions $m \times n$. The value of $f(m, n)$ is 1 if, regardless of how the dual-node blocks are legally arranged, there is guaranteed to be at least one path for the signal packet to reach the exit $(m, n)$ without entering any unit occupied by a block. If there exists at least one configuration of blocks that can completely trap the signal or block all paths to the exit, the value of $f(m, n)$ is 0.

Calculate the result of the following expression:
$10 \cdot f(100, 100) + f(100, 101)$

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
