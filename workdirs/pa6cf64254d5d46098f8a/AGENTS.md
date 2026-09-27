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

In a remote industrial complex, there are $n$ specialized fuel storage tanks, where $n \geq 3$ is a fixed integer. Each tank $i$ contains a specific volume of liquid hydrogen, denoted by $x_i$, where all $x_i > 0$.

A chemical engineer is tasked with arranging these $n$ tanks in a circular sequence $y_1, y_2, \ldots, y_n$ to power a series of $n$ turbines. Each turbine $i$ is positioned between three consecutive tanks in the sequence—$y_i$, $y_{i+1}$, and $y_{i+2}$—and its energy output is determined by the specific efficiency ratio:
\[ \frac{y_i^2}{y_{i+1}^2 - y_{i+1} y_{i+2} + y_{i+2}^2} \]
(In this circular arrangement, the indexing wraps around such that $y_{n+1} = y_1$ and $y_{n+2} = y_2$).

The total power output of the system is the sum of the outputs from all $n$ turbines. The engineer knows that regardless of the specific volumes $x_1, \ldots, x_n$ provided, it is always possible to find at least one permutation (reordering) of the tanks that results in a total power output greater than or equal to some constant value $M$.

Find the largest real number $M$ that satisfies this condition for any set of positive volumes $x_i$ and any $n \geq 3$.

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
