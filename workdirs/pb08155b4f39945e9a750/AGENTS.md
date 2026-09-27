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

A high-security vault uses digital access codes consisting of a set $A$ of unique identification numbers chosen from the registry $\{1, 2, \cdots, 2014\}$. To maintain system stability, the security protocol evaluates "activation triplets." A triplet consists of three ID numbers $x_1, x_2, x_3$ from the set $A$ and three corresponding polarity coefficients $\lambda_1, \lambda_2, \lambda_3$ assigned to them. 

The protocol defines the following constraints for these triplets:
(i) Each polarity coefficient $\lambda_i$ must be chosen from the set $\{-1, 0, 1\}$, and at least one coefficient must be non-zero.
(ii) If the same ID number is used more than once in a triplet (e.g., $x_i = x_j$), their assigned polarities must not be opposites (i.e., their product $\lambda_i \lambda_j$ cannot be $-1$).

The vault remains "secure" if the set $A$ satisfies two safety conditions for every possible triplet and valid polarity assignment:
1. The product of the three IDs, $x_1 x_2 x_3$, is never a multiple of 2014.
2. The weighted sum of the IDs, $\lambda_1 x_1 + \lambda_2 x_2 + \lambda_3 x_3$, is never a multiple of 2014.

The set $A$ is classified as a "Good Configuration" if it maintains these security conditions. What is the maximum number of identification numbers that can be included in a "Good Configuration" $A$?

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
