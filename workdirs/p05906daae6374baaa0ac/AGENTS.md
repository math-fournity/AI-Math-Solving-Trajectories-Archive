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

A specialized logistics company is testing a new circular power grid divided into $2n$ ($n > 1$) segments. Each segment has a unique, known energy output measured in megawatts. Two engineers, Oliver and Alice, are decommissioning the grid by extracting these energy segments.

Alice begins by selecting exactly one segment from anywhere in the circle. After this initial move, Oliver takes two segments, but he must choose them such that all remaining segments in the grid still form one continuous arc. Following this, the two engineers take turns extracting two segments at a time—always ensuring the remaining pieces stay contiguous—until only one segment remains, which is claimed by whoever’s turn it is. Both Alice and Oliver act with perfect strategy to maximize the total energy they collect.

A specific configuration size $n$ is defined as "Alice-dominant" if Alice can strategically assign the unique energy values to the $2n$ segments such that she secures more than 50% of the grid’s total energy, even if she is legally required to pick the segment with the smallest energy value as her very first move.

Let $S$ be the set of all integers $n$ in the range $\{2, 3, 4, 5, 6, 7, 8, 9, 10\}$ for which $n$ is Alice-dominant. Calculate the sum of all elements in $S$.

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
