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

In a remote sector of the ocean, a maritime navigation system is calibrated using three buoys: Alpha ($A$), Bravo ($B$), and Charlie ($C$), positioned such that the distance from Charlie to Alpha is 2022 nautical miles, Alpha to Bravo is 2023 nautical miles, and Bravo to Charlie is 2024 nautical miles. The buoys are arranged in counter-clockwise order.

A research vessel at Bravo undergoes a specific maneuver: it travels along a circular arc centered at buoy Alpha, rotating exactly $90^{\circ}$ counter-clockwise to reach a new coordinate $B'$. To map the seabed, a sonar station $D$ is placed at the exact point on the line passing through Charlie and Alpha that is closest to the vessel's new position $B'$. 

A monitoring buoy $M$ is anchored at the precise midpoint of the straight line connecting the vessel’s original position $B$ and its new position $B'$. A specialized circular sensor network is then established, passing exactly through the locations of station $D$, buoy $M$, and buoy Charlie.

The vessel at Bravo begins moving in a straight line toward buoy $M$. If the vessel continues along this straight-line path (the ray $BM$), it eventually crosses the boundary of the circular sensor network at a point $N$, which is distinct from its passage through buoy $M$. 

Calculate the distance $MN$ between the monitoring buoy and this crossing point.

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
