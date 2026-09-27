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

70. The solution of the boundary-value problem\n\n\[\n\frac{\partial u}{\partial t} = a^2 \left( \frac{\partial^2 u}{\partial r^2} + \frac{1}{r} \frac{\partial u}{\partial r} \right), \quad r_0 \leq r < +\infty, \quad 0 < t < +\infty,\n\]\n\n\[\nu(r_0, t) = U_0 = \text{const.} \quad 0 < t < +\infty,\n\]\n\n\[\nu(r, 0) = 0, \quad r_0 < r < +\infty\n\]\n\nis:\n\n\[ \nu(r, t) = \frac{2U_0}{\pi} \int_{r_0}^{+\infty} \frac{[ 1-e^{-a^2\lambda^2 t} ] K(r, \lambda) \, d\lambda}{J_0^2(r_0 \lambda) + N_0^2(r_0 \lambda)} \cdot \frac{1}{\lambda}, \tag{4} \]\n\nwhere\n\n\[\nK(r, \lambda) = J_0(r_0 \lambda) N_0(r \lambda) - N_0(r_0 \lambda) J_0(r \lambda).\n\tag{5} \n\]\n\n**Method.** Use Weber's integral transform with kernel \( rK(r, \lambda) \) in the interval \( r_0 \le r < +\infty \), namely: firstly, applying this transformation to equation (1), an equation is obtained for the Weber form of the unknown function\n\n\[\nu(\lambda, t) = \int_{r_0}^{+\infty} \nu(r, t)rK(r, \lambda) \, dr,\n\tag{6} \n\]\n\nand then, finding \( \bar{u}(\lambda, t) \), apply Weber's inversion formula\n\n\[\nu(r, t) = \int_{r_0}^{+\infty} \frac{\bar{u}(\lambda, t) \Delta K(r, \lambda) \, d\lambda}{J_0^2(r_0 \lambda) + N_0^2(r_0 \lambda)}\n\tag{7} \n\]

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
