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

A high-tech research facility consists of a circular perimeter with $n$ sensor stations ($n \geq 3$) placed at the vertices of a regular $n$-gon. Each segment of the perimeter fence connecting two adjacent stations is equipped with a signal repeater, and a central server is located in the exact interior of the polygon.

To secure the network, a technician must assign a unique identification code to each of the $2n+1$ components (the $n$ stations, the $n$ repeaters, and the single central server). The security protocol defines a configuration as "stable" if it satisfies the following two calibration requirements:
(a) The code assigned to any signal repeater must be exactly equal to the average of the codes assigned to the two sensor stations it connects.
(b) The code assigned to the central server must be exactly equal to the average of the codes assigned to all $n$ sensor stations.

The technician has been provided with a set of $2n+1$ consecutive integers to use as the identification codes.

Determine the sum of all possible values of $n$ in the range $3 \leq n \leq 100$ for which a stable configuration can be successfully established using these $2n+1$ consecutive integers.

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
