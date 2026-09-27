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

In a specialized logistics archive, there are exactly 2013 secure crates. Each crate contains a single unique component with an ID number ranging from 1 to 2013, such that every integer in that range is represented once. The crates are sealed, so the specific ID inside any individual crate is hidden.

A sophisticated scanner is available that can analyze any chosen collection of crates. When a set of crates is scanned, the device determines if the arithmetic mean of the ID numbers within that set is an integer. For this specific set of crates, every possible scan performed on any subset of crates always returns a "True" result—meaning the average of the IDs in any selected group is always a whole number.

The archive manager wishes to organize these 2013 crates into several distinct storage categories. Within each category, the manager must know exactly which ID numbers are present, even though they do not know which specific crate in that category contains which specific ID.

Based on the mathematical certainty that the mean of any subset of these 2013 crates is an integer, determine the maximum number of such storage categories that can be formed.

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
