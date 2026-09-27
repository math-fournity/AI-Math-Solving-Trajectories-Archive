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

In a specialized metallurgical refinery, two distinct rare-earth metals, Grade A and Grade B, are processed into a high-density alloy. The mass of Grade A is represented by $a$ tons and the mass of Grade B by $b$ tons, where both quantities are positive.

The theoretical structural integrity of the resulting alloy is determined by the total volume of the components, calculated by the sum of their cubes: $a^3 + b^3$.

Engineering safety protocols require that this integrity value must always be greater than or equal to a specific "stress threshold." This threshold is calculated by taking twice the product of the two masses ($2ab$) and multiplying it by a generalized power mean of the masses. Specifically, this mean is the $k$-th root of the average of the $k$-th powers of the masses, expressed as $\sqrt[k]{\frac{a^k + b^k}{2}}$.

Given that the safety inequality $a^3 + b^3 \geq 2ab \sqrt[k]{\frac{a^k + b^k}{2}}$ must be satisfied for all possible positive quantities of $a$ and $b$, what is the largest possible constant value of $k$ that maintains this structural requirement?

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
