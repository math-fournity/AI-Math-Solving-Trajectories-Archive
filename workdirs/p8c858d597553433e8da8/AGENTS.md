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

In a specialized logistics hub, four automated transport containers are assigned unique ID numbers $(a, b, c, d)$. To ensure structural stability during stacking, these IDs must satisfy the following organizational protocols:

1. Each ID must be a whole number greater than 1.
2. The IDs must be sorted in non-descending order, such that $a \leq b \leq c \leq d$.
3. The hub operates under four "Stability Formulas" used to calculate the load-bearing capacity of a stack. For the stack to be considered "Perfectly Balanced," the result of each formula must be a perfect square number:
   *   Formula 1: $a^{2} + b + c + d$
   *   Formula 2: $a + b^{2} + c + d$
   *   Formula 3: $a + b + c^{2} + d$
   *   Formula 4: $a + b + c + d^{2}$

The safety inspector needs to identify every possible set of IDs $(a, b, c, d)$ that results in four Perfectly Balanced stacks. Find all such sets of ID numbers and calculate the sum of the values of the largest ID ($d$) across all valid sets.

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
