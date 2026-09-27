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

In a remote desert, two long, straight pipelines, Pipeline AB and Pipeline AC, originate from the same pumping station, Junction A. Both pipelines are exactly 182 kilometers long. A third service road, Road BC, connects the far ends of the pipelines and is 140 kilometers long.

A technician starts at a monitoring station, $X_1$, located on Pipeline AC at a distance of 130 kilometers from the end Junction C. The technician first travels from Junction B to station $X_1$ to perform an inspection. 

From $X_1$, the technician must lay a new cable to a point $X_2$ on Pipeline AB such that the path $X_1X_2$ is perfectly perpendicular to the initial path $BX_1$. 

The technician then continues this pattern of laying cables in a zigzag formation between the two pipelines. For any cable segment $X_nX_{n+1}$, the new path must be perpendicular to the previous segment $X_{n-1}X_n$. Specifically:
- If $n$ is odd, the technician starts at $X_n$ on Pipeline AC and lays a cable to $X_{n+1}$ on Pipeline AB.
- If $n$ is even, the technician starts at $X_n$ on Pipeline AB and lays a cable to $X_{n+1}$ on Pipeline AC.

This process continues indefinitely, creating an infinite sequence of connected cable segments: $BX_1, X_1X_2, X_2X_3, X_3X_4, \ldots$.

Calculate the total length of the entire path (the sum $BX_1 + X_1X_2 + X_2X_3 + \ldots$). If the total distance is represented as an irreducible fraction $\frac{a}{b}$, find the value of $a + b$.

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
