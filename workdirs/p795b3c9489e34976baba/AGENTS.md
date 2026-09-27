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

Given matrix polynomials \( P(\lambda) = A_m \lambda^m + \ldots + A_1 \lambda + A_0 \) and \( Q(\lambda) = B_m \lambda^m + \ldots + B_1 \lambda + B_0 \), where \( Z(\lambda) = (A_m + B_m) \lambda^m + \ldots + (A_1 + B_1) \lambda + (A_0 + B_0) \) is their sum. Let \( \| A_j \| \) and \( \| B_j \| \) denote the induced 2-norm of the matrices, with \( \| A_j \| = \max_{\| x \|_2 = 1} \| A_j x \|_2 \) and \( \| B_j \| = \max_{\| x \|_2 = 1} \| B_j x \|_2 \). Define \( \| P(\lambda) \| = \max_j \| A_j \| \) and \( \| Q(\lambda) \| = \max_j \| B_j \| \). Assume that \( \det(P(\lambda)) \neq 0 \), \( \det(Z(\lambda)) = 0 \), and \( \| B_j \| \le \varepsilon \) for some small positive \( \varepsilon \). Is it necessarily true that \( \| P(\lambda)^{-1} Q(\lambda) \| \ge 1 \)?

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
