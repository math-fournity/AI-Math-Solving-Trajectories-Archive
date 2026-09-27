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

In a remote desert territory, three border outposts—Alpha (A), Bravo (B), and Charlie (C)—form a triangular perimeter. A circular patrol route is established that passes directly through outpost Bravo. This route intersects the straight supply road between Alpha and Bravo at a checkpoint named Kilo (K), and it intersects the road between Bravo and Charlie at a checkpoint named Lima (L).

The patrol route is designed such that it is tangent to the southern border road (the straight line connecting Alpha and Charlie) exactly at its midpoint, marked as station Mike (M). 

A specialist unit is stationed at a point November (N) on the circular route. Point November lies on the specific arc between Lima and Bravo that does not pass through Kilo. The orientation of this unit is calibrated such that the angle formed between the lines connecting Kilo, Lima, and November ($\angle LKN$) is identical to the internal angle of the territory at outpost Charlie ($\angle ACB$).

Surveyors have determined that the triangle formed by the locations Kilo, Charlie, and November is perfectly equilateral. Based on these geographic constraints, calculate the measure of the internal angle of the territory at outpost Alpha ($\angle BAC$) in degrees.

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
