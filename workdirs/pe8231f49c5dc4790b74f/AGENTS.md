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

In the competitive world of artisanal perfume manufacturing, three distillers—Aiden, Bella, and Cassian—produce unique essential oils. The volume of their individual batches, denoted by non-negative real numbers $a, b,$ and $c$, is strictly governed by a regulatory quality constraint: the sum of all pairwise products of their volumes, plus the product of all three volumes, must exactly equal 4 ($ab + bc + ca + abc = 4$).

A chemical engineer is studying a specific stability index for these oil blends. For any fixed chemical reagent level $r$, the stability of the mixture is defined by the product of three adjusted values: $(r + ab)(r + bc)(r + ca)$. For the mixture to be considered "commercially viable," this stability index must be greater than or equal to a baseline threshold defined as $(r + 1)^3$.

The engineer discovers that this viability condition holds for every possible valid combination of $a, b,$ and $c$ only when $r$ is within specific ranges. 

Let $R$ be the smallest positive real number such that for all $r \geq R$, the viability inequality is always satisfied. 
Let $L$ be the largest negative real number such that for all $r \leq L$, the viability inequality is always satisfied.

Calculate the value of $(2R - 3)^2 + (2L + 1)^2$.

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
