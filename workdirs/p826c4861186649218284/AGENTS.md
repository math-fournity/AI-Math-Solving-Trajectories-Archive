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

In the remote digital archipelago of Zentopia, a master architect is designing a multi-layered security protocol. The protocol depends on a specific "Master Key" denoted as $k$, where $k$ is a positive integer.

To ensure the system's stability, the architect requires that for every possible configuration of three security nodes with power levels $x, y,$ and $z$—where these levels are integers constrained by the rule $1 \leq x \leq y \leq z \leq 121$—the "Compatibility Index" must always result in a whole number. 

The Compatibility Index for any three nodes is calculated by the formula:
$$k \times \frac{\text{Greatest Common Divisor}(x, y) \times \text{Greatest Common Divisor}(y, z)}{\text{Least Common Multiple}(x, y^2, z)}$$

The Master Key $k$ is defined as the smallest positive integer that satisfies this condition for every valid combination of $x, y,$ and $z$.

Once $k$ is determined, the architect calculates a secondary value, $k'$, which represents the total number of divisors of $k$. To finalize the system's encryption depth, find the total number of divisors of $k'$.

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
