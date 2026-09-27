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

In a specialized digital logistics hub, there are exactly $11,449$ secure storage vaults, indexed from $0$ to $11,448$. This total capacity is defined as the square of the prime security code $p = 107$.

For any data packet $a$ that is not a multiple of $107$, the system assigns it a unique "inverse key" $a^{-1}$ within the range $0 \leq a^{-1} \leq 11,448$. This key is mathematically defined such that the product $a \cdot a^{-1}$ leaves a remainder of $1$ when divided by $11,449$.

A security researcher is investigating "symmetric interference patterns" within the hub. These patterns occur when a specific "buffer value" $b$ (where $1 \leq b \leq 5,724$) can be linked to a data packet $a$ (where $0 \leq a \leq 11,448$) such that the difference $b^2 - (a + a^{-1})$ is exactly divisible by $11,449$.

How many such positive integers $b$ exist in the range $1 \leq b \leq 5,724$ for which at least one valid data packet $a$ can be found to satisfy this interference condition?

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
