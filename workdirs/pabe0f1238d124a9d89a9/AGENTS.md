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

A specialized deep-sea salvage operation involves two autonomous submersibles, the "Alpha" and the "Bravo," both starting at a neutral depth of 0 meters. The submersibles alternate maneuvers to reach specific pressure zones, with Alpha initiating the sequence.

During each of its maneuvers, Alpha has a probability of $1/2$ of ascending $1$ meter and a probability of $1/2$ of descending $1$ meter. When it is Bravo’s turn, it has a probability of $2/3$ of ascending $1$ meter and a probability of $1/3$ of descending $1$ meter.

The mission objective is to reach the target recovery zone at an elevation of $+2$ meters. However, if a submersible sinks to the danger zone at $-2$ meters, its engine fails, and the other submersible is immediately declared the winner of the contract. The game ends as soon as either submersible reaches $+2$ (winning directly) or $-2$ (losing, causing the opponent to win).

What is the probability that Bravo wins the contract?

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
