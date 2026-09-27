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

In a remote forest, a team of environmental engineers is monitoring the net carbon capture of a specialized filtration system over a series of operational days, indexed as $n = 1, 2, 3, \dots$.

For any specific day $n$, the "daily capture efficiency," denoted as $a_n$, is calculated by the following formula:
$$a_{n}=\sqrt{\frac{n}{n+2}}-\frac{n}{n+1}$$
The value $a_n$ represents the net units of carbon captured on that specific day (note that a negative value indicates a net release).

The engineers track the "cumulative storage," $S_n$, which is the total sum of the daily capture efficiencies from the first day up to and including day $n$, such that $S_{n} = \sum_{k=1}^n a_k$.

As the system operates indefinitely, the cumulative storage fluctuates. Determine the supremum (the least upper bound) of the set of all possible cumulative storage values $\{S_n : n \in \mathbb{N}_+\}$.

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
