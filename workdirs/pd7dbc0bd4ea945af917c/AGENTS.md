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

In a remote territory, three survey outposts, $A$, $B$, and $C$, form an acute triangular perimeter where the distance between $A$ and $C$ is not equal to the distance between $B$ and $C$. A central command hub, $H$, is located at the intersection of two straight utility lines: one originating from $A$ perpendicular to the $BC$ boundary, and one originating from $B$ perpendicular to the $AC$ boundary.

A long, straight perimeter fence is constructed along the external bisector of the corner angle at outpost $C$. The utility line from $A$ is extended until it hits this fence at point $Y$, and the utility line from $B$ is extended until it hits the fence at point $X$.

To coordinate communications, a signal beam is projected from the hub $H$ along the path that externally bisects the angle $\angle AHB$. This beam intersects the segment $AX$ at a terminal $P$ and the segment $BY$ at a terminal $Q$. Engineering sensors confirm that the distance between $P$ and $X$ is exactly equal to the distance between $Q$ and $Y$.

Let $k$ be the largest real number such that the sum of the distances $AP + BQ$ is always greater than or equal to $k$ times the distance between the command hub $H$ and outpost $C$. Find the value of $k$.

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
