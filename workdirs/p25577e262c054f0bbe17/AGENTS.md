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

In a remote industrial district, a logistics manager is overseeing the construction of rectangular storage grids. Each grid consists of $n$ rows and $m$ columns of cargo slots, where the dimensions are constrained such that $m \geq n \geq 3$. Each slot is assigned a specific "stability rating" (a real number).

A grid is classified as "Structurally Balanced" if it satisfies two strict environmental safety regulations:
1. Every $2 \times 2$ cluster of adjacent slots must have a total stability rating that is strictly negative.
2. Every $3 \times 3$ cluster of adjacent slots must have a total stability rating that is strictly positive.

Let $S$ be the set of all possible pairs of dimensions $(n, m)$ for which it is mathematically possible to design a Structurally Balanced grid. We define a binary indicator function $f(n, m)$ such that $f(n, m) = 1$ if $(n, m) \in S$, and $f(n, m) = 0$ if no such grid can exist for those dimensions.

The manager needs to evaluate the feasibility of various configurations within the range of $3$ to $10$ for both dimensions. Calculate the total number of feasible configurations by evaluating:
$$\sum_{n=3}^{10} \sum_{m=n}^{10} f(n, m)$$

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
