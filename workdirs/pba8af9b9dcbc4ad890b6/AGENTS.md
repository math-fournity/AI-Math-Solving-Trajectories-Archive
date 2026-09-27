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

In a remote desert, a futuristic observation station is built in the shape of a perfectly symmetrical tetrahedral dome $ABCD$, where every structural beam (edge) has an identical length $L$. 

The base of the station is the equilateral triangle $BCD$. An engineer marks a maintenance port $M$ exactly halfway along the beam $DB$. Outside the station, a sensor $N$ is placed along the straight-line extension of the beam $AB$ (starting from $B$, passing through $A$, and continuing outward). The sensor $N$ is positioned such that the distance from $N$ to the vertex $A$ is exactly half the distance from $N$ to the vertex $B$.

Deep within the base $BCD$, a laser emitter $P$ is located on the altitude line drawn from vertex $D$ to the opposite side $BC$. The safety team projects a flat planar shield passing through the sensor $N$, the maintenance port $M$, and the laser emitter $P$. 

If the intersection of this planar shield with the faces of the tetrahedral dome forms a perfect trapezoid, what is the measure of the angle $\angle MPD$ in degrees?

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
