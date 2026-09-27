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

A specialized logistics hub manages a fleet of "Core Units," which are identified by square-free serial numbers $k$. For any given system capacity $n$, a resource function $f_n(x)$ calculates how many of these Core Units can operate under a load factor $x$, defined as the number of square-free integers $k$ such that $k \cdot x \leq n$.

The hub evaluates its total operational efficiency $v(n)$ for a specific capacity $n$ by summing the interactions between all pairs of maintenance ports $i$ and $j$ (where both $i$ and $j$ range from $1$ to $n$). The efficiency contribution for each pair $(i, j)$ is calculated using the formula:
$f_n(i^2) - 6f_n(ij) + f_n(j^2)$.

The total efficiency $v(n)$ is the sum of these contributions over all $1 \leq i, j \leq n$. 

As the capacity $n$ increases, the hub monitors the "marginal efficiency change," defined as $v(n) - v(n-1)$. 

Find the largest integer $n$ in the range $2 \leq n \leq 100$ for which this marginal efficiency change $v(n) - v(n-1)$ is a negative value.

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
