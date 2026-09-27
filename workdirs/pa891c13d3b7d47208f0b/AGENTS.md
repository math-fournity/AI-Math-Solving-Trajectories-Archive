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

In the city of Gridhaven, a district is laid out in a perfect square grid of 8 columns and 8 rows, creating 64 potential construction plots. A tech mogul wants to install three different types of security automated systems—Type R, Type B, and Type K—with exactly $n$ units of each type deployed on the grid.

Each system has a "interference zone" based on its sensor array, and for the security network to remain stable, no unit can have another unit (of any type) located within its interference zone. The zones are defined as follows:
- **Type R:** Interferes with any unit located in the same row or the same column as itself.
- **Type B:** Interferes with any unit located on either of the two diagonals passing through its plot.
- **Type K:** Interferes with any unit located at the opposite corner of a $2 \times 1$ or $1 \times 2$ rectangle of plots (an "L-shape" away).

The mogul dictates that each of the $3n$ units must be placed on a unique plot such that no unit is positioned within the interference zone of any of the other $3n-1$ units. 

Determine the largest possible value of $n$ for which this deployment is possible.

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
