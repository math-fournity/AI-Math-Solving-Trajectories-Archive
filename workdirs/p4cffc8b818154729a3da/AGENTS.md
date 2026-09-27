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

A specialized logistics company is managing three regional hubs—Alpha (A), Bravo (B), and Charlie (C). The direct fiber-optic cable distances between these hubs are precisely 7 units between Alpha and Bravo, 8 units between Bravo and Charlie, and 9 units between Charlie and Alpha. 

The company operates a central server, Omega (O), which is equidistant from the three hubs. Additionally, an internal security node, Iota (I), is positioned such that it is equidistant from the three direct fiber-optic lines (AB, BC, and CA). The primary network perimeter is defined by a circular boundary, Gamma, passing through Alpha, Bravo, and Charlie.

Within this network, a backup relay, M, is located on the boundary Gamma at the point furthest from the connection between Bravo and Charlie (the midpoint of the major arc BAC). High-altitude sensors have identified a signal interference point, D, located at the intersection of the boundary Gamma and a circular diagnostic zone passing through nodes Iota, M, and Omega (where D is distinct from M). To optimize signal redundancy, engineers establish a secondary reflection point, E, which is the exact mirror image of point D across the straight-line axis connecting Iota and Omega.

Calculate the value of $1000 \cdot \frac{BE}{CE}$, where BE and CE represent the direct distances from the reflection point E to hubs Bravo and Charlie, respectively. Provide the nearest integer.

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
