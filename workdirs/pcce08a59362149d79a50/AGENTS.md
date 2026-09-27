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

A specialized chemical processing plant utilizes three separate reactors to refine a rare compound. Each reactor $i$ (where $i=1,2,3$) operates with a purity level $x, y, z > 0$. The efficiency of an individual reactor is determined by the formula $E(s) = s^2 - s + 1$. 

The total efficiency of the three-reactor system is defined as the product of the efficiencies of each individual reactor: $E(x) \cdot E(y) \cdot E(z)$.

The plant’s chief engineer is comparing this decentralized system to a hypothetical "mega-reactor" that processes the sum of the purity levels of the three individual reactors. The efficiency of this mega-reactor is calculated using the same formula applied to the total sum: $E(x+y+z) = (x+y+z)^2 - (x+y+z) + 1$.

The engineer discovers that the decentralized system's efficiency is always at least a constant fraction $k$ of the mega-reactor's efficiency for any positive values of $x, y,$ and $z$. 

Determine the maximum possible value of the constant $k$ such that the inequality $(x^2 - x + 1)(y^2 - y + 1)(z^2 - z + 1) \geq k[(x + y + z)^2 - (x + y + z) + 1]$ holds true for all $x, y, z > 0$.

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
