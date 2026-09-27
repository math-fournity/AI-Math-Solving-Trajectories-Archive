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

In a specialized optics laboratory, a high-tech circular lens acts as a "reciprocal inverter" for light rays. This lens maps every physical coordinate $(x, y)$ of an incoming light beam to a new projection coordinate $(u, v)$ according to the following physical laws:
- The horizontal projection $u$ is calculated as the ratio of the original horizontal position to the square of the distance from the source: $u = \frac{x}{x^2 + y^2}$.
- The vertical projection $v$ is calculated as the negative ratio of the original vertical position to the square of the distance from the source: $v = \frac{-y}{x^2 + y^2}$.

An engineer places a square-shaped fiber-optic frame in front of the lens. This frame is centered at the origin $(0, 0)$ and has a total side length of $2$ units, with its edges aligned perfectly parallel to the horizontal and vertical axes of the lab.

As light passes through the boundary (the perimeter) of this square frame and is processed by the lens, it forms a closed loop on a sensor screen. Calculate the total area enclosed by the resulting shape projected on the sensor screen.

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
