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

Given standard Borel spaces \((X, \mathcal{X})\) and \((A, \mathcal{A})\), an analytic set \(D \subseteq X \times A\), and a lower semianalytic function \(c:D \rightarrow [0, \infty]\), consider a stochastic kernel \(p(\cdot|\cdot)\) such that \((x,a) \mapsto p(B | x, a)\) is lower semianalytic for each \(B \in \mathcal{X}\), and \(B \mapsto p(B | x, a)\) is a probability measure on \((X, \mathcal{X})\) for each \((x, a) \in D\). Define \(\eta_u(x, a) := c(x, a) + \int_X u(y)p(dy | x, a)\) for a lower semianalytic \(u:X \rightarrow [0, \infty]\) and \((x, a) \in D\). Let \(\eta^*_u(x) := \inf_{a \in D_x}\eta_u(x, a)\) for \(x \in \text{proj}_X(D)\). Given \(\epsilon > 0\), does there exist a universally measurable function \(\varphi:\text{proj}_X(D) \rightarrow A\) such that \(\varphi(x) \in D_x\) for all \(x \in X\) and, for all \(x \in \text{proj}_X(D)\), \(\eta_u(x, \varphi(x)) \leq \eta_u^*(x) + \epsilon\)?

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
