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

A specialized cybersecurity firm uses a multi-layered encryption protocol based on four distinct security checks. The system operates using a specific prime-numbered security key, $p$, which is less than $1000$.

The firmware tracks three positive integer configuration settings: $a$, $b$, and $c$. For the system to remain stable, the following four data packages must be perfectly divisible by the security key $p$:

1.  The first package value is calculated by adding the three settings and adding an offset of $1$: $(a + b + c + 1)$.
2.  The second package value is the sum of the squares of the settings plus an offset of $1$: $(a^2 + b^2 + c^2 + 1)$.
3.  The third package value is the sum of the cubes of the settings plus an offset of $1$: $(a^3 + b^3 + c^3 + 1)$.
4.  The final package value is the sum of the fourth powers of the settings plus a large constant offset of $7459$: $(a^4 + b^4 + c^4 + 7459)$.

A systems analyst needs to identify all potential security keys that satisfy these conditions. Find the sum of all possible values of $p$ less than $1000$.

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
