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

A specialized logistics company manages a series of automated cargo containers, indexed $n = 1, 2, 3, \dots$. Each container $n$ has a specific weight $a_n$ measured in kilograms, where all weights are distinct integers. The containers are organized such that as the index increases, the weight strictly increases ($a_n < a_{n+1}$).

The company’s safety protocol involves a "Balanced Stress Test" for any four containers indexed $i, j, k, l$ that satisfy two conditions: the indices must be ordered such that $1 \leq i < j \leq k < l$, and the sum of the inner and outer indices must be equal ($i + l = j + k$). For every such quadruple, the structural integrity of the facility requires that the combined weight of the outermost containers must strictly exceed the combined weight of the innermost containers ($a_i + a_l > a_j + a_k$).

Based on these operational constraints, calculate the minimum possible weight of the 2008th container ($a_{2008}$).

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
