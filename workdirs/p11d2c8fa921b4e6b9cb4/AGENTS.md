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

Given the circle $x^2 + y^2 = 4$ and the hyperboloid $x^2 + y^2 - z^2 - 1 = 0$, find the length of the circle's intersection with the hyperboloid. The hyperboloid is parameterized as:

$$x(u, v) = (\sinh(u)\sin(v), \sinh(u)\cos(v), \cosh(u))$$

The circle, with a radius of 2, can be parameterized as:

$$c(t) = (2\cos(t), 2\sin(t))$$

Calculate the coefficients of the first fundamental form on $c(t)$:

$$\begin{align*}
E &= \langle x_u, x_u \rangle = \cosh^2(u)\sin^2(v) + \cosh^2(u)\cos^2(v) + \sinh^2(u) \\
F &= \langle x_u, x_v \rangle = 0 \\
G &= \langle x_v, x_v \rangle = \sinh^2(u)\cos^2(v) + \sinh^2(u)\sin^2(v)
\end{align*}$$

With $u$ such that $\sinh(u) = 2$, the differential of arc length is:

$$ds = \sqrt{Edu^2 + Gdv^2} = \sqrt{(\cosh^2(u)\sin^2(v) + \cosh^2(u)\cos^2(v) + \sinh^2(u))\sin^2(t) + (\sinh^2(u)\cos^2(v) + \sinh^2(u)\sin^2(v))\cos^2(t)}$$

Evaluate the integral $\int_0^{2\pi} ds$ to find the length of the intersection.

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
