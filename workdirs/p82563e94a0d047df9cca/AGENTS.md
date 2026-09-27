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

A specialized digital server farm is organized as an infinite grid of processing nodes, corresponding to every lattice point with non-negative coordinates $(x, y)$ in the Cartesian plane. At the start of an experiment, every single node contains exactly one active data packet.

For any given positive integer $n$, the "Monitoring Zone" of a specific node $c$ is defined as the set of all other nodes located within an axis-aligned $(2n+1) \times (2n+1)$ square centered at $c$. The total number of nodes in this Monitoring Zone (excluding $c$ itself) is denoted as $N$.

A data packet is classified based on the status of its Monitoring Zone:
1. It is **Underloaded** if the number of active packets in its zone is strictly less than $N/2$.
2. It is **Overloaded** if the number of active packets in its zone is strictly greater than $N/2$.
3. It is **Balanced** if the number of active packets in its zone is exactly equal to $N/2$.

The system operates in discrete one-minute cycles. At the end of every minute, all Underloaded packets are automatically deleted from the server farm simultaneously. This automated cleanup repeats every minute until a steady state is reached where no Underloaded packets remain.

Let $C(n)$ represent the total number of Balanced packets remaining in the server farm once the system stabilizes. Calculate the value of the following sum:
$$\sum_{n=1}^{10} C(n)$$

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
