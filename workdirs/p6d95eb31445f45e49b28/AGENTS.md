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

A specialized materials lab is developing a new synthetic alloy whose structural stability is modeled by a potential energy function $P(x, y) = a + x^2 y^4 + x^4 y^2 - k x^2 y^2$, where $x$ and $y$ represent stress vectors across two perpendicular axes. 

The lab's lead engineer determines that when the base stability constant $a$ is set to $4$, there exists a critical threshold for the interference coefficient $k$. At this specific value of $k$, the energy function $P(x, y)$ reaches a mathematical "breaking point" where it can no longer be decomposed into a sum of squares of real-coefficient polynomials. This occurs because the required symmetry of the homogeneous components of such a decomposition would lead to a logical contradiction within the real number system.

Suppose we analyze a scenario where $P(x, y)$ is represented as a sum of squares of polynomials, $\sum Q_i(x, y)^2$. Let $s_i(x, y)$ denote the purely quadratic portion of each polynomial $Q_i(x, y)$. If the sum of the squares of the coefficients of the $xy$ terms across all quadratic parts $s_i(x, y)$ must equal exactly $-k$, find the value of $k$.

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
