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

A specialized satellite mapping agency is analyzing a series of digital grids. For a fixed positive integer $k \ge 2$, they consider a massive dataset $\mathcal{F}_m$, which consists of all possible rectangular grids containing exactly $m$ active signals (represented by the value 1, while empty cells are 0). As the total number of signals $m$ becomes sufficiently large, the agency seeks to establish a guaranteed minimum threshold for data extraction.

For any specific grid $A$ in the dataset $\mathcal{F}_m$, a technician must select a subset of its active signals to form a filtered grid $B$. This filtered grid must satisfy two conditions: first, it must not contain any $k \times k$ solid block of signals (meaning no submatrix of size $k \times k$ can consist entirely of 1s); second, it must contain as many signals as possible. Let $f(m)$ be the maximum number of signals that can be guaranteed to remain in $B$ regardless of how the $m$ signals are distributed in the original grid $A$.

The efficiency of this filtering process is measured by the growth rate $g(k)$, defined by the limit:
$$g(k) = \lim_{m \to \infty} \frac{\ln f(m)}{\ln m}$$

Calculate the sum of these efficiency rates for the first three possible configurations of $k$:
$$g(2) + g(3) + g(4)$$

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
