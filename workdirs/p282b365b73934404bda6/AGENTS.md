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

In the high-tech city of Centuria, there are $103^2 - 1$ unique frequency channels available for secure communication. Each channel is identified by a unique coordinate pair $(i, j)$, where $i$ and $j$ are integers from the set $\{0, 1, \dots, 102\}$, excluding the dead-zone channel $(0,0)$. 

A telecommunications company, SignalFlow, has been assigned a specific non-empty set of active channels, denoted as $S$. To prevent interference, the company must select a subset of these active channels, $A \subseteq S$, such that for any three channels (not necessarily distinct) chosen from $A$—say $(x_1, y_1)$, $(x_2, y_2)$, and $(x_3, y_3)$—they never simultaneously satisfy the following two "interference equations" in modulo 103 arithmetic:
1. $x_1 + x_2 \equiv y_3 \pmod{103}$
2. $y_1 + y_2 \equiv -x_3 \pmod{103}$

It is mathematically guaranteed that such a subset $A$ exists such that the size of the subset, $n(A)$, satisfies the inequality $k \cdot n(A) > n(S)$ for a specific constant $k$. Given that $103$ is a prime congruent to $3 \pmod 4$, what is the smallest integer $k$ that guarantees the existence of such a subset $A$ according to the standard bounds for this type of problem?

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
