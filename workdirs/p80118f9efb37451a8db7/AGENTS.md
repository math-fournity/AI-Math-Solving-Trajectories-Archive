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

In a remote desert, two circular irrigation zones, Zone 1 and Zone 2, are nested such that they touch at a single point, $P$, on their western edges. A straight service road runs North-South, passing through the contact point $P$. 

Two observation outposts, $A$ and $B$, are located on this service road such that $P$ is situated between them. Outpost $A$ is to the North, and Outpost $B$ is to the South.

From Outpost $A$, two straight security fences are built to graze the edges of the irrigation zones: fence $a_1$ is tangent to Zone 1, and fence $a_2$ is tangent to Zone 2 (neither fence follows the North-South service road). 

From Outpost $B$, two similar fences are constructed: fence $b_1$ is tangent to Zone 1, and fence $b_2$ is tangent to Zone 2 (again, neither follows the service road).

A supply depot $C$ is constructed at the precise location where fence $a_1$ intersects fence $b_2$. A second supply depot $D$ is constructed where fence $a_2$ intersects fence $b_1$.

A surveyor measures the following straight-line distances between the depots and the outposts:
- The distance from Depot $C$ to Outpost $A$ is 15 kilometers.
- The distance from Depot $C$ to Outpost $B$ is 18 kilometers.
- The distance from Depot $D$ to Outpost $A$ is 12 kilometers.

Based on these measurements, find the straight-line distance (in kilometers) from Depot $D$ to Outpost $B$.

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
