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

In a specialized logistics hub, there are 40 unique equipment crates, each labeled with a distinct ID number from the set $\{1, 2, \ldots, 40\}$. These crates are delivered in a completely random sequence, forming a permutation $a = (a_1, a_2, \ldots, a_{40})$ where every possible ordering is equally likely.

A technician named William is tasked with organizing these crates into two groups: the "Alpha" group consisting of the first 20 crates $(a_1, \ldots, a_{20})$ and the "Beta" group consisting of the remaining 20 crates $(a_{21}, \ldots, a_{40})$. William creates a $20 \times 20$ "Compatibility Matrix" $B$, where the entry $b_{i,j}$ in the $i$-th row and $j$-th column is defined as the higher ID number between the $i$-th crate of the Alpha group and the $j$-th crate of the Beta group (i.e., $b_{i,j} = \max(a_i, a_{j+20})$).

After filling out all 400 entries of the matrix, William accidentally shreds the list of the original sequence $a$. He realizes that for some matrices, there might be multiple original sequences that could have produced those exact values.

Compute the probability that, given only the completed matrix $B$, there are exactly 2 distinct original permutations $a$ that are consistent with the recorded values. If this probability is expressed as an irreducible fraction $\frac{a}{b}$, find the value of $a+b$.

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
