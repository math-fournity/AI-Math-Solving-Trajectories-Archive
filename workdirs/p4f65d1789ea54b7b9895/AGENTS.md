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

In a futuristic industrial colony, a head engineer is optimizing the energy consumption of a multi-stage power grid. The grid consists of $n$ independent power cells, where $n$ is any positive integer. Each cell $i$ has an assigned performance parameter $x_i$, which is a positive real number.

The total "Dynamic Stress" on the system is calculated by summing the stress values of $n+1$ different configurations, indexed from $k=0$ to $k=n$. For a specific configuration $k$, the stress is given by the formula:
$$\frac{(n^3+k^3-k^2n)^{3/2}}{\sqrt{\sum_{j=1}^k x_j^2 + \sum_{j=k+1}^n x_j}}$$
(Note: For $k=0$, the denominator is $\sqrt{\sum_{j=1}^n x_j}$, and for $k=n$, it is $\sqrt{\sum_{j=1}^n x_j^2}$).

The colony's safety protocol dictates that this total Dynamic Stress must never exceed a specific "Threshold Limit." This limit is the sum of three distinct operational costs:
1. A variable efficiency cost: $\sqrt{3} \sum_{i=1}^n \frac{i^3(4n-3i+100)}{x_i}$
2. A structural fatigue cost: $cn^5$
3. A fixed maintenance overhead: $100n^4$

In these equations, $c$ represents a universal constant related to the material strength of the grid. 

Determine the smallest positive real number $c$ such that the total Dynamic Stress is always less than or equal to the Threshold Limit for every possible configuration of $n$ and all possible values of $x_i$.

Compute $\lfloor 2020c \rfloor$.

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
