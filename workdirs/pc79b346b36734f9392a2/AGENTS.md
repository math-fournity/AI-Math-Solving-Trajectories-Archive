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

In a specialized digital archive, a master security key is represented by an $n$-digit integer $a$, where every digit is between 1 and 9 (no zeros). Within this system, a "sub-sequence validator" is defined as any natural number $x$ that has a specific number of significant digits $d$. 

A validator $x$ is said to be "active" at a specific shift $i$ (where $i$ is any natural number) if the integer part of $a/10^i$, when truncated to its last $d$ digits, is exactly equal to $x$. 

Two different validators, $b$ (with $m$ digits) and $c$ (with $k$ digits), are considered "functionally equivalent" for a given key $a$ if they are active at exactly the same shifts $i$. That is, for every $i \in \mathbb{N}$, validator $b$ is active at shift $i$ if and only if validator $c$ is active at shift $i$.

Let $S(a)$ be the size of the largest possible set of validators such that no two validators in the set are functionally equivalent for the key $a$.

For a fixed length $n \ge 2$, consider all possible $n$-digit keys $a$ that do not contain the digit zero. Determine the maximum possible value of $S(a)$ across all such keys.

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
