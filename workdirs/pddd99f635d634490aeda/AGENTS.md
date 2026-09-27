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

The solution of the boundary-value problem\n\n\left\{\n\begin{aligned}\n  & -\frac{\partial p}{\partial x} = \frac{\partial w}{\partial t}, \\\n  & -\frac{\partial p}{\partial t} = \lambda^2 \frac{\partial w}{\partial x}\n\end{aligned}\n\right\} \n\quad 0 < x < l, \quad 0 < t < +\infty,\n\n\begin{aligned}\n    &w(0, t) = \phi(t), \quad p(l, t) = 0, \quad 0 < t < +\infty, \\\n    &w(x, 0) = 0, \quad p(x, 0) = 0, \quad 0 < x < l\n\end{aligned}\n\nhas the form\n\nw(x, t) = \sum_{n=1}^{+\infty} \left[ \tilde{\phi} \left( t - \frac{x + 2nl}{\lambda} \right) - \tilde{\phi} \left( t + \frac{x - 2nl}{\lambda} \right) \right] (-1)^n + \tilde{\phi} \left( t - \frac{x}{\lambda} \right).\n\nwhere\n\n\tilde{\phi}(t) = \n\begin{cases} \n0, & -\infty < t < 0, \\\n\phi(t), & 0 < t < +\infty, \n\end{cases}\n\nand\n\np(x, t) = \lambda \tilde{\phi} \left( t - \frac{x}{\lambda} \right) + \lambda \sum_{n=1}^{+\infty} (-1)^n \left\{ \tilde{\phi} \left( t - \frac{x + 2n l}{\lambda} \right) + \tilde{\phi} \left( t + \frac{x - 2n l}{\lambda} \right) \right\}.\n\nThus\n\np(0, t) = \lambda \tilde{\phi}(t) + 2 \lambda \sum_{n=1}^{+\infty} (-1)^n \tilde{\phi} \left( t - \frac{2n l}{\lambda} \right).

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
