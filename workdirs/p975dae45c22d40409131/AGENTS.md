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

Suppose $S$ and $T$ are simplicial sets such that $S_0 = T_0$, $S_1 = T_1$, and $S_2 = T_2$. The face maps $d_0, d_1 : S_1 \to S_0$ agree with the maps $d_0, d_1 : T_1 \to T_0$, and the degeneracy map $s_0 : S_0 \to S_1$ agrees with $s_0 : T_0 \to T_1$. Additionally, the face maps $d_0, d_1, d_2 : S_2 \to S_1$ agree with $d_0, d_1, d_2 : T_2 \to T_1$, and the degeneracy maps $s_0, s_1: S_1 \to S_2$ agree with $s_0, s_1: T_1 \to T_2$. Given that $S$ and $T$ are simplicial sets of dimension \( \leq 2 \), does it follow that $S$ and $T$ are isomorphic?

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
