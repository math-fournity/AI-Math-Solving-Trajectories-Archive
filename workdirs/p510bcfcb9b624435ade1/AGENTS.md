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

In a specialized logistics simulation, two project managers, Alice and Bob, are tasked with loading cargo into a shared transport vessel. For each simulation, two parameters are defined: a capacity limit $n$ and a target weight $m$. The capacity limit $n$ must be an integer of at least 4, and the target weight $m$ is a positive integer no greater than $2n + 1$.

The simulation begins with Alice. She selects a unique weight from the set of available standardized crates $\{1, 2, \dots, n\}$ and loads it into the vessel. Bob then selects a different weight from the remaining crates in the same set. They continue to take turns, each choosing a weight that has not been used yet in that simulation. The process concludes the moment the total weight of all crates loaded into the vessel is greater than or equal to $m$. The manager who places the final crate that reaches or exceeds this target weight $m$ is declared the winner.

Consider the set $S$ of all pairs $(m, n)$ where $n$ is restricted to the values $\{10, 11\}$ and $m$ is any integer such that $1 \leq m \leq 2n + 1$. Determine the number of such pairs $(m, n)$ for which Alice has a guaranteed winning strategy regardless of Bob's choices.

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
