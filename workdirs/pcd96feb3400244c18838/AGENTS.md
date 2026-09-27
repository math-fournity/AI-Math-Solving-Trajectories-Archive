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

Let \( \triangle ABC \) be a triangle such that \( AB = AC = 182 \) and \( BC = 140 \). Let \( X_1 \) lie on \( AC \) such that \( CX_1 = 130 \). Let the line through \( X_1 \) perpendicular to \( BX_1 \) at \( X_1 \) meet \( AB \) at \( X_2 \). Define \( X_2, X_3, \ldots \), as follows: for \( n \) odd and \( n \geq 1 \), let \( X_{n+1} \) be the intersection of \( AB \) with the perpendicular to \( X_{n-1}X_n \) through \( X_n \); for \( n \) even and \( n \geq 2 \), let \( X_{n+1} \) be the intersection of \( AC \) with the perpendicular to \( X_{n-1}X_n \) through \( X_n \). Find \( BX_1 + X_1X_2 + X_2X_3 + \ldots \). If the answer is of the form of an irreducible fraction $\frac{a}{b}$, compute the value of $a + b$.

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
