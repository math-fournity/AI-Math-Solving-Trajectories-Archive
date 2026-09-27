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

In a specialized logistics warehouse, an inventory robot processes three types of crates: Type-X, Type-Y, and Type-Z. The robot starts with zero crates of each type, denoted as the state $(0,0,0)$. 

The warehouse operates under strict safety protocols regarding the stacking and sequencing of these crates. At any given moment, the current counts of crates $(x, y, z)$ must satisfy the following hierarchical stability conditions:
1. The number of Type-Y crates cannot exceed the number of Type-X crates by more than one ($y + 1 \geq x$).
2. The number of Type-X crates must be at least the number of Type-Y crates ($x \geq y$).
3. The number of Type-Y crates must be at least the number of Type-Z crates ($y \geq z$).
4. The number of Type-Z crates cannot be negative ($z \geq 0$).

The robot performs a "processing cycle" by adding exactly one crate to the inventory at a time (either one Type-X, one Type-Y, or one Type-Z). Each such addition is considered one step.

For any positive integer $n$, let $P(n)$ be the total number of distinct valid sequences of steps the robot can take to reach a final inventory state of exactly $n$ crates of each type $(n, n, n)$ using a total of exactly $3n$ steps, such that every intermediate state throughout the sequence strictly obeys the stability conditions.

Calculate the sum of the number of valid paths for the first four target levels:
$P(1) + P(2) + P(3) + P(4)$

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
