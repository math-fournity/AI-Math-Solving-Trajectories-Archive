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

In the remote logistics hub of Aetheria, three specialized transport drones—Alpha, Beta, and Gamma—operate along a linear magnetic rail. Their horizontal displacements from the central charging station are represented by the positive values $x$, $y$, and $z$ (measured in kilometers). Due to energy grid constraints, the drones must maintain a specific operational balance such that the sum of the distances of Alpha and Beta minus the distance of Gamma is exactly $12$ kilometers ($x + y - z = 12$).

Each drone must also travel to a specific off-rail maintenance platform:
- Alpha must travel from its rail position $(x, 0)$ to a platform located at $(0, 2)$. The distance of this path is $\sqrt{x^2 + 4}$.
- Beta must travel from its rail position $(y, 0)$ to a platform located at $(-3, 4)$. The distance of this path is $\sqrt{(y+3)^2 + 4^2}$, which simplifies to $\sqrt{y^2 + 6y + 25}$.
- Gamma must travel from its rail position $(z, 0)$ to a signal tower located at $(0, 3)$. The distance of this path is $\sqrt{z^2 + 9}$.

An engineer needs to calculate the minimum possible net fuel consumption for a synchronized mission, which is defined by the combined travel distances of Alpha and Beta minus the travel distance of Gamma.

Find the minimum possible value of $\sqrt{x^2+4} + \sqrt{y^2+6y+25} - \sqrt{z^2+9}$.

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
