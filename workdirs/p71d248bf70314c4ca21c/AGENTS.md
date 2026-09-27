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

A high-security research facility uses a master control panel with 19 distinct power levels, indexed as $M = \{1, 2, \dots, 19\}$. To optimize the system, a technician needs to select a subset of "primary" voltage chips, $A = \{a_1, a_2, \dots, a_k\}$, chosen from these 19 levels.

The system is designed such that any required power level $b$ in the set $M$ must be achievable using the primary chips in one of three ways:
1. The level $b$ is directly provided by a primary chip ($b = a_i$).
2. The level $b$ is produced by the sum of two primary chips ($b = a_i + a_j$).
3. The level $b$ is produced by the difference between two primary chips ($b = a_i - a_j$ or $b = a_j - a_i$).

Note that in the second and third methods, the two chips used ($a_i$ and $a_j$) may be the same physical chip type.

What is the minimum number of primary chips $k$ that must be selected to ensure that every power level from 1 to 19 can be generated?

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
