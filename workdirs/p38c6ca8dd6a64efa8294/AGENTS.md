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

A specialized textile factory is designing an 8-by-8 mosaic quilt composed of 64 square fabric patches. The layout is defined by the 144 individual threads that form the boundaries of these squares. The lead designer has 6 distinct colors of silk thread available: red, orange, yellow, green, blue, and purple.

The design constraint for the quilt is strict: for every single one of the 64 square patches, the four threads forming its immediate perimeter must utilize exactly 3 different colors. This means that on every square, one color must be used twice on two of its edges, while two other distinct colors are used once each on the remaining two edges.

Let $N$ be the total number of ways the 144 boundary threads can be colored according to this rule. When $N$ is expressed in its prime factorization form $p_{1}^{e_{1}} p_{2}^{e_{2}} \ldots p_{k}^{e_{k}}$ (where $p_{1} < p_{2} < \cdots < p_{k}$ are prime numbers and $e_{i}$ are positive integers), calculate the sum of the exponents: $e_{1} + e_{2} + \cdots + e_{k}$.

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
