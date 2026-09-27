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

In a specialized optics laboratory, a laser beam is split to track two automated sensors, $P$ and $Q$, moving along the axes of a coordinate plane. For a fixed angle $\theta \in (0, \frac{\pi}{2})$, we define $a(\theta)$ as the minimum power threshold required for a specific safety calibration to be valid. This threshold $a$ must satisfy two operational constraints:

First, the power must be high enough such that the sum of the normalized ranges, defined by the expression $\frac{\sqrt{a}}{\cos \theta} + \frac{\sqrt{a}}{\sin \theta}$, is strictly greater than $1$.

Second, there must exist a positioning coordinate $x$ within the interval $\left[1 - \frac{\sqrt{a}}{\sin \theta}, \frac{\sqrt{a}}{\cos \theta}\right]$ such that the spatial interference, calculated by the sum of squares $\left[(1-x) \sin \theta - \sqrt{a - x^2 \cos^2 \theta}\right]^2 + \left[x \cos \theta - \sqrt{a - (1-x)^2 \sin^2 \theta}\right]^2$, does not exceed the power threshold $a$.

An efficiency function for this optical system is defined as $f(\theta) = \frac{\sin^2 \theta \cos^2 \theta}{a(\theta)}$.

Calculate the exact value of $f\left(\frac{\pi}{12}\right)$.

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
