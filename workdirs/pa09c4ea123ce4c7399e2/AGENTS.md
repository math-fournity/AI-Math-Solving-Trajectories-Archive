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

A galactic federation consists of $n$ member planets, where $n \ge 5$ is an odd number. To manage interplanetary trade, the federation organizes a series of diplomatic summits. Each summit must be attended by a delegation of exactly $2r+1$ planets, where $r$ is a fixed integer such that $1 \le r \le (n-1)/2$.

In accordance with federation law, every possible unique combination of $2r+1$ planets must convene for exactly one summit. During each summit, the participating planets are assigned "Influence Credits" based on their diplomatic performance. The credits awarded at a single summit are the integers $\{-r, -(r-1), \dots, -1, 0, 1, \dots, r-1, r\}$, with each of the $2r+1$ planets receiving exactly one of these values.

At the end of the entire cycle of summits, each planet $i$ (for $i=1, 2, \dots, n$) calculates its total prestige $S_i$ by summing all the Influence Credits it received across all summits it attended. The federation is interested in the "Diplomatic Gap" $N$, defined as the smallest non-negative difference between the total prestige scores of any two distinct planets:
\[N = \min_{i<j} |S_i - S_j|\]

Determine the maximum possible value that $N$ can take.

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
