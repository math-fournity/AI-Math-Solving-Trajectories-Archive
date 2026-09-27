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

In a remote industrial complex, two circular power grids are being designed. The first grid, Grid A, consists of 10 specialized generators, each with a unique power rating chosen from the set $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ kW. The second grid, Grid B, consists of 11 generators with unique power ratings from the set $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\}$ kW.

In both grids, the generators are arranged in a single closed loop. The "Interference Cost" between any two adjacent generators in the loop is calculated by multiplying their power ratings. The total system cost for a grid is the sum of the interference costs between all adjacent pairs in the circle (including the pair formed by the last and the first generator).

Engineers want to arrange the generators in each grid to achieve the absolute minimum possible total system cost. Let $M(10)$ be the minimum total system cost for Grid A, and let $M(11)$ be the minimum total system cost for Grid B.

Find the value of $M(10) + M(11)$.

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
