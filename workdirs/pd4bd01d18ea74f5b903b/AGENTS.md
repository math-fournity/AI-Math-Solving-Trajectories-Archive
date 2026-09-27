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

In a remote mountainous region, three research stations—Base Alpha ($A$), Base Bravo ($B$), and Base Charlie ($C$)—form a triangular communications grid. The distance along the fiber-optic cable connecting Base Alpha to Base Bravo is 20 kilometers, while the cable connecting Base Alpha to Base Charlie is 22 kilometers.

A central server hub is positioned such that it is equidistant from the three cables, and it connects to the cables at three specific access points: point $D$ on the $BC$ cable, point $E$ on the $AC$ cable, and point $F$ on the $AB$ cable. These access points are located where the server's circular signal range is perfectly tangent to the triangular perimeter.

To monitor signal interference, a technician establishes a maintenance path between points $E$ and $F$. A sensor is then placed at point $P$, which is defined as the location on the path $EF$ that is closest to point $D$. 

A specialized survey reveals that the lines of sight from sensor $P$ to Base Bravo and from sensor $P$ to Base Charlie are perfectly perpendicular to one another. 

Calculate the square of the distance between Base Bravo and Base Charlie.

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
