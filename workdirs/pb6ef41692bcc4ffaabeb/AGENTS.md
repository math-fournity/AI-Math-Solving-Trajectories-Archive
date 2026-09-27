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

A specialized chemical refinery manages a mixture of three volatile compounds, whose concentrations are represented by $a, b,$ and $c$ (where $a, b, c \geq 0$). The safety protocols of the facility dictate a strict "Stability Constraint" based on the interactions between these compounds: 
The sum of the pairwise interactions multiplied by 5 must not exceed 4 times the sum of the individual concentrations plus a constant of 3. Mathematically, this is expressed as:
$$5(ab+ac+bc)\leq 4(a+b+c)+3$$

The plant’s efficiency engineer is investigating a "Reaction Power Index," defined by the value $25(abc)^k$, where $k$ is a variable scaling exponent. To ensure the refinery does not reach a critical state, the Reaction Power Index must always stay below a specific "Threshold Limit" defined by the linear and pairwise properties of the mixture:
$$25\left(abc\right)^k\leq1+3(a+b+c)+5(ab+bc+ca)$$

The engineer needs to determine the maximum possible value $K$ such that for any positive scaling exponent $k$ where $k \leq K$, the Reaction Power Index never exceeds the Threshold Limit for any combination of concentrations that satisfy the Stability Constraint.

Calculate the value of $100K$.

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
