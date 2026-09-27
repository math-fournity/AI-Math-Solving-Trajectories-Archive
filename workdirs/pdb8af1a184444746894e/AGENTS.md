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

The number $d_{1}d_{2}\dots d_{9}$ has nine (not necessarily distinct) decimal digits. The number $e_{1}e_{2}\dots e_{9}$ is such that each of the nine 9-digit numbers formed by replacing just one of the digits $d_{i}$ is $d_{1}d_{2}\dots d_{9}$ by the corresponding digit $e_{i}$ ($1 \leq i \leq 9$) is divisible by 7. The number $f_{1}f_{2}\dots f_{9}$ is related to $e_{1}e_{2}\dots e_{9}$ is the same way: that is, each of the nine numbers formed by replacing one of the $e_{i}$ by the corresponding $f_{i}$ is divisible by 7. Show that, for each $i$, $d_{i}-f_{i}$ is divisible by 7. [For example, if $d_{1}d_{2}\dots d_{9} = 199501996$, then $e_{6}$ may be 2 or 9, since $199502996$ and $199509996$ are multiples of 7.]

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
