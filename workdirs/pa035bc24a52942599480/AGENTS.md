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

In the competitive world of high-tech logistics, three regional shipping hubs—Alpha, Beta, and Gamma—handle a specific number of cargo containers denoted by the natural numbers $a$, $b$, and $c$, respectively. These hubs operate under a strict "Capacity Cycle" governed by an efficiency constant $k$, which is a natural number greater than 1.

The network is interconnected by the following structural rules:
1. The inventory at Alpha ($a$) must be a factor of the inventory at Beta raised to the power of $k$ ($b^k$).
2. The inventory at Beta ($b$) must be a factor of the inventory at Gamma raised to the power of $k$ ($c^k$).
3. The inventory at Gamma ($c$) must be a factor of the inventory at Alpha raised to the power of $k$ ($a^k$).

A central auditor is investigating the total systemic load of the network. They are looking for a specific integer exponent $n$ (where $n$ is a function of $k$) that guarantees the combined product of the hubs' inventories ($abc$) will always divide the sum of their inventories raised to that power, $(a+b+c)^n$, regardless of the specific values of $a, b,$ and $c$.

Based on the constant $k$, what is the smallest value of $n$ such that this divisibility condition is guaranteed to hold for all possible inventories satisfying the rules?

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
