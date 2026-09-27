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

A specialized laboratory is testing the chemical stability of various liquid compounds. A scientist has a collection of distinct chemical samples, where each sample $i$ is assigned a specific "potency value," denoted by a real number $a_i$. 

The laboratory uses a stability metric $C$ (a fixed positive constant) to evaluate the interactions between any two different samples. For any two distinct samples $i$ and $j$, the stability of their pairing is governed by the following precise formula: the absolute value of the sum of the square of the first sample’s potency and a fixed calibration constant $k$ divided by the square of the second sample’s potency must exactly equal the stability metric $C$. This relationship is expressed as:
$$\left| a_i^2 + \frac{k}{a_j^2} \right| = C$$

This condition must hold true for every possible pair of distinct samples selected from the collection $\{a_1, a_2, \dots, a_n\}$. Given that the potency values $a_1, a_2, \dots, a_n$ must all be distinct, what is the maximum possible number of samples that can exist in such a collection?

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
