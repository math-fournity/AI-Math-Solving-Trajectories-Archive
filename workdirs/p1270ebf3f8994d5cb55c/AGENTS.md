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

In the competitive world of high-tech manufacturing, a specialized research lab is analyzing the efficiency of dual-processor cooling systems. For a given "prime thermal constant" $p$, a configuration is defined by a pair of positive integer power levels $(a, b)$. 

A configuration is classified as "Synchronized" if it satisfies two stability criteria:
1. The combined thermal stress ratio, defined as the sum of $\frac{4a+p}{b}$ and $\frac{4b+p}{a}$, results in a whole number.
2. The kinetic energy distribution, defined as the sum of $\frac{a^2}{b}$ and $\frac{b^2}{a}$, also results in a whole number.

Let $S_p$ represent the set of all such Synchronized pairs $(a, b)$ for a specific prime constant $p$. The "Total Power Load" for a constant $p$, denoted as $f(p)$, is calculated by summing the values of $a+b$ for every pair $(a, b)$ contained in $S_p$.

The lab technicians are currently running tests on two specific setups: one with a prime thermal constant of $p=3$ and another with a prime thermal constant of $p=5$. 

Calculate the value of $f(3) + f(5)$.

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
