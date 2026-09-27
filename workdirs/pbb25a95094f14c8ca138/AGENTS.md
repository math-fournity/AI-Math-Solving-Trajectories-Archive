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

In a remote digital archives facility, a master encryption key $n$ consists of a sequence of 1000 non-zero data packets (digits). The protocol requires these packets to be organized into 500 distinct pairs. When the two values in each pair are multiplied together and all 500 resulting products are added, they produce a validation checksum $m$. For the key to be valid, this checksum $m$ must be an exact divisor of the total numerical value of $n$.

A security engineer generates a specific candidate for $n$ that contains 999 packets with the value 1 and exactly one packet with the value 4. To calculate the checksum $m$, the engineer groups the packets into 499 pairs of $(1, 1)$ and one final pair of $(1, 4)$. 

The numerical value of this specific 1000-digit key is expressed by the structural formula $n = \frac{10^{1000}-1}{9} + 3 \cdot 10^k$, where $k$ represents the specific positional index of the unique digit 4 within the sequence.

Find the integer value of $k$ that ensures the checksum $m$ is a divisor of $n$.

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
