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

In a remote industrial chemical complex, three specialized reagents—$a, b$, and $c$ (all measured in positive molar concentrations)—are used to stabilize a core reaction. The safety protocol of the facility dictates that these concentrations must strictly satisfy the equilibrium equation:
$$ab + bc + ca + abc = 4$$

The facility’s efficiency is governed by a performance index $P$, which depends on a tunable hardware constant $k$. The system is considered "stable" if the product of three specific stress-test factors satisfies the following condition:
$$(k + ab)(k + bc)(k + ca) \geq (k + 1)^3$$

Engineers have discovered that for certain values of the constant $k$, this stability inequality holds true regardless of the specific concentrations of $a, b$, and $c$ chosen (as long as they meet the equilibrium equation). 

The set of all real values of $k$ for which the system remains stable for all valid concentrations is found to be a union of two distinct ranges: $(-\infty, k_1] \cup [k_2, \infty)$.

Based on these specific threshold values $k_1$ and $k_2$, calculate the final safety certification code given by:
$$k_1^2 + k_1 + k_2^2 - 3k_2$$

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
