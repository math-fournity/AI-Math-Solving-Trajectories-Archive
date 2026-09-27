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

In the competitive world of high-frequency trading, a financial signal $r$ is classified as "stable" if there exist two distinct trading frequencies $z_1$ and $z_2$ on the unit circle of the complex volatility plane (meaning $|z_1|=|z_2|=1$) that satisfy a specific equilibrium condition. To ensure market diversity, these frequencies cannot be the exact polar opposites $\{ -i, i \}$.

The equilibrium condition is reached when the "yield function" of both frequencies is identical. The yield function for a frequency $z$ is defined by the expression $z(z^3 + z^2 + rz + 1)$. Therefore, $r$ is stable if and only if:
\[ z_1(z_1^3+z_1^2+rz_1+1)=z_2(z_2^3+z_2^2+rz_2+1) \]
for some $z_1 \neq z_2$ where $|z_1|=|z_2|=1$ and $\{z_1, z_2\} \neq \{-i, i\}$.

Market analysts have determined that a real-valued signal $r$ is stable if and only if it falls within a specific range $a < r \le b$.

If the sum of the absolute values of the boundaries, $|a| + |b|$, is expressed as a reduced fraction $\frac{p}{q}$ (where $p$ and $q$ are relatively prime positive integers), calculate the final verification code $100p + q$.

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
