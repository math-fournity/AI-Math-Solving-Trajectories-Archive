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

In a circular botanical garden, four landmark trees are planted along the perimeter fence ($\omega$) at locations $A, C, D,$ and $B$ in clockwise order. Straight walking paths connect several points in the garden. The direct distance between tree $C$ and tree $D$ is 6 decameters. The distance from tree $A$ to tree $C$ is 5 decameters, while the distance from tree $D$ to tree $B$ is 7 decameters. A long straight maintenance road follows the chord connecting tree $A$ and tree $B$.

A decorative fountain is located at a specific point $P$ on the perimeter fence. A visitor walking from the fountain $P$ to tree $C$ crosses the maintenance road at point $P_1$, and a visitor walking from the fountain $P$ to tree $D$ crosses the road at point $P_2$. Measuring along the road, the distance from tree $A$ to the crossing $P_1$ is exactly 3 decameters, and the distance from the crossing $P_2$ to tree $B$ is exactly 4 decameters. It is known that $P$ is the only point on the perimeter fence where this specific configuration of $P_1$ and $P_2$ exists.

A second fountain is located at another point $Q$ on the perimeter fence. A visitor walking from $Q$ to tree $C$ crosses the maintenance road at point $Q_1$, and a visitor walking from $Q$ to tree $D$ crosses the road at point $Q_2$. Along the road, $Q_1$ is positioned closer to tree $B$ than $P_1$ is. Furthermore, the distance along the road between the two crossings $P_2$ and $Q_2$ is exactly 2 decameters.

If the distance between the road crossings $P_1$ and $Q_1$ is expressed as a reduced fraction $\frac{p}{q}$, find the value of $p+q$.

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
