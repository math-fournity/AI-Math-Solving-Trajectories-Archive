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

In a vast maritime monitoring zone, two circular sonar ranges are established. The first range, "Sector Alpha," is centered 1 unit west of the central command post (the origin) and has a radius of 1 unit. The second range, "Sector Beta," is centered 2 units east of the command post and has a larger radius of 2 units.

A specialized research vessel is traveling along a perfectly straight-line path, designated Path Delta. As the vessel moves from west to east, its sonar pings identify four distinct boundary points where Path Delta intersects the perimeters of these two sectors. In chronological order, these points are labeled A, B, C, and D. Throughout this entire transit, the vessel remains strictly north of the east-west baseline passing through the command post.

The coordinates of the first boundary point, Point A (where the vessel enters Sector Alpha), are precisely identified as 1.5 units west and $\frac{\sqrt{3}}{2}$ units north of the command post. As the vessel continues its journey, it exits Sector Alpha at Point B and subsequently enters Sector Beta at Point C. Navigational data shows that the angle formed at the command post between the line of sight to Point B and the line of sight to Point C is exactly $60^{\circ}$.

Based on these navigational coordinates and sector constraints, calculate the slope of the straight-line Path Delta.

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
