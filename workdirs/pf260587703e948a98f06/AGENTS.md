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

In a specialized 2014-dimensional data storage facility, there is a central processing hub located at the origin point $O(0,0,\dots,0)$. To ensure maximum redundancy and equidistant signal transmission, a network of $2015$ servers, labeled $A_0, A_1, \dots, A_{2014}$, has been installed. These servers are positioned such that every server is exactly one unit of distance from the hub $O$. Furthermore, the servers are arranged in a perfectly symmetrical configuration known as a regular 2014-simplex, meaning the distance between any two distinct servers $A_i$ and $A_j$ is a constant $c$. 

One specific server, $A_0$, is located at the coordinate $(1, 0, 0, \dots, 0)$. 

A diagnostic probe is placed at a remote monitoring position $P$. The coordinates for $P$ alternate between the values $20$ and $14$ for all $2014$ dimensions: $P = (20, 14, 20, 14, \dots, 20, 14)$.

An engineer needs to calculate the "Total Squared Interference," which is defined as the sum of the squares of the distances from the probe $P$ to each of the $2015$ servers:
\[ S = \sum_{i=0}^{2014} (PA_i)^2 \]

Find the remainder when this total sum $S$ is divided by $1,000,000$.

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
