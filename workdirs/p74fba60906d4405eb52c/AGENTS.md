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

In a remote industrial district, three specialized power plants—Alpha, Beta, and Gamma—are connected in a triangular grid. The lengths of the high-voltage transmission lines connecting them are denoted as $a$, $b$, and $c$. Because these lines form a physical triangle, they must satisfy the triangle inequality.

The efficiency of the grid is determined by comparing two specific energy loss factors. 
The "Clockwise Flux" of the system is calculated by the formula: 
$F_{CW} = ab^2 + bc^2 + ca^2 - 3abc$

The "Counter-Clockwise Flux" of the system is calculated by the formula: 
$F_{CCW} = a^2b + b^2c + c^2a - 3abc$

An engineer needs to determine the maximum guaranteed stability ratio $\delta$. This is the largest possible positive real constant such that the ratio of the Clockwise Flux to the Counter-Clockwise Flux is always greater than or equal to $\delta$, regardless of the specific side lengths $a, b,$ and $c$ (so long as they form a valid triangle).

The optimal value of $\delta$ can be expressed in the simplified form $\frac{p - \sqrt{q}}{r}$, where $p$, $q$, and $r$ are positive integers. Compute the sum $p + q + r$.

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
