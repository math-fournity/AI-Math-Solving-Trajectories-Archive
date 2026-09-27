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

A specialized logistics company manages a high-security warehouse where the total volume of $n$ distinct storage containers, measured in cubic meters as $x_1, x_2, \dots, x_n$, must have a combined product of exactly $1980$. Each container's volume $x_i$ must be a natural number.

To ensure structural stability, the facility’s engineering protocol requires that for every container from the first to the $(n-1)$-th, a "stability index" $a_i$ must be calculated. This index is defined by the sum of the container's volume $x_i$ and the warehouse’s total capacity constant $1980$ divided by that same volume $x_i$. 

Specifically, for each $i = 1, 2, \dots, n-1$, the equation $x_i + \frac{1980}{x_i} = a_i$ must be satisfied, where each stability index $a_i$ is a natural number. Furthermore, these indices must be strictly increasing, such that $a_1 < a_2 < \dots < a_{n-1}$.

Find the greatest natural number $n$ for which it is possible to select such natural numbers $x_1, x_2, \dots, x_n$ and $a_1, a_2, \dots, a_{n-1}$ to satisfy these conditions.

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
