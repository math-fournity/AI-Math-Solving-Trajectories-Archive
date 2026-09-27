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

In a specialized quantum computing facility, engineers are calibrating a four-node synchronization chip. The state of the system is defined by four complex-valued frequency parameters: $w, x, y,$ and $z$. These parameters must satisfy four fundamental energy constraints to ensure the processor's stability.

First, the global resonance condition requires that the product of all four parameters equals exactly $1$:
$$wxyz = 1$$

Second, the first-order interference energy, calculated by the sum of four specific triple-product interactions—where one variable in each term is squared—must total $2$:
$$wxy^2 + wx^2z + w^2yz + xyz^2 = 2$$

Third, the second-order harmonic stress is determined by a complex combination of six interactions. This total must equal $-3$:
$$wx^2y + w^2y^2 + w^2xz + xy^2z + x^2z^2 + ywz^2 = -3$$

Finally, the cross-coupling flux, defined by the sum of four different triple-product interactions (each distinct from the first-order interference terms), must equal $-1$:
$$w^2xy + x^2yz + wy^2z + wxz^2 = -1$$

Given these physical constraints, how many distinct ordered quadruples $(w, x, y, z)$ exist that satisfy this system of equations?

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
