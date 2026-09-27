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

In a specialized thermodynamics laboratory, three distinct chemical agents—Agent X, Agent Y, and Agent Z—are being tested for their heat-generation properties when mixed in pairs. The energy output of these reactions follows a specific quadratic efficiency model based on the concentrations of the agents involved.

During the experiments, the following observations were recorded regarding the total energy released (measured in kilojoules) for different pairings:

1.  When Agent X and Agent Y are combined, the total energy released follows the relationship $x^2 + xy + y^2 = 37$.
2.  When Agent X and Agent Z are combined, the total energy released follows the relationship $x^2 + xz + z^2 = 28$.
3.  When Agent Y and Agent Z are combined, the total energy released follows the relationship $y^2 + yz + z^2 = 19$.

In these equations, $x$, $y$, and $z$ represent the real-valued concentration levels of Agents X, Y, and Z, respectively.

A scientist is interested in the "Productivity Index," defined as the product of the three concentrations, $xyz$. Let $S$ be the set containing all possible values of this Productivity Index $xyz$ that satisfy the experimental data. 

Calculate the sum of the squares of all elements in $S$.

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
