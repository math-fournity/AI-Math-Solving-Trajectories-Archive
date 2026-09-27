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

In the high-tech semiconductor facility of Neo-Kyoto, a precision laser calibration sequence is governed by a complex efficiency protocol involving 104 distinct power stages, indexed from $k = 0$ to $k = 103$.

For each power stage $k$, engineers must calculate a specific "Energy Variance" value. This variance is defined as the square of the difference between two automated sensor readings:

1.  **Sensor Alpha ($A_k$):** This reading is calculated by taking the stage index $k$, multiplying it by the "Phase Variance Constant" $(3 - \sqrt{3})$, and rounding the result down to the nearest integer.
2.  **Sensor Beta ($B_k$):** This reading is more complex. First, the value $(k+1)$ is multiplied by the "Refraction Index" $(2 - \sqrt{3})$, and the result is rounded down to the nearest integer. This intermediate integer is then multiplied by the "Amplification Factor" $(3 + \sqrt{3})$, and the final product is again rounded down to the nearest integer.

The "Total System Delta" is defined as the sum of the Energy Variances across all stages from $0$ to $103$. 

Calculate the Total System Delta:
$$ \sum_{k=0}^{103} (A_k - B_k)^2 $$

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
