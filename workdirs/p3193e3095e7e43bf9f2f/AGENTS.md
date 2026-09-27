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

In a specialized logistics warehouse, an automated transport robot is programmed to deliver a package from the southwestern corner (Coordinate 0,0) to the northeastern corner (Coordinate 6,6). The warehouse floor is a grid with a network of conveyor tracks located at every integer line $x \in \{0, 1, \dots, 6\}$ and $y \in \{0, 1, \dots, 6\}$. 

To conserve energy, the robot is strictly programmed to only move North (increasing $y$) or East (increasing $x$). Under normal conditions, there are many possible paths the robot could take. However, the warehouse manager has placed exactly 6 security sensors on 6 different lattice point intersections $(x, y)$ where $0 \leq x, y \leq 6$. These sensors act as total blockades; the robot cannot pass through any intersection occupied by a sensor.

Upon analyzing the grid, the manager realizes that the sensors have been placed such that there is only one valid path remaining for the robot to reach its destination: it must travel directly North from $(0,0)$ to $(0,6)$, and then turn and travel directly East to $(6,6)$.

How many unique sets of 6 sensor locations could the manager have chosen to ensure that this specific path is the only one available?

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
