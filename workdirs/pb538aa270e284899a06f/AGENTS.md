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

In a futuristic data-processing facility, engineers are designing "System Arrays." A System Array is defined as a large rectangular chip architecture of size $m \times n$, composed of $mn$ individual processing cells arranged in $m$ rows and $n$ columns. The area of each cell represents its processing capacity.

To calibrate the total capacity of the entire $m \times n$ array, a technician selects exactly $m+n-1$ specific cells and records their individual capacities. There are $\binom{mn}{m+n-1}$ ways to choose which cells to measure. However, only certain sets of $m+n-1$ cells provide enough information to mathematically deduce the total capacity of the whole array, regardless of the specific capacity values assigned. Let $C_{m, n}$ be the number of such "complete" sets of cell choices for a given $m$ and $n$.

A master efficiency constant $A$ is defined by the following infinite sum over all possible positive integer dimensions $m$ and $n$:

\[
A = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{C_{m, n} \binom{m+n}{m}}{(m+n)^{m+n}}
\]

Calculate the greatest integer less than $1000A$.

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
