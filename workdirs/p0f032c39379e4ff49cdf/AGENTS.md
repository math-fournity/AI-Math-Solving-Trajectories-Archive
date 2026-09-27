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

A specialized thermal stabilization unit is used to regulate the temperature of a chemical reactor. The temperature of the unit at the end of the $n$-th hour of operation is denoted by the function $f(n)$, where $n$ is a positive integer. 

After the first hour, the temperature is exactly $f(1) = 2$ degrees Celsius. The engineers have observed two specific behavioral constraints of the system for all positive integers $n$:
1. The temperature is non-decreasing over time, such that $f(n+1) \ge f(n)$.
2. Due to heat dissipation limits, the temperature at the $n$-th hour is always at least $\frac{n}{n+1}$ times the temperature recorded at the $2n$-th hour, represented by the inequality $f(n) \ge \frac{n}{n+1} f(2n)$.

Safety protocols require the installation of a failsafe trigger. Determine the minimum positive integer $M$ such that the temperature $f(n)$ is guaranteed to stay strictly below $M$ degrees Celsius for every hour $n$ in the unit's infinite operating life.

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
