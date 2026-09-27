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

In the mountainous region of Triangula, three outposts—Sector A, Sector B, and Sector C—form a triangular perimeter. A straight supply road connects Sector B and Sector C. Along this road, a specialized communication hub, Hub D, is positioned such that the transmission angle from Sector A to Hub D (angle BAD) is identical to the angle observed from Sector C looking toward Sector A (angle ACB).

A circular surveillance perimeter is established that passes through Sector A and is perfectly tangent to the supply road exactly at Hub D. This circular boundary intersects the path between Sector A and Sector B at a checkpoint labeled Station E, and it intersects the path between Sector A and Sector C at Station F.

A secondary data line is laid out in a straight path through Station E and Station F. This data line eventually crosses the original supply road at a remote observation post, Point P.

Technical scans provide the following measurements between these locations:
- The distance from Sector A to Station E is exactly 11 kilometers.
- The distance from Hub D to Station E is exactly 10 kilometers.
- The distance from Station E to Station F is exactly 20 kilometers.

An engineer needs to survey the triangular zone formed by the remote observation post (P), the communication hub (D), and Station F. Compute the total length of the perimeter of triangle PDF.

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
