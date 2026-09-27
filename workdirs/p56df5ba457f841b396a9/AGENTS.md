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

A network of 1000 server hubs is arranged in a perfect physical circle, indexed $i = 1, 2, \dots, 1000$. Each hub $i$ possesses two non-negative integer settings: a power level $a(i)$ and a scanning range $b(i)$. Because the hubs are in a circle, the indices wrap around such that $i \pm 1000 = i$.

A hub $i$ is considered "balanced" if its power level $a(i)$ is exactly equal to the arithmetic mean of the power levels of itself and its neighbors within its scanning range $b(i)$. That is, $a(i)$ must be the average of the $2b(i) + 1$ power levels from $a(i - b(i))$ through $a(i + b(i))$.

In this specific network, every hub is balanced with respect to its scanning range (each $a(i)$ is the mean of its neighbors over range $b(i)$), and simultaneously, every hub's scanning range is balanced with respect to its power level (each $b(i)$ is the mean of the scanning ranges of its neighbors over a range defined by its power level $a(i)$).

It is observed that the power levels across the hubs are not all identical, and the scanning ranges across the hubs are not all identical.

Let $Z$ be the total number of settings across both sequences ($a$ and $b$) that are set to zero. What is the minimum possible value of $Z$?

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
