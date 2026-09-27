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

A specialized digital clock system operates on a cycle of $s$ discrete pulses, where $s$ is an integer greater than 1. Two signals, $m$ and $n$, are broadcast through the system such that both their frequencies are coprime to the cycle length $s$. 

For each pulse $j$ from $1$ to $s-1$, the system calculates two specific signal offsets:
1. The primary offset $X_j$ is the fractional part of the value $\frac{jm}{s}$.
2. The secondary offset $Y_j$ is the fractional part of the value $\frac{jn}{s}$.

The system's "interference coefficient" is calculated by summing the products of these offsets and their complements across the entire cycle:
\[ \text{Interference} = \sum_{j=1}^{s-1} X_j(1 - X_j) Y_j(1 - Y_j) \]

Engineers have determined that for any valid configuration of $s, m,$ and $n$, this interference coefficient is always greater than or equal to a constant threshold $c$ multiplied by the cycle length $s$.

Find the largest real number $c$ for which this inequality is guaranteed to hold for all possible values of $s > 1$ and all positive integers $m, n$ coprime to $s$.

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
