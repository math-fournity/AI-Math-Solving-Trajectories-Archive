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

In the city of Arithema, a master architect is designing a monumental plaza for the year 2020. The plaza consists of $n = 2020$ designated plots arranged in a sequence. However, zoning laws state that a memorial can only be built on a plot $k$ if the index of that plot is "relatively prime" to the total number of plots (meaning $\gcd(k, 2020) = 1$, where $1 \le k \le 2020$).

For every plot $k$ that qualifies for a memorial, the architect installs a cubic sculpture with a volume equal to $k^3$ cubic meters. The "Grand Total Volume," denoted as $f(2020)$, is the sum of the volumes of all such sculptures installed in the plaza.

A materials scientist needs to break down this total volume $f(2020)$ into its fundamental components. To do this, the scientist finds the unique prime factorization of the total volume:
$f(2020) = p_{1}^{e_{1}} p_{2}^{e_{2}} \ldots p_{k}^{e_{k}}$

To finalize the project's structural report, the architect must calculate the "Complexity Index," which is defined as the sum of the products of each prime factor and its corresponding exponent.

Calculate the value of $\sum_{i=1}^{k} p_{i} e_{i}$.

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
