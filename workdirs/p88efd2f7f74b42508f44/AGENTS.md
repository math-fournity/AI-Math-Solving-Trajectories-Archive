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

A specialized logistics firm manages three distinct regional warehouses—Alpha, Beta, and Gamma—each holding a positive volume of inventory denoted by $x, y$, and $z$ million units, respectively. Due to strict internal regulations, the warehouses cannot all hold the exact same volume of inventory, ensuring that $(x - y)^2 + (y - z)^2 + (z - x)^2 \neq 0$.

The firm’s performance efficiency is measured by a complex "Redundancy-to-Scarcity Index," defined by the ratio of two specific operational metrics:

1.  The **Overhead Metric**: This is calculated by taking the product of the pairwise capacity sums squared—$(x + y)^2$, $(y + z)^2$, and $(z + x)^2$—and then subtracting a global friction constant equal to $64x^2y^2z^2$.
2.  The **Resource Penalty**: This is the product of the three individual volumes $xyz$ and a volumetric imbalance factor. The imbalance factor is the difference between the cube of the total inventory $(x + y + z)^3$ and a baseline density value of $27xyz$.

To optimize the firm's tax liability, the auditors must determine the absolute floor of this index. Calculate the minimum possible value of the function:
\[ F(x,y,z) = \frac{(x + y)^2 (y + z)^2 (z + x)^2 - 64x^2 y^2 z^2}{xyz[(x + y + z)^3 - 27xyz]} \]

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
