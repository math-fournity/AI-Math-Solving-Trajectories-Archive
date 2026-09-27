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

Given points $O, A_1, A_2, \dots, A_n$ in the plane such that for any two points $P, Q \in \{O, A_1, \dots, A_n\}$, the square of the distance between them is an integer. It is a known result that there exist two vectors $\vec{x}$ and $\vec{y}$ such that for every $i \in \{1, \dots, n\}$, there exist integers $k_i, l_i$ satisfying $\vec{OA_i} = k_i\vec{x} + l_i\vec{y}$.

For each $i, j \in \{1, \dots, n\}$, let $S_{i,j}$ denote the area of triangle $OA_i A_j$. Let $M$ be the smallest positive integer such that $M \cdot S_{i,j}^2$ is always an integer for any such set of points and any $i, j$.

Consider the specific case where $n=3$ and the squared distances are:
$OA_1^2 = 14$, $OA_2^2 = 21$, $OA_3^2 = 35$,
$A_1A_2^2 = 11$, $A_1A_3^2 = 25$, $A_2A_3^2 = 30$.

Let $V$ be the area of the triangle $A_1 A_2 A_3$. Calculate the value of $M \cdot V^2$.

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
