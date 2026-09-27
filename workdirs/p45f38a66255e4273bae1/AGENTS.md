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

In the competitive landscape of the tech hub "The Sector," three corporate headquarters are located at points $A$, $B$, and $C$, forming an acute triangular region. To expand their influence, three companies built external satellite campuses—$C'$, $B'$, and $A'$—such that triangles $ABC'$, $AB'C$, and $A'BC$ are all equilateral.

A high-speed fiber optic line connects campus $B$ to campus $B'$, and another connects campus $C$ to campus $C'$. These two lines intersect at a central routing hub labeled $F$. 

Infrastructure logistics require further connections:
1. The fiber line $CC'$ crosses the existing boundary road $AB$ at a checkpoint $C_1$.
2. A separate transit line connecting $A$ to $A'$ crosses the boundary road $BC$ at a checkpoint $A_1$.
3. A service path is paved between checkpoints $A_1$ and $C_1$. This path intersects the boundary road $AC$ at a junction point $D$.

Surveyors have mapped the following straight-line distances between these coordinates:
- The distance from the satellite campus $A'$ to the routing hub $F$ is 23 kilometers.
- The distance from headquarters $C$ to the routing hub $F$ is 13 kilometers.
- The distance from the junction point $D$ to the routing hub $F$ is 24 kilometers.

Calculate the straight-line distance, in kilometers, between headquarters $B$ and the junction point $D$.

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
