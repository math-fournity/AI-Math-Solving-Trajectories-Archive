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

(a) The solution of the boundary-value problem\n\nu_t = a^2 u_{xx} + f(x, t), \quad 0 < x < l, \quad 0 < t < +\infty,\n\nu(0, t) = u(l, t) = 0, \quad 0 < t < +\infty,\n\nu(x, 0) = \phi(x), \quad 0 < x < l,\n\nwhere \( f(x, t) = F(x, t)/c \rho \) is:\n\nu(x, t) = \int_0^l \phi(\xi) \left\{ \frac{2}{l} \sum_{n=1}^{+\infty} e^{-\frac{n^2 \pi^2 a^2}{l^2} t} \sin \frac{n \pi x}{l} \sin \frac{n \pi \xi}{l} \right\} \, d\xi +\n\n+ \int_0^t \int_0^l f(\xi, \tau) \left\{ \frac{2}{l} \sum_{n=1}^{+\infty} e^{-\frac{n^2 \pi^2 a^2}{l^2}(t - \tau)} \sin \frac{n \pi x}{l} \sin \frac{n \pi \xi}{l} \right\} \, d\xi \, d\tau.\n\n(b) The solution of the boundary-value problem\n\nu_t = a^2 u_{xx} + \frac{Q}{c \rho} \delta(x - x_0), \quad 0 < x < l, \quad 0 < t < +\infty,\n\nu(0, t) = u(l, t) = 0, \quad 0 < t < +\infty,\n\nu(x, 0) = 0, \quad 0 < x < l\n\nis:\n\nu(x, t) = \frac{2Q}{c \rho \pi a^2} \sum_{n=1}^{+\infty} \frac{1}{n^2} \left( 1 - e^{-\frac{n^2 \pi^2 a^2}{l^2} t} \right) \sin \frac{n \pi x}{l} \sin \frac{n \pi x_0}{l}.

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
