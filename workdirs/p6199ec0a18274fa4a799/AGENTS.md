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

Solve the following initial value problem for the vibrating circular membrane: Find \(u(r, \theta, t), 0<r \leq 1\), such that
\[
\begin{gathered}
\frac{\partial^{2} u}{\partial t^{2}}=\frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial u}{\partial r}\right)+\frac{1}{r^{2}} \frac{\partial^{2} u}{\partial \theta^{2}}, \\
u(r, \theta+2 \pi, t)=u(r, \theta, t), \quad \text { u well-behaved near } r=0, \\
u(1, \theta, t)=0, \\
u(r, \theta, 0)=J_{0}\left(\alpha_{0,1} r\right)+3 J_{0}\left(\alpha_{0,2} r\right)-2 J_{1}\left(\alpha_{1,1} r\right) \sin \theta+4 J_{2}\left(\alpha_{2,1} r\right) \cos 2 \theta .
\end{gathered}
\]

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
