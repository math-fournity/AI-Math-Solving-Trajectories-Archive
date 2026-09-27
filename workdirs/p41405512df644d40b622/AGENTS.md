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

A specialized logistics company is analyzing a triangular delivery route connecting three hubs: Hub A, Hub B, and Hub C. The direct distance between Hub A and Hub B is 8 miles, the distance between Hub B and Hub C is 9 miles, and the distance between Hub C and Hub A is 10 miles.

The company is planning to build a regional distribution center at a specific location, Point T. This location is determined by two conditions: first, Point T must lie on the extended straight line passing through Hubs B and C; second, the straight-line path from T to A must be perfectly perpendicular to the radius of the circle that passes through Hubs A, B, and C.

To manage local deliveries, the company establishes a circular service zone centered at Point T with a radius equal to the distance between T and A. A straight supply road connecting Hubs A and C intersects the boundary of this circular service zone at a second point, designated as Point S.

A courier needs to travel from Hub B to Point S. However, a specialized sensor must be placed at a point P along the supply road segment AS. The location of Point P is chosen such that the path BP perfectly bisects the angle formed by the paths BS and BA.

Calculate the exact distance between Point S and Point P.

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
