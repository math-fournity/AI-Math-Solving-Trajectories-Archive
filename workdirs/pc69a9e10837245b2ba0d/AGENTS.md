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

Let $F$ be an ordered field and $A$ a convex subring of $F$, which is a valuation ring and thus a local ring with maximal ideal $m_A$. For any subfield $C$ of $F$ contained in $A$ and maximal with respect to these conditions, the residue field $F_A = A / m_A$ is algebraic over the image $C_A$ of $C$ under the residue map $A \rightarrow A / m_A$. In this context, $F_A$ is ordered by $a + m_A < a' + m_A \Longleftrightarrow a < a'$. If $F$ is real closed, then $C_A$ is real closed and $C_A = F_A$. In general, $C_A$ may be a proper subfield of $F_A$. For example, if $F$ is an ultrapower of $\mathbb{Q}$ modulo some free ultrafilter on $\mathbb{N}$ and $A$ is the ring of finite and infinitesimal elements, then $F_A \cong \mathbb{R}$ while any maximal subfield of $A$ may contain no algebraic irrational number. Is $C_A$ always dense in $F_A$?

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
