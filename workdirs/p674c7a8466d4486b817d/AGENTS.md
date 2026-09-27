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

In a futuristic data center, a mainframe contains a specific set of active processing ports. Initially, the set of active ports consists of the $n$ smallest integers and the $n$ largest integers from the range $\{1, 2, 3, \ldots, 99\}$, where $n$ is a fixed natural number less than 50.

Two system administrators, Ani and Boyan, engage in a maintenance protocol where they take turns modifying the port configuration. Ani always takes the first turn. On any given turn, a player must perform exactly one of the following two operations:
1. Select one active port number $x$ and increase it to $x + 1$, provided the new number is not already an active port and does not exceed 99.
2. Deactivate one port entirely, removing its number from the set of active ports.

The protocol dictates that at no point can two active ports share the same number, and no port number can ever exceed 99. A player who is unable to perform either operation loses the game.

Determine the sum of all possible values of $n \in \{1, 2, \ldots, 49\}$ for which Ani has a guaranteed winning strategy regardless of Boyan's moves.

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
