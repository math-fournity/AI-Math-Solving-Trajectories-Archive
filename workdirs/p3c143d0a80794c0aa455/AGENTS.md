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

In a remote industrial refinery, a processing system handles a sequence of raw chemical inputs $\{x_n\}$. Each input $x_n$ is a real value representing the chemical potential of the $n$-th batch. From these raw inputs, the system generates a sequence of refined outputs $\{y_n\}$ according to a specific recursive protocol: the first refined output $y_1$ is identical to the first raw input $x_1$. For every subsequent batch $n \geq 1$, the next output $y_{n+1}$ is calculated by taking the raw input $x_{n+1}$ and subtracting the Euclidean norm (the square root of the sum of the squares) of all preceding raw inputs $x_1$ through $x_n$.

The refinery’s efficiency is monitored over a total period of $m$ batches. The "average raw intensity" is defined as the mean of the squares of the first $m$ raw inputs: $\frac{1}{m} \sum_{i=1}^{m} x_{i}^{2}$. This intensity must be contained or "bounded" by a weighted sum of the squares of the refined outputs $\{y_i\}$, where the weight for each $y_i^2$ is determined by a decay constant $\lambda$ raised to the power of $(m-i)$.

A safety engineer needs to determine the rigorous performance threshold of this system. Find the smallest positive real number $\lambda$ such that, for any possible sequence of raw inputs $\{x_n\}$ and for every positive integer $m$, the following inequality is guaranteed to hold:
$$
\frac{1}{m} \sum_{i=1}^{m} x_{i}^{2} \leqslant \sum_{i=1}^{m} \lambda^{m-i} y_{i}^{2}
$$

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
