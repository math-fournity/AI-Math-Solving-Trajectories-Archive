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

In the coastal territory of Planimetria, three critical observation towers—Base Station $B$, Coastal Outpost $C$, and a central Relay Hub $H$—form a strategic triangle. The Relay Hub $H$ is situated at the origin $(0,0)$, while Base Station $B$ is located at $(-10, 0)$ and Coastal Outpost $C$ is at $(15, 0)$. In this geography, the Hub $H$ serves as the orthocenter for the triangular region formed by $B$, $C$, and a third inland peak $A$. 

The territory’s boundaries are defined by communication lines: line $AB$ and line $AC$. Two technical maintenance stations, $T$ and $R$, are located where the signal beams from $B$ and $C$ meet their opposite boundaries at right angles (the feet of the altitudes from $B$ and $C$). A mobile drone $P$ is positioned somewhere on the straight road $BC$ connecting the two base stations.

For surveillance, two circular radar zones, $\omega_1$ and $\omega_2$, are established:
- $\omega_1$ is the circle passing through the drone's projection onto the $AB$ boundary (point $X$), the base station $B$, and the hub $H$.
- $\omega_2$ is the circle passing through the drone's projection onto the $AC$ boundary (point $Y$), the coastal outpost $C$, and the hub $H$.

A monitoring satellite $Q$ is positioned at the intersection point of the two common external tangent lines that graze the perimeters of radar zones $\omega_1$ and $\omega_2$. Meanwhile, a maritime buoy $K$ is anchored at the specific point where the straight line passing through maintenance stations $R$ and $T$ intersects the road $BC$.

If the coordinates of the satellite $Q$ are $(x_Q, y_Q)$, and $KQ$ and $QH$ represent the straight-line distances between those respective points, calculate the value of the product:
$$x_Q \cdot \frac{KQ}{QH}$$

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
