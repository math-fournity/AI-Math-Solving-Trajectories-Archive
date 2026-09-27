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

A specialized logistics company, Zenith-99, operates a square distribution hub divided into a grid of $99 \times 99$ distinct storage bays. Two bays are considered "connected" if they share at least one boundary point (meaning they are adjacent horizontally, vertically, or diagonally).

A security officer, Maéna, is tasked with assigning a unique security clearance level, represented by an integer from 1 to $99^2$, to every single bay in the hub. She is free to distribute these levels across the grid in any arrangement she chooses.

Once the levels are assigned, a courier named Théodore must perform a delivery run. He starts by placing his transport bot in any single bay of his choice. From there, he can move the bot from its current bay to any connected bay, provided that the destination bay has a strictly higher security clearance level than the bay he is currently in. He can repeat this process as many times as possible.

Theodore wants to maximize his total number of moves, while Maéna wants to arrange the numbers to limit him as much as possible. What is the maximum number of moves that Théodore can guaranteed to be able to make, regardless of the specific arrangement of clearance levels Maéna chooses?

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
