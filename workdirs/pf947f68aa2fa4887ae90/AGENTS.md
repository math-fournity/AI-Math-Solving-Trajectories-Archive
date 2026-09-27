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

In a remote territory, a triangular solar farm designated Sector $ABC$ covers exactly $1$ square kilometer. To optimize energy collection, the engineers have partitioned the farm using a grid based on internal relay stations.

First, three primary stations ($A'$, $B'$, and $C'$) were installed exactly at the midpoints of the perimeter boundaries $BC$, $CA$, and $AB$, respectively. To further refine the grid, a second tier of stations ($A''$, $B''$, and $C''$) was established at the midpoints of the internal lines connecting the primary stations: $A''$ is the midpoint of the line between $B'$ and $C'$, $B''$ is the midpoint of the line between $C'$ and $A'$, and $C''$ is the midpoint of the line between $A'$ and $B'$.

A specific maintenance zone has been cordoned off in the shape of the trapezoid defined by the boundary points $B$, $B''$, $C''$, and $C$. The area of this maintenance zone is expressed as a simplified fraction $\frac{m}{n}$ of the total farm area, where $m$ and $n$ are relatively prime positive integers. 

Calculate the value of $m+n$.

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
