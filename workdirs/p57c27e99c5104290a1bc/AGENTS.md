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

In a specialized cyber-security network, a server’s security level is determined by a positive integer $n$. A server is classified as "Shield-Resilient" if every one of its positive divisors $d$ satisfies a specific integrity check: at least one of the values $d-1$ or $d+1$ must be a prime number. 

For instance, a server with security level $8$ is Shield-Resilient because its divisors—$1, 2, 4,$ and $8$—all pass the check: 
- For $d=1$, $1+1=2$ is prime.
- For $d=2$, $2+1=3$ is prime.
- For $d=4$, $4+1=5$ (or $4-1=3$) is prime.
- For $d=8$, $8-1=7$ is prime.

Conversely, a server with security level $9$ is not Shield-Resilient because for the divisor $d=9$, neither $9-1=8$ nor $9+1=10$ is a prime number.

Based on these criteria, determine the largest possible integer $n$ that can represent a Shield-Resilient security level.

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
