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

A high-security vault uses an 8-slot rotating digital tumbler. Each slot displays a single digit from a base-6 system (0, 1, 2, 3, 4, or 5). Leading zeros are allowed, meaning any sequence of eight digits is a valid display.

The vault's locking mechanism is governed by a "Cyclic Divisibility" protocol. Let the current sequence of digits visible in the slots be represented by the integer $N_0 = (a_1 a_2 a_3 a_4 a_5 a_6 a_7 a_8)_6$. As the tumbler rotates one position at a time, it generates a series of new integers $N_i$ by shifting the digits cyclically to the left. Specifically:
- $N_1 = (a_2 a_3 a_4 a_5 a_6 a_7 a_8 a_1)_6$
- $N_2 = (a_3 a_4 a_5 a_6 a_7 a_8 a_1 a_2)_6$
- ... and so on, until $N_7 = (a_8 a_1 a_2 a_3 a_4 a_5 a_6 a_7)_6$.

The vault will only remain locked if the original integer $N_0$ is a divisor of every subsequent rotated integer $N_i$ for $i = 1, 2, \dots, 7$. Note that the value 0 does not divide any positive integer, but by convention of the mechanism, the sequence $(00000000)_6$ is excluded as the problem specifies the integers must be positive.

How many distinct 8-digit base-6 positive integers satisfy this cyclic divisibility requirement?

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
