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

A specialized deep-sea research facility operates a sequence of $n$ modular filtration units. Each unit $i$ has an internal capacity $a_i$, where $a_i$ is a positive integer. The total pressure resistance of the system at any external depth setting $x$ is determined by the product of the individual unit tolerances: $f(x) = (x + a_1)(x + a_2) \cdots (x + a_n)$.

The facility's structural integrity is measured by the "Stability Index" relative to a specific prime thermal constant $p$. For any integer depth $N$, the Stability Index is defined as $v_p(N)$, which is the largest non-negative integer $t$ such that $p^t$ divides $N$.

The Chief Engineer needs to establish a safety protocol based on a "Pressure Jump" constant $m$, which is a positive integer. This constant must be large enough so that, regardless of how the individual capacities $a_1, \ldots, a_n$ are chosen and regardless of the current non-negative integer depth setting $k$, there will always exist an alternative non-negative integer depth setting $k'$ that results in a strictly higher Stability Index, but one that does not exceed the current index by more than $m$.

Mathematically, for any chosen set of positive integers $\{a_1, \ldots, a_n\}$ and any non-negative integer $k$, there must exist a non-negative integer $k'$ such that:
\[v_p(f(k)) < v_p(f(k')) \leq v_p(f(k)) + m\]

Find the minimum value of the constant $m$ that satisfies this requirement for all possible configurations of $a_i$.

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
