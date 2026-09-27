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

In a remote digital archipelago, there are $2m$ distinct server nodes arranged in a global network, where $m$ is a positive integer such that $m \geq 17$. The network administrators must perform a complete synchronization protocol consisting of $2m - 1$ distinct phases. 

In each phase, the $2m$ nodes are paired up into $m$ exclusive pairs to exchange data packets. The protocol is designed such that by the end of the $2m - 1$ phases, every single node has exchanged data exactly once with every other node in the network.

The system security officer is monitoring the formation of "isolated clusters." An isolated cluster is defined as any set of 4 specific nodes. The officer is looking for a state where, within such a set of 4 nodes, the number of data exchanges that have occurred between them is exactly 1. If a set of 4 nodes has either 0 exchanges (none have talked to each other) or at least 2 exchanges among them, the set is considered "stable."

Find the minimum number of phases $n$ that must be completed to guarantee that there exists a synchronization schedule where, after $n$ phases, every possible set of 4 nodes in the network is "stable."

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
