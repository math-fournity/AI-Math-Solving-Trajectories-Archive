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

In a futuristic energy grid, a central AI manages a variable power load represented by a sequence $a_n$ (measured in megawatts). The initial output levels for the first three cycles are recorded as $a_0 = 1$, $a_1 = 0$, and $a_2 = 2005$. For all subsequent cycles where $n = 1, 2, \dots$, the AI updates the power level according to the protocol $a_{n+2} = -3a_n - 4a_{n-1} + 2008$.

A stability index, $b_n$, is calculated for any cycle $n$ based on the fluctuations between non-consecutive cycles and the deviation from a target baseline of $502$. The formula for this index is:
$b_n = 5(a_{n+2} - a_n)(502 - a_{n-1} - a_{n-2}) + 4^n \times 2004 \times 501$

An engineer needs to determine the "Resonance Ratio" of the system at the tenth cycle. This ratio is defined as the square root of the tenth stability index, divided by a weighted sum of the system's recent deviations from the 502 MW baseline.

Calculate the value of:
$$\frac{\sqrt{b_{10}}}{2(a_{11} + a_{10} - 502) + 4(a_{10} + a_{9} - 502)}$$

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
