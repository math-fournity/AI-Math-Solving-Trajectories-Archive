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

In a specialized irrigation district, three primary control valves form a triangular network. Valve $B$ is located at coordinates $(-3, 0)$ and Valve $C$ is at $(3, 0)$, creating a baseline distance of $a = 6$ units. Valve $A$ is positioned at a point with a positive $y$-coordinate such that the distance from $A$ to $B$ and the distance from $A$ to $C$ are both exactly $b = 5$ units.

Two adjustable sensors, $M$ and $N$, move along the pipelines. Sensor $M$ is placed on the pipeline $AC$ and Sensor $N$ is placed on the pipeline $AB$. To maintain hydraulic balance, the positions of these sensors must satisfy the specific pressure-flow relationship:
$a^2 \cdot AM \cdot AN = b^2 \cdot BN \cdot CM$

A monitoring hub, $P$, is situated at the exact intersection of two underground cables: one connecting Valve $B$ to Sensor $M$, and the other connecting Valve $C$ to Sensor $N$. As the sensors $M$ and $N$ shift while maintaining the hydraulic balance, the hub $P$ traces a path $\mathcal{L}$ which forms the arc of a circle.

Let $R$ be the radius of this circular path, and $(x_0, y_0)$ be the coordinates of the center of the circle in the defined coordinate system.

Calculate the value of $R^2 + x_0^2 + y_0^2$.

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
