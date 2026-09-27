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

A solid conducting cylinder of unit height and radius and with diffusivity \( \kappa \) is initially at temperature \( f(\rho, z) \) (see Fig. 6-8). The entire surface is suddenly lowered to temperature zero and kept at this temperature. Find the temperature at any point of the cylinder at any subsequent time.\n\nSince there is no \(\phi\)-dependence, as is evident from symmetry, the heat conduction equation is\n\n\[ \frac{\partial u}{\partial t} = \kappa \left( \frac{\partial^2 u}{\partial \rho^2} + \frac{1}{\rho} \frac{\partial u}{\partial \rho} + \frac{\partial^2 u}{\partial z^2} \right) \]\n\nwhere \( u = u(\rho, z, t) \). The boundary conditions are given by\n\n\[ \n\begin{align*}\nu(\rho, z, 0) &= f(\rho, z), \\\nu(\rho, 0, t) &= 0, \\\nu(\rho, 1, t) &= 0, \\\nu(1, z, t) &= 0, \\\n|u(\rho, z, t)| &< M\n\end{align*}\n\]\n\nwhere \( 0 \leq \rho < 1, \, 0 < z < 1, \, t > 0 \).

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
