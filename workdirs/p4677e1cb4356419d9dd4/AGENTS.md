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

In a specialized logistics hub, three cargo platforms are positioned at coordinates $A$, $B$, and $C$. The distance between platform $A$ and platform $B$ is exactly 5 kilometers, while the distance between platform $A$ and platform $C$ is exactly 4 kilometers.

The facility is undergoing an expansion involving two new auxiliary docking stations, $D$ and $E$. Station $D$ is placed such that the segment $AB$ acts as a perpendicular bisector to the path between $C$ and $D$. Similarly, station $E$ is placed such that the segment $AC$ acts as a perpendicular bisector to the path between $B$ and $E$. Engineers have noted a unique structural alignment: the points $D$, $A$, and $E$ all lie perfectly along a single straight access road.

To complete the infrastructure, two long straight pipelines are laid out. The first pipeline connects station $D$ to platform $B$, and the second pipeline connects station $E$ to platform $C$. These two pipelines eventually intersect at a junction point labeled $F$.

Calculate the area (in square kilometers) of the triangular region formed by platform $B$, platform $C$, and the junction point $F$.

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
