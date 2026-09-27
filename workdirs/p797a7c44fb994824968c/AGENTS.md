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

In a specialized chemical processing plant, three storage tanks—Alpha, Beta, and Gamma—contain quantities of a specific catalyst, denoted by $a, b,$ and $c$ tons respectively. Due to strict storage regulations, the total mass of the catalyst across all three tanks must be exactly $3$ tons ($a + b + c = 3$), where the amount in each tank cannot be negative.

The facility's structural stability is measured by a "Rigidity Index," calculated as the sum of the squares of the masses in each tank: $a^2 + b^2 + c^2$. 

Engineers have discovered a "Pressure Ratio" formula that governs the pipes connecting the tanks. This ratio depends on a constant additive safety factor, $k$. The total pressure across the system is defined as the sum of the relative masses adjusted by this factor:
$$\frac{a+k}{b+k} + \frac{b+k}{c+k} + \frac{c+k}{a+k}$$

To ensure the safety of the facility, the Rigidity Index must always be greater than or equal to the total Pressure Ratio for any valid distribution of the $3$ tons of catalyst. 

What is the smallest non-negative value of the constant $k$ that ensures the inequality $a^2 + b^2 + c^2 \ge \frac{a+k}{b+k} + \frac{b+k}{c+k} + \frac{c+k}{a+k}$ holds true for all possible non-negative values of $a, b,$ and $c$ such that $a + b + c = 3$?

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
