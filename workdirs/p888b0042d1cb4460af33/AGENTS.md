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

Consider the partial differential equation (PDE) for $u(x,t)$:

$$u_t - c^2u_{xx} = F(t)$$

with boundary and initial conditions:

$$0 < x < L, \quad t > 0$$
$$u(x,0) = f(x)$$
$$u_x(0,t)u_x(L,t) = 0$$

For the homogeneous part of the PDE ($L[v(x,t)]=0$), the eigenvalues and eigenfunctions are given by:

$$\lambda_n = \left(\frac{n\pi}{L}\right)^2$$
$$X(x) = \cos\left(\frac{n\pi x}{L}\right)$$

The general solution is proposed as:

$$u(x,t) = \sum_{n=0}^{\infty} a_n(t) \cos\left(\frac{n\pi x}{L}\right)$$

Using the initial condition, we obtain:

$$a_n(0) = \frac{2}{L} \int_0^L f(x) \cos\left(\frac{n\pi x}{L}\right) dx$$

Upon differentiation and substitution into the original PDE, we find:

$$\sum_{n=0}^{\infty} \left[ a_n'(t) + c^2 \left(\frac{n\pi}{L}\right)^2 a_n(t)\right] \cos\left(\frac{n\pi x}{L}\right) = F(t)$$

The surprising result is:

$$a_n'(t) + c^2 \left(\frac{n\pi}{L}\right)^2 a_n(t) = \frac{2}{L} F(t) \int_0^L \cos\left(\frac{n\pi x}{L}\right) dx$$

Does this imply that $F(t)$ becomes zero?

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
