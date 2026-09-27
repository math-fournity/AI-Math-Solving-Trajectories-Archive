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

In a remote industrial terminal, a logistics grid is defined by 21 horizontal conveyor tracks and 26 vertical conveyor tracks, creating a network of 20 by 25 rectangular storage zones. This grid contains a set of "internal junction points" where the interior tracks intersect, excluding any points on the outer boundary of the terminal.

An automated transport robot must follow a single, continuous, closed loop along the track segments. The robot’s path is subject to three strict operational constraints:
1. The path must never cross over itself.
2. The path must visit every single one of the $(20-1) \times (25-1)$ internal junction points exactly once.
3. The path is forbidden from touching or passing through any junction points located on the outer perimeter of the grid.

To evaluate the efficiency of the robot's route, the following metrics are recorded:
- Let $A$ be the total number of internal junction points where the robot moves in a straight line (entering and exiting the junction in the same direction).
- Let $B$ be the total number of storage zones (rectangles) where the robot’s path utilizes exactly two opposite sides of the zone’s boundary.
- Let $C$ be the total number of storage zones where the robot’s path does not utilize any of the four sides of the zone’s boundary.

Calculate the final efficiency rating defined by the value of $A - B + C$.

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
