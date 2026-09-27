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

$u(r, \phi, t) = \int_0^{+\infty} \rho d\rho \int_0^{\phi_0} f(\rho, \phi') G_i(r, \phi, \rho, \phi', t) d\phi', \quad i = 1, 2;$ in case (a) $i = 1$, $G_1(r, \phi, \rho, \phi', t) = \frac{2}{\phi_0} \sum_{n=1}^{+\infty} \left\{\int_0^{+\infty} e^{-a^2\lambda^2t} J_{n\zeta}\left(\lambda \rho\right) J_{n\zeta}\left(\lambda r\right) \lambda d\lambda \right\} \sin\frac{n\pi\phi'}{\phi_0} \sin\frac{n\pi\phi}{\phi_0};$ in case (b) $i = 2$, $G_2(r, \phi, \rho, \phi', t) = \frac{2}{\phi_0} \sum_{n=0}^{+\infty} e_n \left\{\int_0^{+\infty} e^{-a^2\lambda^2t} J_{n\zeta}\left(\lambda \rho\right) J_{n\zeta}\left(\lambda r\right) \lambda d\lambda \right\} \cos\frac{n\pi\phi'}{\phi_0} \cos\frac{n\pi\phi}{\phi_0},$ $e_n = \begin{cases} \frac{1}{2} & \text{for } n \neq 0, \ 1 & \text{for } n = 0. \end{cases}$ **Method.** Let us look for particular solutions of the equation $\frac{\partial u}{\partial t} = a^2 \left\{ \frac{\partial^2 u}{\partial r^2} + \frac{1}{r} \frac{\partial u}{\partial r} + \frac{1}{r^2} \frac{\partial^2 u}{\partial \phi^2} \right\}$ in the form $U(r, \phi, t) = W(r, t) \phi(\phi),$ requiring that in case (a) and (b) the appropriate boundary conditions are fulfilled. In the case of (a) this leads to particular solutions $u_n(r, t) \neq \sin \frac{n\pi \phi}{\phi_0},$ $n = 1, 2, 3, \ldots ,$ and in the case of (b) to particular solutions $u_n(r, t) \neq \cos \frac{n\pi \phi}{\phi_0},$ $n = 0, 1, 2, 3, \ldots$ In both cases $u_n(r, t)$ is a solution of the equation $\frac{\partial u_n}{\partial t} = a^2 \left\{ \frac{\partial^2 u_n}{\partial r^2} + \frac{1}{r} \frac{\partial u_n}{\partial r} - \left( \frac{n\pi}{\phi_0 r} \right)^2 u_n \right\}, \quad 0 < r, \quad t < + \infty.$

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
