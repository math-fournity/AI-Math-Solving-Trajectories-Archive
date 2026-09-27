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

A specialized logistics drone is tasked with inspecting a solar array grid. The array consists of $3n$ solar panels arranged in a rectangular formation of $n$ columns and $3$ rows. Each panel's center can be represented by a coordinate $(c, r)$ where $c \in \{1, 2, \dots, n\}$ identifies the column and $r \in \{1, 2, 3\}$ identifies the row.

The drone must perform a "Full-Grid Inspection," which is defined by the following flight parameters:
1. The drone moves in a sequence of $3n$ positions, $p_1, p_2, \dots, p_{3n}$, where each position corresponds to the center of a different solar panel.
2. Between any two consecutive steps $p_i$ and $p_{i+1}$, the drone must travel exactly 1 unit of distance (moving either to an adjacent row in the same column or an adjacent column in the same row).
3. The drone must visit every single panel in the $n \times 3$ grid exactly once.

The drone's mission is programmed to always begin the inspection at the panel located at $(1, 1)$ and conclude the inspection at the panel located at $(n, 1)$.

In terms of $n$, how many distinct inspection paths are possible for the drone to complete this mission?

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
