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

The boundary and initial conditions are\n\nu(0, y, z) = 0, \quad u(a, y, z) = 0\n\nu(x, 0, z) = 0, \quad u(x, b, z) = 0\n\nu(x, y, 0) = 0, \quad u(x, y, c) = f(x, y)\n\nThe conditions X(0) = Y(0) = Z(0) = 0 give c_1 = c_3 = c_5 = 0. The conditions X(a) = 0 and Y(b) = 0 yield two sets of eigenvalues:\n\n\alpha = \frac{m\pi}{a}, \quad m = 1, 2, 3, \ldots \quad \text{and} \quad \beta = \frac{n\pi}{b}, \quad n = 1, 2, 3, \ldots\n\nBy the Superposition Principle\n\nu(x, y, t) = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{mn} \sinh \omega_{mn} z \sin \frac{m\pi}{a} x \sin \frac{n\pi}{b} y\n\nwhere\n\n\omega_{mn}^2 = \frac{m^2 \pi^2}{a^2} + \frac{n^2 \pi^2}{b^2}\n\nand\n\nA_{mn} = \frac{4}{ab \sinh \omega_{mn} c} \int_0^b \int_0^a f(x, y) \sin \frac{m\pi}{a} x \sin \frac{n\pi}{b} y \, dx \, dy

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
