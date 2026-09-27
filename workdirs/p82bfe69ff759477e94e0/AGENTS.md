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

In the city of Arithmos, a data packet is classified as a "Downlink Stream" if its initial size $S$ is an integer greater than 1. The stream undergoes a systematic compression process: if the current packet size is $a_n$, the next packet size $a_{n+1}$ is calculated by dividing $a_n$ by its smallest prime factor $p_n$. This compression continues step-by-step until the packet size reaches exactly 1, at which point the stream terminates. For example, a stream starting at 864 follows the sizes 864, 432, 216, 108, 54, 27, 9, 3, 1, while a stream starting at 2022 follows 2022, 1011, 337, 1.

A Downlink Stream is designated as "High-Density" if at least one packet size in the sequence (including the initial size) is a perfect cube strictly greater than 1. In the examples above, the stream starting at 864 is High-Density because it contains the size $27 = 3^3$, whereas the stream starting at 2022 is not High-Density because none of its terms are perfect cubes greater than 1.

Calculate the total number of distinct High-Density Downlink Streams whose initial packet size $S$ is less than 2022.

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
