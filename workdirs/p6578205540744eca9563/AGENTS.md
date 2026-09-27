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

In the coastal territory of Arithmetica, two primary trade routes, Route AB and Route AC, originate from the central Port A. Route AB spans exactly 3 leagues, while Route AC spans exactly 4 leagues. A straight shoreline, Route BC, connects the two far ends of these routes to form an acute triangular territory.

A strategic supply depot, Depot M, is established at the exact midpoint of the shoreline BC. To monitor the territory, a command center, Center N, is positioned at the midpoint of the access road AM.

To facilitate logistics, two specialized service paths are paved: Path ME is the shortest distance from Depot M to Route AB (meeting it at Point E), and Path MF is the shortest distance from Depot M to Route AC (meeting it at Point F). 

Engineers then map two straight transit lines: the first line passes through Center N and Point E, intersecting the shoreline BC at a checkpoint called Station S. The second line passes through Center N and Point F, intersecting the shoreline BC at a second checkpoint called Station T.

To ensure safety, two circular radar zones are established: the first is the unique circle passing through Depot M, Point E, and Station S, with its center located at coordinates X. The second is the unique circle passing through Depot M, Point F, and Station T, with its center located at coordinates Y.

A final boundary patrol route follows the unique circle that passes through the three main ports A, B, and C. It is observed that the straight-line distance XY between the two radar centers is perfectly tangent to this boundary patrol circle.

What is the area of the triangular territory ABC?

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
