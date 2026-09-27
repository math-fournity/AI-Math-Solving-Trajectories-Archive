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

A high-tech manufacturing firm is developing a series of modular solar panels, labeled $i = 1, 2, 3, \dots$. Each panel $A_i B_i C_i D_i$ is designed as a convex quadrilateral. For the first panel ($i=1$), the vertices are positioned on a coordinate grid at $A_1(0, 48)$, $B_1(80, 64)$, $C_1(128, 40)$, and $D_1(40, 0)$.

For every subsequent panel $i+1$, the vertices are determined by the midpoints of the sides of the previous panel $i$. Specifically, $A_{i+1}$ is the midpoint of $A_i B_i$, $B_{i+1}$ is the midpoint of $B_i C_i$, $C_{i+1}$ is the midpoint of $C_i D_i$, and $D_{i+1}$ is the midpoint of $D_i A_i$.

The total surface area of this infinite progression of panels is given by the sum of the areas of each quadrilateral:
\[ \sum_{i=1}^{\infty} \text{Area}(A_i B_i C_i D_i) = \frac{a^2 b}{c} \]
where $a, b,$ and $c$ are positive integers, $b$ is square-free, and the fraction is in simplest form such that $c$ is as small as possible.

Compute the value of $a + b + c$.

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
