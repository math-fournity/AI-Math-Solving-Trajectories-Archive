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

State and explain the properties of intersection multiplicity \( I(P, F \cap G) \) as given in Theorem 8.10, including:  
(a) Symmetry: \( I(P, F \cap G) = I(P, G \cap F) \),  
(b) Invariance under addition: \( I(P, F \cap G) = I(P, F \cap (G + HF)) \) for any projective plane curve \( H \) with \( \deg HF = \deg G \) and \( G + HF \neq 0 \),  
(c) Non-negativity: \( I(P, F \cap G) > 0 \) if and only if \( P \) lies in \( V_K(F) \cap V_K(G) \),  
(d) Monotonicity: \( I(P, F \cap G) \leq I(P, AF \cap BG) \) for any projective plane curves \( A \) and \( B \), with equality if \( A \) and \( B \) are nonvanishing at \( P \),  
(e) Finiteness: \( I(P, F \cap G) \) is finite if and only if \( F \) and \( G \) have no common factor of degree \( \geq 1 \) vanishing at \( P \),  
(f) Additivity: \( I(P, F \cap GH) = I(P, F \cap G) + I(P, F \cap H) \), and consequently, if \( F = \prod_i F_i^{r_i} \) and \( G = \prod_j G_j^{s_j} \), then \( I(P, F \cap G) = \sum_{i,j} r_i s_j I(P, F_i \cap G_j) \),  
(g) Lower bound: \( I(P, F \cap G) \geq m_P(F)m_P(G) \), with equality if \( F \) and \( G \) have no tangent lines in common at \( P \).

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
