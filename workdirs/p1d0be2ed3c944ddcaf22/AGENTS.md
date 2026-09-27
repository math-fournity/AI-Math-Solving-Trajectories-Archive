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

A specialized architectural firm is designing a sprawling modular campus consisting of several zones defined by rigid square platforms. 

The project begins with a central triangular atrium, $ABC$. The distances between the corners are precisely measured: the path from $A$ to $B$ is 13 decameters, from $B$ to $C$ is 14 decameters, and from $C$ to $A$ is 15 decameters.

To expand the facility, three "Tier 1" square plazas are built outward from the sides of the atrium: 
1. Plaza $ABB_1A_2$ is built on side $AB$.
2. Plaza $BCC_1B_2$ is built on side $BC$.
3. Plaza $CAA_1C_2$ is built on side $CA$.

The exterior corners of these plazas form a large hexagonal boundary, $A_1A_2B_1B_2C_1C_2$. To further extend the footprint, three "Tier 2" square docking bays are constructed outward from the edges of this hexagon that connect the Tier 1 plazas:
1. Docking bay $A_1A_2A_3A_4$ is built on the edge $A_1A_2$.
2. Docking bay $B_1B_2B_3B_4$ is built on the edge $B_1B_2$.
3. Docking bay $C_1C_2C_3C_4$ is built on the edge $C_1C_2$.

The outward edges of these docking bays form a second hexagon, $A_4A_3B_4B_3C_4C_3$. Finally, three "Tier 3" square garden zones are constructed outward from the gaps between the docking bays:
1. Garden $A_3B_4B_5A_6$ is built on the edge $A_3B_4$.
2. Garden $B_3C_4C_5B_6$ is built on the edge $B_3C_4$.
3. Garden $C_3A_4A_5C_6$ is built on the edge $C_3A_4$.

Calculate the total area of the final hexagonal perimeter $A_5A_6B_5B_6C_5C_6$ in square decameters.

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
