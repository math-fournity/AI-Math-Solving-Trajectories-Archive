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

The solution of the boundary-value problem\n\n\[\n\frac{\partial u}{\partial x} = \frac{a^2}{v_0} \left( \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right), \quad 0 < x < +\infty, \quad 0 < y < l_1, \quad 0 < z < l_2,\n\]\n\n\[\n\left( \frac{\partial u}{\partial y} - hu \right) \bigg|_{y=0} = \left( \frac{\partial u}{\partial y} + hu \right) \bigg|_{y=l_1} = \left( \frac{\partial u}{\partial z} - hu \right) \bigg|_{z=0} = \left( \frac{du}{dz} + hu \right) \bigg|_{z=l_2} = 0,\n\]\n\n\[\nu|_{x=0} = U_0, \quad 0 < y < l_1, \quad 0 < z < l_2\n\]\n\nis:\n\n\[\nu(x, y, z) = 16U_0 h^2 \sum_{m,n=0}^{+\infty} e^{-\frac{a^2}{v_0^2} (\mu_{2m+1}^2 + \nu_{2n+1}^2)x} \times\n\]\n\n\[\n\times \left( \frac{\cos \mu_{2m+1} y + \frac{h}{\mu_{2m+1}} \sin \mu_{2m+1} y}{[l_1(\mu_{2m+1}^2 + h^2) + 2h]} \right) \left( \frac{\cos \nu_{2n+1} z + \frac{h}{\nu_{2n+1}} \sin \nu_{2n+1} z}{[l_2(\nu_{2n+1}^2 + h^2) + 2h]} \right),\n\]\n\nwhere \(\mu_1, \mu_2, \dots\); \(\nu_1, \nu_2, \dots\) are respectively the roots of the equations\n\n\[\n\cot l_1 \mu = \frac{1}{2} \left( \frac{\mu}{h} - \frac{h}{\mu} \right), \quad \cot l_2 \nu = \frac{1}{2} \left( \frac{\nu}{h} - \frac{h}{\nu} \right).\n\]

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
