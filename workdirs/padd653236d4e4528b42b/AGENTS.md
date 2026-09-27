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

A specialized artificial intelligence, "PROJECT FIBO," generates a daily output of energy packets. For the first ten days, the output $P(n)$ exactly matches the Fibonacci sequence where $F_1 = F_2 = 1$ and $F_{n+2} = F_{n+1} + F_n$. However, the AI’s programming is constrained such that $P(n)$ must be the unique polynomial of the lowest possible degree that satisfies these values for $1 \le n \le 10$.

A data analyst is calculating the net surplus of energy for a long-term projection. The analyst focuses on the output for the 100th day, $P(100)$, and subtracts the total sum of the daily outputs recorded from day 11 through day 98 inclusive. 

The analyst discovers that this net value satisfies the following equation:
\[P(100) - \sum_{k=11}^{98} P(k) = \frac{m}{10} \binom{98}{9} + 144\]

Compute the integer $m$ that satisfies this energy projection.

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
