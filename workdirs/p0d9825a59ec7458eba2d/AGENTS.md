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

A specialized logistics hub is designed on a coordinate grid. Three main distribution centers are located at the following coordinates: Center $A$ at $(0, 12)$, Center $B$ at $(-4, 0)$, and Center $C$ at $(6, 0)$. A regional management office is situated at the centroid $G$ of the triangle formed by these three centers.

A straight supply road, designated as Line $(d)$, is constructed such that it is perpendicular to the straight path connecting Center $A$ to the management office $G$. This road $(d)$ passes through a specific refueling station located at $(0, -5)$.

A mobile maintenance unit $M$ can be stationed at any arbitrary point along the road $(d)$. Two secondary staging areas are established: Staging Area $E$ is at the midpoint of the path between the maintenance unit $M$ and Center $B$, while Staging Area $F$ is at the midpoint of the path between the maintenance unit $M$ and Center $C$.

From Staging Area $E$, a service corridor is built perpendicular to road $(d)$, which intersects the main transport line $AB$ at a junction point $P$. Similarly, from Staging Area $F$, another service corridor is built perpendicular to road $(d)$, which intersects the main transport line $AC$ at a junction point $Q$.

A dedicated communication cable, Line $(d')$, is laid starting from the maintenance unit $M$ such that it is perpendicular to the line segment connecting junction points $P$ and $Q$. It has been mathematically determined that this communication cable $(d')$ will always pass through a fixed coordinate $(x_0, y_0)$, regardless of where the maintenance unit $M$ is positioned along road $(d)$.

Find the value of $x_0 + y_0$.

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
