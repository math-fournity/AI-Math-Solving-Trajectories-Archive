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

In the city of Centuria, there are exactly $n = 100$ districts arranged in a circular perimeter, labeled $1, 2, \ldots, 100$. For any index $i$ greater than 100, the district $i$ refers back to district $i \pmod{100}$ (specifically, $a_{100+i} = a_i$ for all $i \geq 1$).

Each district $i$ is assigned a positive integer security clearance level, $a_i$. These levels must adhere to a strict bureaucratic hierarchy and a localized access constraint:

1.  The clearance levels must be non-decreasing across the districts, but the final district's level cannot exceed the first district's level by more than the total number of districts. That is: $a_1 \leq a_2 \leq \dots \leq a_{100} \leq a_1 + 100$.
2.  The "Recursive Access Rule" states that for every district $i$, the clearance level assigned to the district whose ID matches the value $a_i$ must not exceed the value of the current district's ID plus 99. Mathematically, $a_{a_i} \leq 100 + i - 1$ for all $i = 1, 2, \ldots, 100$.

The High Council wishes to calculate the total sum of clearance levels across all districts, defined as $\sum_{i=1}^{100} a_i$. Given all possible valid assignments of $a_i$, what is the maximum possible value that this sum can reach?

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
