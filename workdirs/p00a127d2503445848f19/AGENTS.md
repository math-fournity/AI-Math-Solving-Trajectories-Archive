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

In a bustling commercial district, there is a small $3 \times 3$ warehouse floor divided into nine identical square storage zones. A modular conveyor belt system, consisting of $k$ linked robotic segments, is deployed across the floor. This "robotic snake" occupies a sequence of $k$ distinct zones, where each segment is connected to the next across a shared boundary.

The robot moves using a "follow-the-leader" protocol: the lead segment moves into an adjacent unoccupied zone, and every subsequent segment shifts forward one position into the zone previously occupied by the segment ahead of it. 

The warehouse manager needs to determine if the conveyor system can undergo a "complete orientation reversal." This means that through a series of valid moves, the robotic snake must eventually occupy the exact same set of $k$ zones it started in, but with the segments arranged in the perfectly reversed sequence (the segment that was originally the head is now the tail, and vice versa).

What is the largest integer $k$ for which such a conveyor system can be placed in the $3 \times 3$ warehouse and successfully perform this reversal?

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
