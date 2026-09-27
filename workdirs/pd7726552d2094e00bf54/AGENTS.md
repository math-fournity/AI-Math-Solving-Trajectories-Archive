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

There are 4 outlets \(A, B, C, D\) in a room, each with 2 sockets denoted with subscripts 1 and 2 (i.e., outlet \(A\) has sockets \(A_{1}\) and \(A_{2}\)). A baby starts plugging wires into the sockets. They have 3 wires, and each wire has two ends that each plug into a socket. Each socket can take at most one plug.

A short circuit happens when there is a loop from one outlet to itself. For example, \(A_{1} \leftrightarrow A_{2}\) is a short circuit and \(A_{1} \leftrightarrow B_{1}, B_{2} \leftrightarrow C_{1}, A_{2} \leftrightarrow C_{2}\) is a short circuit, but \(A_{1} \leftrightarrow B_{1}\) is not.

Provided that the baby randomly connects every plug to a socket, what is the probability that the baby causes a short circuit? If the answer is of the form of an irreducible fraction $\frac{a}{b}$, compute the value of $a + b$.

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
