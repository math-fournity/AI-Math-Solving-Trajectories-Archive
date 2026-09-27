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

A high-security data vault uses a rotating encryption cycle based on $n = 100$ distinct digital states. To test the vault's resilience, a security consultant must select a set of $k$ unique access codes $\{a_1, a_2, \ldots, a_k\}$, where each code corresponds to one of the $100$ states. Because the states are distinct, no two chosen codes can have a difference divisible by 100.

For a specific system offset $m$ (where $1 \le m \le 100$), let $k(100, m)$ be the minimum number of codes the consultant must select to guarantee that at least one pair of codes $(a_p, a_s)$ in the set satisfies the "trigger condition": the sum of the offset and the first code, minus the second code, is exactly divisible by 100 (i.e., $m + a_p - a_s \equiv 0 \pmod{100}$).

The consultant performs this calculation for every possible integer offset $m$ from 1 to 100 inclusive. Calculate the total sum of all these minimum requirements: $\sum_{m=1}^{100} k(100, m)$.

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
