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

In a remote logistics network, there are $n$ supply depots located at integer coordinates $1, 2, \dots, n$ along a straight road. A cargo manifest $(a_1, a_2, \dots, a_n)$ is a permutation of the values $(1, 2, \dots, n)$, where $a_k$ represents the number of resource units stored at depot $k$.

Three logistics companies—Alpha, Bravo, and Charlie—must each choose a headquarters location ($x_A, x_B, x_C$, respectively) from the available integer coordinates $\{1, 2, \dots, n\}$. The resources at each depot $k$ are distributed according to proximity: the $a_k$ units are divided equally among the companies whose headquarters are at the minimum distance to depot $k$. Specifically, if a company is the unique closest to depot $k$, it claims all $a_k$ units; if two or three companies are tied for the minimum distance, they split the $a_k$ units equally.

A company is defined as "unhappy" if there exists an alternative coordinate $x' \in \{1, 2, \dots, n\}$ such that, by moving its headquarters to $x'$ while the other two companies remain at their current locations, it would receive a strictly greater total number of resource units.

Let $S$ be the set of all integers $n \geq 2$ for which there exists at least one permutation of resources $(a_1, a_2, \dots, a_n)$ and a selection of headquarters $x_A, x_B, x_C$ such that all three companies are simultaneously happy (not unhappy). 

Find the sum of all elements in the set $S$.

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
