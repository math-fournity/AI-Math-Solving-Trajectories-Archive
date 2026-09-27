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

In a remote industrial complex, three chemical reactors—Alpha, Beta, and Gamma—operate using specific volumes of a rare catalyst, represented by $a$, $b$, and $c$ liters respectively. Due to supply constraints, the total volume of catalyst available is strictly limited such that $a + b + c = 3$, where each reactor must contain a positive amount of the substance.

The efficiency of the facility is determined by a complex stability index. The primary maintenance cost is calculated by the sum of the reciprocals of the volumes used: $\frac{1}{a} + \frac{1}{b} + \frac{1}{c}$. Additionally, the facility utilizes a stabilizer unit whose performance depends on a specific "interactivity sum" of the reactors, defined as $a^2 + b^2 + c^2 + ab + bc + ca$. The stabilizer contributes a bonus to the system equal to $6k$ divided by this interactivity sum, where $k$ is a non-negative safety constant.

The plant's engineers have mandated that for any distribution of the 3 liters of catalyst, the total system efficiency—the sum of the maintenance cost and the stabilizer bonus—must never fall below a baseline threshold of $3 + k$.

What is the maximum possible value of the safety constant $k$ that ensures the inequality 
$$\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{6k}{a^2 + b^2 + c^2 + ab + bc + ca} \geq 3 + k$$ 
remains true for all valid catalyst distributions?

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
