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

In the city of Metros, the Department of Energy monitors two distinct power grids, represented by the continuous functions $P(t)$ and $Q(t)$, where $t$ is time. These grids are considered "Load-Equivalent" if they satisfy a specific stability condition over a cycle of $N=5$ work-weeks.

Each work-week $i$ (where $i \in \{1, 2, 3, 4, 5\}$) consists of exactly 2015 individual hours. Specifically, the $i$-th week covers the time intervals $t$ from $2015i - 2014$ to $2015i$.

The stability condition requires that for every week $i$, the set of 2015 hourly output values recorded by grid $P$—specifically $\{P(2015i), P(2015i-1), \ldots, P(2015i-2014)\}$—must contain exactly the same values as the set of 2015 hourly output values recorded by grid $Q$—specifically $\{Q(2015i), Q(2015i-1), \ldots, Q(2015i-2014)\}$. In other words, for each week, the sequence of outputs for $Q$ is simply a rearrangement of the outputs for $P$.

If $P(t)$ and $Q(t)$ are distinct polynomial functions of time with real coefficients that are Load-Equivalent for these $N=5$ weeks, what is the minimum possible degree $d_{min}$ that these polynomials can have?

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
