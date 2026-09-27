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

An architectural firm is designing a massive triangular support structure using three pressurized hydraulic beams with lengths $a, b,$ and $c$ meters. The total length of the beams is $L = a+b+c$.

The efficiency of the system's pressure distribution is measured by the product of the total length and the sum of the reciprocal lengths: $(a+b+c)(\frac{1}{a} + \frac{1}{b} + \frac{1}{c})$. Safety regulations require that this efficiency value must always be greater than or equal to a base constant of $9$ plus a stability correction factor.

This stability correction factor is defined as a constant $k$ multiplied by the variance ratio of the beams. The variance ratio is calculated by taking the square of the maximum difference between any two beam lengths—$\max\{(a-b)^2, (b-c)^2, (c-a)^2\}$—and dividing it by the square of the total length $(a+b+c)^2$.

For the design to be certified for all possible positive beam lengths $a, b,$ and $c$, what is the maximum possible value of the constant $k$ that ensures the inequality holds?

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
