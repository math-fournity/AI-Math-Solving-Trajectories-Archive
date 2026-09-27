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

In a remote sector of the ocean, a circular navigation route is monitored by a central control buoy, $O$. Two primary shipping lanes are defined by diametrically opposite beacons: Lane 1 connects beacon $A$ to beacon $B$, and Lane 2 connects beacon $C$ to beacon $D$, both passing through the center $O$.

A specialized research vessel is currently stationed at a fixed point $P$ located somewhere along the straight-line path between beacons $A$ and $D$. A supply ship travels along a straight trajectory starting from beacon $B$, passing through the research vessel at $P$, and continuing until it intersects the straight-line path connecting beacons $A$ and $C$ at a checkpoint designated as $X$. Along this specific trajectory, the supply ship passes a perimeter marker $M$ (located on the original circular route) exactly halfway between the research vessel $P$ and the checkpoint $X$.

To calibrate its radar, the supply ship identifies a secondary coordinates point $Y$ (distinct from $X$) such that its distance from $B$ is identical to the distance $BX$. The orientation of the ship is such that the line segment $XY$ is perfectly parallel to the shipping lane $CD$.

If the sensor at point $Y$ measures the angle $\angle PYB$ to be exactly $10^{\circ}$, determine the measure of the angle $\angle XCM$ formed between the checkpoint $X$, beacon $C$, and the perimeter marker $M$.

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
