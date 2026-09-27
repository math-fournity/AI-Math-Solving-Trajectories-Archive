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

In a specialized logistics network, there are $n$ servers, labeled $S_1, S_2, \dots, S_n$, where $n \ge 8$. These servers establish two-way data links with one another. The network architecture is defined by the following connection protocols:

1. For each server $S_k$ in the initial range where $1 \le k \le n-6$, the server is connected to exactly $k+3$ other servers.
2. The three specific servers $S_{n-5}, S_{n-4},$ and $S_{n-3}$ are each connected to exactly $n-2$ other servers.
3. The final three servers $S_{n-2}, S_{n-1},$ and $S_n$ are each connected to all other $n-1$ servers in the network.

A connection is always mutual (if $S_a$ is connected to $S_b$, then $S_b$ is connected to $S_a$) and no server connects to itself.

Determine the sum of all possible integer values of $n \ge 8$ for which such a network configuration can physically exist.

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
