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

In a specialized digital vault, "megacodes" are defined as $n$-digit sequences where every digit is a prime number (2, 3, 5, or 7), the entire sequence represents a prime number, and the sum of all digits is also a prime number. Let $S$ be the collection of all possible $n$-digit sequences composed solely of prime digits. Let $M(n)$ denote the total count of megacodes of length $n$.

For the specific case where $n = 2018$, researchers have established an upper bound for $M(2018)$ expressed as $C \cdot 4^{n-3} - 3 \cdot 2^{n-3}$. This bound is derived by systematically excluding sequences in $S$ that cannot be megacodes based on the following security protocols:

1. A sequence in $S$ is disqualified if the number it represents is even, or if it is divisible by 5 (and exceeds 5), or if the total sum of its digits is an even number (and exceeds 2).
2. A sequence in $S$ is disqualified if the number it represents is divisible by 3 (and exceeds 3).

By applying these constraints to filter the set $S$ and utilizing the inclusion-exclusion principles associated with these properties to estimate the remaining candidates, find the integer value of $C$ such that:
$$M(2018) \le C \cdot 4^{2015} - 3 \cdot 2^{2015}$$

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
