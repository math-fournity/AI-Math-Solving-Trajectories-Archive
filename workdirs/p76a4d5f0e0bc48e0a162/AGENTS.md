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

Solving the problem of steady-state heat conduction in a semi-infinite strip with Dirichlet boundary conditions involves finding the function \( u(x, y) \) that is bounded and harmonic in the vertical semi-infinite strip \( 0 < x < a, \, y > 0 \) and satisfies the following problem:\n\[\n\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0, \quad 0 < x < a, \, y > 0,\n\]\n\[\nu(0, y) = g_1(y),\n\]\n\[\nu(a, y) = g_2(y),\n\]\n\[\nu(x, 0) = f(x),\n\]\n\[\n|u(x, y)| \text{ bounded as } y \to \infty.\n\]\nUsing the superposition principle, we write \( u(x, y) = v(x, y) + w(x, y) \), where \( v \) and \( w \) satisfy Laplace’s equation and the boundary conditions shown below.\n\n#### Problem I:\n\n\[\n\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0, \quad 0 < x < a, \, y > 0,\n\]\n\[\nv(0, y) = 0,\n\]\n\[\nv(a, y) = 0,\n\]\n\[\nv(x, 0) = f(x),\n\]\n\[\n|v(x, y)| \text{ bounded as } y \to \infty.\n\]\n\n#### Problem II:\n\n\[\n\frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} = 0, \quad 0 < x < a, \, y > 0,\n\]\n\[\nw(0, y) = g_1(y),\n\]\n\[\nw(a, y) = g_2(y),\n\]\n\[\nw(x, 0) = 0,\n\]\n\[\n|w(x, y)| \text{ bounded as } y \to \infty.\n\]

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
