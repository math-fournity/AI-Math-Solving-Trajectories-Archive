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

In a futuristic laboratory, a team of engineers is testing three distinct energy-regulating devices: the **Linear-Square-Square (LSS) Core**, the **Square-Linear-Square (SLS) Core**, and the **Square-Square-Linear (SSL) Core**. These devices regulate three physical parameters—$x, y,$ and $z$—measured in standard units.

To maintain system stability, the parameters must satisfy three simultaneous calibration laws:
1. The sum of $x$, the square of $y$, and the square of $z$ must equal a target stability constant $a$.
2. The sum of the square of $x$, the value of $y$, and the square of $z$ must equal the same target stability constant $a$.
3. The sum of the square of $x$, the square of $y$, and the value of $z$ must equal the same target stability constant $a$.

Let $N(a)$ represent the total number of unique valid configurations of $(x, y, z)$ that satisfy these three laws for a given value of $a$.

The engineering team needs to run three different tests where the target stability constant is set to $a = 2$, $a = 1$, and $a = 0$, respectively. 

Calculate the total number of configurations across all three tests, specifically the value of $N(2) + N(1) + N(0)$.

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
