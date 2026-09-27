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

A logistics company manages a massive automated warehouse with a storage floor divided into an $n \times n$ square grid of $n^2$ slots (where $n \ge 2$). There are $n^2$ unique heavy storage crates, labeled with distinct identification numbers from $1$ to $n^2$.

Currently, the crates are arranged in an initial configuration, $A$, where each slot $(i, j)$ contains a specific crate $a_{ij}$. The company needs to reorganize the entire warehouse into a target configuration, $B$, where each slot $(i, j)$ must contain a specific crate $b_{ij}$. Both configurations $A$ and $B$ utilize the exact same set of $n^2$ crates.

The warehouse uses a specialized robotic crane that can only move along the fixed tracks of the grid. Because of the weight of the crates and the mechanical limits of the crane, it can only perform one specific type of maneuver, called a "transposition": the crane selects exactly two crates that are currently located in the same row or the same column and swaps their positions, leaving all other $n^2 - 2$ crates exactly where they were.

What is the smallest positive integer $m$ such that, regardless of the initial arrangement $A$ and the target arrangement $B$, the crane can always transform $A$ into $B$ using no more than $m$ transpositions?

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
