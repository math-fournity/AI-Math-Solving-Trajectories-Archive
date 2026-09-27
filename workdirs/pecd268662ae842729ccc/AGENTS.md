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

In a futuristic research facility, there is a specialized glass containment chamber shaped like a regular tetrahedron, designated as Chamber $T$. This chamber has a total interior capacity of exactly 1 unit of breathable air.

Inside the chamber, a tiny floating sensor drone is positioned at an arbitrary point $P$. To stabilize the drone, the facility’s computer generates four internal force-field partitions. Each partition is a flat plane that passes through the drone’s location $P$ and is perfectly parallel to one of the four triangular walls of the chamber. These four partitions intersect to subdivide the interior volume of the chamber into exactly 14 distinct spatial zones.

The facility’s maintenance protocol requires the removal of specific zones from the total volume calculation:
1. Any zone that is shaped like a tetrahedron.
2. Any zone that is shaped like a parallelepiped.

Let $f(P)$ represent the total combined volume of all the remaining zones that were not removed (the "leftover" regions). 

As the sensor drone $P$ moves to different locations within the chamber, the value of $f(P)$ fluctuates. Your task is to determine the highest possible value that $f(P)$ can never exceed (the minimum upper bound $U$) and the lowest possible value that $f(P)$ can never fall below (the maximum lower bound $L$). 

Calculate and report the value of $U + L$.

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
