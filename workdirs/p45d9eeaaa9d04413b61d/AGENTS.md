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

A high-security digital vault requires two four-digit access codes, $M$ and $N$, to be entered into a system. To be valid, both codes must be perfect squares of integers. The security protocol defines a "Shift-Square Pair" based on the following synchronization rules between the two codes:

1. Comparing the four-digit string of $M$ to the four-digit string of $N$, the digits must be identical in exactly two of the four positions.
2. In the other two positions, the digit in $M$ must be exactly one unit greater than the digit in the corresponding position in $N$.

For instance, if $M = 3600$ and $N = 2500$, they form a pair because the digits in the third and fourth positions are identical ($0$ and $0$), while the digits in the first and second positions of $M$ ($3$ and $6$) are each exactly one greater than those in $N$ ($2$ and $5$).

Identify every pair of four-digit integers $(M, N)$ that satisfies these criteria. Calculate the total sum of all $M$ values and all $N$ values found across all unique pairs.

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
