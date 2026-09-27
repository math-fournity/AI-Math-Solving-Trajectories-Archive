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

In a specialized optics laboratory, a precision laser is mounted at the origin $(0,0)$ of a coordinate grid. A technician is mapping a specific "interference zone" on a flat sensor plate that corresponds to the 2D plane.

The zone is defined by the overlap of two distinct signal regions:

1.  **The Proximity Region:** This region consists of all coordinates $(x,y)$ such that their distance from a signal repeater located at $(1,0)$ is strictly less than $1$ unit.
2.  **The Inversion Region:** This region consists of all coordinates $(x,y)$ such that the reciprocal of their position—defined by the transformation of their coordinates as a complex value $z = x+iy$—is within $1$ unit of the signal repeater at $(1,0)$. Specifically, this encompasses all points where the magnitude of the difference between the reciprocal of the coordinate and the repeater's position is less than $1$ (i.e., $|\frac{1}{z} - 1| < 1$).

Calculate the total area of the sensor plate covered by the intersection of these two regions.

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
