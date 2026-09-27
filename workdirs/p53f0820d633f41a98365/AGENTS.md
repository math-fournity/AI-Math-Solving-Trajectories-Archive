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

A specialized digital scanner is designed to read infinite streams of data represented as decimal values between 0 and 1. For any given data stream $x$ in the interval $(0, 1)$, let its sequence of digits be represented as $0.a_1 a_2 a_3 \dots$.

The scanner is programmed to search for a specific "sync-code": the four-digit sequence $1, 9, 6, 6$. We define $n(x)$ as the number of digits that pass through the scanner before this four-digit sequence first appears. Specifically, $n(x)$ is the smallest non-negative integer such that the block of four consecutive digits starting immediately after the $n(x)$-th decimal place (the digits at positions $n(x)+1, n(x)+2, n(x)+3,$ and $n(x)+4$) exactly forms the number $1966$.

If a data stream $x$ is chosen uniformly at random from the continuous interval $(0, 1)$, what is the expected value of the number of digits skipped before the sync-code appears? In other words, calculate:
\[ \int_0^1 n(x) dx \]

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
