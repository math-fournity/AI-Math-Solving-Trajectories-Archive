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

In a remote industrial complex, three power generators—**A**, **B**, and **C**—operate at positive efficiency levels represented by $a$, $b$, and $c$. The interaction between these generators determines the system's total stability index.

The facility tracks two specific types of operational metrics:

1.  **Coupling Efficiency:** For every pair of generators, the engineers calculate a "Harmonic Ratio," defined as the ratio of their geometric mean to their arithmetic mean: $\frac{\sqrt{\text{product}}}{\text{average}}$. There are three such pairings ($a$ with $b$, $b$ with $c$, and $c$ with $a$). The sum of these ratios is given by:
    $$\sum_{\text{cyclic}} \frac{2\sqrt{ab}}{a+b}$$

2.  **Cross-Load Ratio:** The engineers also measure the relative strain of each generator against the output of the others, calculated as the efficiency of one divided by the geometric mean of the other two. The sum of these three ratios is given by:
    $$\sum_{\text{cyclic}} \frac{a}{\sqrt{bc}}$$

A safety protocol dictates that the system remains stable only if a specific linear combination of these metrics meets a threshold. Specifically, there exists a "Stability Constant" $\alpha$ such that:
$$\alpha \times (\text{Total Coupling Efficiency}) + 2 \times (\text{Total Cross-Load Ratio}) \geq 3\alpha + 6$$

Determine the greatest possible value of the constant $\alpha$ for which this safety inequality holds true for all possible positive efficiency levels $a, b, c$.

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
