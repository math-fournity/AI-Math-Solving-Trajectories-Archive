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

A network of $N$ servers (where $N \geq 3$ and $N$ is odd) is being evaluated for processing priority. Initially, a Chief Engineer ranks the servers from 1 to $N$ based on their theoretical hardware specifications, where Rank 1 is the highest and Rank $N$ is the lowest.

To test actual performance, every server is paired against every other server exactly once in a "latency duel." In each duel, one server must be declared the winner (the one with the faster response time). A duel is classified as an "anomaly" if the server with the lower theoretical rank (the numerically higher rank) wins the match against a server with a higher theoretical rank.

After all duels are completed, a final performance list is generated. The servers are ordered based on their total number of wins. If two or more servers have the same number of wins, their relative priority is determined by the Chief Engineer’s original theoretical ranking (the one with the higher theoretical rank is placed higher on the list).

After the testing concludes, the engineers are shocked to find that the final performance list is identical to the Chief Engineer’s initial theoretical ranking in every position.

What is the maximum possible number of anomalies that could have occurred during the latency duels?

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
