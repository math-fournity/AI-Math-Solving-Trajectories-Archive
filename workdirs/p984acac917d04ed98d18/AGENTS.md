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

In a specialized logistics warehouse, there are 100 designated storage bays, numbered $i = 1$ to $100$. A manager must distribute exactly 100 identical cargo crates among these bays, where $a_i$ represents the number of crates placed in bay $i$. Each $a_i$ must be a non-negative integer.

The placement of crates is subject to the following strict operational protocols:
1. There exists some positive integer threshold $k \leq 100$ such that the number of crates in the bays is non-decreasing up to bay $k$ (i.e., $a_1 \leq a_2 \leq \cdots \leq a_k$), and all bays after $k$ must remain empty ($a_i = 0$ for all $i > k$).
2. The total number of crates across all bays is exactly 100 ($\sum_{i=1}^{100} a_i = 100$).
3. The "weighted maintenance index" of the warehouse, calculated by multiplying each bay's number by the number of crates it holds, must equal exactly 2022 ($\sum_{i=1}^{100} i \cdot a_i = 2022$).

The manager's performance is evaluated based on the "total kinetic load" of the configuration. This load is calculated by multiplying the square of each bay's number by the number of crates in that bay ($\sum_{i=1}^{100} i^2 \cdot a_i$).

Find the minimum possible value of this total kinetic load.

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
