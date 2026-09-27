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

Let \( \triangle ABC \) be a triangle with \( BC = 13 \), \( CA = 11 \), \( AB = 10 \). Let \( A_1 \) be the midpoint of \( BC \). A variable line \(\ell\) passes through \( A_1 \) and meets \( AC, AB \) at \( B_1, C_1 \). Let \( B_2, C_2 \) be points such that \( B_2B = B_2C \), \( B_2C_1 \perp AB \), \( C_2B = C_2C \), \( C_2B_1 \perp AC \), and define \( P = BB_2 \cap CC_2 \). Suppose the circles of diameters \( BB_2, CC_2 \) meet at a point \( Q \neq A_1 \). Given that \( Q \) lies on the same side of line \( BC \) as \( A \), the minimum possible value of \(\frac{PB}{PC} + \frac{QB}{QC}\) can be expressed in the form \(\frac{a \sqrt{b}}{c}\) for positive integers \( a, b, c \) with \(\gcd(a, c) = 1\) and \( b \) squarefree. Determine \( a + b + c \).

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
