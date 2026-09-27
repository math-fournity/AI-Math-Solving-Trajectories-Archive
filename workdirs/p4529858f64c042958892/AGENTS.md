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

In a specialized logistics warehouse, there are 10 distinct cargo containers labeled with the integers from 1 to 10. These containers must be processed one by one in a specific sequence, forming a permutation of the set $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$.

The warehouse tracks a "cumulative load factor" throughout the processing sequence. If the containers are processed in the order $[a_1, a_2, \dots, a_{10}]$, the load factor after the $k$-th step is the product of all container labels processed up to that point ($a_1 \cdot a_2 \cdot \dots \cdot a_k$).

For every step $k$ in the sequence (from $k=1$ to $10$), the warehouse incurs a "storage fee." The fee for a single step is calculated by taking the cumulative load factor at that step, dividing it by 100, and rounding down to the nearest integer. The total cost for a specific sequence is the sum of these 10 individual fees.

Let $M$ be the minimum possible total cost achievable across all possible permutations of the 10 containers. How many different permutations of $\{1, 2, \dots, 10\}$ result in this minimum total cost $M$?

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
