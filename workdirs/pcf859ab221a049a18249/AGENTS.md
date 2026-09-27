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

A digital trading platform tracks a specialized index where "Relative Dominance" is calculated between two consecutive price fluctuations, $x$ and $y$. The Dominance value is defined as follows: if the ratio of their magnitudes $\frac{|x|}{|y|}$ is a positive integer, that integer is the value; if the ratio $\frac{|y|}{|x|}$ is a positive integer, that integer is the value; in all other cases, the Dominance is zero.

An analyst is building a "Prime Sequence" of non-zero price fluctuations $l_1, l_2, \dots, l_n$. A sequence is considered "Valid" only if the Dominance value between every pair of adjacent fluctuations $(l_i, l_{i+1})$ is non-zero. The "Total Strength" of the sequence is the sum of these Dominance values across all adjacent pairs.

The analyst must adhere to the following strict regulatory protocols:
1. Every fluctuation in the sequence must have an absolute value between 2 and 6 inclusive.
2. The platform's security protocol forbids repeating any specific directed transition: if a fluctuation with value $b$ immediately follows a fluctuation with value $a$ once in the sequence, the pair $(a, b)$ cannot occur again. Furthermore, once the transition $(a, b)$ has been used, the reverse transition $(b, a)$ is strictly prohibited from appearing anywhere in the sequence.

What is the maximum possible Total Strength that a Valid sequence can achieve under these constraints?

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
