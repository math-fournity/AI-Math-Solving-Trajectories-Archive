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

A specialized cryptography department is designing a new security protocol for data packets. For a given network size $n$ (where $n$ is a positive integer), the department assigns a unique identification rank from the set $\{1, 2, \ldots, n\}$ to each of the $n$ nodes in the network.

To generate a sequence of security keys, the engineers must arrange these $n$ nodes into a specific transmission order $(a_1, a_2, \ldots, a_n)$, such that each rank appears exactly once. For each step $k$ (from $1$ to $n$), a "cumulative verification value" $P_k$ is calculated by multiplying the ranks of the first $k$ nodes in the sequence: $P_k = a_1 \times a_2 \times \cdots \times a_k$.

The protocol is considered "balanced" if and only if the sequence of these $n$ cumulative values $(P_1, P_2, \ldots, P_n)$, when taken modulo $n$, results in a set containing every possible remainder from $0$ to $n-1$.

Let $S$ be the set of all network sizes $n$ for which such a balanced protocol can be successfully constructed. Calculate the sum of all integers in $S$ that are less than or equal to 50.

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
