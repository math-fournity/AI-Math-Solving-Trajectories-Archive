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

In a specialized cyber-security competition, three engineers—Celia, Alice, and Betsy—are competing to consolidate six unique encrypted data fragments: the 9, 10, J, Q, K, and A blocks. Alice and Betsy are on the Blue Team, while Celia is on the Red Team. Each engineer currently holds exactly two fragments in their private server. While the total pool of six fragments is known to everyone, no one knows which specific fragments the others hold (critically, teammates Alice and Betsy cannot see each other’s servers).

It is Celia’s turn. The rules of the "Data Capture" protocol are as follows:
1. On their turn, an engineer must target an opponent and request a specific fragment from the set of six that is not already in the requester's possession.
2. If the target holds that fragment, they must transfer it to the requester’s server. The requester then continues their turn, making another request (to the same or a different opponent).
3. If the target does not have the fragment, the turn ends immediately, and the person who was just questioned begins their turn.
4. A player is prohibited from requesting a fragment if they already possess information proving the target cannot have it.
5. The game ends when one team (either Celia alone or Alice and Betsy combined) secures all six fragments.

Assuming every player employs a perfect strategy to maximize their team's probability of winning, the probability that Celia (the Red Team) wins the game can be expressed as a simplified fraction \(p/q\).

Find the value of \(100p + q\).

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
