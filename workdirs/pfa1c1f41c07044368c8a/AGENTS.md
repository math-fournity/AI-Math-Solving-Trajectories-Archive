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

In a remote industrial manufacturing zone, a specialized production cycle is defined by a sequence of energy outputs recorded at $2n-1$ discrete intervals, where $n \geq 2$. The energy output at the $j$-th interval is denoted by $a_j$. The cycle is deemed "Symmetric Peak" if there exists a constant adjustment factor $k$ such that the initial output $a_1$ is exactly $1$ unit, the output increases by $k$ units at each step for the first $n-1$ transitions (so $a_{j+1} - a_j = k$ for $1 \leq j \leq n-1$), and then decreases by $k$ units at each step for the remaining $n-1$ transitions (so $a_{j+1} - a_j = -k$ for $n \leq j \leq 2n-2$).

An efficiency expert evaluates these cycles using a performance function $P(x) = \sum_{j=1}^{2n-1} a_j x^j$. A specific adjustment factor $k$ is classified as "Stable" if there exists a Symmetric Peak cycle using that $k$ such that the performance function evaluates to zero when the input $x$ is $-3$ (i.e., $P(-3) = 0$).

Let $S$ be the sum of all Stable values of $k$ that satisfy the condition $k \geq 5$ or $k \leq 3$. Given that $S$ can be expressed as a fraction $b/c$ in lowest terms, where $b$ and $c$ are relatively prime positive integers, calculate the value of $b+c$.

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
