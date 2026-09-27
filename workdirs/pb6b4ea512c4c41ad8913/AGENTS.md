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

In a specialized cyber-security network, an encryption protocol is defined by a security level $q$, where $q$ is an odd prime number. For each such $q$, a complexity index is calculated using a base value $x$ according to the polynomial $\Phi_{q}(x) = x^{q-1} + x^{q-2} + \dots + x + 1$.

A system administrator is testing a range of "stability primes" $p$ within the inclusive range $3 \leq p \leq 100$. A stability prime $p$ is deemed "hyper-compatible" if there exists at least one security level $q$ (an odd prime) and at least one positive integer capacity $N$ such that the system satisfies two specific data-integrity conditions:

1. The number of ways to distribute $N$ packets into $\Phi_{q}(p)$ storage slots must be congruent to the number of ways to choose $N$ packets from a set of $2\Phi_{q}(p)$ available packets, when evaluated under modulo $p$ arithmetic.
2. Neither of these two counts (the binomial coefficients) can be divisible by $p$.

Find the sum of all hyper-compatible stability primes $p$ in the range $[3, 100]$.

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
