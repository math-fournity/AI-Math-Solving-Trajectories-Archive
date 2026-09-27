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

A network of $n$ regional power stations is being audited for efficiency. Each station $i$ (where $i=1, 2, \dots, n$) is assigned a control dial $x_i$, which can be set to any intensity level in the continuous range from $0$ to $1$, inclusive.

The total energy output of the network is calculated by a specific performance index. Each station $i$ contributes an internal efficiency value $f_i(x_i)$ based on its local dial setting, where $f_i$ can be any real-valued function. From the sum of these $n$ efficiency values, a "coupling loss" is subtracted. This loss is defined as the product of all dial settings: $x_1 x_2 \cdots x_n$.

An auditor wants to determine the deviation of this performance index from zero. Specifically, for any fixed set of efficiency functions $\{f_1, \dots, f_n\}$, the auditor will strategically choose a set of dial settings $x_1, x_2, \dots, x_n$ (each $x_i \in [0,1]$) to maximize the absolute value of the result:
$$|f_1(x_1) + f_2(x_2) + \dots + f_n(x_n) - x_1 x_2 \dots x_n|$$

For a given $n$, let $c_n$ be the largest constant such that, regardless of which functions $f_i$ are provided, the auditor can always find settings $x_1, \dots, x_n$ that ensure this absolute value is at least $c_n$. Find the value of $c_n$ in terms of $n$.

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
