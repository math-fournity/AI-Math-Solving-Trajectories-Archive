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

The solution of the boundary-value problem\n\nu_t = a^2 u_{xx}, \quad 0 < x, \quad t < +\infty,\n\nc_0 u(0, \tau) = \lambda S u_x(0, \tau), \quad 0 < \tau < +\infty,\n\nu(x, 0) = f(x), \quad 0 < x < +\infty\n\nis:\n\nu(x, t) = \frac{-1}{2a\sqrt{\pi t}} \int_{-\infty}^{+\infty} F(\xi) e^{\frac{-(x-\xi)^2}{4a^2 t}} \, d\xi,\n\nwhere\n\nF(x) = \begin{cases} \tilde{f}(x) & \text{for } -\infty < x < 0, \\ f(x) & \text{for } 0 < x < +\infty, \end{cases}\n\n\tilde{f}(x) = \frac{e^{a^2 x - 1}}{a^2} f'(-0+) + f(+0) + f(0+) x \int_0^x \left\{ f''(-\xi) + a^2 f'(-\xi) \right\} e^{-a^2 (x-z)} \, d\xi,\n\n a^2 = \frac{\lambda S}{a^2 c_0},\n\n\(\lambda\) is the coefficient of heat conduction of the rod, \(S\) the cross-sectional area, \(a^2\) the coefficient of thermal conductivity of the rod.

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
