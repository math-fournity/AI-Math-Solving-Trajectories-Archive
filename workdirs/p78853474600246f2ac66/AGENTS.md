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

Define a function $w:\mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ as follows. For $|a|,|b| \leq 2$, let $w(a,b)$ be as in the table shown; otherwise, let $w(a,b)=0$.
\begin{center}
\begin{tabular}{|cc|r|r|r|r|r|}
\hline
\multicolumn{2}{|c|}{\multirow{2}{*}{$w(a,b)$}} & \multicolumn{5}{|c|}{$b$} \\
& & -2 & -1 & 0 & 1 & 2 \\
\hline
& -2 & -1 & -2 & 2 & -2 & -1 \\
& -1 & -2 & 4 & -4 & 4 & -2 \\
$a$ & 0 & 2 & -4 & 12 & -4 & 2 \\
& 1 & -2 & 4 & -4 & 4 & -2 \\
& 2 & -1 & -2 & 2 & -2 & -1 \\
\hline
\end{tabular}
\end{center}
For every finite subset $S$ of $\mathbb{Z} \times \mathbb{Z}$, define $A(S)=\sum_{(\mathbf{s},\mathbf{s}') \in S \times S} w(\mathbf{s}-\mathbf{s}')$. Prove that if $S$ is any finite nonempty subset of $\mathbb{Z} \times \mathbb{Z}$, then $A(S)>0$. (For example, if $S=\{(0,1),(0,2),(2,0),(3,1)\}$, then the terms in $A(S)$ are $12,12,12,12,4,4,0,0,0,0,-1,-1,-2,-2,-4,-4$.)

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
