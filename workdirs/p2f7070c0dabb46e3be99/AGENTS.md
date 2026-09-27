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

Consider a system of $p$ linear equations in $q$ variables $x_1, \ldots, x_q$:
\[\begin{matrix} a_{11}x_{1}+\ldots+a_{1q}x_{q}=0,\\ a_{21}x_{1}+\ldots+a_{2q}x_{q}=0,\\ \vdots \\ a_{p1}x_{1}+\ldots+a_{pq}x_{q}=0,\\ \end{matrix}\]
where $q=2p$ and every coefficient $a_{ij} \in \{-1, 0, 1\}$. It is known that there exists a non-zero integer solution $(x_1, \ldots, x_q)$ such that $|x_j| \leq K$ for all $j=1, \dots, q$. Using the standard Pigeonhole Principle argument comparing the number of vectors $(x_1, \dots, x_q)$ with $0 \leq x_i \leq q$ to the number of possible values of the $p$ linear combinations, what is the smallest integer value for $K$ that can be guaranteed by this specific method for any such system?

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
