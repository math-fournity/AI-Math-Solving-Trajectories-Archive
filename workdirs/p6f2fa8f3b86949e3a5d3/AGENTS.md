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

In a futuristic city, two high-speed laser transport beams are projected across a square-shaped docking bay defined by corners $A$, $B$, $C$, and $D$. The diagonal distance of this square bay, from corner $A$ to $C$, is exactly 1 kilometer.

Two sensors are positioned on the perimeter: Sensor $E$ is located on the straight-line boundary between $A$ and $B$, and Sensor $F$ is located on the boundary between $B$ and $C$. Two laser paths are activated: one originates at corner $C$ and travels to Sensor $E$, and the other originates at corner $A$ and travels to Sensor $F$. The angle between the path $CE$ and the boundary $BC$ is $30^\circ$, and the angle between the path $AF$ and the boundary $AB$ is also $30^\circ$.

The two laser paths, $CE$ and $AF$, intersect at a central control hub denoted as point $G$. This intersection divides the area into several zones, including two triangular safety zones: Triangle $AGE$ and Triangle $CGF$. 

To calibrate the system, engineers must place a localized signal stabilizer at the incenter of Triangle $AGE$ and another at the incenter of Triangle $CGF$. Compute the exact distance between these two signal stabilizers.

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
