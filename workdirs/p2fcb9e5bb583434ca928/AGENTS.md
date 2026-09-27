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

In the coastal city of Altis, a main harbor dock stretches exactly 12 meters between two bollards, Point A and Point B. Two parallel piers, Pier X and Pier Y, extend indefinitely into the ocean, both starting perpendicularly from bollards A and B respectively, and both heading North.

A marine engineering firm is testing a modular floating platform designed in the shape of a rhombus, $MNPQ$. To secure the platform for a stability test, the following constraints must be met:
- Corner $M$ must be anchored somewhere along the 12-meter dock segment $AB$.
- Corner $P$ must float somewhere along the line of Pier X (the ray $Ax$).
- Corner $Q$ must float somewhere along the line of Pier Y (the ray $By$).
- The mechanical linkage at corner $M$ is fixed such that the internal angle $\angle NMQ$ is maintained at exactly $60^\circ$.

As the platform is shifted to different valid positions along the piers and the dock, the remaining corner, $N$, moves accordingly. It has been mathematically determined that the collection of all possible locations for corner $N$ forms a perfectly straight path (a line segment) on the surface of the water.

Calculate the total length of this segment formed by all possible positions of $N$.

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
