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

In a specialized logistics network, every package is identified by a positive integer ID, $n$. For each ID, we define two efficiency metrics:
1.  **Storage Index** $\sigma(n)$: The total number of distinct positive divisors of $n$.
2.  **Core Factor** $\operatorname{rad} n$: The product of the distinct prime divisors of $n$ (with $\operatorname{rad} 1 = 1$).

A global distribution hub calculates the **Cumulative Network Load** ($L$) by summing a specific performance ratio across all possible package IDs from 1 to infinity. For any given ID $n$, the ratio is defined as:
- The numerator is the product of the Storage Index of $n$ and the Storage Index of the value $(n \cdot \operatorname{rad} n)$.
- The denominator is the product of $n^2$ and the Storage Index of the Core Factor of $n$.

The total load is therefore represented by the infinite sum:
\[ L = \sum_{n=1}^{\infty}\frac{\sigma(n)\sigma(n \operatorname{rad} n)}{n^2\sigma(\operatorname{rad} n)} \]

To determine the final capacity requirement for the hub, engineers must calculate the cube root of this Cumulative Network Load, multiply the result by 100, and then round down to the nearest whole integer.

Find the final capacity requirement (the greatest integer not exceeding $100 \cdot L^{1/3}$).

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
