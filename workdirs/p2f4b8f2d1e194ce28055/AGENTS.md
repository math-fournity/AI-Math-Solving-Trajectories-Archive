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

In a remote territory, four strategic outposts define a convex perimeter at specific GPS coordinates: Outpost A is at $(0, 10)$, Outpost B is at $(12, 14)$, Outpost C is at $(8, 0)$, and Outpost D is at $(0, 2)$. A central communications hub, Command Center P, is positioned somewhere within the region bounded by these four outposts.

To establish a secure relay network, the engineers have marked four signal towers—K, L, M, and N—along the boundary fences. These towers are positioned exactly where the angular bisectors of the lines of sight from Command Center P to each pair of adjacent outposts intersect the perimeter. Specifically:
- Tower K is on the fence between A and B, located on the bisector of $\angle APB$.
- Tower L is on the fence between B and C, located on the bisector of $\angle BPC$.
- Tower M is on the fence between C and D, located on the bisector of $\angle CPD$.
- Tower N is on the fence between D and A, located on the bisector of $\angle APD$.

In this specific geographic layout, the terrain constraints dictate that there is exactly one unique location $(x, y)$ for Command Center P that causes the four relay towers $KLMN$ to form a perfect parallelogram.

Find the sum of the coordinates $(x + y)$ for this unique location of Command Center P.

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
