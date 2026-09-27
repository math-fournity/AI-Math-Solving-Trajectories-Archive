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

A high-tech research facility is constructed in the shape of a massive cube. To define the layout, let the vertices of the cube be represented in 3D space. Three adjacent square exterior walls meet at a corner point $E(0,0,0)$. These walls are defined by the vertices $E(0,0,0)$, $F(s,0,0)$, $G(s,s,0)$, and $H(0,s,0)$ for the floor; $E, F, D, C$ for the right wall; and $E, H, B, C$ for the left wall. A laser measurement reveals the distance from corner $E$ to the opposite corner of these three walls, $C$, is exactly $8$ units. The eighth vertex of the cube, located furthest from $E$, is designated as point $A$.

Engineers decide to install a triangular ventilation shaft that passes entirely through the cube. First, they mark three points for the shaft's entrance: point $I$ is on the edge $\overline{EF}$, point $J$ is on the edge $\overline{EH}$, and point $K$ is on the edge $\overline{EC}$, such that the distance from $E$ to each point is exactly $2$ units ($EI=EJ=EK=2$).

The shaft is then bored through the cube such that its three flat interior walls are all perfectly parallel to the main diagonal $\overline{AE}$. These three walls are formed by extending the lines $\overline{IJ}$, $\overline{JK}$, and $\overline{KI}$ through the interior of the cube in the direction of vector $\vec{EA}$.

The total surface area of the resulting solid $S$ (which includes all original exterior faces of the cube minus the holes created by the shaft, plus the area of the three internal walls of the shaft) can be expressed in the form $m+n\sqrt{p}$, where $m, n,$ and $p$ are positive integers and $p$ is square-free. Find the value of $m+n+p$.

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
