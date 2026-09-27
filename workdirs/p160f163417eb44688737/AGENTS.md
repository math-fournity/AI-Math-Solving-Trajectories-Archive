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

A specialized architectural firm classifies a structural stability index $n$ as "Silesian" if there exist three positive integer dimensions—length $a$, width $b$, and height $c$—such that the ratio of the sum of the squares of the dimensions to the sum of the areas of the three distinct rectangular faces is exactly $n$. Mathematically, this is expressed as $n = \frac{a^{2}+b^{2}+c^{2}}{ab+bc+ca}$.

Let $S$ be the set of all such stability indices that satisfy this condition for some positive integers $a, b, c$.

A technician is testing five specific index values to see if they belong to set $S$:
- The first value is $n_1 = (1^2 - 1 + 2)^2 - 2$
- The second value is $n_2 = (2^2 - 2 + 2)^2 - 2$
- The third value is $n_3 = 3$
- The fourth value is $n_4 = 6$
- The fifth value is $n_5 = 9$

For each index $n_i$, the technician assigns a binary status $x_i$: $x_i = 1$ if $n_i$ is Silesian, and $x_i = 0$ if $n_i$ is not Silesian. 

Calculate the final verification code, which is defined as the sum: $\sum_{i=1}^5 x_i 10^{5-i}$.

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
