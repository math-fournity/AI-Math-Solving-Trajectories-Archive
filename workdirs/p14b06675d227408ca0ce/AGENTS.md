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

A specialized irrigation system is designed for a triangular field with vertices labeled $A$, $B$, and $C$. The field boundaries have lengths $AB = 7$ units, $BC = 6$ units, and $AC = 5$ units. At the exact center of the field sits a circular reservoir, $\Gamma$, which is perfectly tangent to all three boundary fences. The point where this reservoir touches the fence $BC$ is marked as point $P$.

An underground sensor line is laid out starting from $P$, running perfectly parallel to the straight path connecting vertex $A$ to the center of the reservoir, $I$. This sensor line intersects the edge of the circular reservoir at a second point, $Q$. 

A straight access road, $\ell$, is constructed such that it is tangent to the circular reservoir at point $Q$. This road spans across the field, intersecting the boundary fence $AB$ at a security post $S$ and the boundary fence $AC$ at a security post $R$.

What is the straight-line distance between the two security posts $R$ and $S$?

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
