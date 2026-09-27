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

Two people, A and B, play a game. A first writes down a sequence of length $n = 6$ consisting of the letters $\mathrm{L}$ and $\mathrm{R}$. Then B chooses $n$ distinct prime weights $p_1 < p_2 < \dots < p_6$. B places these weights on a balance scale one by one. After each weight is placed, B writes down 'L' if the balance tilts to the left and 'R' if it tilts to the right (once a weight is placed, it is not removed). B wins if the sequence of $n$ letters matches the sequence written by A.

If A writes the sequence $(L, R, R, L, L, L)$, and B uses a strategy where the weights are placed in a specific order $(a_1, a_2, a_3, a_4, a_5, a_6)$ where each $a_i \in \{p_1, \dots, p_6\}$, such that B wins, determine the indices $k_1, k_2, k_3, k_4, k_5, k_6$ where $a_i = p_{k_i}$. Calculate the value of the integer $V = \sum_{i=1}^{6} i \cdot k_i$.

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
