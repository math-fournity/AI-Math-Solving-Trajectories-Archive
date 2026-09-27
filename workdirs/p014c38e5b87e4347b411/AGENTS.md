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

In a remote industrial sector, a structural engineer is testing the stability of triangular support frames. These frames are designed such that the lengths of their three sides represent specific configurations of three-digit codes.

A code is defined as a three-digit integer $100A + 10B + C$, where $A, B$, and $C$ are the individual digits and the leading digit $A$ cannot be zero. For a code to be "geometrically stable," it must satisfy a specific Pythagorean relationship: the square of the full code value must be exactly equal to the sum of the squares of two derived measurements:
1. The value formed by the last two digits of the code ($10B + C$).
2. The value formed by the first two digits of the code followed by a zero ($100A + 10B$).

The engineer discovers that for every stable code $\overline{ABC}$, its reverse sequence $\overline{CBA}$ also forms a stable code (provided the new leading digit $C$ is not zero).

Identify every three-digit natural number that satisfies this "geometrically stable" property and calculate the sum of all these numbers.

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
