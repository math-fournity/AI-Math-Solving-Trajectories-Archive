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

In the high-tech city of Parity, a logistics supervisor and a data analyst are testing a new power grid involving $n$ unique energy cells, labeled $1, 2, \ldots, n$, where $n$ is an even positive integer.

The supervisor (Player 1) must first organize all $n$ cells into $n/2$ distinct bundles, with each bundle containing exactly two cells. Once the bundles are locked in, the analyst (Player 2) inspects each bundle and selects exactly one cell from each to activate. The goal of the analyst is to ensure that the total energy output—the sum of the labels on the $n/2$ selected cells—is exactly divisible by $n$.

If the analyst can choose a cell from each bundle such that the sum is a multiple of $n$, the analyst wins the round. Otherwise, if the supervisor has arranged the bundles in such a way that no matter which cells the analyst picks, the sum is never a multiple of $n$, the supervisor wins.

Let $S$ be the set of all even integers $n$ in the range $1 \leq n \leq 100$ for which the analyst has a guaranteed winning strategy, assuming both participants play with perfect mathematical foresight.

Find the sum of all elements in $S$.

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
