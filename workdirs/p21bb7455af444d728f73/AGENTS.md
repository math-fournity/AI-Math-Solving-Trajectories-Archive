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

A specialized logistics drone is programmed to navigate a linear warehouse grid consisting of $2n$ equal segments, where $n = 2020$. The drone starts its mission at a base station (Position 0) at time $t=0$. Every second, for $2n$ seconds, it must move exactly one unit distance either forward ($+1$) or backward ($-1$) along the grid. After $2n$ seconds, the drone is required to return exactly to the base station (Position 0). Let $s_j$ represent the drone's position at time $t=j$, such that $s_0 = s_{2n} = 0$ and $|s_j - s_{j-1}| = 1$ for all $j=1, \dots, 2n$.

Each possible flight path $\mathbf{v}$ consumes a total energy $q(\mathbf{v})$ calculated by the formula:
\[q(\mathbf{v}) = 1 + \sum_{j=1}^{2n-1} 3^{s_j}\]

The logistics company analyzes the efficiency of the drone by calculating $M(n)$, which is the arithmetic mean of the value $\frac{1}{q(\mathbf{v})}$ across all possible valid flight paths $\mathbf{v}$.

Evaluate $M(2020)$.

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
