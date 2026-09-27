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

In a massive logistics hub, a highly specialized automated sorting robot operates on a grid of shipping containers arranged in a square block of 999 rows and 999 columns. Due to its unique mechanical constraints, the robot can only move between containers that share a direct side. Furthermore, its steering system is restricted: after every single move between two containers, the robot must perform a 90-degree turn. This means it can never move in the same direction twice in a row (e.g., if it moves North, its next move must be East or West).

A "delivery circuit" is defined as a sequence of distinct container locations that the robot visits one by one. To avoid collisions and maintain system integrity, the robot is strictly forbidden from visiting the same container more than once in a single circuit. A circuit is considered "cyclic" if, after arriving at the final container in the sequence, the robot is positioned such that its very next move brings it back to the first container of the sequence while still obeying the mandatory turn rule (meaning the move from the last square to the first square must be perpendicular to the move that brought it to the last square, and the move from the first square to the second square must be perpendicular to the move from the last square to the first).

What is the maximum number of containers that can be included in such a cyclic, non-intersecting delivery circuit?

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
