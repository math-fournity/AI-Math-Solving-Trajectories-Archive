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

In a specialized logistics simulation, a mainframe computer processes data packets represented by complex polynomials. The system analyzes two types of transmission signals: a primary signal $g(X) = X^n + aX + b$ and a reference signal $f(X) = X^m + aX + b$. A "Harmonic Connection" occurs only when the data structure of the primary signal is perfectly divisible by the reference signal, under the constraint that $a, b, m,$ and $n$ are all integers and $n > m > 1$.

An analyst is tasked with calculating a "Stability Index" for a specific subset $S'$ of all possible Harmonic Connections $(a, b, m, n)$. The Stability Index is defined as the sum of the expression $|a| + |b| + m + n$ calculated for every unique quadruplet in $S'$.

The subset $S'$ consists of the following three categories of connections:
1. All valid Harmonic Connections where $1 < m < n \leq 6$ and neither $a$ nor $b$ is equal to zero.
2. All valid Harmonic Connections where the parameters are fixed at $a = 0$ and $b = 1$, within the range $1 < m < n \leq 10$.
3. All valid Harmonic Connections where the parameters are fixed at $a = 1$ and $b = 0$, within the range $1 < m < n \leq 10$.

Calculate the total Stability Index (the sum of $|a| + |b| + m + n$ over all quadruplets in $S'$).

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
