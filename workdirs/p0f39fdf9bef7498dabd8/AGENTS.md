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

A specialized triangular space station module, represented by a planar region $ABC$ with side length $a$, is fixed in deep space. A square cargo container $ABPQ$ with side length $a$ is docked such that its edge $AB$ perfectly aligns with the module's edge $AB$. The container is located entirely outside the triangle's perimeter.

A robotic arm begins to move the container around the triangular module in a counterclockwise direction. The movement is a "no-slip roll": the container pivots around a shared vertex until its next side lies flat against the next side of the triangle. A "full round" is defined as the container completing a journey around the perimeter of the triangle until one of its sides (not necessarily the original side $AB$) once again coincides with the original segment $AB$ of the triangle.

The rolling process continues until the container reaches its absolute initial state—meaning each specific vertex $A, B, P$, and $Q$ of the square occupies the exact same coordinate in space as it did at the start of the mission.

Let:
- $n$ be the total number of full rounds around the triangle $ABC$ required for the vertices to first return to their original positions.
- $r$ be the total number of full $360^{\circ}$ rotations the square container has performed relative to its own center $M$ throughout this entire process.

Calculate the value of $10n + r$.

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
