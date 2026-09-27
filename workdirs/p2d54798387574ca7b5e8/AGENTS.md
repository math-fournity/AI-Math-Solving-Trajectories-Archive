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

In the city of Metron, three urban developers—Alpha, Beta, and Gamma—are designing a complex of three interconnected plazas. The dimensions of these plazas are governed by a strict zoning regulation. If we represent the areas of the intersections between the plazas as $ab$, $bc$, and $ca$, and the lengths of the plazas as $a$, $b$, and $c$, the city code dictates a "Balance Requirement": the sum of the intersection areas plus one unit of green space must exactly equal the total combined length of the plazas. Mathematically, this is expressed as:
$ab + bc + ca + 1 = a + b + c$

The lead architect is investigating a "Stability Index" for the project. He defines the "Core Tension" of the design as the square of the difference between the sum of the intersection areas and the unit of green space: $(ab + bc + ca - 1)^2$.

He compares this to the "Volume Strain," which is calculated by multiplying the product of the three lengths ($abc$) by the "Linear Excess" (the total length minus 3 units). Specifically, he seeks a universal safety constant $k$ such that the Core Tension is always greater than or equal to $k$ times the product of the three lengths and the Linear Excess.

What is the largest possible value of the constant $k$ that ensures the inequality
$(ab + bc + ca - 1)^2 \ge k \cdot abc(a + b + c - 3)$
holds true for all real-valued dimensions $a, b,$ and $c$ that satisfy the Balance Requirement?

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
