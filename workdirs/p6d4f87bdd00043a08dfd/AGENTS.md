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

In a vast desert reclamation project, three surveyor outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. The distance between Bravo and Charlie is 2,007 meters, the distance between Charlie and Alpha is 2,008 meters, and the distance between Alpha and Bravo is 2,009 meters.

A circular irrigation system, controlled by a central hub ($O$), is installed as an excircle to the triangular region. The boundary of this circular system is tangent to the existing path between Bravo and Charlie at a specific distribution point ($D$). Furthermore, the boundary is tangent to the extended straight-line paths originating from Alpha through Charlie at point $E$, and from Alpha through Bravo at point $F$. In this configuration, Charlie is located on the segment between Alpha and $E$, while Bravo is located on the segment between Alpha and $F$.

A straight maintenance road ($EF$) connects the two outer tangent points. To monitor the system, a linear sensor array ($\ell$) is laid out such that it passes through the central hub ($O$) and is oriented strictly perpendicular to the direct line of sight between Alpha ($A$) and the distribution point ($D$).

The sensor array ($\ell$) and the maintenance road ($EF$) intersect at a specific monitoring station ($G$). Based on these spatial coordinates, calculate the exact distance between the distribution point ($D$) and the monitoring station ($G$).

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
