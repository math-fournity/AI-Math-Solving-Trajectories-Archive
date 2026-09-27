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

Near the end of a game of Fish, Celia is playing against a team consisting of Alice and Betsy. Each of the three players holds two cards in their hand, and together they have the Nine, Ten, Jack, Queen, King, and Ace of Spades (this set of cards is known by all three players). Besides the two cards she already has, each of them has no information regarding the other two's hands (In particular, teammates Alice and Betsy do not know each other's cards).

It is currently Celia's turn. On a player's turn, the player must ask a player on the other team whether she has a certain card that is in the set of six cards but not in the asker's hand. If the player being asked does indeed have the card, then she must reveal the card and put it in the asker's hand, and the asker shall ask again (but may ask a different player on the other team); otherwise, she refuses and it is now her turn. Moreover, a card may not be asked if it is known (to the asker) to be not in the asked person's hand. The game ends when all six cards belong to one team, and the team with all the cards wins. Under optimal play, the probability that Celia wins the game is \(\frac{p}{q}\) for relatively prime positive integers \(p\) and \(q\). Find \(100p+q\).

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
