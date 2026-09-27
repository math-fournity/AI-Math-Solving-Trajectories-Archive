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

In a futuristic data-storage facility, an array of memory cells is arranged in a specific grid consisting of 2012 vertical columns. The architecture follows a staggered pattern: every odd-numbered column (1st, 3rd, ...) contains 2012 cells, while every even-numbered column (2nd, 4th, ...) contains 2013 cells. 

To initialize the system, an engineer sets the energy level of every cell in the $i$-th column to the integer value $i$, for all columns $1 \le i \le 2012$. 

The system's state can be altered by a "Triple-Sync" operation. This operation requires selecting three memory cells that are all mutually adjacent to one another. There are two types of Triple-Sync operations:
1.  **Clockwise Pulse:** The energy levels of the three chosen cells are rotated in a clockwise direction, and then each of the three values is decreased by 1.
2.  **Counter-Clockwise Pulse:** The energy levels of the three chosen cells are rotated in a counter-clockwise direction, and then each of the three values is increased by 1.

Let $N$ represent the total number of memory cells in the entire grid. After performing any number of these operations in any order, what is the maximum number of cells that can simultaneously have an energy level of exactly 0?

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
