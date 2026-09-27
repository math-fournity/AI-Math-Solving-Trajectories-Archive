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

A high-tech manufacturing firm operates a production line with $n$ specialized modules, indexed from $1$ to $n$ and arranged in a fixed linear sequence. Each module $k$ initially possesses a "power rating" equal to its index $k$.

Two engineers, Alice and Bob, are tasked with decommissioning the line through a series of "merger operations" to reduce the system to a single central power core. Alice goes first, and they alternate turns. In each turn, the engineer must select two modules that are currently adjacent in the sequence and merge them into a single unit. The engineer can choose to set the power rating of the new merged unit to be either the sum or the product of the power ratings of the two modules being replaced.

The process continues until only one power core remains. If the final power rating of this core is an odd number, Alice receives a performance bonus; if the final rating is even, Bob receives the bonus.

Let $W$ be the set of all integers $n$ in the range $1 \le n \le 100$ for which Alice can guarantee she receives the bonus, regardless of the choices Bob makes during his turns.

Find the sum of all elements in the set $W$.

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
