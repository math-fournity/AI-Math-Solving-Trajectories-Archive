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

A digital security firm is stress-testing a new cryptographic algorithm based on a massive "Network Expansion Protocol." The protocol operates across a lattice of $2 \cdot 10^{10}$ distinct processing nodes.

The total security strength of the system, denoted as $S$, is calculated by evaluating specific configurations of these nodes. Specifically, the system designer defines $S$ as the sum of the capacities of all possible even-sized sub-clusters. For any cluster of size $k$ (where $k$ must be an even number between $0$ and $2 \cdot 10^{10}$ inclusive), its capacity is defined by the number of ways to choose that cluster from the total nodes, multiplied by a "Pentagonal Power Factor" of $5^{k/2}$.

Mathematically, the total strength $S$ is expressed as:
$$S = \sum_{n=0}^{10^{10}} \binom{2 \cdot 10^{10}}{2n} 5^n$$

To determine the vulnerability of the system to binary-based brute force attacks, the engineers need to find the "Bit-Depth Resistance." This is defined as the largest integer $v$ such that $2^v$ divides $S$.

Find the value of this greatest power of $2$.

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
