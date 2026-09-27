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

The temperature at the centre of the cube \(-l \leq x, y, z \leq l\) equals\n\n\[\nU = 8U_0 \frac{h^3}{l^3} \left[ \sum_{k=0}^{+\infty} e^{-a^2 \lambda_k^2 t} (-1)^k \sqrt{\frac{1 + \frac{h^2}{\lambda_k^2}}{l(\lambda_k^2 + h^2) + h}} \right],\n\]\n\nwhere \(\lambda_0, \lambda_1, \lambda_2, \ldots\) are positive roots of the equation\n\n\[\n\tan \lambda l = \frac{h}{\lambda}.\n\]\n\nFor all values of time \(t\) satisfying the inequality\n\n\[\nt \geq t^* = -\frac{1}{a^2(\lambda_1^2 - \lambda_0^2)} \ln \left[ e \frac{(hl)^2 + hl + (l\lambda_1)^3}{(hl)^2 + hl + (l\lambda_0)^3} \sqrt{\frac{1 + \left( \frac{h}{\lambda_0} \right)^2}{1 + \left( \frac{h}{\lambda_1} \right)^2}} \right].\n\]\n\n------page471------\nwhere $\tilde{\varepsilon}$ equals the smaller of the numbers 1 and $\varepsilon /9$, a steady-state will occur at the centre of the cube correct to $\varepsilon$.

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
