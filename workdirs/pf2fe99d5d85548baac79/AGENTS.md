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

We again consider the telegraph partial differential equation over the finite interval \( I = \{ x \mid 0 < x < 1 \} \). The telegraph equation reads as\n\n\[\n\frac{\partial^2}{\partial t^2} u(x, t) = c^2 \left( \frac{\partial^2}{\partial x^2} u(x, t) \right) - \gamma \left( \frac{\partial}{\partial t} u(x, t) \right) - \zeta u(x, t)\n\]\n\nwith \( c = 1/4 \), \( \gamma = 1/5 \), \( \zeta = 1/10 \), and boundary conditions\n\n\[\nu_x(0, t) - u(0, t) = 0 \quad \text{and} \quad u(1, t) = 0\n\]\n\nThe left end of the string is attached to an elastic hinge, and the right end of the string is secured. The initial conditions are\n\n\[\nu(x, 0) = f(x) \quad \text{and} \quad u_t(x, 0) = g(x)\n\]\n\nUse the method of separation of variables to evaluate the eigenvalues and corresponding orthonormalized eigenfunctions, and write the general solution. Evaluate the solution for each of the three sets of initial conditions given:\n\n- \( f_1(x) = 1 \) and \( g_1(x) = 0 \)\n- \( f_2(x) = 1 - x \) and \( g_2(x) = 1 \)\n- \( f_3(x) = -\frac{2x^2}{3} + \frac{x}{3} + \frac{1}{3} \) and \( g_3(x) = 0 \)\n\nGenerate the animated solution for each case, and plot the animated sequence for \( 0 < t < 5 \).

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
