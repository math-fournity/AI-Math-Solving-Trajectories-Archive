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

In the coastal region of Trimetria, three guard towers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Surveyors have measured the straight-line distances between them: the distance from Alpha to Bravo is exactly 13 kilometers, from Bravo to Charlie is 14 kilometers, and from Charlie back to Alpha is 15 kilometers.

A specialized communications drone is programmed to deliver messages between the borders formed by these towers. The drone's flight path follows a strict protocol:
1. It launches from Tower Alpha and flies in a straight line that is perpendicular to the border line $\overline{BC}$.
2. Upon reaching the border $\overline{BC}$, it immediately changes course and flies in a straight line perpendicular to the border line $\overline{CA}$.
3. Upon reaching the border $\overline{CA}$, it changes course to fly in a straight line perpendicular to the border line $\overline{AB}$.
4. Upon reaching the border $\overline{AB}$, it resets its logic and again flies in a direction perpendicular to the border line $\overline{BC}$.

As the drone continues this cycle indefinitely—alternating its perpendicular approaches to $\overline{BC}$, then $\overline{CA}$, then $\overline{AB}$—its flight path converges toward a stable, finite triangular circuit, which we shall call $T_\infty$.

What is the ratio of the total length of the perimeter of this final circuit $T_\infty$ to the total perimeter of the original triangle formed by the three towers $\triangle ABC$?

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
