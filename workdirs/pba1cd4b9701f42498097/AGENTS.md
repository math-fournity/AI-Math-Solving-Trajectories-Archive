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

In a futuristic data-transmission hub, a signal is governed by a fundamental unit of rotation $\omega$, defined as the first primitive $2013$-th root of unity. This means $\omega^{2013} = 1$, but for any positive integer $m$ less than $2013$, $\omega^m \neq 1$.

Engineers are calibrating a dual-stage filtering system. The efficiency of the first stage is determined by an integer setting $a$, resulting in a cumulative gain of $S_a = \sum_{k=0}^{a} \omega^k$. The efficiency of the second stage is determined by an integer setting $b$, resulting in a cumulative gain of $S_b = \sum_{k=0}^{b} \omega^k$.

The combined output of the system is calculated as the product of these gains divided by a constant damping factor of $3$:
\[ \text{Output} = \frac{S_a \cdot S_b}{3} \]

The system is considered "harmonically stable" if this Output is an algebraic integer—that is, it serves as a root of a monic polynomial with integer coefficients.

Calculate the total number of possible ordered pairs of settings $(a, b)$, where $1 \le a, b \le 2013$, that result in a harmonically stable system.

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
