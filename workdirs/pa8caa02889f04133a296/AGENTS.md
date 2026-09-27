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

A specialized deep-sea exploration network is mapped across a grid of acoustic sensors. Three primary sensors, $A$, $B$, and $C$, form a triangular surveillance zone. Within this zone, four specific signal-processing hubs are positioned: the internal hub $I$ (the triangle’s incenter) and three external relay hubs $I_A$, $I_B$, and $I_C$ (the triangle’s excenters). The master control center is located at $O$, the center of the unique circular boundary (circumcircle) passing through sensors $A$, $B$, and $C$.

Advanced sonar mapping identifies two circular interference patterns. The first pattern is the circular path defined by the locations of hubs $I$, $C$, and $I_B$. The second pattern is the circular path defined by the three external relay hubs $I_A$, $I_B$, and $I_C$. These two circular paths intersect at two distinct coordinates: the relay hub $I_B$ and a secondary data node labeled $E$.

A linear fiber-optic cable is laid starting from node $E$ and passing through the internal hub $I$. This cable continues until it reaches the circular boundary of the $ABC$ surveillance zone at a point designated as $F$. 

Technical readouts confirm the following distances:
- The distance between the internal hub $I$ and the boundary point $F$ is exactly 17 units.
- The distance between the internal hub $I$ and the master control center $O$ is exactly 23 units.

Calculate the distance between the data node $E$ and the internal hub $I$.

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
