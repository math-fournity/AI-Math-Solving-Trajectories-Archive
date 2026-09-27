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

### Logistics Optimization and Architectural Volume Study

**Part 1: The Efficiency Spread**
A logistics company measures the performance of a delivery route using an efficiency function $f(t) = xt^2 + yt$, where $t$ represents the normalized time elapsed during a shift ($0 \leq t \leq 1$). The coefficient $x$ is a strictly positive performance factor, and $y$ is a real-valued adjustment variable. Calculate the total range of this function (the difference between its maximum and minimum values) over the duration of the shift $0 \leq t \leq 1$.

**Part 2: The Feasibility Region $S$**
An urban planner is mapping a 2D coordinate plane $(x, y)$ to determine "stable zones." A point $(x, y)$ is included in the domain $S$ if it satisfies the following condition: for a given $x > 0$, there must exist at least one vertical offset constant $z$ such that the entire performance curve $xt^2 + yt + z$ stays within the unit interval $[0, 1]$ for all $t$ in the range $0 \leq t \leq 1$. Sketch the outline of the domain $S$ on the $xy$-plane.

**Part 3: The Volume of the Safe Zone $V$**
An architect is designing a 3D structural component defined by coordinates $(x, y, z)$. This component occupies a region $V$ in the coordinate space. A point $(x, y, z)$ is considered part of the solid $V$ if it meets two criteria:
1. The $x$-coordinate is constrained such that $0 \leq x \leq 1$.
2. For every possible value of $t$ in the interval $0 \leq t \leq 1$, the linear combination $xt^2 + yt + z$ must never be less than $0$ and never greater than $1$.

Calculate the total volume of the domain $V$ in the $(x, y, z)$ coordinate space.

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
