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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Along the straight roads connecting them, three relay stations have been placed: Station $A_1$ on the road between $B$ and $C$, Station $B_1$ on the road between $C$ and $A$, and Station $C_1$ on the road between $A$ and $B$.

The logistics team has calibrated these stations such that the difference in road distances satisfies a specific equilibrium: the distance from $A$ to $B_1$ minus the distance from $A$ to $C_1$ is exactly equal to the distance from $C$ to $A_1$ minus the distance from $C$ to $B_1$, which is also equal to the distance from $B$ to $C_1$ minus the distance from $B$ to $A_1$.

Within this territory, three local hubs serve the smaller triangular sectors formed by the stations:
- Hub $I_A$ is the center of the largest circle that can be drawn inside the triangular area $AB_1C_1$.
- Hub $I_B$ is the center of the largest circle that can be drawn inside the triangular area $A_1BC_1$.
- Hub $I_C$ is the center of the largest circle that can be drawn inside the triangular area $A_1B_1C$.

A regional monitoring station is positioned at the circumcenter of the triangle formed by these three hubs ($I_A$, $I_B$, and $I_C$). Let $R$ be the distance from this monitoring station to any of the three hubs. 

Let $I$ be the center of the largest circle that can fit within the main perimeter $ABC$. The radius of this circle is $r = 7$ units. The straight-line distance from this central point $I$ to the relay station $A_1$ is exactly $11$ units. 

If $d$ represents the distance between the central point $I$ and the regional monitoring station, calculate the value of $R^2 - d^2$.

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
