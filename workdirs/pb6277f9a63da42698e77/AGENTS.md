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

In a futuristic industrial facility, an artist is designing a heavy-metal sculpture composed of three intersecting solid components, each centered at the origin of a 3D coordinate system $(x, y, z)$.

The first component, Component A, is a solid cylinder oriented along the x-axis. It is defined by the region where the absolute value of the x-coordinate is less than or equal to 1, while the cross-section in the $yz$-plane is a circle of radius 1 (satisfying $y^2 + z^2 \leq 1$).

The second component, Component B, is an identical solid cylinder but oriented along the y-axis. It is defined by the region where the absolute value of the y-coordinate is less than or equal to 1, while its cross-section in the $zx$-plane is a circle of radius 1 (satisfying $z^2 + x^2 \leq 1$).

The third component, Component C, is the final cylinder oriented along the z-axis. It is defined by the region where the absolute value of the z-coordinate is less than or equal to 1, while its cross-section in the $xy$-plane is a circle of radius 1 (satisfying $x^2 + y^2 \leq 1$).

The sculpture is formed by the union of these three cylinders (the total space occupied by at least one of the components). Calculate the total volume of this union.

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
