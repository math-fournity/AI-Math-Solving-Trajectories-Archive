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

In a remote territory, two specialized supply routes, Route $AB$ and Route $AC$, originate from a central Command Hub $A$. A third boundary road, Route $BC$, connects the two terminal outposts $B$ and $C$. The distances between these locations are precisely measured: the distance from $A$ to $B$ is 13 km, from $A$ to $C$ is 15 km, and the boundary road $BC$ spans 14 km. A midpoint relay station $M$ is established exactly halfway along the road $BC$.

The territory is divided into two triangular sectors: Sector $ABM$ and Sector $ACM$. In Sector $ABM$, a circular patrol zone (the incircle) is established such that it touches the supply route $AB$ at a checkpoint $D$. Simultaneously, in Sector $ACM$, a second circular patrol zone (its incircle) is established, touching the supply route $AC$ at a checkpoint $E$.

To facilitate coordination, a reconnaissance drone is positioned at a coordinate $F$ such that the four locations $D$, $M$, $E$, and $F$ form the vertices of a parallelogram $DMEF$ in that specific order.

In a separate logistical plan, a straight communication line is laid from Hub $A$ to a point $L$ on the boundary road $BC$, following the exact path that bisects the angle formed by the two primary supply routes at Hub $A$. 

If the straight-line distance from Command Hub $A$ to the drone at $F$ is denoted as $d$, and the length of the communication line $AL$ is denoted as $v$, calculate the ratio $d/v$.

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
