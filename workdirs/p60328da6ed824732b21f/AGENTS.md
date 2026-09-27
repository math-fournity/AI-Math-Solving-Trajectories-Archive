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

The solution of the boundary-value problem\n\n\begin{align*}\n\frac{\partial u_1}{\partial t} &= a_1^2 \frac{\partial^2 u_1}{\partial x^2}, \quad 0 < x < \xi(t), \\\n\frac{\partial u_2}{\partial t} &= a_2^2 \frac{\partial^2 u_2}{\partial x^2}, \quad \xi(t) < x < +\infty,\n\end{align*}\n\n0 < t < +\infty,\n\nu_1(\xi(t), t) = u_2(\xi(t), t), \quad u_1(0, t) = U_1, \quad u_2(+\infty, t) = U_2,\n\nwhere the freezing point is taken as zero, \( x = \xi(t) \) the coordinate of the freezing front\n\n\left( k_1 \frac{\partial u_1}{\partial x} - k_2 \frac{\partial u_2}{\partial x} \right)_{x = \xi(t)} = Q \rho \frac{d\xi}{dt}, \quad 0 < t < +\infty,\n\n\( Q \) the latent heat of fusion, \( \rho \) the mass density of the liquid,\n\nu_2(x, 0) = U_2, \quad 0 < x < +\infty,\n\nis:\n\nu_1(x, t) = A_1 + B_1 \Phi \left( \frac{x}{2a_1 \sqrt{t}} \right),\n\nu_2(x, t) = A_2 + B_2 \Phi \left( \frac{x}{2a_2 \sqrt{t}} \right),\n\nwhere\n\nA_1 = U_1, \quad B_1 = -\frac{U_1}{\Phi \left( \frac{a}{2a_1} \right)}, \quad A_2 = \frac{U_2 \Phi \left( \frac{a}{2a_2} \right)}{1 - \Phi \left( \frac{a}{2a_1} \right)}, \quad B_2 = \frac{U_2}{1 - \Phi \left( \frac{a}{2a_2} \right)},\n\nand \( a \) is the root of the transcendental equation\n\n\frac{k_1 U_1 e^{-\frac{a^2}{a_1^2}}}{a_1 \Phi \left( \frac{a}{2a_1} \right)} + \frac{k_2 U_2 e^{-\frac{a^2}{a_2^2}}}{a_2 \left[ 1 - \Phi \left( \frac{a}{2a_2} \right) \right]} = -Q \rho \frac{\sqrt{\pi}}{2} a.

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
