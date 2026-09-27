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

In the remote kingdom of Geometria, three watchtowers—Alpha, Bravo, and Charlie—form a triangular perimeter. The internal bearing angles at these towers, denoted as $A$, $B$, and $C$ respectively, are all measured in whole numbers of degrees. 

To expand the kingdom's territory, two massive square-shaped plazas are paved directly outside the perimeter:
1. Plaza Delta is built using the boundary segment between Bravo and Charlie as one of its sides. Its outer corners are marked by stone pillars $D_1$ and $D_2$.
2. Plaza Echo is built using the boundary segment between Alpha and Charlie as one of its sides. Its outer corners are marked by stone pillars $E_1$ and $E_2$.

A royal surveyor discovers a unique phenomenon: the four outer pillars ($D_1, D_2, E_1, E_2$) all lie perfectly on the circumference of a single circular patrol path.

Based on this structural constraint, how many distinct sets of integer internal angles $(A, B, C)$ are mathematically possible for the layout of the three watchtowers?

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
