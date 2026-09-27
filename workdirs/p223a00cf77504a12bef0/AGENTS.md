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

Let $n$ be a positive integer such that $ 2 \leq n \leq 5 $. For each such $n$, let $A_nB_nC_nD_n$ be a rectangle with vertex $A_n$ at $(-n, 1 + 6 \sqrt{2} - \sqrt{2}n)$, and vertex $B_n$ the reflection of $A_n$ through the origin. The line segments $A_nC_n$ and $B_nD_n$ are parallel to the $x$-axis, and the line segments $A_nD_n$ and $B_nC_n$ are parallel to the $y$-axis.
Let $P_i \quad (1 \leq i \leq 36)$ be 36 distinct points on the curve $(y - |x|)^2 + x^2 = 1$. For each point $P_i$, let the distances to the 16 sides of the four rectangles be denoted by $r_{i_1}, r_{i_2}, \ldots, r_{i_{16}}$.
Let $d_i = \min \Big( r_{i_k} \Big) , \quad (1 \leq k \leq 16)$, and suppose that these values satisfy the condition $ 3 \sum_{i=1}^{36}d_{i}^{3}  -15\sum_{i=1}^{36} d_{i}^{2} = -1200$.
Find the maximum value of $\sum_{i=1}^{36} d_i$.
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
