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

A specialized materials lab is testing two types of experimental conductive films, Type-X and Type-Y. The electrical resistance of these films is governed by a specific polynomial function $P$ with real coefficients.

A stability threshold exists for these films based on their thickness. For Type-X film with thickness $x$ and Type-Y film with thickness $y$, the following two conditions are discovered to be perfectly reciprocal (one is true if and only if the other is true):

Condition A: The squared thickness of the Type-Y film differs from the resistance $P(x)$ by no more than twice the magnitude of $x$. That is, $|y^2 - P(x)| \le 2|x|$.

Condition B: The squared thickness of the Type-X film differs from the resistance $P(y)$ by no more than twice the magnitude of $y$. That is, $|x^2 - P(y)| \le 2|y|$.

The lab director is interested in the potential "base resistance" of such a material, defined as the value $P(0)$. Let $S$ be the set of all possible real values that $P(0)$ can take such that the reciprocal property holds for all real $x$ and $y$.

Determine which of the following candidate values $k \in \{-10, -5, 0, 1, 5\}$ are contained in the set $S$. Define $v_k = 1$ if $k \in S$ and $v_k = 0$ if $k \notin S$. 

Calculate the total sum: $v_{-10} + v_{-5} + v_0 + v_1 + v_5$.

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
