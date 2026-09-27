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

In a circular conservation district known as Zone Omega, three observation outposts—P, Q, and M—are positioned along the perimeter. Outpost M is situated exactly halfway along the shorter coastal route between P and Q, such that the straight-line distances from M to P and from M to Q are both exactly 3 kilometers.

A mobile research unit, X, travels along the longer outer boundary of the district between P and Q. A direct supply path is established from M to X, which intersects the straight transit line connecting P and Q at a junction point, R. To monitor local activity, a specialized sensor beam is projected from junction R. This beam is oriented perfectly perpendicular to the supply path MX and extends until it hits a receiver, S, located on the shorter coastal boundary between P and Q. Finally, a data link is established from M through S, extending until it reaches a terminal, T, located on the extended line passing through P and Q.

During a specific phase of operations, the research unit X moves to a position such that the distance between terminal T and unit X is exactly 5 kilometers. It is observed that at this precise moment, the distance between outpost M and receiver S has reached its absolute minimum value. Based on these measurements, what is this minimum distance MS?

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
