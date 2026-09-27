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

(a) For the Schrödinger equation \( \left(-\frac{d^2}{dx^2} - 2 \text{sech}^2 x\right) \psi = E \psi \), the eigensolutions are given by \( \psi_k(x) = e^{ikx}(-ik + \tanh x) \) with eigenvalue \( E = k^2 \). For \( x \) large and positive, \( \psi_k(x) \approx A e^{ikx} e^{i\eta(k)} \), and for \( x \) large and negative, \( \psi_k(x) \approx A e^{ikx} e^{-i\eta(k)} \), where \( A \) is a complex constant. Express the phase shift \( \eta(k) \) as the inverse tangent of an algebraic expression in \( k \).

(b) Impose periodic boundary conditions \( \psi(-L/2) = \psi(+L/2) \), where \( L \gg 1 \). Find the allowed values of \( k \) and derive an explicit expression for the \( k \)-space density \( \rho(k) = \frac{dn}{dk} \) of the eigenstates.

(c) Compare your expression for \( \rho(k) \) with the density \( \rho_0(k) = \frac{L}{2\pi} \) for the zero-potential case. Compute the integral \( \Delta N = \int_{-\infty}^{\infty} \{\rho(k) - \rho_0(k)\} \, dk \).

(d) Deduce that one eigenfunction is missing from the continuum and corresponds to the localized bound state \( \psi_0(x) = \frac{1}{\sqrt{2}} \text{sech} x \).

---

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
