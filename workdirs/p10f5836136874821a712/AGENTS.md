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

In a specialized coastal monitoring zone, three radar stations are positioned at locations $A$, $B$, and $C$. The straight-line distances between these stations are measured as $AB = 4$ kilometers, $BC = 6$ kilometers, and $CA = 5$ kilometers. 

A central maintenance hub, $M$, is located exactly halfway between stations $B$ and $C$ along the straight path connecting them. A drone-tracking perimeter is defined by the unique circle passing through all three stations $A$, $B$, and $C$. A surveillance drone is hovering at a specific point $P$ on this circular perimeter such that the line segment $MP$ is perfectly perpendicular to the line segment $PA$.

To coordinate signal coverage, two signal relay towers, $D$ and $E$, are placed on the boundaries of the zone. Tower $D$ is located on the straight line $AC$ such that the path $BD$ is perpendicular to $AC$. Tower $E$ is located on the straight line $AB$ such that the path $CE$ is perpendicular to $AB$.

The drone $P$ projects two laser beams for calibration:
1. The first beam passes through $P$ and tower $D$, intersecting the straight line $BC$ at a logistical point $X$.
2. The second beam passes through $P$ and tower $E$, intersecting the straight line $BC$ at a logistical point $Y$.

Calculate the square of the area of the triangular region formed by the station $A$ and the two points $X$ and $Y$.

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
