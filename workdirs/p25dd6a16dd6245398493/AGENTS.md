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

In a remote digital archipelago, a network administrator named Alice and her colleague Bob are managing a series of square server clusters. There are 36 distinct clusters in total, ranging in size from $1 \times 1$ to $6 \times 6$. For every possible pair of integers $(m, n)$ where $1 \le m \le 6$ and $1 \le n \le 6$, there is exactly one $n \times n$ cluster designated for a specific maintenance task involving $m \times m$ blocks.

Alice and Bob play a competitive resource-allocation game on each cluster individually. Starting with a completely unallocated $n \times n$ grid of processing nodes, they take turns (Alice always goes first) performing one of two possible operations:
1. They can occupy a contiguous, completely unallocated $m \times m$ square block of nodes.
2. They can occupy a single, unallocated node anywhere in the grid.

The last player to perform an allocation wins the game on that specific cluster, or equivalently, a player loses if all nodes are occupied or if the remaining unallocated nodes cannot form a single node allocation (which is impossible until the grid is full). Both Alice and Bob use an optimal strategy to ensure they win whenever mathematically possible.

For each pair $(m, n)$, let the value $f(m, n) = 1$ if Alice wins the game on that $n \times n$ cluster using the $m \times m$ block rule, and $f(m, n) = 0$ if Bob wins.

Calculate the total number of clusters in which Alice wins. That is, find the value of:
$$\sum_{m=1}^{6} \sum_{n=1}^{6} f(m,n)$$

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
