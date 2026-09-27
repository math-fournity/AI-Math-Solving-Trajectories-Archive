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

In a remote sector of the galaxy, three navigational beacons—**A**, **B**, and **C**—form a triangular communications network. A massive, circular energy field, the "Circum-Shield," passes perfectly through all three beacons.

The network’s central hub, Beacon **A**, broadcasts two distinct signal beams. The first beam, a "Synchronized Pulse," bisects the internal angle of the sector at **A**. The second beam, a "Lateral Wave," bisects the external angle at **A**. These beams travel across the sector until they intersect the boundary of the Circum-Shield at coordinates **D** (for the Synchronized Pulse) and **E** (for the Lateral Wave).

A maintenance drone travels along a straight-line trajectory connecting beacons **A** and **B**. Simultaneously, a survey cable is stretched in a straight line between the shield coordinates **D** and **E**. The drone’s path and the survey cable intersect at a specific docking waypoint, **F**.

Telemetric data from the network reveals two critical spatial ratios:
1. The scanning angle measured at beacon **C** (between beacons **A** and **B**) is exactly twice the magnitude of the angle measured at beacon **B** (between beacons **A** and **C**).
2. Waypoint **F** is positioned such that the distance from beacon **B** to **F** is exactly twice the distance from beacon **A** to **F**.

Based on these spatial constraints, calculate the precise measurement of the internal angle at Beacon **A** (the angle between the paths to beacons **B** and **C**).

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
