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

In a futuristic data-processing facility, an automated cooling system is controlled by the energy output levels $x$ of a central server. For the system to remain stable, the server's "Stability Index" must not be positive. 

The Stability Index is calculated by the following formula:
The numerator is defined by a primary power draw of $2^x$ units minus a fixed baseline of $16$ units.
This is divided by the product of two specific dampening factors:
1. The first dampening factor is a high-frequency regulator calculated as $9$ raised to the power of $(2x+1)$, decreased by a calibration constant of $243$.
2. The second dampening factor is a thermal surge protector calculated as the square root of the quantity: $5$ raised to the power of $\frac{x^2-3}{2}$, minus a safety threshold of $125$.

The system is operational and the Stability Index is defined only when the thermal surge protector's internal value (the expression inside the square root) is strictly positive, and the high-frequency regulator is non-zero. Under these operational constraints, the system is deemed "Stable" when the total Stability Index is less than or equal to zero.

Let $S$ be the set of all real energy levels $x$ for which the system is Stable. If $S$ is expressed as a union of disjoint intervals ordered from left to right on the real number line, calculate the sum of all finite endpoints of these intervals.

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
