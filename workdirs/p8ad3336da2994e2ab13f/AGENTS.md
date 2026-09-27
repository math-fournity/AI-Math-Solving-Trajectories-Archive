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

A specialized chemical refinery processes a sequence of $n$ raw material batches, where each batch $j$ has a purity level denoted by $a_j > 0$. The total energy consumption of the facility is determined by the sum of the fourth powers of these purity levels: $\sum_{j=1}^{n} a_{j}^{4}$.

The refinery also utilizes a secondary set of catalysts with efficiency ratings $b_1, \ldots, b_n > 0$. For every production stage $k$ (where $1 \leq k \leq n$), the facility generates a "yield value" and a "stability factor":
1. The **Stage Yield** is calculated by a convolution of purity levels and catalysts: $\sum_{j=1}^{k} a_{j} b_{k+1-j}$.
2. The **Stage Stability** is calculated using the catalyst ratings and a factorial growth component: $\sum_{j=1}^{k} b_{j}^{2} j!$.

The refinery’s safety protocol dictates that the total energy consumption must always be greater than or equal to a constant $c$ times the sum over all stages $k$ of the ratio of the fourth power of the Stage Yield to the square of the Stage Stability.

Determine the largest possible value of $c > 0$ such that the following safety inequality holds for any number of batches $n$ and any positive values of $a_j$ and $b_j$:

\[ \sum_{j=1}^{n} a_{j}^{4} \geq c \sum_{k=1}^{n} \frac{\left(\sum_{j=1}^{k} a_{j} b_{k+1-j}\right)^{4}}{\left(\sum_{j=1}^{k} b_{j}^{2} j!\right)^{2}} \]

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
