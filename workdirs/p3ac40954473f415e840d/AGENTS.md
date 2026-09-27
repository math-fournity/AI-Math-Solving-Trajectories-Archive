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

In a circular industrial power grid, there are $n$ distinct energy storage modules, where $n$ is a fixed positive integer. These modules are arranged in a ring, such that module $n$ is adjacent to module 1. To ensure stability, the grid must satisfy the constraint $n \ge 4k$, where $k$ is a fixed positive integer representing the "load-sharing span."

Each module $i$ possesses a positive energy output level denoted by $a_i$ (where $i=1, 2, \ldots, n$). For every module $i$, engineers calculate a "normalized efficiency factor" defined as the ratio of its own output, $a_i$, to the root-sum-square of its output and the outputs of the next $k$ modules in the sequence (calculated as $\sqrt{a_i^2 + a_{i+1}^2 + \cdots + a_{i+k}^2}$, where indices wrap around from $n$ back to 1).

The total system efficiency is defined as the sum of these factors across all $n$ modules:
\[ \sum_{i=1}^n \frac{a_i}{\sqrt{a_i^2 + a_{i+1}^2 + \cdots + a_{i+k}^2}} \]

Determine the minimal constant $\lambda$ (expressed in terms of $n$ and $k$) that serves as an upper bound for this total system efficiency, regardless of the specific positive values chosen for the outputs $a_1, a_2, \ldots, a_n$.

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
