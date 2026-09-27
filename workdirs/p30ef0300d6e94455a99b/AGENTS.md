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

In a remote digital archipelago, a network consists of $n$ servers ($n > 1$). These servers are linked by data cables such that every server is reachable from any other server through a sequence of cables. To prevent data echoes, the network is designed so that there are no closed loops; it is impossible to start at one server, travel through a sequence of distinct servers, and return to the starting point.

Each server $S$ has a "bandwidth capacity" defined as the total number of other servers to which it is directly connected by a single cable. Let this capacity be $x$. Within that set of $x$ direct neighbors, let $y$ be the number of neighbors that have a bandwidth capacity strictly smaller than the capacity of server $S$. The "Performance Ratio" of server $S$ is then calculated as the fraction $\frac{y}{x}$.

A network architect is analyzing the total efficiency of the archipelago, defined as the sum of the Performance Ratios of all $n$ servers. Find the smallest positive real number $t$ such that this sum is always strictly less than $tn$, regardless of the number of servers $n$ or how the cables are arranged.

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
