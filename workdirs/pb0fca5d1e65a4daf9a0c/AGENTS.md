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

In the circular command center of a deep-sea station, a technician is installing modular floor panels to cover a circular deck with a radius of 1 meter. The deck must be entirely filled using wedge-shaped panels (sectors), each with a radius of 1 meter. These panels come in two sizes: a narrow size with a central angle of $36^{\circ}$ and a wide size with a central angle of $72^{\circ}$. 

Each panel is available in three possible colors: White, Green, and Red. To comply with safety and aesthetic regulations, the technician must follow two specific placement rules:
1. Any two adjacent panels must be of different colors.
2. For any sequence of three consecutive panels, if the middle panel is a narrow ($36^{\circ}$) wedge, all three panels in that sequence must be of different colors (meaning the panels on either side of the narrow one must be different from the narrow one and also different from each other).

It is not required to use all three colors or both sizes of panels in a completed design. Two floor layouts are considered identical if one can be rotated to match the other, but they are considered distinct if they can only be matched via reflection.

In how many distinct ways can the technician tile the circular deck?

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
