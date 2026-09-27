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

A specialized chemical refinery uses two reactors to process a compound. The efficiency of the first reactor is determined by the ratio $E_1 = \frac{a}{a + \lambda b}$ and the efficiency of the second reactor is $E_2 = \frac{b}{b + \lambda a}$, where $a$ and $b$ represent the positive flow rates of two catalyst types and $\lambda$ is a positive tuning parameter for the system.

The refinery monitors the "Total Energy Output," defined as the sum of the squares of these efficiencies: $E_1^2 + E_2^2$.

Engineers have observed two distinct operational phases based on the value of $\lambda$:
1. In the "Stable Phase," the Total Energy Output is always greater than or equal to the baseline value $\frac{2}{(1+\lambda)^2}$ for any choice of flow rates $a, b > 0$. The set of all parameters $\lambda$ that satisfy this condition is $S_1 = [\lambda_1, \infty)$.
2. In the "Limited Phase," the Total Energy Output is always less than or equal to the same baseline value $\frac{2}{(1+\lambda)^2}$ for any choice of flow rates $a, b > 0$. The set of all parameters $\lambda$ that satisfy this condition is $S_2 = (0, \lambda_2]$.

Calculate the final system calibration constant defined by the expression $10\lambda_1 + \lambda_2^2 + 2\lambda_2$.

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
