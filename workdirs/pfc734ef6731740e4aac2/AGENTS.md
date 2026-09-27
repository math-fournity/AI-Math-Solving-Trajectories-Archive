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

A specialized architecture firm is designing a coastal monument located on a flat, triangular plot of land defined by three landmarks: $A$, $B$, and $C$. The plot forms an isosceles right triangle where the corner at landmark $A$ is a perfect $90^{\circ}$ angle, and the straight boundary $AB$ measures exactly $1$ kilometer.

A central drainage hub, $D$, is installed at the exact midpoint of the boundary $BC$. Two additional observation sensors, $E$ and $F$, are placed at different locations along the same boundary $BC$. 

To map the signal interference zones, technicians define several circular zones:
1. They identify the circular perimeter passing through points $A, D$, and $E$.
2. They identify the circular perimeter passing through points $A, B$, and $F$.
The unique point where these two perimeters intersect (other than landmark $A$) is labeled as signal node $M$.

Next, they identify a third circular perimeter passing through points $A, C$, and $E$. The point where the straight line extending from $A$ through $F$ intersects this third perimeter (other than landmark $A$) is labeled as signal node $N$.

Finally, the technicians map a fourth circular perimeter that passes through the three signal nodes $A, M$, and $N$. A straight maintenance path is laid out starting from landmark $A$ and passing through the drainage hub $D$. The point where this path intersects the fourth circular perimeter (other than landmark $A$) is designated as point $P$.

Calculate the precise distance, in kilometers, between landmark $A$ and point $P$.

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
