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

In a remote industrial lab, an automated chemical reactor operates based on a specific "Stability Recipe." The process begins with an initial chemical mixture defined by two non-zero real-valued catalysts, $a_1$ and $b_1$. These catalysts are used to set the parameters of a reaction chamber governed by the equation $x^2 + a_1 x + b_1 = 0$.

For the process to continue to a next stage, this chamber equation must yield real-valued pressure readings, $p$ and $q$. If these readings exist, they are ordered such that $p \leq q$. These two readings then serve as the new catalysts for the next stage's reaction chamber, creating a new equation: $x^2 + px + q = 0$.

This cycle repeats indefinitely as long as the current chamber’s equation produces real-valued pressure readings. Each time a set of real readings is generated, they are used as the coefficients ($p$ as the linear coefficient and $q$ as the constant term) for the subsequent chamber.

Determine $N$, the maximum number of such reaction chambers that can be linked in this sequence before a chamber fails to produce real-valued pressure readings.

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
