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

In a specialized maritime navigation zone, two stationary rescue buoys, Alpha and Bravo, are anchored exactly 2 nautical miles apart. A survey vessel, the *Pathfinder*, is scouting potential positions, denoted as point $P$, to drop a deep-sea sensor.

The vessel’s navigation computer calculates two critical bearings from its current position $P$:
1.  **The Median Route:** The direct path from the vessel $P$ to the exact midpoint of the line segment connecting buoy Alpha and buoy Bravo.
2.  **The Symmedian Route:** The path formed by taking the Median Route and reflecting it across the internal angle bisector of the angle $\angle APB$ formed between the vessel and the two buoys.

Regulations state that the *Pathfinder* may only deploy the sensor at locations $P$ where these two specific routes—the Median Route and the Symmedian Route—are perfectly perpendicular to each other.

The set of all possible coordinates where the vessel can be positioned to satisfy this perpendicularity requirement defines a specific patrol region $R$ on the ocean surface. Calculate the total area of region $R$.

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
