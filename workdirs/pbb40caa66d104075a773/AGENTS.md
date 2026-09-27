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

In a specialized chemical processing plant, a purification sequence is conducted across an infinite series of filtration stages. Each stage $n$ (where $n=1, 2, 3, \dots$) involves a specific chemical yield calculated based on the following logistical parameters:

For each stage $n$:
1. The **Input Intensity** is defined by the $n$-th odd number starting from 3 (i.e., $2n + 1$).
2. The **Stability Coefficient** is the product of four specific pressure readings taken during that stage:
   - The first reading is $3n - 1$.
   - The second reading is $3n + 1$.
   - The third reading is $3n + 2$.
   - The fourth reading is $3n + 4$.

The net efficiency of the entire plant is determined by an alternating accumulation of these stage yields. Specifically, the yield of the first stage is added, the yield of the second stage is subtracted, the yield of the third is added, and so on.

The total efficiency $E$ is given by the sum of the infinite series:
\[ E = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{2n+1}{(3n-1)(3n+1)(3n+2)(3n+4)} \]

Which, expanded, begins as:
\[ \frac{3}{2 \cdot 4 \cdot 5 \cdot 7} - \frac{5}{5 \cdot 7 \cdot 8 \cdot 10} + \frac{7}{8 \cdot 10 \cdot 11 \cdot 13} - \frac{9}{11 \cdot 13 \cdot 14 \cdot 16} + \cdots \]

Calculate the exact value of the total efficiency $E$.

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
