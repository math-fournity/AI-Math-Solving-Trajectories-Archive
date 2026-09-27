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

In a remote industrial network, three specialized filtration units—Unit X, Unit Y, and Unit Z—operate under a strict synchronization protocol. The efficiency levels of these units ($x, y, z$) are non-zero real numbers that are perpetually constrained by the "Balance Law": twice the product of their efficiencies must equal the sum of their efficiencies ($2xyz = x+y+z$).

A central monitoring software, defined by a polynomial function $P$ with real coefficients, tracks the system's performance. The software's "Global Stress Index" is calculated by two different diagnostic methods that must always yield the same result:

1.  **The Distributed Load Method**: Summing the software's output for each unit’s efficiency, where each output is scaled down by the product of the other two units' efficiencies. That is: $\frac{P(x)}{yz} + \frac{P(y)}{zx} + \frac{P(z)}{xy}$.
2.  **The Differential Impact Method**: Summing the software's output based on the relative efficiency gaps between the units. That is: $P(x-y) + P(y-z) + P(z-x)$.

The system designers have noted that when the efficiency of a unit is at a zero-baseline, the software returns a constant safety value of $P(0) = 3$.

Let $S$ be the sum of the values of $P(1)$ for every possible polynomial $P$ that satisfies these operational conditions for all valid efficiency levels $x, y, z$. Compute $S$.

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
