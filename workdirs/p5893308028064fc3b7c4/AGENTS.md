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

A specialized automated logistics system manages 1,988 delivery hubs, indexed sequentially from $n = 1$ to $1988$. Each hub $n$ is assigned a specific efficiency rating $f(n)$ based on its index. The system determines these ratings according to a recursive protocol:

- The first and third hubs are calibrated as the baseline: $f(1) = 1$ and $f(3) = 3$.
- For any even-indexed hub, the rating is identical to the hub at half its index: $f(2n) = f(n)$.
- For hubs with indices of the form $4n+1$, the rating is calculated by doubling the rating of hub $2n+1$ and subtracting the rating of hub $n$: $f(4n+1) = 2f(2n+1) - f(n)$.
- For hubs with indices of the form $4n+3$, the rating is calculated by tripling the rating of hub $2n+1$ and subtracting twice the rating of hub $n$: $f(4n+3) = 3f(2n+1) - 2f(n)$.

A "perfectly balanced" hub is defined as any hub where the assigned efficiency rating is exactly equal to its index, such that $f(n) = n$. 

Determine the total number of perfectly balanced hubs among the first 1,988 hubs.

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
