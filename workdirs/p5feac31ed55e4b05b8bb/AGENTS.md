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

Find the dimensionless temperature \( y(\xi_1, \xi_2, \zeta) \) that satisfies the partial differential equation:
\[
\tilde{L}^2 \left( \frac{\partial^2 y}{\partial \xi_1^2} + \frac{\partial^2 y}{\partial \xi_2^2} + \frac{\partial^2 y}{\partial \zeta^2} \right) = 0 \quad \text{in } D,
\]
where \( D \) is the domain defined by:
\[
D = \left\{ (\xi_1, \xi_2, \zeta) : 0 < \zeta < 1, \xi_1^2 + \xi_2^2 < \tilde{R}(\zeta)^2 \right\},
\]
with the boundary conditions:
\[
\frac{\partial y}{\partial \nu_A} = 1 \text{ on } S_1, \quad \frac{\partial y}{\partial \nu_A} = 0 \text{ on } S_2, \quad y = 0 \text{ on } S_3.
\]
Here, \( \frac{\partial y}{\partial \nu_A} \) is the conormal derivative defined as:
\[
\frac{\partial y}{\partial \nu_A} = \tilde{L}^2 \left( \nu_1 \frac{\partial y}{\partial \xi_1} + \nu_2 \frac{\partial y}{\partial \xi_2} + \nu_3 \frac{\partial y}{\partial \zeta} \right),
\]
and \( \nu \) is the outward normal to the boundary surface \( S = S_1 \cup S_2 \cup S_3 \).

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
