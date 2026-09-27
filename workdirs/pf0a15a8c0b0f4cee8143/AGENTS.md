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

A specialized digital archives department is organizing a massive database of "Hyper-Records." The size of the database is determined by a variable $n$. The total number of records to be indexed is given by the square of the archive size, $n^2$.

A security protocol generates a unique "parity key" for every possible sub-selection of records. Specifically, for every integer $k$ from $0$ to $n^2$, the system calculates the number of ways to choose a subset of $k$ records from the $n^2$ total records. This is represented by the combinatorial value $\binom{n^2}{k}$. 

A record $k$ is flagged as "Stable" if its corresponding parity key is **not** divisible by the prime number $43$. Let $f(n)$ be the total count of these "Stable" records for a given archive size $n$.

The lead engineer initializes the system with a specific, large-scale archive size defined by the formula:
\[ \text{Size} = \frac{43^{n}-1}{42} \]

The system's efficiency reaches a critical threshold when the total count of Stable records, $f(\text{Size})$, is perfectly divisible by the massive constant $43^{43}$. 

Find the least positive integer $n$ that satisfies this efficiency threshold.

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
