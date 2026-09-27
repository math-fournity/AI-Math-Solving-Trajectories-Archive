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

In a remote digital archipelago, a network of servers is arranged in a perfect square grid. Each server is identified by its coordinates $(i, j)$ within an $n \times n$ layout. To ensure data redundancy and security, each server must be assigned a unique "Security Key." A Security Key consists of a sequence of $k$ bits (each bit being either 0 or 1).

A configuration is considered "Interference-Resistant" if, for every pair of servers located in adjacent grid cells (sharing a horizontal or vertical boundary), their assigned Security Keys share a maximum of one identical bit at the same position in the sequence.

Let $P(n, k)$ be a logical property that is true (1) if an interference-resistant configuration of unique keys exists for an $n \times n$ grid using $k$-bit keys, and false (0) if no such configuration is possible.

Evaluate the property $P(n, k)$ for the following three network deployments:
1. A $8 \times 8$ grid using $6$-bit keys.
2. A $4 \times 4$ grid using $4$-bit keys.
3. A $16 \times 16$ grid using $8$-bit keys.

Calculate the sum of the values (where true = 1 and false = 0) for these three specific cases.

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
