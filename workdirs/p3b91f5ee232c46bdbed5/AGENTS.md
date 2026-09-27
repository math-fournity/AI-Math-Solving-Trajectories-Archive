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

A specialized deep-sea research station is powered by three experimental thermal generators, which produce energy levels represented by the variables $x$, $y$, and $z$ (measured in gigawatts). Because of the unique cooling requirements of the facility, these energy levels are strictly positive and are governed by the fundamental equilibrium equation: the sum of the squares of the energy levels is exactly equal to the product of the three energy levels ($x^2 + y^2 + z^2 = xyz$).

Engineers are monitoring the "Cross-Coupling Efficiency" of the system, defined by the sum of the pairwise products of the energy levels ($xy + yz + zx$). They have discovered a safety threshold governed by a specific architectural constant $a$. This threshold dictates that the Cross-Coupling Efficiency must always be greater than or equal to a value calculated by taking $a$ times the total sum of the energy levels ($x+y+z$) and then subtracting nine times the quantity $(a - 3)$.

Given that the equilibrium equation must always hold for any configuration of the three generators, what is the maximum possible value of the constant $a$ that ensures the safety inequality $xy + yz + zx \ge a(x + y + z) - 9(a - 3)$ is never violated?

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
