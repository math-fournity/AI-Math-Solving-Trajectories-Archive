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

In the circular city of Modulo-100, there are 100 designated delivery hubs arranged in a perfect circle, indexed from 0 to 99. The city council decides to grant a "Primary Franchise" to a delivery company by allowing them to select a set $A$ of exactly 10 hubs to build their main warehouses.

To ensure competition, the council dictates that regardless of which 10 hubs the company chooses for $A$, there must exist a strategy for a secondary company. This second company must choose a set $B$ of exactly 10 hubs to serve as distribution centers. The council is interested in the total coverage of the city, defined as the number of unique hub locations reachable by the sum of one warehouse location $a \in A$ and one distribution center location $b \in B$, calculated under the city's circular indexing (modulo 100).

Let $k$ be the largest guaranteed number of unique covered locations. That is, $k$ is the minimum possible value such that for any choice of $A$ with 10 elements, one can always find a set $B$ with 10 elements such that the set $\{a+b \pmod{100} : a \in A, b \in B\}$ contains at least $k$ distinct values.

Find the largest integer $m$ such that the existence of this $k$ proves $k \ge m$.

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
