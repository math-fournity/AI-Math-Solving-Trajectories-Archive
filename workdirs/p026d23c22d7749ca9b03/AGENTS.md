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

In a remote territory, three supply depots—Alpha, Beta, and Gamma—form the vertices of a triangular perimeter ($A, B, C$). The region is strictly governed such that the angle between any two supply routes is always less than 90 degrees. 

To secure the perimeter, three outpost stations—X-Ray, Yankee, and Zulu—are built outside the triangle. 
- X-Ray ($X$) is positioned such that the distance to Beta ($B$) equals the distance to Gamma ($C$), and the path $BX$ is perpendicular to $CX$. 
- Yankee ($Y$) is positioned such that the distance to Gamma ($C$) equals the distance to Alpha ($A$), and the path $CY$ is perpendicular to $AY$. 
- Zulu ($Z$) is positioned such that the distance to Alpha ($A$) equals the distance to Beta ($B$), and the path $AZ$ is perpendicular to $BZ$.

The High Command calculates the "Structural Integrity" of the inner perimeter as the sum of the squares of the distances between the depots: $S_{in} = AB^2 + BC^2 + CA^2$. They calculate the "Network Expansion" as the sum of the squares of the distances between the outposts: $S_{out} = XY^2 + YZ^2 + ZX^2$.

Find the largest real number $k$ such that the Structural Integrity is always at least $k$ times the Network Expansion ($S_{in} \ge k \cdot S_{out}$) for every possible configuration of the depots.

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
