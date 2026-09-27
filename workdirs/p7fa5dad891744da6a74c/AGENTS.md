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

A specialized logistics company uses a modular robotic arm to paint a 64-square-meter floor, organized into an $8 \times 8$ grid of 1-meter square tiles. The robot uses a "Z-stamp" applicator that always covers exactly five grid-sized squares in a specific configuration. Relative to a starting square $(i, j)$, the stamp covers: $(i, j)$, $(i, j+1)$, $(i+1, j+1)$, $(i+2, j+1)$, and $(i+2, j+2)$.

The stamping process follows these operational rules:
1. The stamp can be rotated in 90-degree increments to change its orientation.
2. When the stamp is pressed, some of its five squares may land outside the boundaries of the $8 \times 8$ floor. Only the squares that land on the grid are considered "painted."
3. Multiple stamps can overlap on the same tile; a tile is considered covered if at least one stamp has touched it.

What is the minimum number of stamp applications required to ensure that every one of the 64 tiles on the $8 \times 8$ floor has been covered at least once?

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
