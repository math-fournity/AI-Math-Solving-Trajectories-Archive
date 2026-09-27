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

An elite logistics firm is designing a pipeline route through 10 specific survey stations, denoted sequentially as $a_1, a_2, \ldots, a_{10}$, where the value of each $a_i$ represents the positive distance from a central hub to that station. 

The cost to connect any two adjacent stations $a_i$ and $a_{i+1}$ is determined by a "resistance metric" involving a friction constant $k$. The cost formula for the segment between $a_i$ and $a_{i+1}$ is $\sqrt{a_i^2 - k a_i a_{i+1} + a_{i+1}^2}$. The total cost of the pipeline connecting the first station to the last through all intermediate points is the sum of these nine segments: $\sum_{i=1}^{9} \sqrt{a_i^2 - k a_i a_{i+1} + a_{i+1}^2}$.

The firm’s safety protocol requires that this total path cost must always be greater than or equal to a "theoretical direct return cost" between the first and last stations, calculated using a reflected friction constant as $\sqrt{a_1^2 + k a_1 a_{10} + a_{10}^2}$. 

This requirement must hold true regardless of the distances chosen for the ten stations ($a_i > 0$). Given the constraint that the friction constant $k$ cannot exceed 2, let $k'$ be the maximum possible value of $k$ that ensures this inequality is never violated. 

Compute $(2k' - 5)^6$.

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
