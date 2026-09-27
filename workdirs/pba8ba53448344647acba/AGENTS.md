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

In a futuristic data-storage facility, a security protocol is governed by a sequence of encryption keys $f_n$. This sequence follows a strict growth rule: the first two keys are $f_0 = 1$ and $f_1 = 1$, and every subsequent key is the sum of the previous two ($f_n = f_{n-1} + f_{n-2}$ for $n \geq 2$).

An engineer is testing the stability of "Accumulated Resource Nodes." For a chosen positive integer index $n$, a node is considered stable if there exists a positive integer capacity $a$, constrained by the range $f_n \leq a \leq f_{n+1}$, such that the "Efficiency Coefficient" $E$ results in a whole number. 

The Efficiency Coefficient $E$ for a given $n$ and $a$ is calculated by the following formula:
$$E = a \times \left( \frac{1}{f_1} + \frac{1}{f_1 f_2} + \frac{1}{f_1 f_2 f_3} + \cdots + \frac{1}{f_1 f_2 \cdots f_n} \right)$$

Find the sum of all positive integers $n$ for which a stable node can be constructed.

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
