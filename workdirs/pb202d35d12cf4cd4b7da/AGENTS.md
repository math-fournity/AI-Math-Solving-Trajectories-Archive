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

[G. Pólya, problem: Arch. Math. Phys. Series 3, 20, p. 271 (1913).] The corresponding quadratic form\n\n\[\n\int_a^b [(t_1^2 + t_2^2 + \cdots + t_n^2)((f_1(x))^2 + (f_2(x))^2 + \cdots + (f_n(x))^2) - [t_1 f_1(x) + t_2 f_2(x) + \cdots + t_n f_n(x)]^2] \, dx = \int_a^b \sum_{p \ne k}^{1, 2, \ldots, n} [t_p f_p(x) - t_k f_k(x)]^2 \, dx\n\]\n\nis positive. It vanishes for a set of numbers \( t_1, t_2, \ldots, t_n \) with \( t_1^2 + t_2^2 + \cdots + t_n^2 > 0 \), if and only if \( f_v(x) = \varphi(x), v = 1, 2, \ldots, n \), where \(\varphi(x)\) does not depend on \(v\).

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
