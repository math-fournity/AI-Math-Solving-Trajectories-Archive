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

(a) The solution of the first boundary-value problem \( u_{xx} + u_{yy} + u_{zz} = 0 \) in semispace \( z > 0 \), \( u|_{z=0} = f \) is sought in the form of the potential of a double layer \[ u(x, y, z) = W = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} \frac{\cos \phi}{r^2} v(\xi, \eta) d\xi d\eta, \quad r^2 = (x-\xi)^2 + (y-\eta)^2 + z^2 \] and is given by the formula \[ u(x, y, z) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} \frac{z f(\xi, \eta) d\xi d\eta}{[(x-\xi)^2 + (y-\eta)^2 + z^2]^{3/2}} \quad \left( \mu = \frac{1}{2\pi} f \right). \] (b) The solution of the second boundary-value problem \[ u_{xx} + u_{yy} + u_{zz} = 0 \quad \text{for} \quad z > 0, \quad \left. \frac{\partial u}{\partial z} \right|_{z=0} = f \] is sought in the form of the potential of a single layer \[ u(x, y, z) = V(x, y, z) = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} \frac{\mu(\xi, \eta) \, d\xi \, d\eta}{\sqrt{(x-\xi)^2 + (y-\eta)^2 + z^2}} \] and is given by the formula \[ u(x, y, z) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} \frac{f(\xi, \eta) \, d\xi \, d\eta}{\sqrt{(x-\xi)^2 + (y-\eta)^2 + z^2}} + \text{const.} \quad \left( \mu = \frac{1}{2\pi} f \right). \]

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
