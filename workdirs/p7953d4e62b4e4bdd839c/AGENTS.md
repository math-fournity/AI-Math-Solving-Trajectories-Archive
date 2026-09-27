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

In a specialized vertical hydroponic facility, a technician manages a grid of nutrient delivery nodes located at integer coordinates $(x, y)$. The facility's active zone, $S_{100}$, is defined by a strict environmental boundary. A node is considered part of the active zone if its coordinates satisfy the inequality:
\[ |x| + \left|y + \frac{1}{2}\right| < 100 \]
The facility uses automated inspection drones to monitor these nodes. A drone can traverse a "path," which is a sequence of distinct nodes $(x_1, y_1), (x_2, y_2), \dots, (x_{\ell}, y_{\ell})$ within $S_{100}$ such that each consecutive node in the sequence is exactly 1 unit of distance away from the previous one (moving either horizontally or vertically).

To ensure efficient monitoring, every single node in the set $S_{100}$ must be inspected, and for data integrity, each node must belong to exactly one drone's path.

Determine the minimum number of drones (paths) required to partition all nodes in $S_{100}$ such that every node is visited by exactly one drone.

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
