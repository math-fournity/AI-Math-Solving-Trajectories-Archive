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

In a remote sector of the galaxy, an ancient crystalline structure has been discovered. This structure is a convex polyhedron with a unique geometric signature: no two of its structural struts (edges) are parallel to each other, and no strut is parallel to any of its flat crystalline panels (faces) except for the two panels that the strut directly connects.

The Federation of Architects defines a "Stabilizing Alignment" for any two points on the structure if it is possible to place two parallel force-fields such that each field touches one of the two points, with the entire crystal perfectly encased between them.

The Chief Engineer needs to calculate two specific values for the structural integrity report:
1.  Let $A$ be the total number of pairs of vertices that form a Stabilizing Alignment.
2.  Let $B$ be the total number of pairs of edge midpoints that form a Stabilizing Alignment.

Let $V$ represent the total number of vertices, $E$ represent the total number of edges, and $F$ represent the total number of faces of this crystal. Determine the value of the difference $A - B$ expressed solely in terms of $V, E,$ and $F$.

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
