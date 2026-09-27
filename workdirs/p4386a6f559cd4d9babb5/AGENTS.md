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

In a specialized logistics network, a series of cargo containers is delivered day by day. On day $n$, a container arrives with a weight capacity of exactly $c_n$ units, where $c_n$ is a positive integer. This series of deliveries is classified as "Optimally Versatile" if it satisfies a specific distribution property: for every day $n$, any target total weight $m$ (where $m$ is any integer from $1$ up to the cumulative capacity delivered through that day, $c_1 + c_2 + \dots + c_n$) must be exactly representable as a sum of fractional loads from each available container. 

Specifically, for a given $m$, there must exist positive integers $a_1, a_2, \dots, a_n$ such that:
$m = \frac{c_1}{a_1} + \frac{c_2}{a_2} + \dots + \frac{c_n}{a_n}$

Let $C(n)$ denote the maximum possible weight capacity that the $n$-th container can have while still allowing the entire sequence to remain "Optimally Versatile." 

Find the value of $C(10)$.

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
