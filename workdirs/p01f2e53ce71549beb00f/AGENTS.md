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

Consider the boundary value–initial value problem for the solution \( u(r, \theta, \phi, t) \) of the homogeneous wave equation on a hemispherical solid \( H \):\n\n\[\n\frac{\partial^2 u}{\partial t^2} = \nabla^2 u, \quad (r, \theta, \phi) \in H, \quad t > 0,\n\]\n\n\[\nu(1, \theta, \phi, t) = 0,\n\]\n\n\[\nu(r, \theta, -\frac{\pi}{2}, t) = \nu(r, \theta, \frac{\pi}{2}, t) = 0,\n\]\n\n\[\nu(r, \theta, \phi, 0) = f(r, \theta, \phi),\n\]\n\n\[\n\frac{\partial u}{\partial t}(r, \theta, \phi, 0) = 0,\n\]\n\nwhere the hemisphere is parametrized using spherical coordinates as\n\n\[\nH = \left\{ (r, \theta, \phi) \mid 0 \leq r \leq 1, \ -\frac{\pi}{2} \leq \phi \leq \frac{\pi}{2}, \ 0 \leq \theta \leq \pi \right\}.\n\]\n\n(a) Supplement the problem above with an appropriate number of additional side conditions which will guarantee that there is a unique bounded solution.\n\n(b) Assume a separated solution of the form\n\n\[\nu(r, \theta, \phi, t) = R(r) \cdot S(\theta) \cdot \Phi(\phi) \cdot T(t),\n\]\n\nand separate the differential equation and side conditions to derive a radial problem for \( R \), an azimuthal problem for \( S \), a polar problem for \( \Phi \), and a time problem for \( T \).\n\n(c) The radial, azimuthal, and polar problems are complete, that is, have the right number of side conditions, while the temporal problem is incomplete. The polar problem depends on one separation constant, and this problem should be solved first.\n\n(d) Solve the azimuthal problem and identify the second separation constant.\n\n(e) Solve the radial problem and identify the third separation constant.\n\n(f) Solve the time problem and use the superposition principle to write the general solution.\n\n(g) Solve the boundary value–initial value problem with the following initial condition:\n\n\[\nf(r, \theta, \phi) = 4j_2(\alpha_{23}r)P_2^1(\cos \theta) \cos \phi,\n\]\n\nwhere \( j_2 \) is the spherical Bessel function of the first kind of order 2, \( \alpha_{23} \) is the third positive zero of this function, and \( P_2^1(\cos \theta) \) is the associated Legendre function of degree 2 and order 1.

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
