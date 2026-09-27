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

It is required to find the function \n\nG(x, y, z, \xi, \eta, \zeta) = \frac{e^{-ikr}}{4 \pi r} + v,\n\nr = \sqrt{(x - \xi)^2 + (y - \eta)^2 + (z - \zeta)^2},\n\nwhere v is the regular solution of the wave equation, which must be chosen so that for z = 0 one of the conditions: G|_{z=0} = 0, \frac{\partial G}{\partial z} |_{z=0} = 0 is fulfilled.\n\n(a) G(x, y, z, \xi, \eta, \zeta) = \frac{e^{-ikr}}{4 \pi r} - \frac{e^{-ikr_1}}{4 \pi r_1},\n\nr_1 = \sqrt{(x - \xi)^2 + (y - \eta)^2 + (z + \zeta)^2}.\n\nThe solution of the first boundary-value problem will be:\n\nu(x, y, z) = -\frac{z}{2 \pi} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \left( ik + \frac{1}{R} \right) \frac{e^{-ikR}}{R} f(\xi, \eta) d\xi d\eta,\n\nR = \sqrt{(x - \xi)^2 + (y - \eta)^2 + z^2};\n\n(b) \hat{G}(x, y, z, \xi, \eta, \zeta) = \frac{e^{-ikr}}{4 \pi r} + \frac{e^{-ikr_1}}{4 \pi r_1}.\n\nThe solution of the second boundary-value problem will be:\n\nu(x, y, z) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \hat{G}|_{z=0} f(\xi, \eta) d\xi d\eta = \frac{1}{2 \pi} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \frac{e^{-ikR}}{R} f(\xi, \eta) d\xi d\eta.\n\nMethod. In order to find the source function G use the method of images.

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
