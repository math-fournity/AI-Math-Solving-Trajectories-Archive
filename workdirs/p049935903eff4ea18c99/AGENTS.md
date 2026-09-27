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

Let \( K \) be a compact subset of \( \mathbb{C}^n \) and let \( P_0(K) \) be the set of all polynomials on \( K \). The \( P \)-hull of \( K \), the polynomial convex hull of \( K \), is defined by\n\n\[\nP\text{-hull } K = \{ z \in \mathbb{C}^n : |p(z)| \leq \sup_K |p(z)| \text{ for all } p \in P_0(K) \}.\n\]\n\nLet \( P(K) \) be the uniform closure of \( P_0(K) \) in \( C(K) \), the continuous functions on \( K \). Let Šilov Bd \((P(K))\) denote the Šilov boundary of the uniform algebra \( P(K) \); that is, the smallest closed subset of the structure space of a commutative Banach algebra where an analogue of the maximum modulus principle holds; see Alexander and Wermer [24, Chap.9]. Determine all compact subsets \( K \) in \( \mathbb{C}^n, n > 1 \) such that\n\n\[\n\text{Šilov Bd }(P(K)) = \text{Boundary }(P\text{-hull } K).\n\]\n\nFor \( n = 1 \), every compact set \( K \) in \( \mathbb{C} \) has this property. For \( n > 2 \), examples of \( K \) are compact convex sets and closed spheres.

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
