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

In the coastal province of Geometria, two surveying outposts, Station A and Station B, are established exactly 841 kilometers apart along a straight coastline. 

To the north of this coastline, a cargo ship (Point C) is positioned such that its distance to Station B is 840 kilometers and its distance to Station A is 41 kilometers. A navigational buoy (Point M) is anchored at the precise geographic center—the centroid—of the triangular region formed by the ship and the two outposts.

To the south of the coastline, a research submarine (Point D) is located such that its distance to Station A is 609 kilometers and its distance to Station B is 580 kilometers. A second navigational buoy (Point N) is anchored at the geographic center—the centroid—of the triangular region formed by the submarine and the two outposts.

A logistics officer needs to calculate the direct distance between buoy M and buoy N. If this distance is expressed as a fraction in its simplest form, find the sum of the resulting numerator and denominator.

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
