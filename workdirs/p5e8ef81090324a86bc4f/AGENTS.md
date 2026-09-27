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

A specialized climate research agency is designing a grid of sensors to measure thermal deviations across various rectangular regions of a polar ice shelf. Each region is defined as an $n \times m$ grid of measurement points, where $n$ and $m$ are integers representing the number of rows and columns, respectively. The dimensions must satisfy the constraint $m \geq n \geq 3$.

The agency classifies a grid as "Thermally Unstable" if they can assign a real number (representing a temperature deviation) to every single point in the grid such that both of the following conditions are met:
1. The sum of deviations in every possible $2 \times 2$ subgrid is strictly less than zero.
2. The sum of deviations in every possible $3 \times 3$ subgrid is strictly greater than zero.

Let $S$ be the set of all pairs $(n, m)$ for which such a "Thermally Unstable" grid configuration can exist. Your task is to analyze all possible grid dimensions within the range $3 \leq n \leq m \leq 10$. 

Calculate the sum of all values of $m$ such that the pair $(n, m)$ is an element of $S$ within the specified range.

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
