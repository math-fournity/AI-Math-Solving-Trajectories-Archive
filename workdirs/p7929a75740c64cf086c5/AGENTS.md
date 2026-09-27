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

In a specialized automated warehouse, a logistics drone must navigate a strictly defined grid system to transport a package. The warehouse floor is modeled as a coordinate plane where $n$ is a fixed, positive odd integer representing the grid's scale.

The drone's journey begins at a charging dock located at coordinates $(0, 1)$ and must conclude at a delivery terminal located at $(n+1, n)$. To navigate, the drone must stop at a sequence of $m$ distinct sorting sensors, labeled $P_1, P_2, \dots, P_m$, where $m$ is a non-negative integer. Each sensor $P_i$ is located at a position where both the $x$ and $y$ coordinates are integers between $1$ and $n$, inclusive. Let $P_0$ denote the starting dock and $P_{m+1}$ denote the final terminal.

The drone is programmed with a rigid movement protocol consisting of $m+1$ straight-line segments connecting $P_i$ to $P_{i+1}$ for $i = 0, 1, \dots, m$:
1. For every even index $i$, the drone must move horizontally (parallel to the $x$-axis) to reach the next point.
2. For every odd index $i$, the drone must move vertically (parallel to the $y$-axis) to reach the next point.

To avoid sensor interference and signal collisions, the path is constrained such that for any two distinct segments in the journey, they may share at most one point (meaning they cannot overlap or run along the same line for any distance, though they may cross or meet at an endpoint).

Based on these navigation constraints, what is the maximum possible number of sensors $m$ that the drone can visit?

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
