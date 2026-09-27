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

In a specialized logistics hub, two automated sorting lines, Line $M$ and Line $N$, operate on cyclical schedules. Line $M$ completes one full sorting cycle every $m$ minutes, and Line $N$ completes one full cycle every $n$ minutes, where $m$ and $n$ are positive integers. The "Synchronization Interval" of the hub is defined as the least amount of time required for both lines to finish a cycle simultaneously, calculated as the least common multiple of their cycle durations.

A system engineer is testing "delay shifts." If an identical delay of $k$ minutes ( where $k$ is any positive integer) is added to both cycle durations, the new cycle times become $m+k$ and $n+k$. 

The engineer identifies a specific set of "Stable Pairs" $(m, n)$. A pair is considered stable if the original Synchronization Interval is always less than or equal to the shifted Synchronization Interval, regardless of the value of $k$ chosen. Specifically:
$$\text{lcm}(m, n) \leq \text{lcm}(m + k, n + k) \text{ for all } k \in \{1, 2, 3, \dots\}$$

Let $S$ be the set of all such Stable Pairs $(m, n)$ where the cycle durations are constrained such that $1 \leq m \leq 10$ and $1 \leq n \leq 10$. 

Calculate the total sum of the values $m + n$ for all unique pairs $(m, n)$ contained in set $S$.

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
