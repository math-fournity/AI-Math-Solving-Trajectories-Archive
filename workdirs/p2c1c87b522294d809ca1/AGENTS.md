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

A remote island sanctuary is enclosed by a circular perimeter fence $\Omega$. Within this sanctuary, four observation towers—$A_1, A_2, A_3$, and $A_4$—are positioned exactly on the fence line. Rangers have measured the direct distances between the towers: the path from $A_1$ to $A_2$ is 28 kilometers, from $A_2$ to $A_3$ is $12\sqrt{3}$ kilometers, from $A_3$ to $A_4$ is $28\sqrt{3}$ kilometers, and from $A_4$ to $A_1$ is 8 kilometers. Two straight supply roads, $A_1 A_3$ and $A_2 A_4$, cross at a central hub $X$.

To monitor the wildlife, four circular conservation zones $\omega_1, \omega_2, \omega_3, \omega_4$ are established. Each zone $\omega_i$ is nestled in the wedge-shaped region formed by the hub $X$ and two adjacent towers ($A_i$ and $A_{i+1}$, with $A_5=A_1$). Specifically, each $\omega_i$ is tangent to the two supply roads meeting at $X$ and also tangent to the outer perimeter fence $\Omega$. 

The contact points for these zones are meticulously mapped: 
- Each zone $\omega_i$ touches the road $A_1 A_3$ at a point $X_i$.
- Each zone $\omega_i$ touches the road $A_2 A_4$ at a point $Y_i$.
- Each zone $\omega_i$ touches the perimeter fence $\Omega$ at a point $T_i$.

Four specialized tracking beacons are then placed at the following coordinates:
- $P_1$ is located at the intersection of the sightlines $T_1 X_1$ and $T_2 X_2$.
- $P_3$ is located at the intersection of the sightlines $T_3 X_3$ and $T_4 X_4$.
- $P_2$ is located at the intersection of the sightlines $T_2 Y_2$ and $T_3 Y_3$.
- $P_4$ is located at the intersection of the sightlines $T_1 Y_1$ and $T_4 Y_4$.

Calculate the area (in square kilometers) of the quadrilateral formed by these four beacons, $P_1 P_2 P_3 P_4$.

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
