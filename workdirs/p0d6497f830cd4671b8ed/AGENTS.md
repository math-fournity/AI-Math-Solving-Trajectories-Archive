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

A specialized logistics company manages 100 regional warehouses, each containing 25 distinct storage compartments indexed by their capacity to hold liquid fuel. Initially, the amount of fuel in the $j$-th compartment of the $i$-th warehouse is recorded as $x_{i, j}$ (where $i=1, 2, \dots, 100$ and $j=1, 2, \dots, 25$). All fuel measurements are non-negative real numbers. The company enforces a strict safety protocol: the total amount of fuel stored in any single warehouse must not exceed 1 unit.

To optimize their inventory, the company performs a "Virtual Reorganization." For each specific compartment index $j$ (from 1 to 25), they gather the fuel levels from that compartment across all 100 warehouses and reassign them into a new set of 100 virtual slots. These slots are ranked from highest to lowest, such that for each $j$, the new values $x_{i, j}^{\prime}$ satisfy $x_{1, j}^{\prime} \geq x_{2, j}^{\prime} \geq \dots \geq x_{100, j}^{\prime}$.

Following this reorganization, the company calculates the "Virtual Total" for each virtual warehouse level $i$, defined as the sum of the rearranged fuel levels across all 25 compartments: $\sum_{j=1}^{25} x_{i, j}^{\prime}$.

Find the smallest natural number $k$ such that for any initial distribution of fuel satisfying the safety protocol, it is guaranteed that for all virtual levels $i \geq k$, the Virtual Total $\sum_{j=1}^{25} x_{i, j}^{\prime}$ is also less than or equal to 1.

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
