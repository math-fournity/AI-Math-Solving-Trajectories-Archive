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

A digital clockmaker is designing a rhythmic light installation controlled by a specific power output sequence $\{a_n\}_{n \geq 0}$, measured in milliwatts. On the launch day (index $n=0$), the system outputs $a_0 = 20$ mW. On the next day ($n=1$), the output is $a_1 = 100$ mW. For every subsequent day $n \geq 0$, the power output for the day $n+2$ is calculated by taking four times the previous day's output ($4a_{n+1}$), adding five times the output from the day before that ($5a_n$), and adding a constant surge of $20$ mW.

The clockmaker wants to find a specific cycle length, $h$, representing a period of days after which the power output levels repeat their values relative to a safety threshold. Specifically, the difference between the power output on any day $n+h$ and day $n$ must always be a perfect multiple of $1998$ for all possible values of $n$ starting from zero.

What is the smallest positive integer $h$ that ensures the condition $a_{n+h} \equiv a_n \pmod{1998}$ holds for every $n \geq 0$?

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
