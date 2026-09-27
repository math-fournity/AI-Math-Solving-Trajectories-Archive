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

Return your final response within \boxed{}. Let \(\left\{a_{n}\right\}\) be an arithmetic sequence with a common difference that is non-zero, and it satisfies the conditions \(a_{3} + a_{6} = a_{9}\) and \(a_{5} + a_{7}^{2} = 6a_{9}\). Denote the sum of the first \(n\) terms of the sequence \(\left\{b_{n}\right\}\) by \(S_{n}\), and \(4S_{n} + 2b_{n} = 3\). For any \(i \in \mathbf{Z}_{+}\), insert \(i\) numbers \(x_{i1}, x_{i2}, \cdots, x_{ii}\) between \(b_{i}\) and \(b_{i+1}\) such that \(b_{i}, x_{i1}, x_{i2}, \cdots, x_{ii}, b_{i+1}\) forms an arithmetic sequence. Let \(T_{n} = \sum_{i=1}^{n} \sum_{j=1}^{i} x_{i j}\). Does there exist positive integers \(m\) and \(n\) such that \(T_{n} = \frac{a_{m+1}}{2a_{m}}\)? If so, find all such pairs of positive integers \((m, n)\); if not, explain why.

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
