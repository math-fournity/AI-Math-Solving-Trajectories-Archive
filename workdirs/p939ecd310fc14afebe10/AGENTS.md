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

In the competitive world of high-end chemical fragrance manufacturing, a lab technician is tasked with distributing exactly one liter of a concentrated base essence into a $3 \times 3$ grid of nine specialized mixing vials. 

The technician may allocate any non-negative amount of the essence to each of the nine vials, provided the total volume used across all vials is exactly $1$ liter. Once the vials are filled and placed in their respective grid positions, the "aromatic intensity" of a line is defined as the product of the volumes of the three vials in that line.

The laboratory safety protocol requires that the technician must be able to arrange these nine volumes within the $3 \times 3$ grid such that no single row and no single column has an aromatic intensity exceeding a specific safety threshold, $M$.

Determine the smallest real number $M$ such that, no matter how the one liter of essence is initially partitioned into nine non-negative amounts, there always exists at least one way to arrange them in the grid to satisfy the safety threshold for all three rows and all three columns.

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
