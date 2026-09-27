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

Three. (This question is worth 50 points) In a $100 \times 25$ rectangular table, each cell is filled with a non-negative real number. The number in the $i$-th row and $j$-th column is denoted as $x_{i, j} (i=1,2, \cdots, 100 ; j=1,2, \cdots, 25)$ (as shown in Table 1). Then, the numbers in each column of Table 1 are rearranged in descending order from top to bottom as
$$
\begin{array}{c}
x_{1, j}^{\prime} \geqslant x_{2, j}^{\prime} \geqslant \cdots \geqslant x_{100, j}^{\prime} \\
(j=1,2, \cdots, 25) . \text { (as shown in Table 2) }
\end{array}
$$

Find the smallest natural number $k$, such that if the numbers in Table 1 satisfy
$$
\sum_{j=1}^{25} x_{i, j} \leqslant 1(i=1,2, \cdots, 100),
$$

then when $i \geqslant k$, in Table 2 it can be guaranteed that
$$
\sum_{j=1}^{25} x_{i, j}^{\prime} \leqslant 1
$$

holds.
Table 1
\begin{tabular}{|c|c|c|c|}
\hline$x_{1,1}$ & $x_{1,2}$ & $\cdots$ & $x_{1,25}$ \\
\hline$x_{2,1}$ & $x_{2,2}$ & $\cdots$ & $x_{2,25}$ \\
\hline$\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ \\
\hline$x_{100,1}$ & $x_{100,2}$ & $\cdots$ & $x_{100,25}$ \\
\hline
\end{tabular}

Table 2
\begin{tabular}{|c|c|c|c|}
\hline$x_{1,1}^{\prime}$ & $x_{1,2}^{\prime}$ & $\cdots$ & $x_{1,25}^{\prime}$ \\
\hline$x_{2,1}^{\prime}$ & $x_{2,2}^{\prime}$ & $\cdots$ & $x_{2,25}^{\prime}$ \\
\hline$\cdots$ & $\cdots$ & $\cdots$ & $\cdots$ \\
\hline$x_{100,1}^{\prime}$ & $x_{100,2}^{\prime}$ & $\cdots$ & $x_{100,25}^{\prime}$ \\
\hline
\end{tabular}
(Proposed by the Problem Committee)

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
