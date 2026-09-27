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

In a specialized cyber-security lab, a group of engineers is testing the stability of "Modular Security Locks." Each lock is assigned an identification number $n$, where $n$ is an integer ranging from $2$ to $50$ inclusive.

For a lock with ID $n$, the engineers identify a specific set of "Secure Keys." These keys are the positive integers $k$ in the range $1 \leq k \leq n$ that share no common factors with $n$ other than $1$. The total count of these Secure Keys is denoted by the value $\varphi(n)$.

The engineers are studying the "Interference Profile" of each lock, which is defined as the mathematical difference between two specific configurations:
1.  The **Baseline Configuration**: A simple polynomial defined as $x^{\varphi(n)} - 1$.
2.  The **Keyed Configuration**: A product of linear terms $(x-k)$ for every Secure Key $k$ associated with that lock ID $n$.

A lock ID $n$ is classified as "Harmoniously Stable" if every single coefficient of the resulting Interference Profile polynomial is perfectly divisible by the ID number $n$.

Based on the lab’s parameters for $2 \leq n \leq 50$, how many unique lock IDs $n$ satisfy the condition for being Harmoniously Stable?

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
