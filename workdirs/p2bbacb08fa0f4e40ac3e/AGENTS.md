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

In a specialized chemistry laboratory, a researcher is testing the efficiency ratios of various liquid compounds. She identifies four unique chemical additives, each assigned a discrete concentration level represented by an integer from 1 to 9. Let these distinct levels be $A, B, C$, and $D$.

The researcher prepares two specific mixtures to compare their potency:
1. **Mixture Alpha:** This mixture is formulated by combining $A$ units of a base concentrated at 100%, $B$ units of a catalyst at 10%, and $C$ units of a stabilizer at 1%.
2. **Mixture Beta:** This mixture is formulated by combining $B$ units of the 100% base, $A$ units of the 10% catalyst, and $D$ units of a different stabilizer at 1%.

Through a series of experiments, she discovers a precise mathematical equilibrium: the ratio of the total potency of Mixture Alpha to the total potency of Mixture Beta is exactly equal to the ratio of the concentration level of stabilizer $C$ to the concentration level of stabilizer $D$.

Identify all sets of distinct concentration levels $\{A, B, C, D\}$ that satisfy this equilibrium. Once identified, treat each set as the digits of a four-digit identification code in the format $ABCD$. Calculate the sum of all such four-digit codes that represent valid solutions to the equilibrium equation.

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
