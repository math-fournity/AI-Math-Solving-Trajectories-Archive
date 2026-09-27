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

Find all positive integers \(\mathbf{n}\) such that for any: \({a}_{n} \geq {a}_{n - 1} \geq {a}_{n - 2} \geq \cdots \cdots {a}_{2} \geq {a}_{1} > 0,\) satisfying \(\mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k} = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{{a}_{k}}\), the inequality \(\mathop{\prod }\limits_{{k = 1}}^{n}{a}_{k}^{k} \geq 1\) holds.
After solving the above problem, please output a set (completely enumerating all elements) as your final answer in the following format:
### The final answer is: $\boxed{\{<your answer>\}}$
Example:
### The final answer is: $\boxed{\{101, 102, 103, 104, 105, 106, 107, 108, 109, 110\}}$
Note: Please use enumeration to give your final answer. Do not use descriptive methods (e.g., $\boxed{\{x | 101 \leq x \leq 110\}}$).
The final answer should be given as precisely as possible (using LaTeX symbols such as \sqrt, \frac, \pi, etc.). If the final answer involves a decimal approximation, it must be accurate to at least four decimal places.

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
