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

A specialized artificial intelligence is being trained to manage a complex power grid across $n$ independent zones. For each zone $k$ (where $k=1, 2, \ldots, n$), a technician must assign a performance function $f_k(x_k)$ based on a local control setting $x_k$ chosen from the range $[0, 1]$.

Once the functions $f_1, f_2, \ldots, f_n$ are locked in by the technician, an auditor arrives to test the grid's stability. The auditor searches for a specific set of settings $x_1, x_2, \ldots, x_n$ (each within $[0, 1]$) that minimizes the "Discrepancy Error" of the system. The Discrepancy Error is defined as the absolute difference between the sum of the performance outputs and the product of all the settings:
$$\text{Error} = \left| \sum_{k=1}^n f_k(x_k) - \prod_{k=1}^n x_k \right|$$

For a fixed $n$, let $C_n$ represent the "Guaranteed Minimum Error." This is the largest real number such that, regardless of which functions $f_1, \ldots, f_n$ the technician chooses, the auditor can always find at least one set of settings $x_1, \ldots, x_n$ where the Discrepancy Error is at least $C_n$.

Calculate the value of the following sum:
$$\sum_{n=1}^{10} (2n \cdot C_n)$$

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
