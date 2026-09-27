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

A network of $n$ server racks is arranged in a closed data ring. The number of active data packets in each rack $R_i$ is tracked. To optimize the system, a diagnostic protocol is applied to every set of four adjacent racks $(R_i, R_{i+1}, R_{i+2}, R_{i+3})$ for $i = 1, 2, \dots, n$ (where the indices wrap around from $n$ back to $1$).

The protocol follows a specific parity rule for each set:
- If the total sum of packets in the four chosen racks is an odd number, the system draws 1 packet away from each of those four racks.
- If the total sum of packets in the four chosen racks is an even number, the system injects 1 additional packet into each of those four racks.

After the protocol has been executed exactly once for every one of the $n$ possible sets of four consecutive racks, it is observed that the total number of packets across the entire ring of $n$ racks has not changed from its initial value.

Let $S$ be the set of all possible integer values for the number of racks $n$ such that $40 < n < 60$. Find the sum of all elements in $S$.

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
