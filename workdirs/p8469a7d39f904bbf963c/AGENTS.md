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

In the remote Archipelago of Geometry, a triangular marine sanctuary is defined by three research stations: $A$, $B$, and $C$, forming an acute triangle. At the exact center of this sanctuary sits a central monitoring buoy, $O$, which is equidistant from all three stations. 

A specialized fiber-optic cable runs along a straight path starting at station $A$, passing through the sanctuary's circular boundary to a submerged sensor located at point $Q$. This cable path is engineered to be perfectly perpendicular to the straight-line supply route connecting stations $B$ and $C$.

A secondary circular patrol zone, which passes through the central buoy $O$ and stations $B$ and $C$, is established for conservation drones. This circular zone intersects the supply line $AC$ at a secondary checkpoint $D$, and intersects the supply line $AB$ at a secondary checkpoint $E$.

During a logistical audit, it is discovered that three major transit lines—the fiber-optic cable $AQ$, the supply route $BC$, and the straight-line path between checkpoints $D$ and $E$—all intersect at a single coordinates point.

Telemetry data indicates that the distance from the central buoy $O$ to checkpoint $D$ is exactly 3 units, and the distance from the buoy $O$ to checkpoint $E$ is exactly 7 units. 

Based on these coordinates, calculate the total length of the fiber-optic cable $AQ$.

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
