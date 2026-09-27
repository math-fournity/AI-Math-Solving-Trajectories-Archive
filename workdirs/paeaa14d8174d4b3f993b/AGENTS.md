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

A specialized architecture firm is designing a structural support system consisting of a vertical pillar connected to three ground anchors. The three ground anchors, labeled $A$, $B$, and $C$, form a triangular base on a flat construction site. In this triangle, the internal angle at anchor $A$ is $20^\circ$, the angle at $B$ is $40^\circ$, and the radius of the circle passing through all three ground anchors is exactly $10$ units.

A vertical steel column $SC$ is erected such that its base is at anchor $C$ and it stands perfectly perpendicular to the ground plane $ABC$. Three support cables are then stretched from the top of the column, $S$, to each of the ground anchors $A, B$, and $C$.

To analyze the structural stability, engineers measure three specific "shadow angles":
- Let $\alpha$ be the angle between the cable $SA$ and the vertical wall formed by the plane $SBC$.
- Let $\beta$ be the angle between the cable $SB$ and the vertical wall formed by the plane $SAC$.
- Let $\gamma$ be the angle between the vertical column $SC$ and the slanted roof plane formed by $SAB$.

The structural integrity of the design is governed by the following relationship:
$$\frac{1}{\sin \alpha} + \frac{1}{\sin \beta} - \frac{1}{\sin \gamma} = 1$$

Based on these geometric specifications and the integrity constraint, calculate the square of the height of the vertical column, denoted as $|SC|^2$.

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
