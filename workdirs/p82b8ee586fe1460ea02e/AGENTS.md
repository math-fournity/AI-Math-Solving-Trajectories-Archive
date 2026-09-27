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

In a massive logistics hub, there are 100 shipping containers stacked vertically in 25 separate columns, forming a grid-like structure of 100 rows and 25 columns. Each position in this grid holds a cargo weight (a non-negative real number). 

Initial quality control inspections established a strict safety rule for the horizontal distribution: in the original loading configuration, the total weight of the 25 items across any single horizontal row was guaranteed to be at most 1 metric ton.

To optimize the stability of the stacks, a robotic crane system rearranged the cargo within each of the 25 columns independently. In every column, the 100 items were re-stacked so that their weights are now in descending order from the top (Row 1) to the bottom (Row 100).

The facility manager needs to identify a specific safety threshold, $k$. She needs to find the smallest integer $k$ such that, regardless of what the specific initial weights were, the total weight of the 25 items in any row from the $k$-th row down to the 100th row is now guaranteed to be at most 1 metric ton.

Determine the value of $k$.

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
