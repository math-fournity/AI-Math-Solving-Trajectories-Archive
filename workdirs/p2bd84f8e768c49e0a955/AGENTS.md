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

A high-security digital vault requires a 3-part access code to unlock. This code is validated based on a specific "divisibility by 9" checksum protocol. 

The system operates as follows:
A user is presented with a set of $n$ data packets, each containing a single integer. From this set of $n$ packets, the user must select exactly three packets (let’s call the integers inside them $n_1, n_2$, and $n_3$). These packets are not necessarily distinct; the user may choose the same physical packet multiple times.

Each of the three selected integers must then be multiplied by a "security coefficient" ($\lambda_i$). For each integer, the user has only two choices for the coefficient: it must be either 4 or 7.

The vault will open if, and only if, the sum of these three products—$(\lambda_1 \cdot n_1 + \lambda_2 \cdot n_2 + \lambda_3 \cdot n_3)$—is a multiple of 9.

What is the minimum number of data packets $n$ that must be provided to the user to guarantee that, no matter what integers are inside the packets, it is always possible to select three packets and assign coefficients from the set $\{4, 7\}$ to satisfy the checksum?

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
