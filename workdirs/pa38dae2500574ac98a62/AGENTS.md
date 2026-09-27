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

In a specialized laboratory, a robotic arm moves along a four-dimensional grid system. The position of the arm is defined by a coordinate tuple $(a, b, c, d)$, where each coordinate is an integer from the set $\{1, 2, 3, 4\}$. There are 256 possible locations in this grid, but one specific location—the origin point $(1, 1, 1, 1)$—is strictly off-limits because its product $abcd$ is not greater than 1.

The robot must perform a maintenance routine that visits every single one of the 255 valid locations exactly once. This sequence of locations is labeled $P_1, P_2, \dots, P_{255}$. Due to mechanical constraints, the robot can only move between adjacent locations. Specifically, for every step from $P_n$ to $P_{n+1}$, the robot must change exactly one of its four coordinates by a value of 1 (either increasing or decreasing), while the other three coordinates remain identical.

The routine begins at a starting position $P_1 = (a_1, b_1, c_1, d_1)$. It is known that for this initial position, both the third and fourth coordinates are equal to 1 ($c_1 = 1$ and $d_1 = 1$).

Determine the sum of all possible values of the sum $a_1 + b_1$ that would allow the robot to successfully complete this 255-step path covering every valid location.

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
