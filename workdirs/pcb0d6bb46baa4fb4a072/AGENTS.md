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

A high-security digital vault utilizes a rotation of 130 unique access codes, indexed $n = 1, 2, \dots, 130$. For each code index $n$, a security clearance audit is performed on a set of potential authorization keys labeled $a = 1, 2, \dots, 130$.

An authorization key $a$ is deemed "valid" for a specific vault index $n$ if there exists some positive integer power $b$ such that the authentication signal $a^b$ leaves a remainder of $n$ when processed by the system’s primary modulus, 131.

For each vault index $n$, let $f(n)$ represent the total count of valid authorization keys $a$ that can access that vault. Furthermore, let $g(n)$ represent the sum of the labels of all such valid authorization keys for that specific $n$.

The system supervisor needs to calculate a master checksum. To do this, they compute the product of the count and the sum $f(n) \cdot g(n)$ for every vault index from 1 to 130, and then find the total sum of these products.

Find the remainder when this grand total sum $\sum_{n=1}^{130} [f(n) \cdot g(n)]$ is divided by 131.

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
