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

Let \( S \) be the set of lattice points \((x, y) \in \mathbb{Z}^{2}\) such that \(-10 \leq x, y \leq 10\). Let the point \((0,0)\) be \( O \). Let Scotty the Dog's position be point \( P \), where initially \( P=(0,1) \). At every second, consider all pairs of points \( C, D \in S \) such that neither \( C \) nor \( D \) lies on line \( OP \), and the area of quadrilateral \( OCPD \) (with the points going clockwise in that order) is \( 1 \). Scotty finds the pair \( C, D \) maximizing the sum of the \( y \) coordinates of \( C \) and \( D \), and randomly jumps to one of them, setting that as the new point \( P \). After \( 50 \) such moves, Scotty ends up at point \( (1,1) \). Find the probability that he never returned to the point \( (0,1) \) during these \( 50 \) moves. If the answer is of the form of an irreducible fraction $\frac{a}{b}$, compute the value of $a + b$.

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
