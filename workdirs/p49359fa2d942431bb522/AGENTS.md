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

In a specialized engine laboratory, engineers are monitoring a fuel efficiency curve \(f(x)\) over a performance range \(x \in [1, 3]\). The rate of efficiency change, \(f'(x)\), is known to be continuous and strictly increasing throughout this interval.

The laboratory sensors provide the following boundary telemetry:
- Twice the initial rate of change is equal to three times the final rate of change, which is also equal to four times the initial efficiency value, all being equal to a constant value of 8 units (i.e., \(2f'(1) = 3f'(3) = 4f(1) = 8\)).

During high-stress testing, two complex stress integrals were recorded:
1. A thermal vibration metric, calculated by integrating the product of the rate of change of the efficiency slope and the square root of the ratio of the cubic range to the efficiency slope, yielded a value of \(4 - 4\sqrt{2}\):
\[ \int_1^3 f''(x) \sqrt{\frac{x^3}{f'(x)}} \, dx = 4 - 4\sqrt{2} \]

2. A structural strain metric, determined by integrating the square root of a combination of the range and the squared rate of change, resulted in a value of \(\frac{16\sqrt{2} - 8}{3}\):
\[ \int_1^3 \sqrt{x + 1 + \frac{x^2 (f'(x))^2}{4(x+1)}} \, dx = \frac{16\sqrt{2} - 8}{3} \]

Based on these specific engine parameters, calculate the total accumulated efficiency over the range, defined as the integral of the efficiency function:
\[ \int_1^3 f(x) \, dx \]

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
