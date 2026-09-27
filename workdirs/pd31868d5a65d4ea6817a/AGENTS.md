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

A specialized circular power grid consists of $n$ distribution hubs connected by $n$ transmission lines. Each hub is assigned a non-negative integer power level $e_1, e_2, \ldots, e_n$, and each transmission line connecting hub $i$ to hub $i+1$ (where the $n$-th hub connects back to the 1st) is assigned a non-negative integer load $k_i$.

The grid's configuration must satisfy two strict engineering constraints:
1. The set of power levels assigned to the hubs $(e_1, \ldots, e_n)$ must be a mathematical permutation of the set of loads assigned to the transmission lines $(k_1, \ldots, k_n)$.
2. The load on any transmission line $k_i$ must be exactly equal to the absolute difference between the power levels of the two hubs it connects: $k_i = |e_{i+1} - e_i|$ (with $e_{n+1} = e_1$).

For a specific target integer $m$, let $n(m)$ represent the minimum number of hubs required such that every integer from $0$ to $m$ inclusive appears at least once in the list of hub power levels and at least once in the list of transmission line loads.

Calculate $n(2024)$.

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
