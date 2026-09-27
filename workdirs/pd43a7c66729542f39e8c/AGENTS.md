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

In a remote digital treasury, a secure vault requires a unique "Base-Factor Code" to be unlocked. The security system is governed by a specific prime number $p$, which determines the architecture of the vault's encryption.

To authorize a transaction of exactly 2013 gold credits, a technician must define a storage duration $m$ (a positive integer) and assign a series of security clearance levels $a_0, a_1, \dots, a_m$. According to the treasury protocols, each individual clearance level $a_i$ must be a non-negative integer strictly less than the prime $p$.

The system validates the transaction based on two distinct encrypted sums:
1. The **Weighted Power Sum**: When the clearance levels are used as coefficients for increasing powers of the prime $p$, the total value must exactly match the credit transaction:
   $$a_0 + a_1 p^1 + a_2 p^2 + \dots + a_m p^m = 2013$$
2. The **Digit Sum Integrity**: The simple arithmetic sum of all the clearance levels must equal a specific security constant of 11:
   $$a_0 + a_1 + a_2 + \dots + a_m = 11$$

Identify all possible prime numbers $p$ that would allow a technician to find a valid duration $m$ and a set of clearance levels $a_i$ satisfying these two treasury requirements.

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
