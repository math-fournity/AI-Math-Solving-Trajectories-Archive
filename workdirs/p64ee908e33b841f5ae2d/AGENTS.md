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

In the city of Neo-Veridia, a circular maglev track has a total circumference of $10\pi$ kilometers. The city planning committee needs to pave the entire track using curved sections of rail. They have access to a warehouse containing six specific types of rails, all with a radius of curvature of $5$ kilometers. These rails come in two lengths—$\pi$ kilometers and $2\pi$ kilometers—and each length is available in three distinct colors: Red, Green, and Blue.

The committee must tile the track such that the rails are placed end-to-end to cover the $10\pi$ distance exactly, with no gaps and no overlapping. To ensure the track meets aesthetic and safety standards, the following two regulations must be met:

1. No two adjacent rails can share the same color.
2. For any sequence of three consecutive rails, if the middle rail is a short rail (length $\pi$), then all three rails in that sequence must be of different colors.

How many unique ways can the committee pave the circular track? Two paving patterns are considered the same if one can be rotated to match the other. However, two patterns are considered distinct if one is a reflection of the other and they cannot be matched through rotation alone.

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
