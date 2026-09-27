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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Two specialized logistics hubs, $T_1$ and $T_2$, are located on the straight supply lines connecting the depots: $T_1$ is positioned on the road between $B$ and $C$, while $T_2$ is on the road between $A$ and $C$.

The positions of these hubs are mathematically determined by the landscape: $T_1$ is the specific point where the boundary of the "External Sector $A$" (a circular zone tangent to side $BC$ and the extensions of $AB$ and $AC$) touches the road $BC$. Similarly, $T_2$ is the point where the boundary of the "External Sector $B$" (a circular zone tangent to side $AC$ and the extensions of $BA$ and $BC$) touches the road $AC$.

A Central Command post ($I$) is located at the triangle's Incenter (the point equidistant from all three perimeter roads). A scout drone identifies a specific coordinate $I'$ by taking the location of Central Command ($I$) and reflecting it across the exact midpoint of the road connecting Alpha and Bravo ($AB$).

Sensors confirm that this coordinate $I'$ lies exactly on the circular boundary of a surveillance zone defined by the three points $C$, $T_1$, and $T_2$.

Based on this spatial configuration, calculate the exact measurement of the angle at depot Charlie ($\angle BCA$) in degrees.

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
