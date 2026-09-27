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

In a large logistics network with $n$ hubs, a "route-swap" is defined as a protocol that exchanges the cargo destinations of exactly two distinct hubs while leaving all other $n-2$ hubs unaffected.

Suppose we are given four fixed, distinct route-swaps, denoted $\sigma_1, \sigma_2, \sigma_3, \sigma_4$. Let $q$ be any prime number representing the size of a finite field $\mathbb{F}_q$. We consider data-processing systems that assign a security code $f(x_1, \ldots, x_n) \in \mathbb{F}_q$ to a matrix of $n$ logistics vectors $(x_1, \ldots, x_n)$, where each $x_i \in \mathbb{F}_q^n$. These systems must satisfy two operational constraints:
1. **Linearity**: The code must be additive in each vector input, such that $f(\dots, y+z, \dots) = f(\dots, y, \dots) + f(\dots, z, \dots)$ for any hub's data vector.
2. **Swap-Inversion**: Applying any of the four specific route-swaps $\sigma \in \{\sigma_1, \sigma_2, \sigma_3, \sigma_4\}$ to the ordering of the input vectors must negate the resulting security code: $f(x_{\sigma(1)}, \ldots, x_{\sigma(n)}) = -f(x_1, \ldots, x_n)$.

For a specific set of input vectors $(x_1, \ldots, x_n)$, let $g(x_1, \ldots, x_n)$ be the number of distinct possible values the security code can take across all valid system configurations $f$. If the input vectors are chosen uniformly at random from $(\mathbb{F}_q^n)^n$, let $\varepsilon(q, \sigma_1, \sigma_2, \sigma_3, \sigma_4)$ be the expected value of $g$.

We define the "complexity index" of these four swaps as:
$$\kappa(\sigma_1, \sigma_2, \sigma_3, \sigma_4) = -\lim_{q \to \infty} \log_q \left( -\ln \left( \frac{\varepsilon(q, \sigma_1, \sigma_2, \sigma_3, \sigma_4) - 1}{q - 1} \right) \right)$$

Now, imagine we select the four distinct route-swaps $\sigma_1, \dots, \sigma_4$ uniformly at random from the set of all possible swaps for $n$ hubs. Let $\pi(n)$ be the expected value of the complexity index $\kappa$. Given that there exist real polynomials $p(x)$ and $q(x)$ such that $\pi(n) = \frac{p(n)}{q(n)}$ for infinitely many $n$, and $q(-3) \neq 0$, calculate the value of $\frac{p(-3)}{q(-3)}$.

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
