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

In a remote sector of the galaxy, three navigational beacons—codenamed Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular formation. The central command station, the Origin ($O$), is located at the center of the unique circular orbit that passes through all three beacons, and the radius of this orbit is defined as the Sector Radius ($R$). Due to gravitational interference, the sector also has a unique energetic focal point known as the Harmonic Point ($H$).

The Galactic Engineering Corps decides to deploy three new relay satellites, Delta ($D$), Echo ($E$), and Foxtrot ($F$). These satellites are positioned via "mirrored deployment":
- Satellite Delta ($D$) is placed such that the line segment $BC$ is the perpendicular bisector of the path between Beacon $A$ and Satellite $D$.
- Satellite Echo ($E$) is placed such that the line segment $AC$ is the perpendicular bisector of the path between Beacon $B$ and Satellite $E$.
- Satellite Foxtrot ($F$) is placed such that the line segment $AB$ is the perpendicular bisector of the path between Beacon $C$ and Satellite $F$.

Deep-space scanners determine that a rare phenomenon occurs where the three satellites Delta, Echo, and Foxtrot align perfectly along a single straight path. Theoretical models show that this alignment happens if and only if the distance between the Origin ($O$) and the Harmonic Point ($H$) satisfies the power-balance equation:
$$(OH)^k = n R^k$$
where $n$ and $k$ are positive integers.

Find the value of $n + k$.

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
