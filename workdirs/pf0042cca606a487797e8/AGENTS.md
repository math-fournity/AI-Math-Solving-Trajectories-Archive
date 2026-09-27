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

In a specialized logistics simulation, a mainframe starts with a specific three-digit inventory code, $n$, representing a natural number of units. Two operators, Alpha and Beta, take turns modifying this inventory, with Alpha initiating the first sequence.

During a turn, the active operator must select a proper divisor of the current inventory number—specifically, an integer that divides the current value exactly, excluding the number 1 and the value of the number itself. The operator then subtracts this chosen divisor from the current inventory to create a new, smaller total for the next person's turn. For instance, if the inventory stands at 6, the operator could subtract 2 (since 2 is a divisor other than 1 and 6), leaving 4 units for the opponent.

The simulation concludes when an operator receives a number that has no proper divisors, leaving them unable to perform a subtraction; that operator is declared the loser, and their opponent is the winner. 

Records show that there are certain initial values of $n$ where Alpha has a guaranteed winning strategy regardless of Beta's moves, and other values of $n$ where Beta has a guaranteed winning strategy regardless of Alpha's moves.

Based on these rules, how many possible three-digit natural numbers $n$ exist?

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
