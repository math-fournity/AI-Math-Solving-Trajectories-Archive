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

A specialized satellite network is positioned in a circular orbit, denoted as Orbit $O$. Around this orbit, 36 relay stations, $A_1, A_2, \dots, A_{36}$, are spaced at perfectly equal intervals (forming a regular 36-gon).

A repair drone is currently maintaining a spherical signal zone, Circle $C_1$. This zone is situated outside Orbit $O$ and touches the orbit’s perimeter exactly at station $A_{18}$. A straight laser transmission beam connects station $A_{10}$ to station $A_{28}$. The signal zone $C_1$ is perfectly tangent to this $A_{10}A_{28}$ laser beam at a specific coordinate point $P$.

Simultaneously, a second repair drone maintains another spherical signal zone, Circle $C_2$. This zone is also outside Orbit $O$ and touches the orbit’s perimeter exactly at station $A_{30}$. A second laser transmission beam connects station $A_{21}$ to station $A_{23}$. The signal zone $C_2$ is perfectly tangent to this $A_{21}A_{23}$ laser beam at a specific coordinate point $Q$.

A monitoring technician calculates two straight-line trajectories for data transfer: the first line passes through station $A_8$ and the coordinate point $P$, and the second line passes through station $A_{30}$ and the coordinate point $Q$. These two trajectories intersect at a navigation hub, $R$.

Calculate the measure of the angle $\angle PRQ$ at the navigation hub, where $0^\circ \leq \angle PRQ \leq 180^\circ$.

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
