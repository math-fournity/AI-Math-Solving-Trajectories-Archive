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

In a chemistry laboratory, two automated synthesis machines are programmed with base chemical concentration profiles over time ($x$): $P_1(x) = x^3 - 3x^2 + 5$ and $P_2(x) = x^2 - 4x$.

The lab's computer system allows researchers to derive new concentration profiles by performing four specific operations on any profiles $f(x)$ and $g(x)$ currently in the database:
1. Creating a new profile by adding or subtracting them: $f(x) \pm g(x)$.
2. Creating a new profile by multiplying them: $f(x)g(x)$.
3. Creating a composite reaction profile where one serves as the input for the other: $f(g(x))$.
4. Scaling a profile by any real-valued constant $c$: $cf(x)$.

Let $S$ be the set of all possible concentration profiles that can be generated starting from $P_1(x)$ and $P_2(x)$ using these four operations.

A researcher is interested in a specific family of target profiles defined by $Q_n(x) = x^n - 1$. Calculate the sum of all integers $n$ in the range $\{1, 2, 3, \dots, 100\}$ such that the profile $Q_n(x)$ can be successfully generated and added to the set $S$.

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
