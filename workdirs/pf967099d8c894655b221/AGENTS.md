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

8. (GBR) ${ }^{\mathrm{IMO} 2}$ Four different points $A, B, C, D$ are chosen on a circle $\Gamma$ such that the triangle $B C D$ is not right-angled. Prove that: (a) The perpendicular bisectors of $A B$ and $A C$ meet the line $A D$ at certain points $W$ and $V$, respectively, and that the lines $C V$ and $B W$ meet at a certain point $T$. (b) The length of one of the line segments $A D, B T$, and $C T$ is the sum of the lengths of the other two. Original formulation. In triangle $A B C$ the angle at $A$ is the smallest. A line through $A$ meets the circumcircle again at the point $U$ lying on the $\operatorname{arc} B C$ opposite to $A$. The perpendicular bisectors of $C A$ and $A B$ meet $A U$ at $V$ and $W$, respectively, and the lines $C V, B W$ meet at $T$. Show that $A U=T B+T C$.

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
