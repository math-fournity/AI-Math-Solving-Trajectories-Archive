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

In a specialized robotics testing facility, a central control hub is connected to several power transmission cables. For a testing configuration to be "balanced," a set of $n$ distinct, non-zero force vectors must be applied to the hub by $n$ different cables, where $n \geq 3$. Each cable is calibrated to pull with exactly the same magnitude of force, and the configuration is only stable if the resultant sum of all $n$ force vectors is exactly zero.

An additional safety constraint for these experiments is that no two cables can be positioned in a "direct conflict" arrangement; that is, for any two distinct force vectors $\vec{v}$ and $\vec{w}$ in the set, their sum cannot be the zero vector (meaning no two cables pull in exactly opposite directions).

Let $S$ be the set of all possible integers $n$ for which such a balanced, conflict-free configuration of $n$ cables can be constructed in the two-dimensional plane.

Calculate the sum of all elements $n$ in the set $S$ that satisfy the condition $3 \leq n \leq 20$.

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
