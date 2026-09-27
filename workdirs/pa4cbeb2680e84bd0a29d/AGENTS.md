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

In the remote Arctic research station of Isotope-3, three specialized thermal stabilizers—codenamed X-Ray, Yankee, and Zulu—are used to regulate the core temperature of a reactor. The operational efficiency of each stabilizer is measured by a real-valued performance index ($x$, $y$, and $z$ respectively). 

Due to the physical limitations of the hardware, the internal mechanisms of these stabilizers will fail if their performance index falls anywhere within the high-sensitivity range strictly between -1 and 1. Consequently, for each stabilizer, the index must satisfy the constraint that it does not lie in the open interval $(-1, 1)$.

A central monitoring computer tracks the equilibrium of the system. The chief engineer has determined that the stabilizers are in perfect balance when the sum of their performance indices plus the sum of their reciprocal efficiencies equals exactly zero. This is represented by the governing equation:
$$\frac{1}{x} + \frac{1}{y} + \frac{1}{z} + x + y + z = 0$$

The facility's total thermal output is defined as the sum of the three indices: $x + y + z$. To ensure the reactor does not overheat during a safety test, the engineer needs to determine the upper bound of this output.

What is the maximum possible value of $x + y + z$?

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
