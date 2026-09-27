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

In a specialized thermodynamics laboratory, three distinct pressure readings, measured in kilopascals, are recorded as $a$, $b$, and $c$. These three values are the real roots of the characteristic system equation $x^3 - 3x^2 - 7x - 1 = 0$.

An engineer is calculating the "Resonance Coefficient" ($\Omega$) of the system, which is defined by the relationship between the cube roots of these pressure readings:
\[\Omega = \left( \dfrac{1}{\sqrt[3]{a}-\sqrt[3]{b}} + \dfrac{1}{\sqrt[3]{b}-\sqrt[3]{c}} + \dfrac{1}{\sqrt[3]{c}-\sqrt[3]{a}} \right)^2\]

After simplifying the expression, the engineer determines that the value of $\Omega$ can be expressed in the exact form $\frac{p\sqrt[3]{q}}{r}$, where $p$, $q$, and $r$ are positive integers such that the greatest common divisor of $p$ and $r$ is 1, and $q$ contains no factor that is a perfect cube of a prime.

Find the value of $100p + 10q + r$.

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
