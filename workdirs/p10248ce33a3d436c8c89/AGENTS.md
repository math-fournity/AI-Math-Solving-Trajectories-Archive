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

In the coastal kingdom of Geometria, three watchtowers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are positioned such that they form a triangular perimeter. A central naval command center, Station $O$, is located at the exact center of the circle passing through all three towers.

Surveyors have noted two specific measurements: the angle formed at tower Alpha between the paths to Bravo and Charlie is exactly $60^\circ$. Furthermore, there is a supply depot $M$ located exactly halfway between Bravo and Charlie. The angle formed at this depot between tower Alpha and tower Charlie is also $60^\circ$.

The kingdom's engineers are mapping out several strategic lines:
1.  Two observation posts, Echo ($E$) and Foxtrot ($F$), are placed on the walls $AC$ and $AB$ respectively, at the points where the shortest paths (altitudes) from $B$ and $C$ meet the opposite walls.
2.  The straight road connecting $E$ and $F$ is extended until it intersects the straight coastline $BC$ at a harbor designated as Point $P$.
3.  A north-south meridian line passes through the central Station $O$ and is perpendicular to the coastline $BC$. This line crosses $BC$ at the depot $M$. It also intersects the kingdom's circular boundary at two points: $L$ (located on the longer arc between $B$ and $C$) and $N$.
4.  A long-range signal beam is projected from tower $A$ through point $L$.
5.  A specialized scout, Point $Q$, is positioned somewhere along this signal beam $AL$ such that the line segment connecting the central Station $O$ to $Q$ is perfectly perpendicular to the path connecting $A$ to the harbor $P$.

The High Cartographer needs to determine the exact ratio of the distance between the central Station $O$ and the scout $Q$ to the distance between tower $A$ and the harbor $P$.

Compute the value of $OQ / AP$.

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
