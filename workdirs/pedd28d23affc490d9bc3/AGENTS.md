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

In a remote industrial lab, three chemical catalysts—labeled $a, b,$ and $c$—are used in a pressurized reaction chamber. The concentration levels of these catalysts are represented by positive real numbers $a, b,$ and $c$. The stability of the system is governed by a specific regulatory constraint: the weighted sum of their individual squares and their pairwise interactions must equal a fixed limit. Specifically, the catalysts must satisfy the equation:
\[a^2 + b^2 + c^2 + k(ab + ac + bc) = 1 + k\]
where $k$ is a constant system parameter.

An efficiency inspector monitors the "resistance" of the mixture. The total resistance of the system is calculated by summing the internal stress between each pair of catalysts. The stress between two catalysts is defined as the reciprocal of the difference between $1$ and the square of their average concentration. For the system to be considered safe, the total resistance must not exceed $4.5$ units:
\[\frac{1}{1-\left(\frac{a+b}{2}\right)^2} + \frac{1}{1-\left(\frac{b+c}{2}\right)^2} + \frac{1}{1-\left(\frac{c+a}{2}\right)^2} \le \frac{9}{2}\]

Determine the largest possible value of the parameter $k$ such that the safety condition is guaranteed to hold for all valid positive concentrations $a, b,$ and $c$.

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
