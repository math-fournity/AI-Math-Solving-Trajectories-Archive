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

In a remote sector of the ocean, three research buoys—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. The straight-line distances between these buoys are designated as $c$ (between $A$ and $B$), $a$ (between $B$ and $C$), and $b$ (between $A$ and $C$). A central Command Hub ($I$) is positioned at the exact location where the paths bisecting the interior angles of the triangular perimeter meet.

An automated drone is stationed at point $M$, which is the precise midpoint of the cable connecting buoy $A$ and buoy $B$. The distance from the Command Hub ($I$) to this drone ($M$) is exactly 5 units.

The research team performs two spatial transformations to establish new observation coordinates:
1. Coordinate $A_1$ is established by reflecting the position of buoy $A$ across the line representing the internal angle bisector of $\angle B$.
2. Coordinate $B_1$ is established by reflecting the position of buoy $B$ across the line representing the internal angle bisector of $\angle A$.

A secondary sensor is placed at point $N$, which is the midpoint of the direct path between the new coordinates $A_1$ and $B_1$. The distance from the Command Hub ($I$) to this sensor ($N$) is exactly 7 units.

If the distance between buoy $A$ and buoy $B$ is measured to be 10 units, determine the length of the straight-line segment between the coordinates $A_1$ and $B_1$.

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
