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

A logistics company operates a warehouse organized into a grid of 30 storage bays, arranged in 5 rows and 6 columns. To optimize inventory tracking, the manager assigns a unique security code—an integer from 1 to 30—to each bay, ensuring every number is used exactly once.

The facility's automated retrieval system has a specific constraint: for any two codes that are consecutive integers ($n$ and $n+1$), the bays assigned those codes must be located in either the same row or the same column.

Due to a system error, only the following bay assignments are currently visible in the warehouse database:
- Row 1: Bay 1 contains code 29.
- Row 2: Bay 2 contains code 19; Bay 5 contains code 17.
- Row 3: Bay 1 contains code 13; Bay 4 contains code 21; Bay 6 contains code 8.
- Row 4: Bay 2 contains code 4; Bay 4 contains code 15; Bay 6 contains code 24.
- Row 5: Bay 1 contains code 10; Bay 4 contains code 26.

The manager needs to verify the security of the perimeter. Find the sum of the four security codes located in the four corner bays of the grid.

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
