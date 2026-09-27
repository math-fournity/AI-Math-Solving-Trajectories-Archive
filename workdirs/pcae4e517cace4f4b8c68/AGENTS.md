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

A specialized cargo drone operates within a square grid of delivery hubs. The hubs are located at every integer coordinate $(x, y)$ such that $-10 \leq x, y \leq 10$. The central control tower is fixed at the origin $O(0, 0)$. The drone, nicknamed "Scotty," begins its mission at terminal $P(0, 1)$.

Every minute, the drone calculates its next move by identifying all possible pairs of idle logistics hubs $C$ and $D$ within the grid that satisfy two conditions:
1. Neither hub $C$ nor hub $D$ lies on the straight line passing through the control tower $O$ and the drone’s current position $P$.
2. The quadrilateral formed by the sequence of points $O, C, P, D$ in clockwise order has an area of exactly $1$ square unit.

From the set of all such pairs $(C, D)$, Scotty identifies the specific pair that maximizes the sum of the $y$-coordinates of $C$ and $D$. He then chooses one of these two hubs at random (each with a probability of $1/2$) and flies to it, establishing that hub as his new position $P$.

After exactly $50$ such moves, Scotty is located at terminal $(1, 1)$. Given this final destination, find the probability that Scotty never occupied the starting terminal $(0, 1)$ at any point during the $50$ moves (excluding his initial presence there at $t=0$). 

If the probability is expressed as an irreducible fraction $\frac{a}{b}$, calculate the value of $a + b$.

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
