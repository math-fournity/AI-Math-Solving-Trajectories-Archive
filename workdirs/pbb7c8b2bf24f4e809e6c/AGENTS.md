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

In the high-security vaults of the "Seven Sages" treasury, there are seven distinct mechanical locks arranged in a circle, labeled $L_1, L_2, \dots, L_7$. Each lock $L_i$ is currently set to a secret integer code $a_i$, where each code is strictly between 2 and 166, inclusive. 

To synchronize the security system, each lock $L_i$ is assigned a positive integer "transmission key" $b_i$. The security protocol requires that for every lock $i$ from 1 to 7, the value of the current lock's code $a_i$ raised to the power of its transmission key $b_i$ must be congruent to the square of the next lock's code $a_{i+1}$ modulo 167 (where the "next" lock after $L_7$ is $L_1$, so $a_8 = a_1$).

The system's efficiency is measured by a "Complexity Factor," defined as the product of all seven transmission keys multiplied by the sum of all seven transmission keys. 

What is the minimum possible value of this Complexity Factor, $b_1b_2b_3b_4b_5b_6b_7(b_1 + b_2 + b_3 + b_4 + b_5 + b_6 + b_7)$?

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
