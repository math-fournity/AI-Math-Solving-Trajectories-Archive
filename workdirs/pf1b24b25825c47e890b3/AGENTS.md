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

A data analytics firm is processing a batch of 35 unique server logs, partitioned into two non-empty sets: "High-Priority" and "Legacy." Each log has a distinct processing duration. Consider the following four logical conditions regarding these durations:

1. Every High-Priority log has a longer duration than every Legacy log.
2. The number of Legacy logs with a duration shorter than the shortest High-Priority log is greater than the number of High-Priority logs with a duration shorter than the longest Legacy log.
3. The number of High-Priority logs that take longer than at least one Legacy log is greater than the number of Legacy logs that take longer than at least one High-Priority log.
4. The arithmetic mean of the durations of the Legacy logs is strictly lower than the arithmetic mean of the durations of the High-Priority logs.

Let $S = \{1, 2, 3, 4\}$ be the set of indices for these conditions. For any two distinct indices $i, j \in S$, let $a_{i,j} = 1$ if condition $i$ logically necessitates condition $j$ regardless of the specific durations assigned to the logs, and $a_{i,j} = 0$ otherwise. 

Calculate the value of the double sum:
$$\sum_{i=1}^4 \sum_{j \in S, j \neq i} a_{i,j}$$

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
