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

In a specialized laboratory, a team of researchers is testing the stability of a circular chemical chain. They are experimenting with $n$ distinct chemical concentrations, $x_1, x_2, \dots, x_n$, where $n$ is an integer such that $4 \leq n \leq 30$.

The concentrations are arranged in a specific sequence around a ring. The laboratory protocol requires that every set of three adjacent concentrations in the ring must be "balanced." A set of three values is considered balanced if, when they are sorted from smallest to largest, the difference between the middle value and the smallest value is exactly equal to the difference between the largest value and the middle value.

This balancing rule applies to every triplet of neighbors around the entire cycle:
- $\{x_1, x_2, x_3\}$
- $\{x_2, x_3, x_4\}$
- ...
- $\{x_{n-2}, x_{n-1}, x_n\}$
- $\{x_{n-1}, x_n, x_1\}$
- $\{x_n, x_1, x_2\}$

Let $S$ be the set of all possible values for the number of chemicals $n$ in the range $4 \leq n \leq 30$ for which such a sequence of distinct concentrations can actually exist. 

Determine the sum of all elements in $S$.

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
