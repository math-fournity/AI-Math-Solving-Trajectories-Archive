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

For an integer \( n \geq 2 \), let \( G_{n} \) be an \( n \times n \) grid of unit cells. A subset of cells \( H \subseteq G_{n} \) is considered quasi-complete if and only if each row of \( G_{n} \) has at least one cell in \( H \) and each column of \( G_{n} \) has at least one cell in \( H \). A subset of cells \( K \subseteq G_{n} \) is considered quasi-perfect if and only if there is a proper subset \( L \subset K \) such that \(|L|=n\) and no two elements in \( L \) are in the same row or column. Let \(\vartheta(n)\) be the smallest positive integer such that every quasi-complete subset \( H \subseteq G_{n} \) with \(|H| \geq \vartheta(n)\) is also quasi-perfect. Moreover, let \(\varrho(n)\) be the number of quasi-complete subsets \( H \subseteq G_{n} \) with \(|H|=\vartheta(n)-1\) such that \( H \) is not quasi-perfect. Compute \(\vartheta(20)+\varrho(20)\).

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
