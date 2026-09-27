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

An experimental architecture firm is testing the structural integrity of a triangular support system. They are monitoring three positive stress loads, represented by $a, b,$ and $c$.

To ensure the safety of the structure, the firm defines a "Safety Efficiency Metric" ($S$) that must not exceed a specific "Material Resistance Threshold" ($R$). 

The Material Resistance Threshold is calculated as:
\[ R = \frac{a^2+b^2+c^2}{3} \]

The Safety Efficiency Metric is calculated by taking the square of the sum of two distinct stress factors:
1. The first factor is a stability coefficient $k_{max}$ multiplied by the square root of the variance-like spread of the loads: $\sqrt{a^2+b^2+c^2-ab-bc-ca}$.
2. The second factor is a volume-to-surface ratio defined as $\frac{9abc}{(a+b+c)^2}$.

The safety requirement is expressed by the following inequality, which must hold true for all possible positive values of the loads $a, b,$ and $c$:
\[ \left(k_{max}\sqrt{a^2+b^2+c^2-ab-bc-ca}+\frac{9abc}{(a+b+c)^2}\right)^2 \leq R \]

Determine the maximum possible value of the stability coefficient $k_{max}$ that allows this safety condition to be satisfied under all circumstances.

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
