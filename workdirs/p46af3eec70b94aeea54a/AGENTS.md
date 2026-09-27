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

The Legendre polynomials can be defined as the coefficients of the expansion into a power series [VI 91]\n\n\[\n\frac{1}{\sqrt{1 - 2zx + z^2}} = \frac{P_0(x)}{z} + \frac{P_1(x)}{z^2} + \frac{P_2(x)}{z^3} + \cdots + \frac{P_n(x)}{z^{n+1}} + \cdots.\n\]\n\nDeduce from this Laplace's formula (VI 86)\n\n\[\nP_n(x) = \frac{1}{\pi} \int_{-1}^{1} \left( x + \alpha \sqrt{x^2 - 1} \right)^n \frac{d\alpha}{\sqrt{1 - \alpha^2}}\n\]\n\nand the Dirichlet-Mehler formula\n\n\[\nP_n(\cos \vartheta) = \frac{2}{\pi} \int_{0}^{\vartheta} \frac{\cos(n + \tfrac{1}{2}) t}{\sqrt{2 (\cos t - \cos \vartheta)}} \, dt = \frac{2}{\pi} \int_{\vartheta}^{\pi} \frac{\sin(n + \tfrac{1}{2}) t}{\sqrt{2 (\cos \vartheta - \cos t)}} \, dt,\n\]\n\n\[\n0 < \vartheta < \pi.\n\]\n\n(The square roots are positive.)

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
