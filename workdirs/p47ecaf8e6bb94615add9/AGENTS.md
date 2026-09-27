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

A circular power grid consists of exactly $N = 2024$ sectors, arranged in a ring and indexed $1$ through $2024$. Each sector $i$ is assigned two non-negative integer values: $a_i$, representing the number of active power generators, and $b_i$, representing the "range" of a local stability protocol. Because the grid is circular, the indices wrap around such that sector $i$ is identical to sector $k$ if $i-k$ is a multiple of $2024$.

A configuration is called "balanced" if every sector's value is the average of the values of itself and its neighbors within its specified range. Specifically:
1. The sequence of generators $\mathbf{a}$ is balanced by the ranges $\mathbf{b}$ if, for every sector $i$, $a_i$ is the arithmetic mean of the values $\{a_{i-b_i}, a_{i-b_i+1}, \ldots, a_i, \ldots, a_{i+b_i}\}$.
2. The sequence of ranges $\mathbf{b}$ is balanced by the generators $\mathbf{a}$ if, for every sector $i$, $b_i$ is the arithmetic mean of the values $\{b_{i-a_i}, b_{i-a_i+1}, \ldots, b_i, \ldots, b_{i+a_i}\}$.

A regulatory agency inspects the grid and notes two conditions:
- Neither the number of generators nor the ranges are uniform across the grid (neither sequence $\mathbf{a}$ nor $\mathbf{b}$ is constant).
- Both $\mathbf{a}$ is balanced by $\mathbf{b}$, and $\mathbf{b}$ is balanced by $\mathbf{a}$.

Let $Z$ be the total number of zeros found when looking at all $2024$ generator counts and all $2024$ range values together. Find the minimum possible value of $Z$.

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
