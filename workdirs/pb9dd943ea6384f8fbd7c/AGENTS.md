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

A high-tech manufacturing firm uses a central server to manage industrial codes. The set $S$ consists of every positive integer that is a divisor of $6000$. To run a specific simulation, the server’s security protocol must randomly select four codes $(a, b, c, d)$ from the set $S$, where each code is chosen independently and with replacement.

The simulation will only initialize successfully if the chosen quadruple satisfies a specific "Balance Condition" regarding their shared and combined properties. Specifically, let $G_{1}$ be the greatest common divisor of the first two codes $(a, b)$, and let $G_{2}$ be the greatest common divisor of the last two codes $(c, d)$. Furthermore, let $L_{1}$ be the least common multiple of the first two codes $(a, b)$, and let $L_{2}$ be the least common multiple of the last two codes $(c, d)$. 

The Balance Condition is met if the least common multiple of $G_{1}$ and $G_{2}$ is exactly equal to the greatest common divisor of $L_{1}$ and $L_{2}$. 

What is the probability that a randomly selected quadruple $(a, b, c, d) \in S^4$ satisfies this Balance Condition? If the probability is expressed as an irreducible fraction $\frac{a}{b}$, calculate the value of $a+b$.

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
