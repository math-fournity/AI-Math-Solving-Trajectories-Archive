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

In a remote archipelago, there are exactly 2008 islands connected by a series of bridges. The geography of this archipelago is unique: while there are various paths and loops, no two cycles of bridges share a single island (meaning the network is a "cactus graph").

Two rival factions, the Raiders and the Guardians, are competing for control of the archipelago. The conflict proceeds in turns:

1.  **The First Incursion:** On the 1st move, the Raider Captain chooses any island in the archipelago and establishes a base there.
2.  **The First Defense:** On the 2nd move, the Guardian Commander chooses any other unoccupied island and establishes a fortification there.
3.  **Expansion Phase:** For all subsequent turns:
    *   On every $(2k+1)$-th move, the Raiders may expand to one new island, provided it is currently unoccupied and is directly connected by a bridge to an island already controlled by the Raiders.
    *   On every $(2k+2)$-th move, the Guardians may expand to one new island, provided it is currently unoccupied and is directly connected by a bridge to an island already controlled by the Guardians.

If a faction has no legal moves available on their turn, they must pass. The conflict ends only when neither the Raiders nor the Guardians can claim any more islands. 

Assuming both the Raider Captain and the Guardian Commander play with perfect strategy—the Raiders seeking to maximize their territory and the Guardians seeking to minimize it—determine the maximum number of islands the Raiders can guarantee to control at the end of the game.

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
