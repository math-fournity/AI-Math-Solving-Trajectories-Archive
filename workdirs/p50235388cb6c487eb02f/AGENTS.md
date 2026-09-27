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

In a remote desert, a square solar farm is enclosed by a perimeter fence measuring 100 kilometers on each side. An underground fiber-optic cable, denoted as $L$, is laid in a single continuous path within the farm. This cable consists of $n$ straight-line segments connected end-to-end, starting at point $A_0$ and ending at a different point $A_n$, without ever crossing or touching itself.

To ensure monitoring capabilities, the cable was installed such that every single point along the 400-kilometer perimeter fence is within a distance of no more than 0.5 kilometers from at least one point on the cable.

An engineer is analyzing the signal latency between different points along the cable. Let $M$ be the maximum possible value such that, for any cable layout satisfying the coverage requirement, there must exist two points $X$ and $Y$ on the cable that are separated by a direct Euclidean distance $d(X, Y) \leq 1$ kilometer, yet the actual length of the fiber-optic cable connecting $X$ and $Y$ is at least $M$ kilometers.

Find the value of $M$.

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
