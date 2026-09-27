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

Deep in a subterranean research facility, a spherical drone named "Fred" is stationed at a specific corner (vertex) inside a hollow, cubic containment chamber with an interior side length of 2 meters. On the exterior surface of this 2-meter cube, a robotic sensor named "Aaron" is positioned at an unknown starting point.

At a precise signal, both units move toward the same target: the corner of the cube exactly opposite to Fred’s starting position. Fred, being a drone, flies through the air inside the cube in a perfectly straight line at a constant speed of $\sqrt{3}$ meters per second. Aaron, being a surface-crawler, must remain on the exterior faces of the cube at all times, moving at a constant speed of $\sqrt{2}$ meters per second. Aaron follows the shortest possible path available to him on the surface to reach the target corner.

If Aaron reaches the target corner in strictly less time than it takes Fred to arrive, Aaron is considered "successful." The total area of the exterior surface of the cube from which Aaron could have started his journey to ensure success can be expressed in the form $a\pi + \sqrt{b} + c$, where $a, b,$ and $c$ are integers.

Find the value of $a + b + c$.

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
