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

A specialized digital vault requires a master access code $N$, which is a massive positive integer. To ensure security, the system's architecture imposes three specific mathematical protocols based on "Key Values."

According to the system logs:
1. For the Key Value 17, the quotient of the master code divided by 17 must be a perfect 17th power of an integer.
2. For the Key Value 18, the quotient of the master code divided by 18 must be a perfect 18th power of an integer.
3. For a third variable Key Value $b$, the quotient of the master code divided by $b$ must be a perfect $b$th power of an integer.

An auditor is testing the system's compatibility with different hardware configurations. They need to identify all possible settings for the variable Key Value $b$ such that $b$ is a positive integer, $1 \le b \le 2013$, and $b$ is distinct from the primary keys (so $b \neq 17$ and $b \neq 18$).

How many such values of $b$ exist that allow for the existence of at least one master code $N$ satisfying all three protocols?

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
