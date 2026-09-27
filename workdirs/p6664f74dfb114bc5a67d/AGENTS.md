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

In a futuristic data center, a security system operates using a digital vault represented by a grid of coordinates. The system utilizes a specific prime number $p$, where $p > 2$. The vault's state space, denoted as $\Lambda$, is a collection of three-dimensional vectors $(x_1, x_2, x_3)$, where each coordinate is an integer chosen from the range of possible values in the modular ring $\mathbb{Z}/p^2\mathbb{Z}$. This means each coordinate can take any of the $p^2$ available values, and all arithmetic is performed modulo $p^2$.

The vault is protected by a "Balance Equation" defined by a perfect symmetric bilinear form. For any vector $x = (x_1, x_2, x_3)$ in the vault, the system calculates a "Stability Score" using the function $S(x) = (x, x)$. Because the form is perfect and symmetric over this specific ring, it can be represented in a standard basis such that the score of a vector is calculated as:
$$S(x) = a_{11}x_1^2 + a_{22}x_2^2 + a_{33}x_3^2 + 2a_{12}x_1x_2 + 2a_{13}x_1x_3 + 2a_{23}x_2x_3 \pmod{p^2}$$
where the determinant of the coefficients is coprime to $p$.

A vector is considered a "Null-Key" if its Stability Score is exactly zero: $(x, x) \equiv 0 \pmod{p^2}$.

To calibrate the security threshold, the system administrators need to know the total number of unique Null-Keys that exist within the vault. 

Find the total number of vectors $x \in \Lambda$ such that $(x, x) = 0$, expressed as a polynomial in terms of $p$.

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
