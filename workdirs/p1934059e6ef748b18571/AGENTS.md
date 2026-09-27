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

In a remote desert territory, two surveillance drones, Alpha and Bravo, are stationed at outposts $A$ and $B$. Two logistics hubs, Charlie and Delta, are located at points $C$ and $D$. These four locations form a convex quadrilateral $ABCD$ where the sensor paths $AC$ and $BD$ intersect at a central relay station $E$. The geography is such that the sites do not lie on a single circular perimeter.

The regional dispatch has noted a specific symmetry in the signal angles: the sum of the bearing from outpost $B$ between $A$ and $D$ plus the bearing from outpost $A$ between $D$ and $C$ exactly equals the sum of the bearing from $B$ between $C$ and $D$ plus the bearing from $C$ between $D$ and $A$.

Surveying teams have provided the following exact distances between the nodes:
- The distance from outpost $A$ to outpost $B$ is 10 kilometers.
- The distance from outpost $B$ to hub $C$ is 15 kilometers.
- The relay station $E$ is located 7 kilometers from outpost $A$ along the path to hub $C$.
- The relay station $E$ is located 13 kilometers from hub $C$.

Based on this telemetry, calculate the total length of the straight-line path between outpost $B$ and hub $D$.

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
