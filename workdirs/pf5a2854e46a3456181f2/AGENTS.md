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

A quadrupole charge distribution consists of four point charges arranged in the \( x_1, x_2 \)-plane as follows:
- A charge \( +q \) at \( (a, 0, 0) \),
- A charge \( -q \) at \( (0, a, 0) \),
- A charge \( +q \) at \( (-a, 0, 0) \),
- A charge \( -q \) at \( (0, -a, 0) \).

(a) Using Dirac \( \delta \)-functions, express the charge density \( \rho_c(x_1, x_2, x_3) \) of this distribution.

(b) The quadrupole moment of this charge distribution is a second-rank tensor given by:
\[
\mathbf{Q} = Q_{ij} \mathbf{\hat{e}}_i \mathbf{\hat{e}}_j,
\]
where the elements are:
\[
Q_{ij} = \int_{-\infty}^{\infty} dx_1 \int_{-\infty}^{\infty} dx_2 \int_{-\infty}^{\infty} dx_3 \rho_c(x_1, x_2, x_3) \left[ 3x_i x_j - (x_k x_k) \delta_{ij} \right].
\]
Evaluate all the elements of the quadrupole tensor for this charge distribution.

(c) Does this charge distribution have a dipole moment?

(d) Find the coordinate system in which this quadrupole tensor is diagonal. Express the elements of \( \mathbf{Q} \) in this system.

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
