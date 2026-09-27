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

A specialized logistics hub is tasked with distributing exactly $\frac{674}{385}$ tons of high-grade compound across three different transport containers. The total load must be split into three distinct shipments, represented by the positive irreducible fractions $\frac{n_1}{d_1}$, $\frac{n_2}{d_2}$, and $\frac{n_3}{d_3}$.

The project engineers have established the following strict operational constraints:
1. Each denominator $d_i$ must be a positive integer divisor of 385.
2. The sum of the three cargo weights must be exactly $\frac{n_1}{d_1} + \frac{n_2}{d_2} + \frac{n_3}{d_3} = \frac{674}{385}$.
3. The sum of the three numerators $(n_1 + n_2 + n_3)$ must exactly equal the sum of all the individual digits that make up the three denominators $d_1, d_2,$ and $d_3$. (For example, if the denominators were 5, 11, and 77, the sum of the digits would be $5 + 1 + 1 + 7 + 7 = 21$).

A "set" of fractions is considered distinct based on the values of the fractions themselves, regardless of their order. For every unique set of three fractions that satisfies all the criteria above, calculate the product of their numerators $(n_1 \cdot n_2 \cdot n_3)$. 

Determine the sum of all such products across all possible distinct sets.

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
