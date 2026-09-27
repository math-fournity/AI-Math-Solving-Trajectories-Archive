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

In a specialized logistics warehouse, a floor is divided into a rectangular grid of storage bays with 6 rows (labeled $R_1$ to $R_6$) and 8 columns (labeled $C_1$ to $C_8$). A system administrator is deploying 24 specialized tracking sensors across these bays according to the following strict protocols:

1.  **Deployment Density:** Every row must contain exactly four sensors, and every column must contain exactly four sensors.
2.  **Sensor Pairing:** The sensors are paired by frequency. There are 12 distinct frequencies, labeled 1 through 12, and each frequency is assigned to exactly two sensors.
3.  **Transmission Range:** For each frequency $n$ (where $n = 1, 2, \ldots, 12$), the two sensors tuned to that frequency must be placed such that the walking distance between them (calculated by the sum of the absolute differences of their row and column indices) is exactly $n$ units.

The following sensors have already been installed in the grid:
*   A frequency **6** sensor is at $(R_1, C_5)$
*   A frequency **10** sensor is at $(R_2, C_2)$
*   A frequency **1** sensor is at $(R_2, C_3)$
*   A frequency **2** sensor is at $(R_3, C_4)$
*   A frequency **8** sensor is at $(R_3, C_8)$
*   A frequency **5** sensor is at $(R_4, C_2)$
*   A frequency **2** sensor is at $(R_4, C_5)$
*   A frequency **7** sensor is at $(R_5, C_6)$
*   A frequency **9** sensor is at $(R_5, C_7)$
*   A frequency **3** sensor is at $(R_6, C_5)$

Let $(r_n, c_n)$ and $(r_n', c_n')$ represent the row and column coordinates for the two sensors of frequency $n$. Calculate the total sum of all coordinate indices for all 24 sensors: $\sum_{n=1}^{12} (r_n + r_n' + c_n + c_n')$.

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
