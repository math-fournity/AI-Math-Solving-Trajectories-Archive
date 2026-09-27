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

Triangle \(ABC\) has circumcenter \(O\) and circumcircle \(\omega\). Let \(A_{\omega}\) be the point diametrically opposite \(A\) on \(\omega\), and let \(H\) be the foot of the altitude from \(A\) onto \(BC\). Let \(H_B\) and \(H_C\) be the reflections of \(H\) over \(B\) and \(C\), respectively. Point \(P\) is the intersection of line \(A_{\omega}B\) and the perpendicular to \(BC\) at point \(H_B\), and point \(Q\) is the intersection of line \(A_{\omega}C\) and the perpendicular to \(CB\) at point \(H_C\). The circles \(\omega_1\) and \(\omega_2\) have the respective centers \(P\) and \(Q\) and respective radii \(PA\) and \(QA\). Suppose that \(\omega, \omega_1\), and \(\omega_2\) intersect at another common point \(X\). If \(AO=\frac{\sqrt{105}}{5}\) and \(AX=4\), then \(|AB-CA|^2\) can be written as \(m-n\sqrt{p}\) for positive integers \(m\) and \(n\) and squarefree positive integer \(p\). Find \(m+n+p\).

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
