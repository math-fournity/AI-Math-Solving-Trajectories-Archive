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

In a remote desert, two straight pipelines, Line Alpha (passing through points $A$ and $B$) and Line Beta (passing through points $A$ and $C$), converge at a central pumping station $A$. The distance along Line Alpha from $A$ to $B$ is exactly equal to the distance along Line Beta from $A$ to $C$. A third straight connecting pipe $BC$ completes a triangular layout $ABC$.

An irrigation hub $O$ is located at the center of the triangle, equidistant from all three pipelines. The hub maintains three maintenance valves: valve $K$ on pipe $BC$, valve $L$ on pipe $CA$, and valve $M$ on pipe $AB$, marking the closest points on each pipe to the hub. 

A straight access road is paved through hub $O$ and valve $L$. Simultaneously, a service cable is laid in a straight line between valves $K$ and $M$. These two paths intersect at a monitoring station $N$. A surveyor then sights a straight line of sight from station $B$ through station $N$ until it hits the pipeline $CA$ at a junction $Q$.

An engineer measures the efficiency of this layout by dropping a perpendicular line from the pumping station $A$ to the line of sight $BQ$, meeting it at point $P$. The survey team records a specific spatial relationship: the distance $BP$ is exactly equal to the distance $AP$ plus twice the distance $PQ$.

Let $r$ represent the ratio of the length of pipeline $AB$ to the length of pipeline $BC$. There are two possible values for this ratio, $r_1$ and $r_2$, that satisfy these geometric conditions. Find the value of $r_1^2 + r_2^2$.

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
