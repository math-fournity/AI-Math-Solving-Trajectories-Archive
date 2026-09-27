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

In a remote industrial refinery, three storage tanks hold varying quantities of liquid chemicals, represented by the non-negative real volumes $x$, $y$, and $z$ (measured in kiloliters). 

The efficiency of the refining process is evaluated by comparing two different methods of mixing. The "Primary Yield" is defined as the average of the cubed volumes of the three tanks, $\frac{x^3 + y^3 + z^3}{3}$. The "Baseline Output" is defined as the product of the three volumes, $xyz$.

A specialized chemical engineer observes that the Primary Yield always meets or exceeds the Baseline Output. However, they discover that a "Volatility Surcharge" can be added to the Baseline Output without exceeding the Primary Yield. This surcharge is calculated as a constant factor $\alpha$ multiplied by the absolute product of the differences between the three tank volumes: $|(x-y)(y-z)(z-x)|$.

The refinery operates under the safety constraint that the following inequality must hold for any possible non-negative volumes $x, y$, and $z$:
$$\frac{x^3 + y^3 + z^3}{3} \ge xyz + \alpha |(x-y)(y-z)(z-x)|$$

Determine the maximal real constant $\alpha$ that ensures this safety constraint is never violated.

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
