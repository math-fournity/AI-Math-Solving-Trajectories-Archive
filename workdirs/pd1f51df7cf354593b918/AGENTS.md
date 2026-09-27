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

In a specialized logistics network, a cargo vessel travels between $n$ consecutive maritime waypoints, indexed from $k=0$ to $k=n$. The position of the vessel at each waypoint $k$ is recorded as an integer coordinate $a_k$, forming a sequence $\{a_0, a_1, \dots, a_n\}$.

For a given journey of length $n$, the logistics protocol defines a "valid route" $f(n)$ as one meeting the following criteria:
1. The journey must start at coordinate $a_0 = 0$ and terminate exactly at $a_n = 2n$.
2. To maintain engine efficiency, the distance covered between any two consecutive waypoints must be an integer increment of at least 1 unit but no more than 3 units (i.e., $1 \le a_{k+1} - a_k \le 3$ for $k = 0, 1, \dots, n-1$).
3. To avoid specific radar interference patterns, the vessel’s path must never span a net distance of exactly $n$ units between any two waypoints $i$ and $j$ (where $0 \le i < j \le n$). That is, $a_j - a_i \neq n$ for all possible pairs $(i, j)$.

Let $f(n)$ represent the total number of distinct sequences of coordinates that satisfy these three protocol conditions for a journey of $n$ waypoints.

Calculate the final operational value determined by the formula: $3f(16) - 2f(15) + f(10)$.

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
