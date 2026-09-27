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

A drone surveillance firm is monitoring a triangular territory defined by three radio towers. Tower A is the central command hub located at coordinates (0,0). Tower B is an offshore platform at (200, 100), and Tower C is a mountain outpost at (30, 330). All coordinates are measured in kilometers.

The firm has divided the entire region into a grid of 1km x 1km square sectors. Each sector is identified by the integer coordinates $(x, y)$ of its bottom-left corner (e.g., the sector $(5, 5)$ covers the area where $5 \le \text{East} \le 6$ and $5 \le \text{North} \le 6$).

A signal sensor is placed at the exact center of every square sector. A sensor is considered "active" only if it lies strictly within the interior of the triangle formed by Towers A, B, and C.

Compute the number of active sensors (i.e., the number of ordered pairs of integers $(x, y)$ such that the point $(x+0.5, y+0.5)$ lies inside triangle ABC).

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
