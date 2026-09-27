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

In a remote territory, two circular radar coverage zones, Zone 1 and Zone 2, overlap. Their perimeters intersect at two specific observation outposts: Outpost A and Outpost B. A straight supply road connects a fuel depot P (located on the boundary of Zone 1) to a communication hub Q (located on the boundary of Zone 2). This road PQ is perfectly tangent to the perimeter of Zone 1 at P and tangent to the perimeter of Zone 2 at Q. Between the two outposts, Outpost A is situated geographically closer to the supply road PQ than Outpost B.

A drone is stationed at a point X on the boundary of Zone 1 such that the flight path PX is perfectly parallel to the straight line connecting hub Q to Outpost B. Simultaneously, a technician is located at a point Y on the boundary of Zone 2 such that the path QY is perfectly parallel to the straight line connecting depot P to Outpost B.

Surveyors determine that the angle formed between the path from Outpost A to depot P and the supply road PQ is exactly 30°. Furthermore, the angle formed between the path from Outpost A to hub Q and the supply road PQ is exactly 15°.

Calculate the ratio of the distance between Outpost A and drone X to the distance between Outpost A and technician Y (the value of AX / AY).

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
