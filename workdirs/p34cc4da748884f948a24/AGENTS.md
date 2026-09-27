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

In the digital city of Bit-Topia, the central mainframe operates based on a specific capacity constant \( n \), defined exactly as \( 2^{2015} - 1 \). This mainframe processes data packets of size \( x \), where \( x \) can be any integer such that \( 1 \leq x < n \).

Every time a packet \( x \) is processed, the system triggers a diagnostic routine to calculate the "Entropy Index," denoted as \( f_{n}(x) \). This index is determined by comparing the packet \( x \) with the remaining capacity \( n-x \) and the total capacity \( n \). Specifically, the index is the sum of a series of values calculated for every prime number \( p \). For each prime, the system calculates the sum of the digits of \( n-x \) in base \( p \), adds the sum of the digits of \( x \) in base \( p \), and then subtracts the sum of the digits of \( n \) in base \( p \). The total Entropy Index \( f_{n}(x) \) is the sum of these results over all primes \( p \).

The system’s "Stability Protocol" is activated only when the resulting Entropy Index \( f_{n}(x) \) is a multiple of 4. 

Let \( N \) be the total number of possible packet sizes \( x \) that trigger this Stability Protocol. What is the remainder when \( N \) is divided by 1000?

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
