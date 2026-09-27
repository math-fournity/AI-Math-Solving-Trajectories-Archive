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

A boutique clockmaker is designing a series of modular circular gears, each with a specific number of teeth $n$, where $1 \le n \le 100$. A gear is considered "perfectly adaptable" if it satisfies a specific engineering requirement for every possible transmission ratio $m$ that shares no common factors with $n$ (where $1 \le m < n$).

The requirement is as follows: for a given ratio $m$, there must exist a reconfiguration of the gear's $n$ teeth positions, represented by a one-to-one mapping $\pi$ of the set $\{1, 2, \ldots, n\}$ onto itself. This reconfiguration must be such that applying the mapping twice in succession is equivalent to shifting the position by the transmission ratio $m$. Specifically, for every tooth position $k \in \{1, 2, \ldots, n\}$, the mapping must satisfy the condition:
$$\pi(\pi(k)) \equiv m \cdot k \pmod{n}$$

Let $S$ be the set of all such integers $n$ in the range $1 \le n \le 100$ that possess this property for every valid $m$. Calculate the sum of all the integers in $S$.

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
