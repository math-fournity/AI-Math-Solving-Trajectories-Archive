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

Determine the highest integer \( n \) such that the following conditions are satisfied for a 1-dimensional vector space \( V \), a 1-dimensional affine space \( A \), and a 1-dimensional projective space \( P \), all over the real numbers \( \mathbb{R} \):

1) For any \( n \) distinct non-zero vectors \( v_1, v_2, \ldots, v_n \in V \) and \( n \) distinct vectors \( v_1^*, v_2^*, \ldots, v_n^* \in V \), there exists a linear mapping \( f: V \rightarrow V \) such that \( f(v_i) = v_i^* \) for \( i = 1, 2, \ldots, n \).
2) For any \( n \) distinct points \( p_1, p_2, \ldots, p_n \in A \) and \( n \) distinct points \( p_1^*, p_2^*, \ldots, p_n^* \in A \), there exists an affinity \( g: A \rightarrow A \) with \( g(p_i) = p_i^* \) for \( i = 1, 2, \ldots, n \).
3) For any \( n \) distinct points \( Q_1, Q_2, \ldots, Q_n \in P \) and \( n \) distinct points \( Q_1^*, Q_2^*, \ldots, Q_n^* \in P \), there exists a projective collineation \( h: P \rightarrow P \) with \( h(Q_i) = Q_i^* \) for \( i = 1, 2, \ldots, n \).

What is the highest value of \( n \) for which these conditions hold?

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
