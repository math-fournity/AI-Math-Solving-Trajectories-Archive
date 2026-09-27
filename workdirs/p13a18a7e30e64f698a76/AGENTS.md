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

A specialized architectural firm is designing a hexagonal central plaza for a new park. The layout is based on a primary equilateral triangular field, denoted as $ABC$, with a side length of $12$ decameters. 

To determine the placement of decorative pavers, the architects define three specific control points, $O_A$, $O_B$, and $O_C$, located within the triangular field:
1. Point $O_A$ is positioned such that its distance to corner $B$ is exactly equal to its distance to corner $C$, and its direct distance from corner $A$ is $\sqrt{3}$ decameters.
2. Point $O_B$ is positioned symmetrically relative to corner $B$ (equidistant from $A$ and $C$, and $\sqrt{3}$ units from $B$).
3. Point $O_C$ is positioned symmetrically relative to corner $C$ (equidistant from $A$ and $B$, and $\sqrt{3}$ units from $C$).

The landscape design calls for three distinct triangular overlapping zones: the region $O_A BC$, the region $AO_B C$, and the region $AB O_C$. Calculate the area of the region where all three triangular zones overlap.

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
