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

In a remote high-tech logistics hub, automated cargo modules are arranged in a perfect square formation of $N \times N$ docking bays. The facility only operates with odd dimensions, such that $N = 2k+1$ for a positive integer $k$. Each bay contains a single energy cell. Due to safety regulations, the charge level of each cell—represented as a real number—must not exceed a magnitude of $1$ unit (positive for surplus, negative for deficit). To maintain grid stability, the total sum of all energy charges across the entire $N \times N$ square must be exactly zero.

The facility manager defines a stability constant $C_k$. This is the smallest non-negative real value that guarantees that, regardless of how the individual charges are distributed, there will always be at least one line (either a full row of bays or a full column of bays) where the absolute value of the sum of the charges in that line is no greater than $C_k$.

Consider two specific configurations of this hub: one where $k=2$ (a $5 \times 5$ grid) and one where $k=3$ (a $7 \times 7$ grid). 

Calculate the value of $10 \times C_2 + 4 \times C_3$.

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
