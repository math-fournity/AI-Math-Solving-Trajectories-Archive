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

In a specialized logistics network, an efficiency metric $E(r, c)$ is assigned to every workstation located at the intersection of row $r$ and column $c$, where $r$ and $c$ are positive integers.

The workstations on the boundary of the grid are calibrated such that for any positive integer $k$, the efficiency at the first row and $k$-th column is $E(1, k) = \frac{1}{k}$, and the efficiency at the $k$-th row and first column is $E(k, 1) = \frac{1}{k}$.

For all other internal workstations, the efficiencies are governed by a "Cross-Stability Protocol." This protocol dictates that for any $2 \times 2$ cluster of adjacent workstations—defined by the coordinates $(x, y), (x+1, y), (x, y+1),$ and $(x+1, y+1)$—the local efficiencies must satisfy the following determinant-like equilibrium:
$$E(x+1, y+1) \cdot E(x, y) - E(x, y+1) \cdot E(x+1, y) = 1$$

Given that the efficiency at the workstation located at $(100, 100)$ can be expressed as a fraction $\frac{m}{n}$ in lowest terms (where $m$ and $n$ are relatively prime positive integers), compute the value of $m+n$.

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
