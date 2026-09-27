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

In a specialized logistics hub, there are four secure storage vaults identified by the unique positive integer ID numbers $a_1, a_2, a_3, a_4$. These vaults are designed with a specific security constraint: it is impossible to arrange all four vaults in a physical circle such that every pair of adjacent vaults has a greatest common divisor (GCD) of their IDs equal to 1.

The facility’s automated auditing system tracks specific "power-link" relationships between triples of these vaults. An ordered triple of distinct vaults $(i, j, k)$—where $i, j, k \in \{1, 2, 3, 4\}$ and no two indices are the same—is classified as a "Power-Link Triple" if the square of the greatest common divisor of IDs $a_i$ and $a_j$ is a mathematical divisor of ID $a_k$.

Given that the four vault IDs strictly satisfy the circular adjacency constraint mentioned above, what is the maximum possible number of such ordered Power-Link Triples that can exist within this set of four vaults?

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
