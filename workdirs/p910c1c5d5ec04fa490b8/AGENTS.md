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

An elite team of nine security specialists—identified by their unique clearance badges numbered 0, 1, 2, 3, 4, 5, 6, 7, and 8—must stand in a single-file line to activate a high-security vault. To be considered a "valid sequence," the arrangement of these nine specialists must satisfy two strict protocols:

1.  **The Quintet Protocol:** Any subset of five specialists standing in consecutive positions in the line must have a total sum of badge numbers that is a multiple of 5.
2.  **The Septet Protocol:** Any subset of seven specialists standing in consecutive positions in the line must have a total sum of badge numbers that is a multiple of 4.

Each specialist's badge number is used exactly once in the sequence. For instance, the sequence 5-7-8-4-6-0-2-1-3 is invalid because, although every consecutive group of seven adds up to a multiple of 4, there is at least one group of five consecutive specialists whose badge sum is not divisible by 5.

If each valid nine-digit sequence is treated as a single nine-digit integer, determine the sum of all possible valid sequences.

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
