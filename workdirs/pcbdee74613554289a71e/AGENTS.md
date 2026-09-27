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

In a specialized robotics facility, a technician is constructing a flexible structural loop using five rigid carbon-fiber struts of identical length $L$. The joints between these struts allow for rotation in three-dimensional space, meaning the resulting structure does not have to lie flat on a table.

The technician begins by connecting the struts one by one. To ensure the structural integrity of the first four corners, they use high-precision brackets that lock the joints at exactly $90^\circ$ angles. Specifically, the angle between the first and second strut is $90^\circ$, the angle between the second and third is $90^\circ$, the angle between the third and fourth is $90^\circ$, and the angle between the fourth and fifth is $90^\circ$.

The final step is to connect the end of the fifth strut back to the beginning of the first strut to close the loop. However, the technician finds that the structure must be bent into a non-planar configuration (warped out of a single flat plane) to satisfy all these constraints simultaneously.

Based on the geometry of this non-planar closed loop with five equal sides and four right angles, what is the value of the fifth and final angle required to close the loop?

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
