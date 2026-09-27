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

A specialized deep-sea research station is anchored at the origin of a 3D coordinate system, denoted as "Base 2." To monitor the surrounding seabed, three sensors have been deployed: Sensor 1 is located at $(0, 1, 0)$ and Sensor 3 is at $(1, 0, 0)$. A vertical communication buoy, "Base 0," is tethered somewhere along the z-axis (the line where $x=y=0$), distinctly separate from Base 2.

The engineering team identifies a specific point $X$ located on the seabed floor (the plane containing the triangle formed by Sensor 1, Base 2, and Sensor 3). This point $X$ maintains a unique mathematical relationship with four specific triangular zones defined by the four bases/sensors. 

Define the four base locations as $T_0$ (the buoy), $T_1$ (Sensor 1), $T_2$ (Base 2), and $T_3$ (Sensor 3). Let $XT_i$ represent the distance from point $X$ to location $T_i$. Let $A_i$ represent the area of the triangle formed by the three locations other than $T_i$ (specifically, $A_i$ is the area of $\triangle T_{i+1}T_{i+2}T_{i+3}$ where indices cycle through $0, 1, 2, 3$).

If the product of the distance and the corresponding area $(XT_i \cdot A_i)$ results in the exact same constant value for every index $i \in \{0, 1, 2, 3\}$, what is the magnitude of the depth (the z-coordinate) of the communication buoy $T_0$?

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
