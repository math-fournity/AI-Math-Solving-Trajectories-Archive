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

A specialized chemical refinery operates with a primary centrifuge that completes exactly $p = 101$ rotations per cycle. To test different production settings, an engineer selects a "stability factor" $s$, where $s$ is an integer such that $0 < s < p$. 

For each chosen stability factor $s$, the engineer monitors two specific timestamps, $m$ and $n$, representing the number of full rotations completed since the start of the cycle. These timestamps must be integers such that $0 < m < n < p$. 

The refinery’s monitoring software calculates the "phase offset" for any timestamp $k$ using the formula $f(k) = \frac{(s \cdot k) \pmod p}{p}$. This value represents the fractional progress toward the next unit of output at that specific rotation.

The engineer flags a stability factor $s$ as "unstable" if there exists at least one pair of timestamps $(m, n)$ that satisfies the following cascading efficiency constraint:
$$ f(m) < f(n) < \frac{s}{p} $$
Let $S_s$ be the set of all such pairs $(m, n)$ for a given $s$. 

The engineer is specifically interested in the set $A$, which consists of all stability factors $s \in \{1, 2, \dots, p-1\}$ for which the set $S_s$ is empty (meaning no such pairs $(m, n)$ can be found).

Find the sum of all the stability factors in set $A$.

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
