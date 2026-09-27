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

Consider the Cauchy problem for the second-order evolution equation\n\n\[\n\frac{d^2 u}{dt^2} + A u = f(t), \quad 0 < t \leq T,\n\]\n\n\[\nu(0) = u_0, \quad \frac{du}{dt}(0) = u_1,\n\]\n\nwith \( A = A^* > 0 \). Obtain the following estimate of solution stability with respect to initial data and the right-hand side:\n\n\[\n\|u(t)\|_{\mathcal{X}}^2 \leq \exp(t) \left( \|u^0\|_A^2 + \|v^0\|^2 + \int_0^t \exp(-\theta) \|f(\theta)\|^2 d\theta \right),\n\]\n\nwhere\n\n\[\n\|u\|_{\mathcal{X}}^2 = \left\| \frac{du}{dt} \right\|^2 + \|u\|_A^2\n\]\n\nand \(\|v\|_{\mathcal{D}}^2 = (\mathcal{D}v, v)\) for the self-adjoint, positive operator \(\mathcal{D}\).

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
