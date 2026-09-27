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

In a specialized vault, a master locksmith is constructing a unique "Divisibility Chain" of security codes. Each code in the sequence is a whole number formed using a string of digits, where every digit must be a non-zero integer (from 1 to 9).

The process begins with a single digit, $a_0$. To grow the chain, the locksmith adds a new non-zero digit $a_1$ to the left of the previous string to create a 2-digit number $(a_1 a_0)$. This process continues such that for any index $k$ (where $1 \leq k \leq n$), a new $k$-digit number is defined as $N_k = (a_{k-1} a_{k-2} \ldots a_0) = \sum_{i=0}^{k-1} a_i 10^i$.

The security protocol requires a strict mathematical property: for every $k$ from 1 to $n$, the $k$-digit number $N_k$ must be a perfect divisor of the $(k+1)$-digit number $N_{k+1}$ formed by placing the next non-zero digit $a_k$ to its left.

What is the maximum possible number of digits $n$ that can be added to the initial digit $a_0$ while maintaining this divisibility property for every step of the sequence $(a_0, a_1, \ldots, a_n)$?

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
