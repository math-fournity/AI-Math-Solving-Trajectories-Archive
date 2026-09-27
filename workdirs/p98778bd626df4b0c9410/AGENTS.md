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

The Bank of Oslo produces coins made of aluminum (A) and bronze (B). Martin arranges $2 n$ coins, $n$ of each type, in a line in an arbitrary order. Then he fixes $k$ as an integer between 1 and $2 n$ and applies the following process: he identifies the longest sequence of consecutive coins of the same type that contains the $k$-th coin from the left, and moves all the coins in this sequence to the left of the line. For example, with $n=4, k=4$, we can have the sequence of operations
$$
A A B \underline{B} B A B A \rightarrow B B B \underline{A} A A B A \rightarrow A A A \underline{B} B B B A \rightarrow B B B \underline{B} A A A A
$$
We say that a pair $(n, k)$ is "stable" if for any initial configuration, the $n$ coins on the left are of the same type after a finite number of steps. Let $S_n$ be the set of all integers $k$ such that $(n, k)$ is stable. Find the sum of all elements in $S_{10}$ and $S_{11}$.

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
