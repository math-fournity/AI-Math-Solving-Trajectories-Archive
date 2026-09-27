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

A specialized cargo ship is designed to transport a sequence of $n$ shipping containers, where $n \geq 3$. Each container $k$ (for $k = 1, 2, \ldots, n$) must be assigned a weight $a_k$, which is restricted to being an integer value such that $1 \leq a_k \leq n$.

An engineer monitors the "instability shift" of the ship as each new container is loaded. Let $W_k$ be the average weight of the first $k$ containers, defined as $W_k = \frac{1}{k} \sum_{i=1}^k a_i$. The instability shift occurring at step $k$ (for $k = 1, \ldots, n-1$) is defined as the absolute difference between the average weight of the first $k+1$ containers and the average weight of the first $k$ containers, denoted as $\Delta_k = |W_{k+1} - W_k|$.

For each $k \in \{1, \ldots, n-1\}$, let $M_k$ represent the smallest possible value that $\Delta_k$ can take, provided that $\Delta_k > 0$, across all possible valid sequences of container weights. 

A sequence of weights $(a_1, a_2, \ldots, a_n)$ is classified as "perfectly balanced" if, for every $k$ from $1$ to $n-1$, the resulting instability shift $\Delta_k$ is exactly equal to $M_k$. 

Calculate the total number of unique perfectly balanced sequences of weights possible for a given $n$.

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
