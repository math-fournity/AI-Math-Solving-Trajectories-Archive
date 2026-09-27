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

A specialized deep-space research station tracks cosmic radiation pulses over a sequence of $n$ consecutive days, labeled $k = 1, 2, \dots, n$. For each day $k$, the station records the "Cumulative Resonance" of the signal, which is mathematically defined as the factorial of the day number, $k!$.

The station’s computer monitors specific "Prime Frequencies" $p$. For a given frequency $p$, the computer calculates the "Polarity" of each day's signal. The Polarity for day $k$ is determined by finding the highest power of $p$ that divides the Cumulative Resonance $k!$. If this exponent is even, the Polarity is $+1$; if the exponent is odd, the Polarity is $-1$.

A Prime Frequency $p$ is classified as "Dominantly Negative" for a period of $n$ days if the sum of the Polarities from day 1 to day $n$ is strictly less than zero.

Determine the smallest positive integer $n$ such that there are at least two distinct odd Prime Frequencies that are Dominantly Negative for that $n$-day period.

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
