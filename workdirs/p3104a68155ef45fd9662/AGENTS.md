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

In a specialized logistics facility, a team is organizing numbered cargo crates labeled $\{1, 2, \dots, R\}$. The manager intends to distribute every single crate into one of two different warehouses, labeled Alpha and Beta.

The facility operates under a specific "Loading Rule": a warehouse is considered "Balanced" if there exist $20$ crates stored within that same warehouse (let’s call their weights $x_1, x_2, \dots, x_{20}$) such that the sum of the weights of the first $19$ crates exactly equals the weight of the $20$th crate (i.e., $x_1 + x_2 + \dots + x_{19} = x_{20}$). Note that the crates used to satisfy this rule do not have to be distinct; the same crate can be used for multiple variables $x_i$ if its weight fits the equation.

The goal of the manager is to determine the threshold $r(20)$, which is the smallest total number of crates $R$ such that no matter how the crates $\{1, 2, \dots, R\}$ are distributed between Warehouse Alpha and Warehouse Beta, at least one of the warehouses will inevitably be "Balanced."

Find the value of $r(20)$.

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
