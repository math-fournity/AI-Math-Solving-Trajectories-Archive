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

A specialized team of $n$ environmental engineers (where $n$ is an odd integer and $n \ge 3$) is tasked with monitoring a circular sequence of $n$ filtration stations, indexed $1$ through $n$. Each engineer is assigned a unique integer power rating from the set $\{1, 2, \dots, n\}$. Let $a_i$ represent the power rating of the engineer stationed at position $i$.

The "Net Filtration Impact" $S_i$ at any station $i$ is calculated using a fluctuating alternating current formula over all $n$ engineers, starting from the $i$-th position and moving clockwise around the circle. Specifically, for each $i \in \{1, \dots, n\}$, the impact is defined as:
$S_i = a_i - a_{i+1} + a_{i+2} - a_{i+3} + \dots + a_{i+n-1}$
(where the indices are treated cyclically modulo $n$).

A configuration of engineers is considered "Efficient" if the Net Filtration Impact $S_i$ is strictly greater than zero for every station $i=1, \dots, n$. An odd integer $n \ge 3$ is classified as "Sustainable" if there exists at least one assignment of the power ratings $\{1, \dots, n\}$ to the stations that results in an Efficient configuration.

Let $N$ be the set of all such Sustainable integers. Calculate the sum of all elements in the set $\{n \in N : 3 \le n \le 50\}$.

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
