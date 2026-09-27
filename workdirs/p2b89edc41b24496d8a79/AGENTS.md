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

In the coastal kingdom of Geometria, a maritime navigation system is established based on a triangular network of three lighthouses: Alpha ($A$), Bravo ($B$), and Charlie ($C$). The lighthouses are situated on a circular coral reef with a radius of exactly $2$ nautical miles. Precise measurements show that the angle formed at lighthouse Bravo is exactly $15^\circ$ larger than the angle formed at lighthouse Charlie ($\angle B - \angle C = 15^\circ$).

Navigators define several key coordinates within this system:
- The central watchtower ($O$) sits at the exact center of the circular reef.
- The signal coordination hub ($H$) is located at the orthocenter of the lighthouse triangle.
- The supply depot ($G$) is located at the centroid of the triangle.
- A long-range buoy ($L$) is placed at the point such that the central watchtower ($O$) is the exact midpoint of the line segment connecting the coordination hub ($H$) and the buoy ($L$).

Two survey lines are drawn from lighthouse Alpha: one passing through the supply depot ($G$) and another through the buoy ($L$). These lines extend to the edge of the circular reef, marking two sonar stations, $X$ and $Y$, respectively.

To assist local fishers, two auxiliary markers, $B_1$ and $C_1$, are placed on the circular reef such that the path from $B$ to $B_1$ is perfectly parallel to the coastline $AC$, and the path from $C$ to $C_1$ is perfectly parallel to the coastline $AB$. 

A specialized research vessel is stationed at point $Z$, which is the intersection of the line segment connecting sonar stations $X$ and $Y$ and the line segment connecting markers $B_1$ and $C_1$.

Deep-sea sensors indicate that the distance between the central watchtower ($O$) and the research vessel ($Z$) satisfies $OZ = 2\sqrt{5}$ nautical miles. The square of the distance between lighthouse Alpha and the research vessel, $AZ^2$, can be expressed in the form $m - \sqrt{n}$ for positive integers $m$ and $n$.

Calculate the value of $100m + n$.

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
