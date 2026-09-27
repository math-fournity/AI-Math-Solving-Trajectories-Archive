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

In a specialized logistics hub, a rectangular grid of storage bays is indexed by coordinates $(k, l)$, where $k$ ranges from $0$ to $n-1$ and $l$ ranges from $0$ to $m-1$ (with $n$ and $m$ being positive integers). Each bay currently contains exactly one autonomous delivery drone.

A redistribution plan is defined by a function $f$ that assigns each drone currently at position $v = (k, l)$ to a new destination bay $f(v)$ within the same grid. A plan is classified as "Optimally Efficient" if it satisfies two strict operational protocols:
1. **No Congestion:** No two drones are assigned to the same destination bay.
2. **Interference-Free Routing:** For any two distinct drones starting at positions $v$ and $w$, their combined displacement—defined as the vector sum of a drone's starting position and its assigned destination—must not be congruent modulo the grid dimensions. That is, the vector $v + f(v)$ and the vector $w + f(w)$ cannot differ by a vector of the form $(an, bm)$ for any integers $a$ and $b$.

Let $S$ be the set of all possible grid dimensions $(n, m)$, where $1 \leq n \leq 100$ and $1 \leq m \leq 100$, such that at least one "Optimally Efficient" redistribution plan exists for that grid size.

Calculate the total number of elements in the set $S$.

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
