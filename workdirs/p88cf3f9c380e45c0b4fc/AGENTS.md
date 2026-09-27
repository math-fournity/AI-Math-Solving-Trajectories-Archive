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

In a remote industrial testing zone, a circular storage tank $\omega$ with center $O$ is situated on a flat plain. A long, straight inspection rail stretches across the ground, containing a specific diameter of the tank denoted by the segment $RM$. Two observation sensors, $A$ and $L$, are positioned on this rail outside the tank’s perimeter, with the points appearing in the order $A, R, M, L$ along the line.

A secondary straight pipeline $LK$ is laid out such that it is perfectly tangent to the circular tank at a connection point $K$. Measurements show that the distance along the pipeline from sensor $L$ to the connection point $K$ is exactly $3$ units ($KL = 3$), while the distance along the rail from the edge of the tank at $M$ to sensor $L$ is exactly $2$ units ($ML = 2$).

A laser beam is fired from sensor $A$ toward the connection point $K$. This beam intersects the tank's shell at a point $Y$ located between $A$ and $K$. A specialized geometric analysis of the site reveals a specific angular relationship: the angle formed between the laser beam and the pipeline ($\angle AKL$) exceeds the angle formed between the shell points $Y$ and $K$ relative to the tank edge $M$ ($\angle YMK$) by exactly $90^{\circ}$.

An engineer needs to calculate the land area enclosed by the triangle formed by sensor $A$, the connection point $K$, and the tank edge $M$ (denoted as $[AKM]$). If this area is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a + b$?

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
