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

Let $X$ be an irreducible smooth projective variety over $\mathbb{C}$, and let $G$ be an affine algebraic group over $\mathbb{C}$. Consider a holomorphic principal $G$-bundle $p : E_G \longrightarrow X$ on $X$. The adjoint vector bundle of $E_G$, denoted $ad(E_G) = E_G \times^G \mathfrak{g}$, is associated with the adjoint representation $ad : G \longrightarrow \text{End}(\mathfrak{g})$ of $G$ on its Lie algebra $\mathfrak{g}$. The fibers of $ad(E_G)$ are $\mathbb{C}$-linearly isomorphic to $\mathfrak{g}$. Consider $ad(E_G)$ as a sheaf of $\mathcal{O}_X$-modules on $X$. Is there an $\mathcal{O}_X$-bilinear homomorphism $[,] : ad(E_G) \times ad(E_G) \to ad(E_G)$ that gives a Lie algebra structure on the sheaf $ad(E_G)$?

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
