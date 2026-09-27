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

In a specialized research laboratory, a team of $n$ robotic sensors is tasked with monitoring deep-sea pressure levels. Each sensor $i$ (where $1 \leq i \leq n$) is calibrated to a unique, non-zero real frequency $a_i$.

The laboratory protocols require a highly specific symmetry for the system to remain stable. Every sensor undergoes a transformation based on its position in the sequence: if a sensor is in an even position $i$, its frequency is modified by adding $1/a_i$ to its original value; if it is in an odd position $i$, its frequency is modified by subtracting $1/a_i$ from its original value. In other words, the new value for each sensor is $a_i + \frac{(-1)^i}{a_i}$.

The stability condition for the laboratory is met if and only if the resulting set of $n$ modified values is exactly identical to the original set of $n$ frequencies $\{a_1, a_2, \ldots, a_n\}$.

Let $S$ be the set of all positive integers $n$ for which it is possible to choose such distinct, non-zero frequencies $a_1, a_2, \ldots, a_n$ that satisfy this stability condition. Calculate the sum of the four smallest elements contained in the set $S$.

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
