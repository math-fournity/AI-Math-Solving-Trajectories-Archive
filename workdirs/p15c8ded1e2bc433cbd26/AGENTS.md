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

In the competitive world of architectural design, a specialized firm is developing a triangular plaza, $\triangle ABC$, designed such that all internal angles are acute and no two sides are of equal length. To optimize the layout, the architects have established several key coordinates and structural points:

1.  Two drainage conduits are installed: one from corner $B$ perpendicular to the opposite side $AC$ (ending at point $E$), and another from corner $C$ perpendicular to side $AB$ (ending at point $F$).
2.  A central fountain is placed at point $O$, which is exactly equidistant from all three corners $A$, $B$, and $C$.
3.  A maintenance access hatch is located at point $M$, which is the precise midpoint of the boundary line $BC$.
4.  A secondary emergency sensor is positioned at a point $M'$ such that the fountain $O$ is the exact midpoint of the line segment $MM'$.

During a site inspection, a surveyor discovers a unique geometric alignment: the emergency sensor $M'$ lies exactly on the straight line path connecting the drainage points $E$ and $F$. 

Given this specific configuration, find the value of the ratio of the distance between the corner $A$ and the maintenance hatch $M$ to the distance between the corner $A$ and the central fountain $O$.

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
