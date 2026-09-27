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

Let \((a_i, b_i)\), for \(1 \leq i \leq 2025\), be 2025 distinct points on the curve
\[3x^2 + 3y^2 = 8 + 4xy + 2(x + y)|x - y|\]
Let \(d_i\) be the distance from the point \((a_i, b_i)\) to the line \(x + y = 6\), and let \(\left\lfloor d_i \right\rfloor\) denote the greatest integer not exceeding \(d_i\).

It is given that:
\[r_i = \left\lfloor \frac{21 - 15\sqrt{2}}{2} \left( d_i^3 - 3d_i^2  - 6d_i^2 \cdot \sqrt{2} + 18d_i + 6d_i \cdot \sqrt{2} + \frac{28}{3} + \frac{16\sqrt{2}}{3} \right) \right\rfloor\]
and that:
\[\sum_{i=1}^{2025} r_i^2 = 2043, \quad \sum_{i=1}^{2025} r_i = 2021\]
Find the maximum value of
\[\sum_{i=1}^{2025} r_i^4\]
After solving the above problem, please output your final answer in the following format:
### The final answer is: $\boxed{<your answer>}$
Example:
### The final answer is: $\boxed{123}$
The final answer should be given as precisely as possible (using LaTeX symbols such as \sqrt, \frac, \pi, etc.). If the final answer involves a decimal approximation, it must be accurate to at least four decimal places.

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
