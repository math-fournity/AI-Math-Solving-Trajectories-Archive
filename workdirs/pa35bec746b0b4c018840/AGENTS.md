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

A high-security data vault contains a total set of $A$ encrypted digital keys. To ensure redundancy and security, a security firm creates $n$ specific access bundles, $A_1, A_2, \dots, A_n$, each containing a subset of these keys. The system is designed with the following technical specifications:

1. Each of the $n$ bundles contains exactly $k$ keys. This bundle size $k$ is strictly greater than half the total number of keys in the vault ($k > |A|/2$).
2. The system is highly redundant: for any two distinct keys $a$ and $b$ in the vault, there must be at least three distinct bundles $A_r, A_s,$ and $A_t$ ($1 \leq r < s < t \leq n$) that both contain both keys.
3. To prevent excessive overlap and potential data leaks, any two distinct bundles $A_i$ and $A_j$ ($1 \leq i < j \leq n$) are permitted to have at most 3 keys in common ($|A_i \cap A_j| \leq 3$).

The firm wishes to maximize the bundle size $k$ relative to the other constraints of the system. Determine all possible values for the total number of bundles $n$ such that $k$ attains its maximum possible value among all such valid configurations.

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
