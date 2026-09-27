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

In a remote circular ecological preserve, three research stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are positioned such that the triangular region they enclose has a total land area of $252$ hectares. To monitor the preserve, scientists have established three supply depots at the exact midpoints of the boundaries between the stations: Depot $A_1$ is halfway between Bravo and Charlie, Depot $B_1$ is halfway between Charlie and Alpha, and Depot $C_1$ is halfway between Alpha and Bravo.

A drone launch pad, Point $P$, is located on the circular perimeter of the preserve. The drone follows three straight-line flight paths from its launch pad through each supply depot until it reaches the opposite side of the circular perimeter. Specifically, the path through Depot $A_1$ hits the perimeter at point $A'$, the path through Depot $B_1$ hits at point $B'$, and the path through Depot $C_1$ hits at point $C'$.

To coordinate communications, the researchers establish three signal relay towers at the intersections of these flight trajectories. Tower $X$ is placed where the straight line connecting Bravo ($B$) to $B'$ intersects the line connecting Charlie ($C$) to $C'$. Tower $Y$ is placed where the line from Charlie ($C$) to $C'$ intersects the line from Alpha ($A$) to $A'$. Tower $Z$ is placed where the line from Alpha ($A$) to $A'$ intersects the line from Bravo ($B$) to $B'$.

Calculate the area, in hectares, of the triangular region formed by the three relay towers $X$, $Y$, and $Z$.

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
