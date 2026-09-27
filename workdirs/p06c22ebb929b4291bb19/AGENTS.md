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

In the coastal city of Geometria, a maritime surveyor is mapping the coordinates of a triangular harbor defined by three jagged cliffs at vertices $A$, $B$, and $C$, forming an acute scalene triangle. At the heart of the harbor lies a lighthouse $I$, located exactly at the harbor's incenter. A rescue station $M$ is positioned at the center of a circular patrol route that passes through the lighthouse $I$ and the two southern cliff bases $B$ and $C$.

On the straight southern shoreline $BC$, the surveyor marks four specific docking points: $D$, $B'$, and $C'$. Point $D$ is the direct projection of the lighthouse onto the shore, while $B'$ and $C'$ are positioned such that the patrol paths $IB'$ and $IC'$ are perpendicular to the lines $IB$ and $IC$ respectively. To coordinate logistics, the surveyor identifies two intersection points: $P$, where the supply line from cliff $A$ to cliff $B$ meets the navigation path $MC'$, and $Q$, where the supply line from cliff $A$ to cliff $C$ meets the navigation path $MB'$.

A central signal buoy $S$ is placed at the intersection of the line $MD$ and the line segment $PQ$. Within the lighthouse’s protective zone (the incircle), a vertical diameter $EF$ is established such that $S$ is closer to cliff $A$ than it is to the diameter’s endpoint $E$. The final coordination point $K$ is found where the line of sight $SI$ intersects the diameter segment $DF$.

The surveyor’s instruments provide the following precise distances based on a local scaling factor $x$:
- The distance from the coordination point to the lighthouse is $KI = 15x$.
- The distance from the signal buoy to the lighthouse is $SI = 20x + 15$.
- The total length of the southern shoreline is $BC = 20x^{5/2}$.
- The direct distance from the docking point $D$ to the lighthouse is $DI = 20x^{3/2}$.

The scaling factor is known to be of the form $x = \frac{a}{b}(n+\sqrt{p})$, where $a, b, n, p$ are positive integers, $p$ is prime, and $\gcd(a, b) = 1$. Calculate the sum $a+b+n+p$.

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
