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

In the competitive world of architectural landscaping, two developers are designing a triangular park defined by three straight walking paths: Avenue $B$ (base), Boulevard $A$ (left side), and Corridor $C$ (right side). The layout is perfectly symmetrical such that the lengths of Boulevard $A$ and Corridor $C$ are equal ($AB=AC$). At the heart of the park is a circular fountain $O$, positioned to be exactly tangent to all three paths. The points where the fountain's edge meets Avenue $B$, Corridor $C$, and Boulevard $A$ are marked as Point $K$, Point $L$, and Point $M$ respectively.

A maintenance pipe follows a straight line $OL$ (from the center of the fountain to its contact point on the Corridor), while a decorative stone path follows the line $KM$. These two paths intersect at a junction called Station $N$. A surveillance cable is laid in a straight line from corner $B$ through Station $N$ until it reaches Corridor $C$ at an access port labeled $Q$. 

To ensure stability, a drainage sensor is placed at point $P$, which is the location on the surveillance cable $BQ$ such that the line from the park's apex $A$ to $P$ is perpendicular to the cable. Measurements from the site survey reveal a specific geometric constraint: the distance from corner $B$ to the sensor ($BP$) is exactly equal to the distance from the apex to the sensor ($AP$) plus twice the distance from the sensor to the access port ($PQ$).

Let $R$ be the set of all possible values for the ratio of the length of a side path (Boulevard $A$) to the length of the base path (Avenue $B$). Find the sum of the squares of all elements in $R$.

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
