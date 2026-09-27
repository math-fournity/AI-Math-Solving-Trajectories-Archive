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

In the city of Arithmos, the Central Vault is secured by a series of electronic locks, each labeled with a unique positive integer. The integers on these locks are exactly the set of all positive divisors of a specific master security code $n$.

Two cybersecurity experts, Alice and Bob, are testing the vault’s integrity through a game. They take turns selecting one of the unassigned locks and assigning it to one of two security protocols: the "Ruby" protocol or the "Sapphire" protocol. Alice always takes the first turn. The process continues until every single lock (every divisor of $n$) has been assigned a protocol.

Alice’s objective is to ensure that the system remains stable. The system is considered stable if the product of all the lock labels assigned to the Ruby protocol is a perfect square. (By convention, if no locks are assigned to the Ruby protocol, the product is 1, which is a perfect square). Bob’s objective is to destabilize the system by ensuring the product of the Ruby-labeled locks is not a perfect square.

Assuming both Alice and Bob play with perfect logical strategy, determine who will win the game for any given positive integer $n$.

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
