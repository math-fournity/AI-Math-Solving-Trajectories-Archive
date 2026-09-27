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

In a remote digital federation, there are 2004 central data hubs linked by bidirectional fiber-optic cables. The network is designed with high redundancy: every hub is reachable from every other hub, and the network is 2-edge-connected, meaning the failure of any single cable will not disconnect any part of the system.

The Federation’s Chief Architect and the Chief Security Officer are engaged in a protocol-setting game to optimize traffic flow. They take turns converting the remaining bidirectional cables into one-way streams. On each turn, a player must choose one existing bidirectional cable and assign it a fixed direction. However, they are bound by a strict "Universal Access" rule: after any direction is assigned, it must still be possible to transmit data from any hub to any other hub in the network (maintaining strong connectivity).

The turns alternate, with the Chief Architect moving first. A player loses the game and must resign if, on their turn, there are no remaining bidirectional cables that can be assigned a direction without violating the Universal Access rule.

Let $n$ be the number of players (out of the two) who possess a winning strategy to force the other to resign, regardless of the sequence of moves made by their opponent. Find the value of $n$.

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
