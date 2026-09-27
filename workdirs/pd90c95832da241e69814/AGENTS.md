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

In a futuristic industrial zone, the "2013 Global Power Grid" is managed by 16 different regional control stations. Each station is identified by a unique ID number $n$, where $n$ is a positive integer divisor of 2013.

Every control station $n$ has a specific "Efficiency Metric" denoted as $s(n)$. To calculate this metric, the station identifies all integer-coded maintenance drones numbered $k$ such that $1 \le k \le n$. The station only includes a drone in its metric calculation if the drone's ID $k$ shares no common factors with the station's ID $n$ (i.e., $\gcd(k, n) = 1$). The metric $s(n)$ is then defined as the sum of the squares of the ID numbers of all such drones assigned to that station.

To evaluate the overall system stability, engineers must calculate a "Normalized Load Factor" for each station, defined as the ratio of its Efficiency Metric to the square of its ID number, or $\frac{s(n)}{n^2}$.

The Project Director requires the total system performance value, which is the sum of these Normalized Load Factors across all 16 stations (all $n$ that divide 2013).

Find the greatest integer that does not exceed the total system performance value:
\[ \sum_{n \mid 2013} \frac{s(n)}{n^2} \]

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
