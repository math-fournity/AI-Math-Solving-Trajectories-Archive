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

In a remote territory, three survey outposts—Station A, Station B, and Station C—form the vertices of a triangular perimeter. To expand the network, two secondary relay hubs, Hub $B_1$ and Hub $C_1$, were constructed outside the triangle.

Hub $B_1$ was positioned such that the distance from $B_1$ to Station A is equal to the distance from $B_1$ to Station C, and the survey lines $B_1A$ and $B_1C$ meet at a perfect $90^\circ$ angle. Similarly, Hub $C_1$ was positioned such that the distance from $C_1$ to Station A is equal to the distance from $C_1$ to Station B, with the survey lines $C_1A$ and $C_1B$ also meeting at a $90^\circ$ angle.

A maintenance depot, Point M, is located exactly halfway along the straight supply road connecting Hub $B_1$ and Hub $C_1$. Field measurements provide the following logistics data:
- The total length of the supply road between Hub $B_1$ and Hub $C_1$ is 12 kilometers.
- The direct distance from Station B to the depot at Point M is 7 kilometers.
- The direct distance from Station C to the depot at Point M is 11 kilometers.

Based on these survey coordinates, what is the total area (in square kilometers) of the triangular region bounded by Stations A, B, and C?

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
