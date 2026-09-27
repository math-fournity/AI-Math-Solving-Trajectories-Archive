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

In a remote industrial facility, a chemical crystallization process is governed by a growth constant $\lambda$. This constant is defined as the unique positive solution to the reaction stability equation $t^2 - 1998t - 1 = 0$.

The facility tracks the purity levels of a substance over discrete time intervals, denoted by the sequence $x_0, x_1, x_2, \ldots, x_n$. On the initial day (Day 0), the purity level is exactly $x_0 = 1$ unit. For every subsequent day, the purity level is calculated by multiplying the previous day’s level by the growth constant $\lambda$ and rounding down to the nearest whole integer (using the floor function). Specifically, for $n \ge 0$, the relationship is defined as $x_{n+1} = \lfloor \lambda x_n \rfloor$.

The plant supervisor needs to conduct a mandatory audit on Day 1998. As part of the safety protocol, they must determine the value of the purity level $x_{1998}$ modulo 1998.

Find the remainder when the purity level on Day 1998, $x_{1998}$, is divided by 1998.

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
