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

A specialized logistics hub coordinates three distinct transport routes, represented by their operational cycles in hours: $a$, $b$, and $c$. These cycles are all unique positive integers.

The hub defines a "Base Coordination Unit" $G$ as the greatest common divisor of all three cycle lengths ($\gcd(a, b, c) = G$).

The system is designed with a "Synchronized Peak" requirement: the lowest common multiple of any two routes must be identical across all pairs ($\operatorname{lcm}(a, b) = \operatorname{lcm}(a, c) = \operatorname{lcm}(b, c)$).

Efficiency is measured by "Coupled Throughput." For any two routes, the sum of their reciprocal cycle lengths must result in a value that is itself the reciprocal of an integer. Specifically, $\frac{1}{a}+\frac{1}{b}$, $\frac{1}{a}+\frac{1}{c}$, and $\frac{1}{b}+\frac{1}{c}$ must all be unit fractions (fractions with a numerator of 1).

Finally, a "Network Stability Index" is calculated by summing the greatest common divisors of each pair of routes. In this hub, the sum $\gcd(a, b) + \gcd(a, c) + \gcd(b, c)$ is exactly equal to $16$ times the Base Coordination Unit $G$.

Find the smallest possible positive integer value for the Base Coordination Unit $G$.

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
