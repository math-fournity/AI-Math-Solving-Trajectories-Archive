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

In a specialized automated warehouse, a heavy-duty cargo transport platform operates using 6 hydraulic support pistons, arranged with 3 pistons on the North side and 3 pistons on the South side. 

A maintenance cycle for the platform consists of an ordered sequence of 12 distinct operations. During this cycle, each of the 6 pistons must be raised exactly once and lowered exactly once. The sequence begins with all 6 pistons down (supporting the platform) and concludes with all 6 pistons back down.

To ensure the structural integrity of the platform and prevent it from tipping over, the maintenance sequence must be "stable." A sequence is considered stable if, at every step throughout the 12-action process, the following two safety conditions are met:
1. At least 3 pistons must be in the down position.
2. It is never the case that the only pistons in the down position are all located on the same side (i.e., you cannot have only North-side pistons down, and you cannot have only South-side pistons down).

Calculate $N$, the total number of unique stable maintenance sequences possible.

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
