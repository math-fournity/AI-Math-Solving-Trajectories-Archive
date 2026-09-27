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

In a remote island nation, a logistics coordinator named Anton and a data analyst named Britta are dividing a cache of $n-1$ specialized radio frequencies, indexed by the set $M = \{1, 2, \dots, n-1\}$. The total number of frequencies $n-1$ is an even integer such that $n$ is an odd prime or composite number $n \ge 5$.

The two colleagues take turns selecting one frequency at a time from $M$ until the cache is depleted. Anton always takes the first turn. Anton stores his selected frequencies in a private database $A$, and Britta stores hers in database $B$. Because $n-1$ is even, both databases will ultimately contain exactly $\frac{n-1}{2}$ frequencies.

Once all frequencies are distributed, Anton must select two distinct frequencies, $x_1$ and $x_2$, from his database $A$ and broadcast them to Britta. After hearing Anton's choices, Britta must select two distinct frequencies, $y_1$ and $y_2$, from her database $B$.

Britta is declared the winner of this technical challenge if the resulting configuration satisfies the following power-congruence relation:
$$(x_1 x_2 (x_1 - y_1) (x_2 - y_2))^{\frac{n-1}{2}} \equiv 1 \pmod n$$
Otherwise, Anton wins.

Determine all values of $n$ for which Britta has a winning strategy, regardless of how Anton selects his frequencies.

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
