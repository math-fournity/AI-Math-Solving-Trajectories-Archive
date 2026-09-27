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

A specialized biological research project is monitoring the growth of a rare synthetic enzyme culture. On the first day of the experiment, the researchers record the enzyme's initial activity level, $x_1$, as exactly $2.1$ units.

The laboratory follows a strict daily protocol to determine the next day’s activity level, $x_{n+1}$, based on the current day’s level, $x_n$. The bio-mathematical model for this transition is defined by the formula:
$$x_{n+1} = \frac{x_n - 2 + \sqrt{x_n^2 + 8x_n - 4}}{2}$$

The researchers are specifically interested in the long-term accumulation of a "stability index" for the project. For any given day $n$, the cumulative stability index, $y_n$, is calculated by summing the reciprocal of the difference between the square of each day's activity level and the constant value $4$. Specifically:
$$y_n = \sum_{i=1}^{n} \frac{1}{x_i^2 - 4}$$

As the experiment continues indefinitely over an infinite timeline, the cumulative stability index $y_n$ approaches a specific limit. Determine the value of $\lim_{n \to \infty} y_n$.

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
