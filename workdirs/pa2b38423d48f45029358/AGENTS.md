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

In a futuristic galactic network, a supercomputer uses a security protocol based on a prime frequency $p$ that is strictly greater than $2013$ THz. Two energy pulses, with integer magnitudes $a$ and $b$ units, are sent through the network. 

The system engineers have observed two specific conditions regarding these pulses:
1. The total combined magnitude $a+b$ is a perfect resonance match for the frequency $p$ (meaning $p$ divides $a+b$), but it is not strong enough to resonate with the square of the frequency (meaning $p^2$ does not divide $a+b$).
2. When the magnitudes are raised to the power of the network's legacy coefficient, $2013$, the sum of these intensified signals, $a^{2013} + b^{2013}$, is found to be perfectly divisible by $p^2$.

A technician is investigating the stability of this intensified signal and needs to determine the maximum depth of the resonance. Find the largest positive integer $n \leq 2013$ such that the sum of the intensified signals $a^{2013} + b^{2013}$ is divisible by $p^n$.

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
