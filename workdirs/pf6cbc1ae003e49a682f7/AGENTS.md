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

In a futuristic data center, a server rack is organized into a square grid of $n \times n$ storage slots. A technician needs to select a specific configuration of slots, called a "Dual-Stream Array," to optimize data flow.

A configuration is defined as a Dual-Stream Array if it satisfies two structural requirements simultaneously:
1. The selected slots can be perfectly partitioned into $n$ horizontal, non-overlapping blocks with dimensions $1 \times 1, 1 \times 2, 1 \times 3, \dots, 1 \times n$.
2. The same set of selected slots can also be perfectly partitioned into $n$ vertical, non-overlapping blocks with dimensions $1 \times 1, 2 \times 1, 3 \times 1, \dots, n \times 1$.

Note that the orientation and placement of these blocks within the $n \times n$ grid can vary, and two configurations are considered distinct if they occupy different sets of slots (even if one can be rotated or reflected to match the other).

In terms of $n$, how many different Dual-Stream Array configurations can the technician create?

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
