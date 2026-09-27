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

A logistics company operates two separate automated conveyor belts, Line A and Line B. Every time a sensor is triggered on Line A, it randomly assigns a weight $a_i$ to a package, where $a_i$ is chosen independently and uniformly from the integer set $\{0, 1, 2, \ldots, 100\}$. Simultaneously, every time a sensor is triggered on Line B, it assigns a weight $b_j$ to a package, where $b_j$ is also chosen independently and uniformly from the integer set $\{0, 1, 2, \ldots, 100\}$.

The lines run continuously, generating sequences $a_1, a_2, \ldots$ and $b_1, b_2, \ldots$. A digital monitor tracks the cumulative weight of packages processed on each line. Let $S_A(m) = \sum_{i=1}^{m} a_i$ be the total weight on Line A after $m$ packages, and $S_B(n) = \sum_{j=1}^{n} b_j$ be the total weight on Line B after $n$ packages.

An alarm is programmed to trigger the first time a non-zero cumulative weight is reached by both lines. Specifically, we look for the smallest non-negative integer $s$ such that there exist positive integers $m$ and $n$ satisfying $s = S_A(m) = S_B(n)$.

Compute the expected value of this smallest shared weight $s$.

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
