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

Positive integers $n$ and $k$ satisfying $n \geq 2k+1$ are given. There are $n$ cards numbered from $1$ to $n$, randomly shuffled in a deck, face down. On each turn $j = 1, 2, \dots, 2k+1$, Alice flips over the top card $a_j$ and puts it face up on the table. If Alice has not yet signed a card, she may choose to sign the current card $a_j$. She must sign exactly one card among the $2k+1$ cards revealed.

Let $A$ be the number on the signed card, and let $M$ be the $(k+1)^{\text{st}}$ largest number among all $2k+1$ cards revealed by the end of the game. Alice's score is $|M-A|$. Alice wants to minimize the score she can guarantee regardless of the order and values of the cards in the deck, while the "deck" (the adversary) effectively wants to maximize it.

Let $d(n,k)$ be the smallest integer such that Alice has a strategy to guarantee her score is no greater than $d(n,k)$. Compute $d(100, 30)$.

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
