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

A specialized desalination plant operates three independent filtration modules with processing capacities $x$, $y$, and $z$ (measured in thousands of liters per hour, where each is a non-negative value).

The relative efficiency of the plant is determined by the sum of three "coupling ratios" representing how the modules interact in sequence: the first module’s capacity relative to the sum of the first and second, the second relative to the sum of the second and third, and the third relative to the sum of the third and update. This sum is expressed as:
$\frac{x}{x+y} + \frac{y}{y+z} + \frac{z}{z+x}$

To ensure structural stability, the plant must also account for a "variance penalty" based on a stability constant $k$. This penalty is calculated by multiplying $k$ by the ratio of the sum of the squares of the individual capacities to the square of the total combined capacity:
$\frac{k(x^2 + y^2 + z^2)}{(x+y+z)^2}$

The plant’s safety protocol dictates that the total system value—the sum of the coupling ratios and the variance penalty—must always be greater than or equal to a fixed safety threshold. This threshold is defined as the sum of a baseline constant $1.5$ and one-third of the stability constant $k$.

Find the largest possible value of the stability constant $k$ such that this safety protocol is satisfied for all possible non-negative capacities $x, y,$ and $z$.

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
