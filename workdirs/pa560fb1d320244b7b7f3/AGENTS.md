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

In the competitive world of high-frequency automated logistics, three independent contractors—Xavier, Yolanda, and Zane—are assigned to manage three separate segments of a supply chain, each represented by a standardized time interval from $0$ to $1$. 

Each contractor must select a specific timestamp ($x$, $y$, and $z$, respectively) from their assigned interval $[0, 1]$. The primary objective of the system is to calculate a "Synergy Index," which is the product of their three chosen timestamps: $x \cdot y \cdot z$. 

However, before the operations begin, three efficiency regulators—$f$, $g$, and $h$—are established. These regulators are functions that map any chosen timestamp in the interval $[0, 1]$ to a real-valued "offset cost." Specifically:
- Regulator $f(x)$ determines an offset based on Xavier’s choice.
- Regulator $g(y)$ determines an offset based on Yolanda’s choice.
- Regulator $h(z)$ determines an offset based on Zane’s choice.

The "System Deviation" is defined as the absolute difference between the Synergy Index and the sum of the three offset costs: $|xyz - (f(x) + g(y) + h(z))|$.

The regulators aim to design their offset functions $f(t)$, $g(t)$, and $h(t)$ in such a way that they minimize the deviation, regardless of which timestamps $x, y, z$ the contractors might pick. Conversely, the system’s architecture guarantees that for any possible choice of functions $f, g, h$, there will always exist at least one set of timestamps $(x, y, z)$ that results in a System Deviation of at least $k$.

What is the maximum possible value of this guaranteed deviation constant $k$?

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
