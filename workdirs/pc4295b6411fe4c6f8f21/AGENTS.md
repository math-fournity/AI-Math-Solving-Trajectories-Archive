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

In a remote sector of the galaxy, a spherical space station serves as a navigational beacon with a radius of exactly 1 megameter. The center of the station is designated as Point O. 

Two reconnaissance drones, Drone P and Drone Q, are stationed at fixed coordinates outside the station. Their positions are aligned such that the straight-line path connecting Drone P and Drone Q passes directly through the station's center, Point O.

Drone P activates its dual-beam scanners, which emit two laser lines tangent to the station's surface at contact points $P_1$ and $P_2$. The equipment sensors indicate that the angle formed between these two scanning beams at Drone P is exactly $45^\circ$.

Simultaneously, Drone Q activates its own dual-beam scanners, creating two laser lines tangent to the station's surface at contact points $Q_1$ and $Q_2$. The sensors at Drone Q indicate that the angle formed between its two scanning beams is exactly $30^\circ$.

A maintenance robot must travel along the surface of the spherical station to transport a component from contact point $P_2$ to contact point $Q_2$. To conserve energy, the robot must take the shortest possible path along the station's surface. What is the minimum possible length of the arc $P_2 Q_2$?

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
