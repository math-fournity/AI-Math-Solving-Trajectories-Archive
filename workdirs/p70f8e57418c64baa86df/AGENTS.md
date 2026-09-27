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

In a remote industrial sector, two logistics managers, Aris and Bron, are competing for control over a chemical distribution network. The network begins with two storage vats containing $a$ and $b$ liters of a volatile reagent, where $1 \le a, b \le 100$ and both are integers.

The managers take turns rebalancing the inventory according to a strict safety protocol. On each turn, the current manager must select a vat that contains an even number of liters. They then transfer exactly half of that vat's contents into the other vat. Aris always takes the first turn. 

The operation concludes under two specific conditions:
1. If a manager encounters a state where both vats contain an odd number of liters, they are unable to perform a transfer and immediately lose the contract.
2. If the distribution of liters in the vats matches a state that has occurred previously in the sequence of turns, the protocol enters an infinite loop, resulting in a permanent stalemate (draw).

Both Aris and Bron are perfect logicians who will always play optimally to win, or to force a draw if a win is impossible.

Calculate the total number of initial pairs $(a, b)$ within the specified range such that Bron has a guaranteed winning strategy.

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
