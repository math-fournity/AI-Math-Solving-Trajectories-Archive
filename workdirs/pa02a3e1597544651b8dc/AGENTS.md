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

In the coastal territory of Arthemia, three watchtowers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular defensive perimeter. The distance between Alpha and Bravo is exactly 17 leagues, the distance between Alpha and Charlie is 25 leagues, and the distance between Bravo and Charlie is 28 leagues.

Two supply outposts are established at the exact midpoints of the existing borders: Outpost Midas ($M$) sits halfway between Alpha and Bravo, while Outpost North ($N$) sits halfway between Alpha and Charlie. A mobile patrol unit, $P$, moves continuously along the 28-league straight road connecting watchtowers Bravo and Charlie.

To coordinate communications, two circular signal zones are mapped: the first is the unique circle passing through $B$, $M$, and the current position of patrol $P$; the second is the unique circle passing through $C$, $N$, and patrol $P$. These two signal zones always intersect at two locations: the current position of the patrol unit $P$, and a secondary relay point $Q$.

Data analysts have observed a unique phenomenon: as the patrol unit $P$ travels back and forth along the road between Bravo and Charlie, the straight line of sight connecting $P$ and the relay point $Q$ always pivots through a single, fixed geographic coordinate $X$.

To calibrate the regional GPS grid, surveyors must determine the sum of the squares of the distances from this fixed point $X$ to each of the three original watchtowers Alpha, Bravo, and Charlie. 

Compute $XA^2 + XB^2 + XC^2$.

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
