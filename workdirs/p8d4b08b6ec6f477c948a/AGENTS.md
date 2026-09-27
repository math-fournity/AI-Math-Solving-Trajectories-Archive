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

In a futuristic data center, a network architect is evaluating the efficiency of a system containing $n$ distinct processing nodes, where $n$ can be any positive integer. Each node $i$ is assigned a unique positive integer identifier, $k_i$.

The architect monitors three specific performance metrics of the network:
1.  **The Connectivity Index:** The sum of the reciprocals of the node identifiers, $\sum_{i=1}^n \frac{1}{k_i}$.
2.  **The Kinetic Potential:** The sum of the values $\sqrt{k_i^6 + k_i^3}$ for each node.
3.  **The System Load:** The square of the sum of the node identifiers, $(\sum_{i=1}^n k_i)^2$.

The "Operational Stability" of the system is defined as the product of the Connectivity Index and the Kinetic Potential, minus the System Load. Engineering protocols require that for any choice of node identifiers, the Operational Stability must always be greater than or equal to a baseline value. This baseline is calculated as the product of a constant factor $\lambda$, the square of the number of nodes ($n^2$), and the variance-like term $(n^2 - 1)$.

Formally, the stability requirement is expressed by the inequality:
\[ \left( \sum_{i=1}^n \frac{1}{k_i} \right) \left( \sum_{i=1}^n \sqrt{k_i^6 + k_i^3} \right) - \left( \sum_{i=1}^n k_i \right)^2 \geq \lambda n^2(n^2 - 1) \]

Find the maximum possible value of the constant $\lambda$ such that this inequality holds true for all possible sets of distinct positive integers $\{k_1, k_2, \dots, k_n\}$ and all positive integers $n$.

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
