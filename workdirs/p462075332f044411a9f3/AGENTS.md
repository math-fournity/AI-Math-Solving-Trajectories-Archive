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

In a specialized cyber-security facility, an encrypted mainframe is protected by a multi-layered security code. To bypass the system, a technician must identify every possible "Security Triple" $(a, b, c)$ that satisfies a specific set of rigorous frequency protocols:

1.  **Frequency Constraints**: The values $a, b,$ and $c$ represent three distinct signal frequencies, all of which must be prime numbers. To maintain signal stability, they must strictly follow the order $a < b < c$, and no frequency can reach or exceed $100$ MHz.
2.  **Geometric Resonance**: When the hardware adds a calibration constant of $1$ MHz to each frequency, the resulting values $(a+1, b+1, c+1)$ must form a perfect geometric sequence. This means the ratio of the second calibrated value to the first must be exactly equal to the ratio of the third calibrated value to the second.

Let the set of all unique triples that meet these two conditions be $S = \{(a_1, b_1, c_1), (a_2, b_2, c_2), \dots, (a_k, b_k, c_k)\}$. 

The final master key required to unlock the mainframe is the total sum of every individual frequency used across all valid triples. Calculate $\sum_{i=1}^k (a_i + b_i + c_i)$.

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
