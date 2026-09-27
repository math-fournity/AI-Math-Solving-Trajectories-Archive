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

In a specialized maritime navigation zone, two circular sonar monitoring stations are positioned. Station Alpha is centered at point $A$ and has a scanning radius of 14 miles. Station Beta is centered at point $B$ and has a scanning radius of 15 miles. The physical distance between the two stations, $A$ and $B$, is exactly 13 miles. The boundaries of these two scanning circles intersect at two specific maritime buoys, labeled $C$ and $D$.

A research vessel $E$ is patrolling the perimeter of Station Alpha's range. A straight communication line is drawn from vessel $E$ through buoy $C$; the point where this line intersects the perimeter of Station Beta’s range for the second time is designated as location $F$. 

To coordinate rescue efforts, two drones are deployed: Drone $M$ is positioned at the exact midpoint of the straight line between buoy $D$ and vessel $E$, while Drone $N$ is positioned at the exact midpoint of the straight line between buoy $D$ and location $F$.

A central command center tracks the intersection of two trajectories: the line passing through Station $A$ and Drone $M$, and the line passing through Station $B$ and Drone $N$. The point where these two lines intersect is designated as $G$. 

As the research vessel $E$ completes a full circuit around the perimeter of Station Alpha, the intersection point $G$ also moves, tracing a circular path. If the radius of this circular path traced by $G$ is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a + b$?

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
