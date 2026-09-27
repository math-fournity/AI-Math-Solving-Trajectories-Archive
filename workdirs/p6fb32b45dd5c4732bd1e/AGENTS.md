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

In the quadrilateral pyramid $S A B C D$, the base $A B C D$ has its axis of symmetry as the diagonal $A C$, which is equal to 9, and the point $E$ of intersection of the diagonals of the quadrilateral $A B C D$ divides the segment $A C$ such that the segment $A E$ is smaller than the segment $E C$. A plane is drawn through the midpoint of the lateral edge of the pyramid $S A B C D$, parallel to the base and intersecting the edges $S A, S B, S C, S D$ at points $A 1, B 1, C 1, D 1$ respectively.

The polyhedron $A B C D A 1 B 1 C 1 D 1$, which is part of the pyramid $S A B C D$, intersects the plane $\alpha$ in a regular hexagon with a side length of 2. Find the area of the triangle $A B D$, if the plane $\alpha$ intersects the segments $B B 1$ and $D D 1$.

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
