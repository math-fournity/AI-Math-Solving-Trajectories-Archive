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

A high-security digital vault uses a prime modulus $p = 10^9 + 7$ for its encryption protocols. To generate access keys, the system first identifies all prime numbers $p_1, p_2, p_3, \dots, p_m$ that are strictly less than $\sqrt[4]{p/2}$, arranged in increasing order.

For each prime $p_i$, the vault calculates a unique "inverse signature" $q_i$, which is the integer in the range $[0, p-1]$ such that the product $p_i q_i$ leaves a remainder of $1$ when divided by $p$. These signatures form the Master Key Set $S_1 = \{q_1, q_2, \dots, q_m\}$.

A security administrator generates a "Transformed Key Set" $S_2$ by selecting two fixed integers $a$ and $b$ (where $0 < a, b < p$) and applying a linear transformation to the original signatures. Specifically, $S_2$ consists of the remainders of $(a q_i + b)$ when divided by $p$, for all $i = 1, \dots, m$.

In order to test the vulnerability of the system to a collision attack, the administrator needs to find the maximum possible number of elements that can be shared between the sets $S_1$ and $S_2$. What is the maximum possible size of the intersection $S_1 \cap S_2$?

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
