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

A specialized automated logistics terminal handles a sequence of 2013 cargo shipment opportunities. For each opportunity $n$ (from $n=1, 2, \dots, 2013$), a computer generates a random binary signal. There is a $50\%$ chance the signal is "Active" and a $50\%$ chance it is "Null."

The terminal has a digital inventory log. If the signal for opportunity $n$ is "Null," no changes are made to the log. If the signal is "Active," the system follows these protocols:
(i) If the inventory log is currently empty, the system records the ID number $n$.
(ii) If the inventory log is not empty, let $m$ represent the highest ID number currently recorded. The system calculates the value $m^2 + 2n^2$. If this value is divisible by 3, the ID $m$ is deleted from the log. If it is not divisible by 3, the new ID $n$ is added to the log.

After all 2013 opportunities have passed, the probability that the inventory log is completely empty can be expressed in simplest form as $\frac{2u+1}{2^k(2v+1)}$, where $u$, $v$, and $k$ are non-negative integers. Find the value of $k$.

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
