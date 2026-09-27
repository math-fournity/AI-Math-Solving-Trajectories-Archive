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

In a remote territory, three survey outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. The distance between Alpha and Bravo is exactly 13 units, Bravo to Charlie is 14 units, and Charlie to Alpha is 15 units.

To secure the perimeter, three square storage facilities are built outward from the triangle’s sides: Square $S_1$ is built on side $AB$ (with vertices $A, B, B_1, A_2$), Square $S_2$ on side $BC$ (vertices $B, C, C_1, B_2$), and Square $S_3$ on side $CA$ (vertices $C, A, A_1, C_2$). These squares collectively form a hexagonal outer boundary defined by the vertices $A_1, A_2, B_1, B_2, C_1, C_2$.

A second layer of square reinforcements is then constructed outward from the gaps of this hexagon: Square $R_1$ is built on the segment $A_1 A_2$ (vertices $A_1, A_2, A_3, A_4$), Square $R_2$ on segment $B_1 B_2$ (vertices $B_1, B_2, B_3, B_4$), and Square $R_3$ on segment $C_1 C_2$ (vertices $C_1, C_2, C_3, C_4$). This expansion creates a second hexagonal boundary with vertices $A_4, A_3, B_4, B_3, C_4, C_3$.

Finally, a third layer of square docking bays is added outward from the remaining sides of the second hexagon: Square $D_1$ is built on segment $A_3 B_4$ (vertices $A_3, B_4, B_5, A_6$), Square $D_2$ on segment $B_3 C_4$ (vertices $B_3, C_4, C_5, B_6$), and Square $D_3$ on segment $C_3 A_4$ (vertices $C_3, A_4, A_5, C_6$).

Calculate the total area of the final hexagon formed by the outermost vertices $A_5, A_6, B_5, B_6, C_5, C_6$.

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
