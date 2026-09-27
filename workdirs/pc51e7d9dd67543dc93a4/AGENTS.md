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

In the city of Arithmea, an urban planner is evaluating the "Efficiency Score" of various infrastructure projects. Each project's progress over a single year (represented by the time interval $t \in [0, 1]$) is modeled by a function $P(t)$, which is a cubic polynomial (a polynomial of degree 3).

The planning commission only approves projects that reach a "Break-Even Point" at some moment during the year. This means that for every approved project, there must be at least one time $t$ in the interval $[0, 1]$ such that the progress score $P(t) = 0$.

The planner needs to compare two specific metrics for these projects:
1.  **The Total Absolute Impact:** Calculated as the integral of the magnitude of the score over the year: $\int_0^1 |P(t)| \, dt$.
2.  **The Peak Intensity:** Defined as the maximum magnitude of the score reached at any point during the year: $\max_{t \in [0, 1]} |P(t)|$.

Find the smallest constant $C$ such that for every possible cubic polynomial project that hits a break-even point in $[0, 1]$, the Total Absolute Impact is always less than or equal to $C$ times the Peak Intensity.

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
