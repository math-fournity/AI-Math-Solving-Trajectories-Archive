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

In a specialized logistics center, a technician must organize 12 distinct shipping containers, labeled with identification numbers $\{1, 2, \ldots, 12\}$, into a single linear queue $p = (a_1, a_2, \ldots, a_{12})$. 

The "Total Transit Friction" of a queue, denoted as $S_p$, is calculated by summing the absolute differences between the identification numbers of all adjacent containers: $S_p = \sum_{i=1}^{11} |a_i - a_{i+1}|$.

A queue is classified as "Optimistic" if every container located between two others has an identification number strictly greater than at least one of its immediate neighbors. That is, $a_i > \min(a_{i-1}, a_{i+1})$ for every $i \in \{2, 3, \ldots, 11\}$.

Determine the sum $M + N + O + Q$, where:
- $M$ is the maximum possible Total Transit Friction $S_p$ achievable by any permutation of the 12 containers.
- $N$ is the total number of permutations that result in this maximum friction $M$.
- $O$ is the total number of unique Optimistic permutations possible.
- $Q$ is the number of Optimistic permutations that achieve the highest possible Total Transit Friction specifically among the set of all Optimistic permutations.

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
