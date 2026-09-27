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

A specialized artificial intelligence lab is developing automated "Validation Protocols" to secure encrypted data streams. 

A protocol $f$ is considered **Secure** if it satisfies two operational constraints:
1. For any two integer access codes $x$ and $y$, the difference between the resulting encrypted keys $f(y) - f(x)$ must be perfectly divisible by the difference of the codes $y - x$.
2. For any integer access code $x$, the resulting encrypted key $f(x)$ must be an integer.

A Secure protocol is further classified as **Obscured** if it is not a null function and all of its non-zero coefficients are strictly between 0 and 1.

The lab is auditing all possible Obscured protocols $f$ that have a maximum degree of 5. For each such protocol, the lab calculates an "Impact Score" by multiplying the protocol's degree by the value it generates when the access code is 2 (i.e., $\text{deg}(f) \cdot f(2)$).

Calculate the sum of the Impact Scores for every possible Obscured protocol of degree at most 5.

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
