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

A high-tech digital storage facility contains exactly $2^n$ unique data servers, labeled $1, 2, \ldots, 2^n$. A security architect is designing a system of "Authorized Access Groups," which is a collection $\mathcal{C}$ of specific subsets of these servers. To ensure system resilience and administrative flexibility, the collection must satisfy two strict protocols:

1. **High-Availability Requirement:** Every possible combination of exactly $2^n - 1$ servers must be registered as an Authorized Access Group in $\mathcal{C}$.
2. **Sequential Deactivation Protocol:** For every non-empty group $C$ already in the collection $\mathcal{C}$, there must exist at least one specific server $c \in C$ such that if that server is removed from the group, the remaining set of servers $C \setminus \{c\}$ is also a registered Authorized Access Group in $\mathcal{C}$.

Note that the empty set (a group containing no servers) may be included in the collection to satisfy the deactivation protocol for single-server groups.

Calculate the minimum possible number of Authorized Access Groups that the collection $\mathcal{C}$ must contain to satisfy both protocols simultaneously. Express your answer in terms of $n$.

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
