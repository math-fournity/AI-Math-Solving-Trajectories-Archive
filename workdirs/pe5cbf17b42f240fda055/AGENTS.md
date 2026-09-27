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

For a positive integer \( n \), we say an \( n \)-transposition is a bijection \(\sigma:\{1,2, \ldots, n\} \rightarrow\{1,2, \ldots, n\}\) such that there exist exactly two elements \( i \) of \(\{1,2, \ldots, n\}\) such that \(\sigma(i) \neq i\).

Fix some four pairwise distinct \( n \)-transpositions \(\sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}\). Let \( q \) be any prime, and let \(\mathbb{F}_{q}\) be the integers modulo \( q \). Consider all functions \( f:\left(\mathbb{F}_{q}^{n}\right)^{n} \rightarrow \mathbb{F}_{q} \) that satisfy, for all integers \( i \) with \( 1 \leq i \leq n \) and all \( x_{1}, \ldots x_{i-1}, x_{i+1}, \ldots, x_{n}, y, z \in \mathbb{F}_{q}^{n} \),

\[ f\left(x_{1}, \ldots, x_{i-1}, y, x_{i+1}, \ldots, x_{n}\right)+f\left(x_{1}, \ldots, x_{i-1}, z, x_{i+1}, \ldots, x_{n}\right)=f\left(x_{1}, \ldots, x_{i-1}, y+z, x_{i+1}, \ldots, x_{n}\right), \]

and that satisfy, for all \( x_{1}, \ldots, x_{n} \in \mathbb{F}_{q}^{n} \) and all \(\sigma \in\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}\right\}\),

\[ f\left(x_{1}, \ldots, x_{n}\right)=-f\left(x_{\sigma(1)}, \ldots, x_{\sigma(n)}\right). \]

(Note that the equalities in the previous sentence are in \(\mathbb{F}_{q}\). Note that, for any \( a_{1}, \ldots, a_{n}, b_{1}, \ldots, b_{n} \in \mathbb{F}_{q} \), we have \(\left(a_{1}, \ldots, a_{n}\right)+\left(b_{1}, \ldots, b_{n}\right)=\left(a_{1}+b_{1}, \ldots, a_{n}+b_{n}\right)\), where \( a_{1}+b_{1}, \ldots, a_{n}+b_{n} \in \mathbb{F}_{q} \).)

For a given tuple \(\left(x_{1}, \ldots, x_{n}\right) \in\left(\mathbb{F}_{q}^{n}\right)^{n}\), let \( g\left(x_{1}, \ldots, x_{n}\right) \) be the number of different values of \( f\left(x_{1}, \ldots, x_{n}\right) \) over all possible functions \( f \) satisfying the above conditions.

Pick \(\left(x_{1}, \ldots, x_{n}\right) \in\left(\mathbb{F}_{q}^{n}\right)^{n}\) uniformly at random, and let \(\varepsilon\left(q, \sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}\right)\) be the expected value of \( g\left(x_{1}, \ldots, x_{n}\right) \). Finally, let

\[ \kappa\left(\sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}\right)=-\lim _{q \rightarrow \infty} \log _{q}\left(-\ln \left(\frac{\varepsilon\left(q, \sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}\right)-1}{q-1}\right)\right). \]

Pick four pairwise distinct \( n \)-transpositions \(\sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}\) uniformly at random from the set of all \( n \) transpositions. Let \(\pi(n)\) denote the expected value of \(\kappa\left(\sigma_{1}, \ldots, \sigma_{4}\right)\). Suppose that \( p(x) \) and \( q(x) \) are polynomials with real coefficients such that \( q(-3) \neq 0 \) and such that \(\pi(n)=\frac{p(n)}{q(n)}\) for infinitely many positive integers \( n \). Compute \(\frac{p(-3)}{q(-3)}\).

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
