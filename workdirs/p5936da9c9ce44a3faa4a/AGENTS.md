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

A thermodynamic research lab is testing a cooling system governed by a "Thermal Variance Function," $f$. The local intensity depends on three temperature settings, $x_1, x_2$, and $x_3$, and is defined by the formula:
$$f(x_1, x_2, x_3) = -2(x_1^3 + x_2^3 + x_3^3) + 3[x_1^2(x_2 + x_3) + x_2^2(x_3 + x_1) + x_3^2(x_1 + x_2)] - 12x_1x_2x_3$$

An engineer must calibrate a sensor over a range of settings. For any chosen real-numbered baseline temperature $r$, a vertical adjustment $s$, and a range start-point $t$, the engineer defines the "Maximum Deviation," $g(r, s, t)$, as the maximum value of the absolute difference $|f(r, r+2, x_3) + s|$ as the third temperature $x_3$ varies across the interval $[t, t+2]$.

The goal is to find the most stable configuration possible by minimizing the sensor's maximum deviation. What is the minimum possible value of $g(r, s, t)$ over all real numbers $r, s,$ and $t$?

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
