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

A digital artist is designing a 4x4 grid of light sensors, where each coordinate $(i, j)$ for $0 \leq i, j \leq 3$ corresponds to a specific cell. For each cell, the artist must decide whether to install a sensor (setting a binary variable $a_{i,j} = 1$) or leave it empty ($a_{i,j} = 0$).

Once the layout of sensors $\{a_{i,j}\}$ is fixed, a technician attempts to calibrate the system by assigning a positive real-valued sensitivity coefficient $c_{i,j}$ to every installed sensor. The goal of this calibration is to ensure that the global intensity function, defined by the polynomial
\[f(x,y)=\sum_{0\leq i,j\leq 3}a_{i,j}c_{i,j}x^iy^j\]
reaches a minimum value over all real-world coordinates $(x, y) \in \mathbb{R}^2$ (i.e., the function is bounded below).

For how many of the $2^{16}$ possible sensor layouts $\{a_{i,j}\}$ is it possible to find a set of positive sensitivity coefficients $\{c_{i,j}\}$ such that the resulting intensity function is bounded below?

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
