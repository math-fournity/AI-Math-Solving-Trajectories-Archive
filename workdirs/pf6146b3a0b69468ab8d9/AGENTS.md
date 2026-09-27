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

A high-security data center has 17 server nodes, labeled with unique identification codes from the set $\{1, 2, 3, \dots, 17\}$. These nodes are arranged in a physical ring topology, where each node is connected to the next one in a specific sequence $(a_1, a_2, \dots, a_{17})$, and the last node $a_{17}$ connects back to the first node $a_1$ to complete the loop.

The system engineers are measuring the "potential difference" between adjacent nodes in the sequence. For every pair of adjacent nodes $(a_i, a_{i+1})$, the difference in their identification codes is calculated as $(a_i - a_{i+1})$. For the final connection, the difference is $(a_{17} - a_1)$.

To calculate the system's total "entropy product," the engineers multiply all seventeen of these differences together. This resulting product must exactly equal $2^n$, where $n$ is a positive integer representing the system's efficiency exponent.

Given that the identification codes $a_1, a_2, \dots, a_{17}$ must be a permutation of the integers from 1 to 17, find the maximum possible value of the exponent $n$.

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
