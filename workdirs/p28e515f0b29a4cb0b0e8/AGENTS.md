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

A specialized architectural firm is designing a quadrilateral courtyard $ABCD$. The northern perimeter $AB$ and southern perimeter $CD$ are parallel, with $AB$ being the longer of the two. A decorative stone path $AC$ runs diagonally across the courtyard. To ensure symmetry, this path is designed to perfectly bisect the interior corner at $A$.

A second structural line, representing the interior angle bisector of corner $B$, is projected across the floor and intersects the stone path $AC$ at a central fountain located at point $E$. A surveyor marks a point $F$ on the northern perimeter $AB$ such that the line connecting $D$ to the fountain $E$ passes directly through $F$.

The construction team measurements confirm two specific spatial equalities: the length of the western wall $AD$ is exactly equal to the length of the segment $FB$, and the length of the eastern wall $BC$ is exactly equal to the length of the segment $AF$.

Using a precision laser, an engineer measures the angle $\angle BEC$ at the fountain to be exactly $54^\circ$. 

Determine the four interior angles of the quadrilateral courtyard: $\angle A, \angle B, \angle C,$ and $\angle D$ (measured in degrees). Calculate the final architectural code given by the expression $1000\angle A + 100\angle B + 10\angle C + \angle D$.

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
