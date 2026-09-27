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

In the competitive world of skyscraper architecture, a developer is testing a structural stability index, $k$, defined by the formula $k = \frac{x^2 - 7}{x^2 - y^2}$. In this model, $x$ and $y$ represent specific integer-based load-bearing coordinates. For the model to be valid, $k$ must result in a positive integer.

The engineering firm categorizes these stability indices into two distinct sets based on the primary load value $x$:

1.  **Set $A$** consists of all possible positive integer values of $k$ that can be produced using integer coordinates $(x, y)$ where the primary load $x$ is strictly greater than $\sqrt{7}$.
2.  **Set $B$** consists of all possible positive integer values of $k$ that can be produced using integer coordinates $(x, y)$ where the primary load $x$ is non-negative and strictly less than $\sqrt{7}$ (specifically $0 \leq x < \sqrt{7}$).

Detailed site surveys have already determined that the stability indices belonging to Set $B$ are exactly $\{1, 2, 4, 7\}$.

Based on this structural model, find the sum of all the distinct positive integers that belong to Set $A$.

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
