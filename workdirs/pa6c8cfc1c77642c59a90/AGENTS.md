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

A network of ancient water filtration stations is built along a river, with each station assigned a unique positive integer ID. A set of stations $S$ is considered "harmonious" if it satisfies a specific hydraulic balance rule: for any two stations in the set with IDs $i$ and $j$ (where $i$ and $j$ can be the same), the system requires the existence of a station whose ID is exactly equal to the sum of their IDs divided by their greatest common divisor. That is, $\frac{i+j}{\gcd(i, j)}$ must also be an ID of a station within the set $S$.

Let $\mathcal{F}$ be the collection of all possible harmonious sets of stations. 

For each harmonious set $S \in \mathcal{F}$, we define two values:
1. $m(S)$: The smallest station ID present in the set $S$.
2. $\Sigma_{10}(S)$: The sum of all station IDs in $S$ that are less than or equal to 10.

Calculate the sum of the products $\left( m(S) \times \Sigma_{10}(S) \right)$ across all distinct harmonious sets $S$ found in $\mathcal{F}$.

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
