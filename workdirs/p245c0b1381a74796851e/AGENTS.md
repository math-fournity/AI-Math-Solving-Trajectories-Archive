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

A specialized logistics hub is being designed to handle $n$ distinct cargo crates, labeled $1, 2, \ldots, n$. The hub must be constructed in the shape of a "Cross Dock": a facility formed by the union of one $a \times 1$ loading strip and one $1 \times b$ loading strip that share exactly one intersection cell ($a, b$ are positive integers). The total number of cells in the resulting footprint must be exactly $n$.

The crates must be placed into the cells of the hub, one crate per cell, following a specific "Safety Expansion" protocol:
1. First, crate 1 is placed in any cell of the chosen hub layout.
2. Then, for every $k$ from 2 up to $n$, crate $k$ must be placed such that the set of cells occupied by crates $\{1, 2, \ldots, k\}$ forms a single "connected area." A set of cells is connected if one can travel between any two cells in the set by moving only between cells that share a common side.

Note that two hub layouts are considered different if they occupy different sets of cells in the plane or have different intersection points, even if they are rotations or reflections of each other.

For a given natural number $n$, determine the total number of ways to choose a Cross Dock layout and populate it with the $n$ crates according to these rules.

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
