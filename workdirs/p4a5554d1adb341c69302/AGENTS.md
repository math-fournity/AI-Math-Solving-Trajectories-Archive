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

In Pompeiu’s formula, \( f(z) \) and \( \int_{\Gamma} f(\zeta)/(\zeta - z) \, d\zeta \) make sense for merely continuous functions, but \n\n\[\n\int \int_\Omega \frac{\partial f}{\partial \bar{\zeta}} \frac{1}{\zeta - z} \, d\zeta \, d\eta\n\]\n\nneeds at least some weak differentiability of \( f \). It would be useful to extend the validity of the formula, for example to cover the case of functions \( f \) in \( \text{Lip} \, \alpha \), with positive \(\alpha\). This prompts the following question: For which Borel sets \(\Omega\) is the inequality\n\n\[\n\left| \left\langle \frac{\partial \chi_\Omega}{\partial \overline{z}}, f \right\rangle \right| \leq C_\Omega \| f \|_{\text{Lip }\alpha}\n\]\n\nvalid? Putting it another way, for which Borel sets \(\Omega\) does \(\chi_\Omega\) act on the Besov space \(B_{\infty,\infty}^{-\alpha}\)? An interesting special case would be when \(\Omega\) is a ‘Swiss cheese’.\n\n(A.G. O'Farrell)

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
