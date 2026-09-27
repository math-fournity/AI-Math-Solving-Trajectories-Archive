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

In a remote sector of the galaxy, three space stations—**Base B**, **Base C**, and **Base D**—form a perfect equilateral triangle with a direct communication distance of **2 units** between any two bases. These stations are all positioned on the boundary of a circular energy field. A mobile scouting vessel, **Craft A**, is stationed on the same circular boundary, specifically positioned on the shorter arc between Base B and Base D.

Three linear supply corridors are established:
1. Corridor **AB** intersects the path **CD** at a junction point **P**.
2. Corridor **AC** intersects the path **DB** at a junction point **Q**.
3. Corridor **AD** intersects the path **BC** at a junction point **R**.

A navigation triangle is formed by the junctions **P**, **Q**, and **R**. From each junction, a sensor probe is dropped perpendicular to the opposite side of this navigation triangle:
- From junction **P**, a probe lands at point **X** on side **QR**.
- From junction **Q**, a probe lands at point **Y** on side **PR**.
- From junction **R**, a probe lands at point **Z** on side **PQ**.

Long-range scans determine that the distance from **Base B** to junction **Q** is exactly $3 - \sqrt{5}$ units. Engineers need to calculate the "Spatial Resonance Product" of the sector, which is defined as the product of the areas of three specific triangular regions: **Triangle XCD**, **Triangle YDB**, and **Triangle ZBC**.

Compute the product of the areas $[\triangle X C D] \cdot [\triangle Y D B] \cdot [\triangle Z B C]$.

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
