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

In the coastal territory of Arcania, three watchtowers—Alpha (A), Bravo (B), and Charlie (C)—mark the vertices of a triangular patrol zone. The distance between Alpha and Bravo is exactly 20 leagues, while the distance from Bravo to Charlie is 15 leagues. A central command outpost, Station Indigo (I), is located at the exact incenter of this triangular region. Long-range scouts report that the distance from tower Bravo to Station Indigo is exactly 12 leagues.

The patrol region is enclosed by a circular naval boundary, $\omega_1$, which passes through towers A, B, and C. A supply route is mapped starting from tower Charlie, passing through Station Indigo, and extending until it hits the naval boundary $\omega_1$ at a remote buoy, Delta (D).

A specialized surveyor, Alice, projects a straight laser line $l$ emanating from buoy Delta. This line cuts across the naval boundary $\omega_1$ at a specific point X, located on the shorter curved path between towers Alpha and Charlie. The line $l$ continues further until it reaches a point Y on a secondary circular sensor grid, $\omega_2$, which is defined as the circle passing through Alpha, Station Indigo, and Charlie. Point Y lies outside the initial naval boundary $\omega_1$.

Upon analyzing her data, Alice discovers a remarkable geometric property: the lengths of the segments $ID$, $DX$, and $XY$ can form the three sides of a right-angled triangle.

Based on these specific coordinates and measurements, determine the exact length of the distance between Station Indigo and point Y.

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
