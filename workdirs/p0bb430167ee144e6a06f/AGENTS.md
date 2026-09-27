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

In a remote digital kingdom, there are $n$ distinct magical keystones, which we can call the set $S$. The kingdom is governed by a "Selection Protocol" (a binary operation $\times$). This protocol is defined by two laws: first, it is associative, meaning the order of operations does not change the result; second, it is a selection rule, meaning that for any two keystones $x$ and $y$, the result $x \times y$ must be either $x$ or $y$.

A "Command Sequence" is any string formed by these $n$ keystones. When a specific Selection Protocol is applied, a sequence is processed from left to right (or in any order, given associativity) until it reduces to a single output keystone from $S$. 

A sequence is classified as "Universal" if every one of the $n$ keystones appears in it at least once. Two sequences are considered "Functionally Identical" if they yield the exact same output keystone for every possible Selection Protocol that satisfies the two laws. 

The High Archives contain a Master Collection $T$. This collection is constructed such that every possible Universal sequence is Functionally Identical to exactly one sequence in $T$, and no two sequences within $T$ are Functionally Identical to each other.

Calculate the total number of unique sequences contained in the Master Collection $T$ as a function of $n$.

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
