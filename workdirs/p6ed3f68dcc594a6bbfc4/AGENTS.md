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

Let \(\mathcal{P}\) be the set of polynomials with degree \(2019\) with leading coefficient \(1\) and non-leading coefficients from the set \(\mathcal{C}=\{-1,0,1\}\). For example, the function \(f=x^{2019}-x^{42}+1\) is in \(\mathcal{P}\), but the functions \(f=x^{2020}\), \(f=-x^{2019}\), and \(f=x^{2019}+2x^{21}\) are not in \(\mathcal{P}\).

Define a swap on a polynomial \(f\) to be changing a term \(ax^{n}\) to \(bx^{n}\) where \(b \in \mathcal{C}\) and there are no terms with degree smaller than \(n\) with coefficients equal to \(a\) or \(b\). For example, a swap from \(x^{2019}+x^{17}-x^{15}+x^{10}\) to \(x^{2019}+x^{17}-x^{15}-x^{10}\) would be valid, but the following swaps would not be valid:

\[
\begin{array}{ccc}
x^{2019}+x^{3} & \text{ to } & x^{2019} \\
x^{2019}+x^{3} & \text{ to } & x^{2019}+x^{3}+x^{2} \\
x^{2019}+x^{2}+x+1 & \text{ to } & x^{2019}-x^{2}-x-1
\end{array}
\]

Let \(\mathcal{B}\) be the set of polynomials in \(\mathcal{P}\) where all non-leading terms have the same coefficient. There are \(p\) polynomials that can be reached from each element of \(\mathcal{B}\) in exactly \(s\) swaps, and there exist \(0\) polynomials that can be reached from each element of \(\mathcal{B}\) in less than \(s\) swaps.

Compute \(p \cdot s\), expressing your answer as a prime factorization.

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
