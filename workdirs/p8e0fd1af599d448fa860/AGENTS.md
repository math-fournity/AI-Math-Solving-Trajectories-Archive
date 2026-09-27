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

Let $n \geq 2$ be a natural number, and let $\left( a_{1};\;a_{2};\;...;\;a_{n}\right)$ be a permutation of $\left(1;\;2;\;...;\;n\right)$. For any integer $k$ with $1 \leq k \leq n$, we place $a_k$ raisins on the position $k$ of the real number axis. 

Now, we place three children A, B, C on the positions $x_A$, $x_B$, $x_C$, where each $x_i \in \{1, 2, \dots, n\}$. For any $k$, the $a_k$ raisins placed on position $k$ are equally handed out to those children whose positions are closest to $k$ on the axis. [So, if there is only one child at distance $d = \min(|x_A-k|, |x_B-k|, |x_C-k|)$ from $k$, then he gets all $a_k$ raisins. If there are two or three children at the same minimum distance, they share the $a_k$ raisins equally.]

A child is unhappy if he could have received more raisins than he actually has received if he had moved to another position in $\{1, 2, \dots, n\}$ (while the other children stayed at their current positions).

Let $S$ be the set of all $n \geq 2$ such that there exists a configuration $\left( a_{1};\;a_{2};\;...;\;a_{n}\right)$ and positions $x_A, x_B, x_C$ where all three children are happy. Find the sum of all elements in $S$.

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
