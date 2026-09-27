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

In a futuristic city, a central plaza is designed in the shape of a perfect regular pentagon, $A_1A_2A_3A_4A_5$, where each side measures exactly 1 kilometer. To expand the pedestrian zone, city planners extend each of the five boundary lines in both directions until they intersect with the extensions of the neighboring sides. This process creates five new outer landmark points, $\{B_1, B_2, B_3, B_4, B_5\}$, resulting in a large, symmetrical 10-sided star-shaped perimeter defined by the boundary segments $B_1A_3$, $A_3B_5$, $B_5A_2$, $A_2B_4$, $B_4A_1$, $A_1B_3$, $B_3A_5$, $A_5B_2$, $B_2A_4$, and $A_4B_1$.

An architectural firm is tasked with paving a specific quadrilateral zone within this complex, defined by the coordinates of the four points $A_2$, $A_5$, $B_2$, and $B_5$. 

What is the ratio of the area of this paved quadrilateral $A_2A_5B_2B_5$ to the total area enclosed by the entire 10-sided outer perimeter?

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
