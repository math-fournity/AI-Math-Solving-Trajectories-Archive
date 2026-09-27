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

In the competitive world of specialized chemical manufacturing, three industrial synthesis labs—Alpha, Beta, and Gamma—operate under strict efficiency constraints based on their respective output volumes $a$, $b$, and $c$ (measured in thousands of liters). Due to resource sharing and equipment limitations, their outputs must satisfy the following stability protocols:
1. Alpha’s output ($a$) must be no less than the product of Beta’s output ($b$) and the square of Gamma’s output ($c^2$).
2. Beta’s output ($b$) must be no less than the product of Gamma’s output ($c$) and the square of Alpha’s output ($a^2$).
3. Gamma’s output ($c$) must be no less than the product of Alpha’s output ($a$) and the square of Beta’s output ($b^2$).

A consultant defines the "System Waste Metric" $E$ as the product of the three total outputs multiplied by the three "surplus margins" of the labs. Specifically:
$$E = abc \cdot (a - bc^2) \cdot (b - ca^2) \cdot (c - ab^2)$$

Given that all output volumes $a, b,$ and $c$ must be strictly positive, determine the maximum possible value that this Waste Metric $E$ can achieve.

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
