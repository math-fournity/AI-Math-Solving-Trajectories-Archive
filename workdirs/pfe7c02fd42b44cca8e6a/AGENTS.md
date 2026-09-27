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

In a specialized precision manufacturing facility, a large circular workspace $\Omega$ contains a smaller circular zone $\Gamma$. These two zones share a single point of contact at a docking station $P$. Two straight laser paths, $PA$ and $PB$, originate from this station and extend to the outer boundary $\Omega$. Along these paths, the laser beams exit the inner zone $\Gamma$ at points $X$ and $Y$ respectively.

The facility tracks several safety and measurement zones based on these coordinates:
- A spherical shielding field $O_1$ is generated with the segment $AB$ as its diameter.
- A secondary containment field $O_2$ is generated with the segment $XY$ as its diameter.
- A calibration point $F$ is located on the path $XP$ such that the line $YF$ is perfectly perpendicular to $XP$.
- A specialized transport bridge of length $TM$ connects a point $T$ on the surface of $O_1$ to a point $M$ on the surface of $O_2$, such that the bridge is tangent to both fields simultaneously.

The engineering team provides the following precise telemetry data:
- The distance from the docking station $P$ to the calibration point $F$ is $12$ units.
- The distance from the calibration point $F$ to the exit point $X$ is $15$ units.
- The length of the tangent bridge $TM$ is $18$ units.
- The total length of the laser path $PB$ is $50$ units.

In the triangle formed by the docking station and the outer boundary points, $\triangle ABP$, let $H$ be the orthocenter (the intersection of the triangle's altitudes). Calculate the exact length of the segment $AH$.

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
