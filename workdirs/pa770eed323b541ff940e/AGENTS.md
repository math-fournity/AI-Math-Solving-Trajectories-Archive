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

A prestigious international culinary academy has established a unique scoring system for its annual masterclass series. The series consists of $n$ consecutive lessons. In each lesson $m$ (where $m=1, 2, \dots, n$), a student earns a "mastery credit" equal to exactly $1/m$ points.

At the end of $n$ lessons, a student’s total score is calculated as the sum of all credits earned: $\sum_{m=1}^n 1/m$. To record these scores in the academy’s ledger, the total must be written as a simplified fraction $p_n/q_n$, where $p_n$ and $q_n$ are positive integers with no common factors greater than 1.

The academy grants a "Purity Certification" for a given series length $n$ only if the denominator $q_n$ of the final score is not divisible by 5. 

Let $S$ be the set containing every positive integer $n$ for which a series of that length qualifies for the Purity Certification. Calculate the sum of all elements in the set $S$.

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
