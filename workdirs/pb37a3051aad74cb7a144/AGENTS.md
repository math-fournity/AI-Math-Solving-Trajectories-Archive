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

A specialized cybersecurity firm classifies certain encryption keys, represented by odd prime numbers $p$, as "stable" based on the behavior of a recursive signal processing algorithm. 

A prime $p$ is considered "stable" if an analyst can generate an infinite sequence of positive integers $a_0, a_1, a_2, \dots$ such that a specific modular resonance condition is met. The condition requires that the initial value $a_0$ is congruent modulo $p$ to every term in a sequence of nested continued fractions of increasing depth. Specifically, for every $n \geq 1$, let $F_n$ be the continued fraction defined by a sequence of $n$ ones followed by a final term of $1/a_n$:
\[F_1 = 1 + \frac{1}{a_1}\]
\[F_2 = 1 + \frac{1}{1 + \frac{1}{a_2}}\]
\[F_3 = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{a_3}}}\]
The stability condition is satisfied if $a_0 \equiv F_n \pmod{p}$ for all $n \in \{1, 2, 3, \dots\}$.

For any two fractions $\frac{a}{b}$ and $\frac{c}{d}$ used in these calculations, the equivalence $\frac{a}{b} \equiv \frac{c}{d} \pmod{p}$ is defined to hold if $p$ divides $(ad - bc)$ and $p$ does not divide the product of the denominators $bd$.

What is the sum of the first three odd primes that are not "stable"?

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
