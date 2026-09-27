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

Let $H = H_1 \times H_2$ be a closed subgroup of a second-countable locally compact Hausdorff group $G = G_1 \times G_2$, with $H_i \leq G_i$. Let $\chi = \chi_1 \otimes \chi_2$ be a unitary character of $H$, where $\chi_i$ is a character of $H_i$. Consider the induced representation $I(\chi) = \operatorname{Ind}_H^G\chi$, which is the Hilbert space of measurable functions $f: G \rightarrow \mathbb{C}$ satisfying $f(hg) = \chi(h)f(g)$ and the norm condition $\int_{H \backslash G} |f(g)|^2 \, dg < \infty$. Let $V \subset I(\chi)$ be the linear space spanned by functions of the form $(g_1,g_2) \mapsto f_1(g_1)f_2(g_2)$, for continuous $f_i \in I(\chi_i)$. Is $V$ norm-dense in $I(\chi)$?

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
