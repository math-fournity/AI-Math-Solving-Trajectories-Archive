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

A specialized logistics hub manages a fleet of transport vehicles identified by a positive integer ID number $n$, ranging from $1$ to $70$ inclusive. Each vehicle's cargo capacity is determined by its unique engine configuration, which follows the standard prime factorization $n = p_1^{e_1}p_2^{e_2}\ldots p_k^{e_k}$, where $p_i$ represents the distinct prime components and $e_i$ represents their respective power frequencies.

The logistics center calculates two specific operational metrics for each vehicle:
1. The **Resource Factor** $Q(n)$, which is the product of each prime component raised to the power of itself: $Q(n) = \prod_{i=1}^{k} p_{i}^{p_{i}}$.
2. The **Reliability Index** $R(n)$, which is the product of each power frequency raised to the power of itself: $R(n) = \prod_{i=1}^{k} e_{i}^{e_{i}}$.

A vehicle is classified as "Optimized" if its Resource Factor $Q(n)$ is exactly divisible by its Reliability Index $R(n)$. 

For how many vehicle IDs in the range $1 \leq n \leq 70$ is the vehicle classified as "Optimized"?

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
