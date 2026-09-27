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

The solution of the boundary-value problem\n\n\[\nv_x + L i_t + R i = 0, \quad \bigg\} \, 0 < x, \, t < + \infty, \quad C R = G L, \tag{1}\n\]\n\n\[\ni_x + C v_t + G v = 0, \tag{1'}\n\]\n\n\[\nv(0, t) = E \sin \omega t, \quad 0 < t < + \infty , \tag{2}\n\]\n\n\[\nv(x, 0) = i(x, 0) = 0, \quad 0 < x < +\infty \tag{3}\n\]\n\nhas the form\n\n\[\nv(x, t) = v_0(x, t) + t v^*(x, t), \tag{4}\n\]\n\n\[\ni(x, t) = i_0(x, t) + t i^*(x, t), \tag{4'}\n\]\n\nwhere\n\n\[\nv_0(x, t) = E e^{-\alpha x} \sin (\omega t - \beta x) \tag{5}\n\]\n\nis the voltage of the steady-state vibrations,\n\n\[\ni_0(x, t) = E e^{-\alpha x} \frac{1}{R^2 + \omega^2 L^2} \left[ (\alpha R + \beta \omega L) \sin (\omega t - \beta x) + (\beta R - \alpha \omega L) \cos (\omega t - \beta x) \right] \tag{6}\n\]\n\nis the current intensity of the steady-state vibrations\n\n\[\n\alpha = \sqrt{\frac{G R + \omega^2 C L + 2 \omega C R}{2}}, \quad \beta = \sqrt{\frac{G R + \omega^2 C L - 2 \omega C R}{2}}, \tag{7}\n\]\n\nand\n\n\[\nv^*(x, t) = e^{-\frac{R}{L} t} \left[ \phi(x - a t) + \psi(x + a t) \right] \tag{8}\n\]\n\nis the voltage of the damped vibrations\n\n\[ \ni^*(x, t) = \sqrt{\frac{C}{L}} e^{-\frac{R}{L} t} [\phi(x-at) - \psi(x-at)] \]\n\nis the current intensity of the damped vibrations\n\n\[\n\phi(z) = \frac{v_0(z, 0) + i_0(z, 0)}{2} \sqrt{\frac{L}{C}}, \quad \psi(z) = \frac{v_0(z, 0) - i_0(z, 0)}{2} \sqrt{\frac{L}{C}}, \n\]\n\n\[\n0 < z < \infty, \quad \phi(z) = -\psi(-z), \quad -\infty < z < 0. \n\]\n\nFor \n\n\[\nt > \frac{1}{\frac{R}{L} + \alpha a}\ln 10 \left[1 + \frac{(|\beta - \alpha \omega| + \alpha R + \beta \omega L)\frac{V}{L}}{(R^2 + \omega^2 L^2) \sqrt{\frac{V}{C}}} \right]\n\]\n\nthe amplitude of the voltage of the damped vibrations will be less than 10 percent of the amplitude of the voltage of the steady-state vibrations.

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
