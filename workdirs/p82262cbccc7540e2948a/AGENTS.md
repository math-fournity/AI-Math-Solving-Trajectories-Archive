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

A specialized data compression algorithm assigns a "Capacity Score" $N$ to any positive integer "Seed" $m$. The score $N$ is calculated by observing the growth of the Seed across ten processing cycles. If $L(x)$ represents the number of digits in an integer $x$, the Capacity Score is defined as the sum of the digit counts of the first ten powers of the Seed: $N = L(m^1) + L(m^2) + \dots + L(m^{10})$.

A positive integer $N$ is classified as "Optimized" if there exists at least one integer Seed $m \ge 1$ that produces $N$ as its Capacity Score.

Let $M$ be a large positive integer, and let $p_M$ represent the probability that a randomly selected integer from the set $\{1, 2, \dots, M\}$ is Optimized. 

Determine the value of the limiting probability as the range of selection grows to infinity:
$$\lim_{M \to \infty} p_M$$

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
