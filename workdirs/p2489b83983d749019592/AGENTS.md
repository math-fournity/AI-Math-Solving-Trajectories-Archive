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

In the coastal city of Cartesian Bay, three major trade routes are defined by precise navigational coordinates $(x, y)$. 

The first route, **Harbor Path 1**, follows the trajectory $2x - y = 7$.
The second route, **Harbor Path 2**, follows the trajectory $5x + y = 42$.
The third route, **Harbor Path 3**, follows the trajectory $x + y = 14$.

A high-tech naval drone is programmed with a "Mirror-Jump" sequence. When the drone executes a jump across a path, its position is reflected across that line. A mission is planned where a drone starts at a refueling station $X$ located somewhere on the East-West Mainline (the $x$-axis). The drone must perform three consecutive jumps:
1. First, it reflects its position across **Harbor Path 3**.
2. From that new location, it reflects across **Harbor Path 2**.
3. Finally, it reflects across **Harbor Path 1**.

The mission is successful only if the drone's final coordinates land exactly on a docking station $Y$ located somewhere on the North-South Quay (the $y$-axis).

Let $t$ represent the straight-line distance between the starting refueling station $X$ and the final docking station $Y$. Find the sum of all possible values of $t^2$.

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
