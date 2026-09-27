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

A specialized logistics hub manages data packets $(x, y, z)$ that represent integer priority levels. The system is governed by a specific stability protocol where the product of the three priority levels must be exactly equal to the sum of the levels plus a fixed system constant $m$, where $m$ is a positive integer. 

Due to hardware limitations, no single packet's priority level can exceed a capacity limit $n$ (where $n$ is a positive integer) in terms of its absolute value; that is, the highest magnitude among the three integers must be less than or equal to $n$.

Let $f(m, n)$ represent the total number of unique ordered priority triples $(x, y, z)$ that satisfy these system requirements. Engineers have observed that when the system constant $m$ is set to 2, and the capacity limit $n$ is at least 6, the total number of valid triples $f(2, n)$ follows a linear function of $n$.

A technician is tasked with configuring a new system. Find the value of the sum $m + n$ such that the total number of valid priority triples $f(m, n)$ is exactly 2018.

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
