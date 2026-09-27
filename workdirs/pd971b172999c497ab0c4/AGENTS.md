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

A network of 2019 servers, indexed from $i=2$ to $2020$, generates data through a specific efficiency coefficient $a_i$ defined as:
$$a_{i}=\frac{\sqrt{3 i^{2}+2 i-1}}{i^{3}-i}$$
For each server $i$, a power allocation $x_i$ (a positive real number) is assigned. The total power grid is constrained such that the sum of the fourth powers of all allocations is:
$$\sum_{i=2}^{2020} x_{i}^{4} = 1-\frac{1}{1010 \cdot 2020 \cdot 2021}$$
The total utility $S$ of the system is the maximum possible value of the aggregate function:
$$\sum_{i=2}^{2020} a_{i} x_{i}\left(\sqrt{a_{i}}-2^{-2.25} x_{i}\right)$$
Let $m$ be the smallest positive integer such that $S^m$ is a rational number. When $S^m$ is expressed as a fraction in its simplest form, let its denominator be prime-factorized as $p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}$, where $p_1 < p_2 < \dots < p_k$ are primes and $\alpha_i$ are positive integers.

Compute the value of the sum $p_{1} \alpha_{1}+p_{2} \alpha_{2}+\cdots+p_{k} \alpha_{k}$.

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
