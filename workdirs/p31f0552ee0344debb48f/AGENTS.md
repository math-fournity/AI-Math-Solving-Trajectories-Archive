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

In a specialized digital signal processing facility, an engineer is analyzing a sequence of 2021 data packets, indexed from $k = 1$ to $k = 2021$. Each packet carries a raw energy value calculated as the cube of its index, $k^3$. 

The facility uses a binary parity filter to determine the phase of each packet. For every index $k$, the engineer calculates $S_2(k)$, which is the total count of '1' bits in the binary representation of $k$. (For instance, if $k=13$, its binary form is $1101_2$, so $S_2(13) = 1+1+0+1 = 3$).

The phase-adjusted energy of a packet is determined by the parity of this bit-sum:
- If $S_2(k)$ is even, the packet retains a positive charge: $+k^3$.
- If $S_2(k)$ is odd, the packet receives a negative charge: $-k^3$.

The total resonance of the system, $T$, is defined as the sum of these phase-adjusted energy values for all packets from $k=1$ to $k=2021$. That is, $T = \sum_{k=1}^{2021} (-1)^{S_2(k)} k^3$.

To calibrate the system's final output, the engineer needs to find the remainder when the total resonance $T$ is divided by the number of packets, 2021. Determine this remainder.

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
