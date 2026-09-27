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

In a futuristic data-encoding facility, a specialized signal-processing algorithm generates an experimental transmission wave represented by a polynomial $P(x)$ of degree 2012. The wave's primary frequency coefficient (the leading coefficient) is normalized to exactly 1, while the subsequent 2012 coefficients ($a_{2011}, a_{2010}, \dots, a_{0}$) are all real numbers.

Engineers have developed a "phase-inversion" technique that allows them to selectively flip the sign of any subset of these coefficients ($a_{2011}$ through $a_{0}$) by multiplying them by -1, while leaving the remaining coefficients untouched. This process is used to stabilize the signal's "interference nodes"—the roots $z$ of the resulting polynomial.

For the signal to remain stable within the facility's hardware, every root $z$ of the modified polynomial must lie within a specific angular safety zone in the complex plane. Specifically, the magnitude of the imaginary part of each root, $|\operatorname{Im} z|$, must not exceed $c$ times the magnitude of its real part, $|\operatorname{Re} z|$, where $c$ is a fixed non-negative real constant.

Determine the smallest real number $c$ such that, regardless of the initial values of the real coefficients $a_{i}$, there always exists a combination of sign flips that forces every root $z$ of the new polynomial to satisfy the stability constraint $|\operatorname{Im} z| \leqslant c|\operatorname{Re} z|$.

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
