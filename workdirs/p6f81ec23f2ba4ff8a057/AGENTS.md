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

A specialized irrigation system is being designed for a triangular vineyard defined by three main water valves: Valve $A$, Valve $B$, and Valve $C$. The straight-line distances between these valves are measured exactly: the distance from $A$ to $B$ is 15 decameters, from $A$ to $C$ is 13 decameters, and from $B$ to $C$ is 14 decameters.

A central monitoring station, $O$, is installed at the precise location that is equidistant from all three valves (the circumcenter of the vineyard). To facilitate drainage, a straight underground pipe, line $l$, is laid starting at Valve $A$ and running across the field such that it is perfectly perpendicular to the straight line connecting valves $B$ and $C$.

Two circular sensor perimeters are established:
1. The first perimeter is the unique circle passing through Valve $A$, Valve $B$, and the monitoring station $O$.
2. The second perimeter is the unique circle passing through Valve $A$, Valve $C$, and the monitoring station $O$.

The drainage pipe $l$ intersects the first circular perimeter at a specific maintenance hatch labeled $X$ (where $X$ is a distinct location from Valve $A$). The pipe $l$ also intersects the second circular perimeter at a maintenance hatch labeled $Y$ (where $Y$ is also distinct from Valve $A$).

Determine the precise distance between hatch $X$ and hatch $Y$. If this distance is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a + b$?

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
