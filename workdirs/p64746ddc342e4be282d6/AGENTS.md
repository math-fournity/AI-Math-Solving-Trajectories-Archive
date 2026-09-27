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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a scalene triangular network. The direct distance between depots $B$ and $C$ is exactly $1099$ units. Within this network, two specialized coordination hubs are defined: Hub $I$ is the "Incenter" (the point equidistant from all three supply routes), and Hub $K$ is the "Symmedian Point" (the isogonal conjugate of the network's centroid).

A central command station, Point $P$, is established within the same plane. To monitor the territory, three sensors—$D, E,$ and $F$—are placed at the nearest points on the straight-line paths $BC, CA,$ and $AB$, respectively, such that each sensor's connection to $P$ is perpendicular to its corresponding path. 

Two critical survey markers are identified: Marker $M$ is placed at the exact midpoint of the line between sensors $E$ and $F$, while Marker $N$ is placed at the exact midpoint of the supply route between $B$ and $C$. 

Technical assessments reveal two specific geometric alignments:
1. Marker $M$, Depot $A$, and Marker $N$ lie perfectly along a single straight line.
2. Hub $K$, Hub $I$, and Sensor $D$ also lie perfectly along a single straight line.

Furthermore, satellite imaging determines that the area of the triangular region formed by the sensors $\triangle DEF$ is exactly $2020$ times the area of the triangular region formed by the depots $\triangle ABC$.

Based on these configurations, determine the largest possible value of $\lceil AB + AC \rceil$, where $AB$ and $AC$ are the distances between the respective depots.

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
