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

In a specialized laboratory, three unique isotopes—codenamed Alpha, Beta, and Gamma—are being studied. Their precise stability levels, represented by the values $a, b,$ and $c$, are defined as the three roots of the environmental stability equation: $x^3 + 3x^2 + 5x + 7 = 0$.

A chemical engineer is calibrating a response function, $P(x)$, which is a cubic polynomial. Initial testing reveals a symmetric interaction between the isotopes:
- When the function is applied to the stability level of Alpha, the output is the combined stability of Beta and Gamma: $P(a) = b + c$.
- When applied to Beta, the output is the combined stability of Gamma and Alpha: $P(b) = c + a$.
- When applied to Gamma, the output is the combined stability of Alpha and Beta: $P(c) = a + b$.

Furthermore, the engineer discovers a "total system" constraint: when the function is applied to the sum of all three stability levels, the resulting output is exactly $-16$. That is, $P(a + b + c) = -16$.

To finalize the calibration of the laboratory equipment, the engineer needs to determine the baseline value of the response function when the input stability is zero. Find the value of $P(0)$.

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
