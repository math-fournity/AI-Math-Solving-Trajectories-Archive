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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular logistics network. A central distribution hub, Gamma ($G$), is located exactly at the centroid of this triangle (the unique point where the three straight paths connecting each depot to the midpoint of the opposite side intersect).

To optimize communications, the logistics team measures the signal angles between the direct paths connecting the depots and the hub. Specifically, they focus on the following six directional angles:
- At depot $A$: the angle between path $AB$ and path $AG$, and the angle between path $AC$ and path $AG$.
- At depot $B$: the angle between path $BA$ and path $BG$, and the angle between path $BC$ and path $BG$.
- At depot $C$: the angle between path $CA$ and path $CG$, and the angle between path $CB$ and path $CG$.

A safety protocol requires that at least three of these six signal angles must be greater than or equal to a specific threshold value, $\alpha$. 

Determine the maximum possible value of $\alpha$ (expressed as an arcsine) such that there exists a configuration of depots $A, B,$ and $C$ where at least three of these angles are at least $\alpha$.

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
