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

In the city-state of Numeria, a master architect is designing a logistical network for 16 distinct supply hubs, indexed $1, 2, \dots, 16$. Each hub must be assigned a "Capacity Rating" from a registry of 243 possible levels, represented by the integers $\{1, 2, \dots, 243\}$. Let $f(n)$ denote the Capacity Rating assigned to hub $n$.

The Grand Council has imposed four strict zoning regulations for the network:
1.  **Foundation Rule:** Hub 1 must have a Capacity Rating of exactly 1.
2.  **Quadratic Scaling Rule:** For any hub index that is a perfect square, $n^2$, its rating must satisfy $f(n^2) = n^2 f(n)$.
3.  **Efficiency Rule:** Every hub's rating must be a multiple of its own index (i.e., $n$ divides $f(n)$).
4.  **Redundancy Rule:** For any two hubs $m$ and $n$, the product of the ratings of their least common multiple hub and their greatest common divisor hub must equal the product of the ratings of hubs $m$ and $n$.

Let $S$ be the set of all possible valid configurations of Capacity Ratings for these 16 hubs. Suppose the total number of valid configurations, $|S|$, is expressed as a prime factorization $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_k^{e_k}$, where the $p_i$ are distinct prime numbers.

Calculate the value of the sum $p_1 e_1 + p_2 e_2 + \ldots + p_k e_k$.

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
