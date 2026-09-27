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

A secure vault is protected by a secret code, which is a positive integer $x$. A team of four security analysts—Alpha, Bravo, Charlie, and Delta—each provides a pair of statements about the code. Crucially, for every analyst, exactly one of their two statements is true and the other is false.

**Analyst Alpha’s Statements:**
A1) The code $x$ is the unique integer that satisfies the conditions of this entire security report.
A2) The code $x$ is a positive integer that contains at least one repeating digit in its decimal form.

**Analyst Bravo’s Statements:**
B1) The value $(x - 5)$ is an integer divisible by 6.
B2) The value $(x + 1)$ is an integer divisible by 12.

**Analyst Charlie’s Statements:**
C1) The code $x$ is a positive integer whose decimal representation begins with the digit 3.
C2) The code $x$ is exactly 389.

**Analyst Delta’s Statements:**
D1) The code $x$ is a three-digit prime number between 300 and 399, specifically one of the following: 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, or 397.
D2) The code $x$ is a positive integer consisting of exactly three identical digits.

Find all possible values for the secret code $x$.

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
