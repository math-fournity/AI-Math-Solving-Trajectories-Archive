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

In a remote desert, four survey markers—$O_1, O_2, O_3$, and $O_4$—were placed to represent the centers of four specialized circular irrigation zones. These zones were designed to be tangent to the boundary of a convex quadrilateral field $ABCD$. Specifically, the center $O_1$ is positioned such that its circle touches the fence line $AB$ and the outward extensions of fences $BC$ and $DA$. Similarly, $O_2$ serves the fence $BC$ and extensions of $CD$ and $AB$; $O_3$ serves fence $CD$ and extensions of $DA$ and $BC$; and $O_4$ serves fence $DA$ and extensions of $AB$ and $CD$.

The field $ABCD$ was eventually removed, leaving only the four irrigation centers. A surveyor measuring the distances between these markers recorded the following data:
- The squared distance between markers $O_1$ and $O_3$ is $O_1O_3^2 = 45$.
- The squared distance between markers $O_2$ and $O_4$ is $O_2O_4^2 = 40$.
- The difference between the squared distance from $O_1$ to $O_4$ and the squared distance from $O_2$ to $O_3$ is $O_1O_4^2 - O_2O_3^2 = 12$.
- The difference between the squared distance from $O_3$ to $O_4$ and the squared distance from $O_2$ to $O_1$ is $O_3O_4^2 - O_2O_1^2 = 3$.

Calculate the square of the perimeter of the original quadrilateral field $ABCD$.

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
