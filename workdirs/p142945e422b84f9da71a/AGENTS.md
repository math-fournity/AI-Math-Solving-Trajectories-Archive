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

In the mountainous kingdom of Geometria, a regional logistics hub is defined by three major outposts arranged in a triangular formation: Outpost A, Outpost B, and Outpost C. To facilitate communication, three specialized relay stations—D, E, and F—have been constructed on the direct paths between the outposts such that each station represents the closest possible point on that path to the opposite outpost (specifically, station D lies on path BC, E on path AC, and F on path AB).

Surveyors have measured the straight-line distances between these three relay stations:
- The distance between stations D and F is exactly 3 kilometers.
- The distance between stations F and E is exactly 4 kilometers.
- The distance between stations D and E is exactly 5 kilometers.

The triangle formed by the three main outposts (A, B, and C) is acute. A circular security perimeter is to be established, centered exactly at Outpost C. The radius of this perimeter must be calibrated so that the boundary is perfectly tangent to the straight supply line connecting relay stations D and E.

What is the radius of this security perimeter?

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
