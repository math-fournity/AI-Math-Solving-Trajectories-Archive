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

In the coastal province of Geometria, three lighthouse stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular network. These stations sit on a circular bay. Two straight piers are built from Alpha and Bravo, tangent to the circular shoreline, extending until they meet at a Supply Depot ($T$). 

A straight underwater cable is laid from Charlie to the Supply Depot ($T$). Along this cable route, a deep-sea sensor ($D$) is installed at the point where the cable path first crosses the circular boundary of the bay. 

To monitor the sensor, three observation buoys are placed:
- Buoy $M$ is the closest point on the straight-line path between Alpha and Bravo to the sensor.
- Buoy $N$ is the closest point on the straight-line path between Bravo and Charlie to the sensor.
- Buoy $P$ is the closest point on the straight-line path between Alpha and Charlie to the sensor.

A maintenance technician at Buoy $M$ looks toward the straight line connecting Buoys $N$ and $P$. He navigates his boat in a direction exactly perpendicular to that $NP$ line until he reaches a specific marker $E$ located on the coast between Bravo and Charlie.

The survey team reports the following measurements:
- The distance along the coast from marker $E$ to Charlie ($C$) is exactly 5 km.
- The distance along the coast from marker $E$ to Bravo ($B$) is exactly 11 km.
- The angle $\angle CEP$ formed by the marker $E$, Charlie, and Buoy $P$ is $120^{\circ}$.

Compute the distance $CP$ between Charlie and Buoy $P$.

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
