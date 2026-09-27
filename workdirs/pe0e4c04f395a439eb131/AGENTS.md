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

In a remote territory, three supply depots, **A**, **B**, and **C**, form a triangular logistics network. To optimize distribution, a central command hub **I** is established at the exact location equidistant from the three straight roads connecting the depots (the incenter).

Three main transit lines are drawn: Line **AA'** connects depot **A** to a point **A'** on the road **BC**, Line **BB'** connects depot **B** to point **B'** on road **AC**, and Line **CC'** connects depot **C** to point **C'** on road **AB**. These lines are specifically calibrated to bisect the angles at each depot.

Two specialized scouting outposts, **Ab** and **Ac**, are positioned based on point **A'**. Outpost **Ab** is located by reflecting the coordinates of **A'** across the transit line **CC'**. Outpost **Ac** is located by reflecting the coordinates of **A'** across the transit line **BB'**.

Regional surveyors are tasked with monitoring two specific circular zones:
1. The nine-point circle of the triangle formed by locations **Ab**, **B**, and **C**.
2. The nine-point circle of the triangle formed by locations **Ac**, **B**, and **C**.

The surveyors need to determine the "Line of Equal Power" (the radical axis) between these two nine-point circles. Identify this line in terms of the original depot locations and the median of the network.

Determine the radical axis of the nine-point circles of triangles \(AbBC\) and \(AcBC\).

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
