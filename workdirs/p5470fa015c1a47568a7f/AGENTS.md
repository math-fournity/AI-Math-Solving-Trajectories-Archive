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

A specialized urban planning drone is hovering at position $P$ within a triangular district defined by three landmarks: the Bakery ($B$), the Cafe ($C$), and the Airport ($A$). The straight-line distance from the Airport to the Bakery is exactly 1 kilometer, while the distance from the Airport to the Cafe is 2 kilometers.

From the drone’s perspective at $P$, the angle measured between the line of sight to the Bakery and the boundary road $BC$ is exactly $70^{\circ}$. 

Two straight service cables are laid out across the district:
1. Cable 1 starts at the Bakery, passes through a relay station $E$ located on the road $AB$, and ends at the drone. The drone observes that the angle between its view of the Bakery and station $E$ ($\angle BPE$) is $75^{\circ}$, and the angle between station $E$ and the Airport ($\angle EPA$) is also $75^{\circ}$.
2. Cable 2 starts at the Cafe, passes through a relay station $D$ located on the road $AC$, and ends at the drone. The drone observes that the angle between its view of the Airport and station $D$ ($\angle APD$) is $60^{\circ}$, and the angle between station $D$ and the Cafe ($\angle DPC$) is also $60^{\circ}$.

In the district's logistics grid, a central hub $Q$ is located at the exact intersection of the straight paths $BD$ and $CE$. A main transit line is drawn from the Airport ($A$) through this hub $Q$ until it hits the boundary road $BC$ at a point $F$. Additionally, a maintenance station $M$ is placed at the exact midpoint of the road $BC$.

Calculate the degree measure of the angle $\angle MPF$ formed at the drone's position between the lines of sight to the maintenance station and the transit line termination point.

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
