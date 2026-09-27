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

In the mountainous kingdom of Isoscelia, a triangular territory is defined by three border outposts: $A$, $B$, and $C$. The distances between the northern outpost $A$ and the two southern outposts $B$ and $C$ are equal ($AB = AC$). 

At the heart of the kingdom lies a circular reservoir $O$, which is perfectly inscribed within the triangle. This reservoir provides water to three distribution hubs located exactly where the circle touches the borders: hub $K$ on border $BC$, hub $L$ on border $CA$, and hub $M$ on border $AB$.

A straight underground pipeline connects hubs $K$ and $M$. Meanwhile, a radial service path runs from the center of the reservoir $O$ to hub $L$. These two paths intersect at a subterranean junction $N$. 

The kingdom’s chief engineer plans a new supply route starting from outpost $B$, passing through junction $N$, and extending until it hits the border $CA$ at a point designated as $Q$. To monitor this route, a surveillance drone is stationed at outpost $A$. The drone’s primary scanner is calibrated to find the point $P$ on the route $BQ$ that is closest to outpost $A$ (the foot of the perpendicular from $A$ to the line $BQ$).

Detailed surveys of these coordinates reveal a specific geographic relationship: the distance from outpost $B$ to point $P$ is exactly equal to the distance from outpost $A$ to point $P$ plus twice the distance from point $P$ to point $Q$. That is, $BP = AP + 2 \cdot PQ$.

Based on these topographic constraints, calculate the sum of all possible values for the square of the ratio of the distance $AB$ to the distance $BC$.

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
