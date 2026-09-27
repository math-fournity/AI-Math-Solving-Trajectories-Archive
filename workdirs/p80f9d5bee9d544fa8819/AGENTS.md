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

In a specialized logistics network, a "Unique Sum System" is defined as a fleet of trucks with specific cargo capacities chosen from the integer range $\{1, 2, \dots, 100\}$. A fleet $S$ qualifies as a "Unique Sum System" if, for any four trucks in the fleet with capacities $a, b, c,$ and $d$, the total combined weight of any two trucks ($a+b$) is equal to the total weight of any other two trucks ($c+d$) only if the two pairs consist of the exact same trucks.

A lead researcher is investigating the limits of these systems. To determine the maximum possible size $n$ of such a fleet, the researcher employs a specific counting strategy. This strategy calculates the total number of distinct pairs of trucks that can be formed from a fleet of size $k$, which is given by the combination $\binom{k}{2}$. The strategy then compares this count to the total number of possible positive differences between any two capacities in the set $\{1, 2, \dots, 100\}$, which is exactly $99$.

By identifying that a "Unique Sum System" is mathematically equivalent to a set where all pairwise differences are distinct (and accounting for the internal structure of 3-term arithmetic progressions within the set), this specific proof strategy can be used to prove the non-existence of such a fleet for certain values of $k$.

Find the largest integer $k$ for which this specific comparison between $\binom{k}{2}$ and the $99$ available differences (under the constraints of the 1-100 range) guarantees that no "Unique Sum System" of size $k$ can exist.

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
