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

Starting at \( t = 0 \), a concentrated load of magnitude \( F_0 \) moves with a constant velocity \( v_0 \) along a semi-infinite string. In this case the wave equation becomes\n\n\[ \na^2 \frac{\partial^2 u}{\partial x^2} - \frac{\partial^2 u}{\partial t^2} + F_0 \delta \left( x - \frac{v_0 t}{\omega} \right) = 0\n\]\n\nwhere \( \delta (x - t/v_0) \) is the Dirac delta function. Solve the above PDE subject to\n\n\[ \nu(0, t) = 0, \quad \lim_{x \to \infty} u(x, t) = 0, \quad t > 0\n\]\n\[ \nu(x, 0) = 0, \quad \frac{\partial u}{\partial t} \bigg|_{t=0} = 0, \quad x > 0\n\]\n\n(a) when \( v_0 \neq a \)\n(b) when \( v_0 = a \).

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
