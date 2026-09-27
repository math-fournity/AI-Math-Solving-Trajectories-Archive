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

(a) The solution of the boundary-value problem\n\n\[u_t = a^2 u_{xx}, \quad 0 < x < l, \quad 0 < t < +\infty,\]\n\[u_x(0,t) - H [u(0,t) - U_1] = 0, \quad u_x(l,t) + H [u(l,t) - U_2] = 0, \quad 0 < t < +\infty, \]\n\[u(x,0) = f(x), \quad 0 < x < l\]\nis:\n\[u(x,t) = w(x) + v(x,t), \quad 0 < x < l, \quad 0 < t < +\infty,\]\nwhere\n\[w(x) = H \frac{U_2-U_1}{2+1HJ}x + \frac{U_2+(1+1HJ)U_1}{2+1HJ}, \quad 0 < x < l\]\nand\n\[v(x,t) = \sum_{n=1}^{+\infty} a_n e^{-a^2 \lambda_n^2 t} \left(\cos \lambda_n x + \frac{H}{\lambda_n} \sin \lambda_n x \right), \quad 0 < x < l, \quad 0 < t < +\infty,\]\n\(\lambda_n = z_n / l\), \(z_n\) are the positive roots of the transcendental equation\n\n\[\cot z = \frac{1}{2}\left( \frac{z}{1H} - \frac{1H}{z} \right).\]\n\n(b) If the temperature of the medium at both ends is the same, and the initial temperature of the rod equals zero, then, taking the middle of the rod as the origin of coordinates, we derive that the temperature in the rod is an even function of \(x\), i.e. for \(x = 0\) \(\partial u/\partial x = 0\). Thus it is possible to consider instead of the whole rod only half of it, where the boundary-value problem 29 is obtained to determine the temperature (it is necessary to replace \(l\) by \(l/2\)).

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
