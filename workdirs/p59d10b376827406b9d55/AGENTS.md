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

A specialized deep-sea research station is housed within a spherical glass hull centered at a command hub $O$. Four observation sensors, $A, B, C$, and $D$, are mounted on the surface of the hull such that the triangular face formed by sensors $A, B$, and $C$ consists entirely of acute angles.

To calibrate the station, engineers deploy a vertical laser level starting from the central hub $O$. This laser is oriented perfectly perpendicular to the floor plane defined by sensors $A, B$, and $C$. The laser beam extends to a calibration point $E$ on the hull’s surface, positioned such that point $D$ and point $E$ are on opposite sides of the floor plane $ABC$. 

A straight fiber-optic cable is stretched between sensor $D$ and calibration point $E$. This cable passes through the floor plane $ABC$ at a specific connection port $F$, located within the interior of the triangle $ABC$. 

Technical readouts confirm the following spatial data:
1. The angle between the cable $DE$ and the line to sensor $A$ (measured from $D$) is exactly equal to the angle between the cable $DE$ and the line to sensor $B$ (also measured from $D$), such that $\angle ADE = \angle BDE$.
2. The distance from connection port $F$ to sensor $A$ is not equal to the distance from $F$ to sensor $B$.
3. The horizontal angle formed at the connection port between the two sensors, $\angle AFB$, is precisely $80^\circ$.

Based on these geometric constraints, find the measure of the angle $\angle ACB$ in degrees.

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
