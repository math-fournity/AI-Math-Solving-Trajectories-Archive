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

In a specialized logistics network, a central hub manages $n$ distinct docking bays, where $n$ is an integer greater than or equal to 1. For a technical synchronization to occur, the hub only communicates with "compatible" units—those assigned a security ID integer $k$ such that $k$ and $n$ share no common factors greater than 1 (relatively prime).

The network is governed by a strict "Symmetry Protocol." This protocol is satisfied if, for any two compatible security IDs $a$ and $b$, the following two conditions are perfectly interchangeable (meaning one is true if and only if the other is true):
1. The IDs are identical relative to the hub's capacity ($a$ and $b$ leave the same remainder when divided by $n$).
2. The product of the IDs yields a base-level synchronization ($ab$ leaves a remainder of 1 when divided by $n$).

Identify all possible values of the hub capacity $n \ge 2$ that allow this Symmetry Protocol to hold for all compatible IDs. Calculate the sum of all such integers $n$.

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
