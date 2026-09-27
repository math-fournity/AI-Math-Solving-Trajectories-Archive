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

In a futuristic grid-based storage facility, a square floor is divided into a $(3n) \times (3n)$ layout of tiles, where $n$ is a natural positive integer. To organize the facility, the floor is initially painted in a diagonal pattern starting from the top-left corner. The diagonals (from top-right to bottom-left) follow a repeating sequence: two consecutive diagonals are painted White, followed by one diagonal painted Black. This 2:1 ratio (White, White, Black) continues until the entire floor is covered.

A specialized maintenance robot can perform a "cycle operation" on any $2 \times 2$ block of tiles. This operation changes the state of the four tiles within that block simultaneously:
- If a tile is currently White, it is repainted Orange.
- If a tile is currently Orange, it is repainted Black.
- If a tile is currently Black, it is repainted White.

The facility manager wants to perform a total overhaul. The goal is to reach a state where every tile that was originally White has become Black, and every tile that was originally Black has become White. (Note: In the final state, no tile should be Orange).

Find all possible values of $n$ for which this transformation can be achieved in a finite number of steps.

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
