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

A specialized chemical refinery processes a rare isotope through a multi-stage enrichment sequence. The isotope’s purity at each stage $i$ is denoted by a real value $a_i$. To maintain the reaction, the purity levels must be strictly increasing, starting with an initial purity of $1$ unit ($1 = a_1 < a_2 < a_3 < \cdots < a_n < \cdots$).

At each transition between two consecutive stages, $i$ and $i+1$, the refinery generates a "stability coefficient" calculated by the formula:
\[ \sqrt[3]{\frac{a_{i+1} - a_i}{(2 + a_i)^4}} \]

An environmental regulation requires that for any possible sequence of purity levels and for any number of stages $n \geq 2$, the total sum of these stability coefficients from the first stage to the $(n-1)$-th stage must never exceed a fixed safety limit $m$.

To comply with the regulation, engineers must determine the smallest possible value of $m$ that satisfies this condition for all valid configurations of the refinery. This minimum value is known to be in the form $1 / \sqrt[3]{k}$ for some integer $k$.

What is the value of $k$?

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
