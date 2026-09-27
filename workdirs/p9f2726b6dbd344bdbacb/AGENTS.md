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

In a specialized logistics network, three automated delivery drones—Model A, Model B, and Model C—are assigned to complete a massive distribution task. Each drone has a unique, integer-based efficiency rating represented by the number of hours it takes to complete the entire task solo. These ratings are strictly ordered such that Model A is faster than Model B, and Model B is faster than Model C, though all three drones are rated under 1000 hours. Specifically, the relationship is defined as $0 < a < b < c < 1000$, where $a, b,$ and $c$ are their respective solo completion times in hours.

When all three drones work together simultaneously, their combined hourly productivity is exactly equal to that of a single master-hub processor which completes the task in 315 hours. This relationship is governed by the total work rate equation:
\[ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{1}{315} \]

Given that there is only one unique set of integer ratings $(a, b, c)$ that satisfies these operational constraints, determine the hourly rating of the fastest drone, $a$.

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
