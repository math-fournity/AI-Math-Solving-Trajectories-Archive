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

Let \( p, q \) be positive integers satisfying the system of congruences:
\[
\begin{cases}
p \equiv 3 \pmod{911}, \\
q \equiv 2 \pmod{997}, \\
p \equiv 738 \pmod{q};
\end{cases}
\]
Let \( \{ a_n \}, \{ b_n \}, \{ c_n \} \) be periodic sequences of rational numbers satisfying the equations:
\[
\left[ 4b_n + 1 - 3\sin(\pi a_n) \right]^2 + \left[ 4c_n - 1 + 3\sin(\pi a_n) \right]^2 = 0 \quad (\forall n \in \mathbb{N})\]
and
\[\left| \sum_{i=1}^{p} b_i^3 \right|+\left| \sum_{i=1}^{q} c_i^3 \right|+\left| p - 3 \sum_{i=1}^{p} b_i \right|+\left| q - 3 \sum_{i=1}^{q} c_i^2 \right| = 0.\]
Find the minimum value of \( p + q + 2a_p^2 + b_q^2 + c_{p+q}^2 + (a_p + a_{q-1})^2 + (b_p + c_q)^2 \).
After solving the above problem, please output your final answer in the following format:
### The final answer is: $\boxed{<your answer>}$
Example:
### The final answer is: $\boxed{123}$
The final answer should be given as precisely as possible (using LaTeX symbols such as \sqrt, \frac, \pi, etc.). If the final answer involves a decimal approximation, it must be accurate to at least four decimal places.

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
