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

In a remote sector of the galaxy, a research station monitors a pulsating cosmic signal. The signal’s intensity is governed by a wave function $f(x) = \sin(\frac{c}{x})$, where $x$ represents the distance from the source in thousands of kilometers ($x \neq 0$) and $c$ is a positive constant representing the "Source Frequency."

The station’s primary sensor array is calibrated to detect "Null Points"—specific distances $x$ where the signal intensity is exactly zero. Galactic regulations for this sector specify that for any integer $m > 1$, there exists exactly one unique Source Frequency $c_m$ such that there are exactly $m$ Null Points within the safety zone of $10 \leq x \leq 20$.

Beyond the safety zone, in the vast expanse of $x \geq 20$, the signal continues to fluctuate. Let $Z_m$ be the distance of the outermost Null Point (the largest value of $x$) located in the range $[20, \infty)$ when the Source Frequency is set to $c_m$.

Calculate the value of $Z_{101}$.

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
