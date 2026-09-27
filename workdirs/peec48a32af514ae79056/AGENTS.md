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

A specialized digital encryption facility operates using a security protocol based on a prime modulus $p = 491$. The facility manages a database of digital keys, where each key is represented as a $k$-tuple of integers $(a_1, a_2, \dots, a_k)$ such that each $0 \leq a_i < p$. Let $S$ be the complete set of all such possible $k$-tuples.

To verify data integrity, the system uses a "Correlation Metric" between any two keys $u = (a_1, \dots, a_k)$ and $v = (b_1, \dots, b_k)$, defined by the sum of products:
$$\langle u, v \rangle = \sum_{i=1}^{k} a_i b_i \pmod{p}$$

A transformation function $f: S \rightarrow S$ is classified as "Securely Preserving" if, for every possible pair of keys $u, v \in S$, the Correlation Metric of their transformed versions is identical to the Correlation Metric of the original keys:
$$\langle f(u), f(v) \rangle \equiv \langle u, v \rangle \pmod{p}$$

Let $m(k)$ represent the total number of unique Securely Preserving functions that can exist for a given tuple length $k$. 

Calculate the remainder when the sum of the number of these functions for all dimensions from 1 to $p$, specifically $m(1) + m(2) + m(3) + \dots + m(491)$, is divided by $488$.

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
