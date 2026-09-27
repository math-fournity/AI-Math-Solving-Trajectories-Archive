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

In a remote digital ecosystem, three distinct data packets—Alpha ($x$), Beta ($y$), and Gamma ($z$)—contain a total of 2016 gigabytes of information. Initially, at Step 0, each packet contains a positive integer number of gigabytes ($x_0, y_0, z_0 \in \mathbb{Z}^+$).

The ecosystem undergoes a periodic "rebalancing cycle." Every minute (Step $n$), the size of each packet is updated based on the sizes from the previous minute (Step $n-1$) according to the following protocol:
- The new size of Alpha ($x_n$) is the sum of the previous sizes of Beta and Gamma minus the previous size of Alpha.
- The new size of Beta ($y_n$) is the sum of the previous sizes of Gamma and Alpha minus the previous size of Beta.
- The new size of Gamma ($z_n$) is the sum of the previous sizes of Alpha and Beta minus the previous size of Gamma.

A system crash occurs if any packet’s size becomes a negative value. Determine the minimum number of minutes ($k$) that must pass to guarantee that at least one of the packets ($x_k, y_k, \text{ or } z_k$) has become negative, regardless of the initial positive integer distribution of the 2016 gigabytes.

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
