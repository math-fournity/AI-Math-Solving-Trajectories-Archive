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

Let $(X,d_X)$ and $(Y,d_Y)$ be compact metric spaces, each with at least two points. Consider a Lipschitz function $f:X\times Y\to\mathbb{R}$, meaning there exists a constant $C>0$ such that for all $x,x'\in X$ and $y,y'\in Y$, \[|f(x,y)-f(x',y')|\leq C(d_X(x,x')+d_Y(y,y')).\] Define the zero marginal superlevel set of $f$ for each $x\in X$ as \[F(x) = \{y\in Y \mid f(x,y)\geq 0\},\] which is a compact subset of $Y$. The space $\mathcal{K}(Y)$ consists of non-empty compact subsets of $Y$, equipped with the Hausdorff distance \[d_H(K,K') = \sup_{y\in Y} |d_Y(y,K) - d_Y(y,K')|,\] where \[d_Y(y,Z) = \inf_{y'\in Z} d_Y(y,y').\] Consider the set-valued map $F:X\to\mathcal{K}(Y)$ defined by $F(x)$. Is $F$ Lipschitz as a map from $(X,d_X)$ to $(\mathcal{K}(Y),d_H)$? That is, does there exist a constant $C'>0$ such that for all $x,x'\in X$, \[d_H(F(x),F(x'))\leq C'd_X(x,x')?\]

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
