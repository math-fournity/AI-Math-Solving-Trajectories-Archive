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

A circular tracking radar screen displays ten critical signal pings: one master beacon labeled $G$, four aircraft signals $A_1$ through $A_4$, and five vessel signals $B_1$ through $B_5$. These signals are positioned such that the sequence of coordinates $G, A_1, A_2, A_3, A_4$ forms the vertices of a perfect regular pentagon inscribed in the circular screen, while the sequence $G, B_1, B_2, B_3, B_4, B_5$ forms the vertices of a perfect regular hexagon. The vessel signal $B_1$ is located on the shorter arc between the master beacon $G$ and the aircraft signal $A_1$.

A technician draws several digital paths between these points to analyze their convergence. The path connecting vessel $B_5$ to vessel $B_3$ crosses the path from vessel $B_1$ to aircraft $A_2$ at a monitoring station designated $G_1$. Simultaneously, the path from vessel $B_5$ to aircraft $A_3$ crosses the path from the master beacon $G$ to vessel $B_3$ at a monitoring station designated $G_2$.

Calculate the exact degree measure of the angle $\angle G G_2 G_1$ formed by these points on the radar display.

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
