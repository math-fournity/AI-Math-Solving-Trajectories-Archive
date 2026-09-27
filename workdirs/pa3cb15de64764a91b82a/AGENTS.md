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

In the specialized logistics hub of Sector 11 (represented by the constant $a=11$), two automated transport beams operate on different calibration frequencies. The "Alpha Beam" processes cargo at a rate of $11 + \sqrt{11}$ units per second, while the "Beta Beam" processes cargo at a rate of $11 - \sqrt{11}$ units per second.

A technician is monitoring the synchronization of these beams over integer time intervals. Let $m$ and $n$ represent positive integer durations in seconds for the Alpha and Beta beams, respectively.

First, the technician identifies the set $S$, which consists of all pairs of durations $(m, n)$ where the two beams have the exact same "offset"—defined as the fractional portion of the total cargo processed during their respective runs. Specifically, $(m, n) \in S$ if the fractional part of $m(11 + \sqrt{11})$ is equal to the fractional part of $n(11 - \sqrt{11})$.

Next, the technician identifies the set $T$, which consists of all pairs of durations $(m, n)$ where the two beams have completed the exact same number of "whole units"—defined as the floor of the total cargo processed. Specifically, $(m, n) \in T$ if the integer part of $m(11 + \sqrt{11})$ is equal to the integer part of $n(11 - \sqrt{11})$.

Calculate the total number of valid pairs across both sets, expressed as $|S| + |T|$.

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
