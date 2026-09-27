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

In a highly secure digital vault, the access protocol is governed by a prime modulus $p = 1,000,000,007$. Scientists have identified a specific set of "Primary Keys," which are all prime numbers $p_1, p_2, \dots, p_m$ strictly less than $\sqrt[4]{\frac{1}{2}p}$, ordered from smallest to largest.

For each Primary Key $p_i$, there exists a unique "Inverse Token" $q_i$ (where $0 < q_i < p$) such that the product $p_i \times q_i$ leaves a remainder of $1$ when divided by $p$. These Inverse Tokens form the foundational security set $S = \{q_1, q_2, \dots, q_m\}$.

To test the system's vulnerability, a security auditor generates a "Transformed Set" $T_{a,b}$ based on two secret tuning parameters, $a$ and $b$ (integers such that $0 < a, b < p$). This set is created by taking each Inverse Token $q_i$, calculating $(a \cdot q_i + b)$, and finding the remainder after division by $p$. Thus, $T_{a,b} = \{ (a q_1 + b) \pmod p, (a q_2 + b) \pmod p, \dots, (a q_m + b) \pmod p \}$.

The vulnerability of the vault is defined by $N$, the maximum possible number of overlapping elements between the foundational set $S$ and the transformed set $T_{a,b}$ across all possible choices of $a$ and $b$.

Find $N$.

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
