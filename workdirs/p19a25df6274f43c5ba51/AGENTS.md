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

In a specialized logistics network, a shipment of $3p$ metric tons of raw material (where $p$ is a prime number greater than 3) must be distributed among six different processing hubs: Alpha, Bravo, Charlie, Delta, Echo, and Foxtrot. Each hub receives a positive integer amount of material, denoted as $a, b, c, d, e,$ and $f$ respectively.

The network is governed by a series of "efficiency ratios" between adjacent pairs of hubs. For the system to remain stable, the following five ratios must all result in whole numbers:

1. The combined material of Alpha and Bravo divided by the combined material of Charlie and Delta.
2. The combined material of Bravo and Charlie divided by the combined material of Delta and Echo.
3. The combined material of Charlie and Delta divided by the combined material of Echo and Foxtrot.
4. The combined material of Delta and Echo divided by the combined material of Foxtrot and Alpha.
5. The combined material of Echo and Foxtrot divided by the combined material of Alpha and Bravo.

Based on these constraints, how many unique distribution sequences $(a, b, c, d, e, f)$ are possible for the $3p$ tons of material?

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
