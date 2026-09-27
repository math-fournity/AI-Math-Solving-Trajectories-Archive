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

In a remote territory, two primary fiber-optic cables, Line AC and Line BC, meet at a central switching station called Junction C. The angle formed between these two cables is exactly $45^\circ$. A specialized signal booster, designated as the Incenter (I), is positioned such that it is equidistant from the three lines of the triangular communication grid formed by AC, BC, and the boundary line AB. The entire grid is contained within a circular transmission zone with a radius of exactly 1 unit ($R=1$).

Two maintenance access paths are laid out: Path AM starts at a point M on Line BC and connects to point A, while Path BN starts at a point N on Line AC and connects to point B. These two paths intersect at a specific coordination hub, Point P.

A technical survey reveals a unique spatial resonance: there exists a point that serves as the intersection of two distinct circular frequency zones. The first zone is the circle passing through points A, N, and P. The second zone is the circle passing through points B, M, and P. These two frequency zones intersect at two distinct locations: one is the coordination hub P, and the other is exactly at the location of the signal booster I.

Based on this configuration, calculate the precise distance between the coordination hub P and the signal booster I.

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
