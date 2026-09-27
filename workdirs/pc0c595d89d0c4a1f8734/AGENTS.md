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

A massive solar power facility is structured as a grid of 2020 rows and 2020 columns of photovoltaic panels. Each panel $(i, j)$ produces a specific amount of energy, represented by a real number $x_{i, j}$, for $1 \leq i, j \leq 2020$.

The facility's wiring dictates a strict equilibrium for every $2 \times 2$ block of adjacent panels. For any row index $i \in \{1, \dots, 2019\}$ and column index $j \in \{1, \dots, 2019\}$, let the energy outputs of the four panels in the block be $a = x_{i,j}$ (top-left), $b = x_{i, j+1}$ (top-right), $c = x_{i+1, j}$ (bottom-left), and $d = x_{i+1, j+1}$ (bottom-right). These values must satisfy the following power balance equations:
\[
\begin{aligned}
a+b+2c+3d &= 0 \\
2a+b+3c+4d &= 0
\end{aligned}
\]

An inspector needs to determine the consistency of the panel outputs. Let $N$ be the maximum integer such that, regardless of the specific values assigned to the panels (provided they satisfy the equations), it is guaranteed that at least $N$ panels in the grid will produce the exact same energy output. 

Find the value of $N$.

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
