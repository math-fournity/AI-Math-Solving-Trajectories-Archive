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

A high-tech manufacturing firm produces specialized alloy canisters that require exactly $n$ units of raw material to be distributed among three different stabilizing agents: Alpha, Beta, and Gamma. For any production cycle of capacity $n$ (where $n$ is an integer and $n \geq 2$), the plant manager wants to create a set of $N(n)$ unique canister specifications. 

Each specification $i$ is defined by a triple of non-negative integers $(a_i, b_i, c_i)$, representing the units of Alpha, Beta, and Gamma agents used, respectively. To ensure the stability of the entire batch, the following constraints must be met:
(1) The total units of agents in every specification must sum exactly to the cycle's capacity: $a_i + b_i + c_i = n$ for all $i = 1, \ldots, N(n)$.
(2) To prevent chemical resonance, no two distinct specifications $i$ and $j$ in the set can share the same amount of any single agent. That is, if $i \neq j$, then $a_i \neq a_j$, $b_i \neq b_j$, and $c_i \neq c_j$.

Let $N(n)$ denote the maximum possible number of such unique specifications that can be included in a set for a given capacity $n$. 

Calculate the total sum of these maximum capacities across all production cycles from $n = 2$ to $n = 100$:
$$\sum_{n=2}^{100} N(n)$$

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
