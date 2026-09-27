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

In a remote industrial refinery, a processing unit is governed by a specific chemical reaction law. When two substances with purity levels $a$ and $b$ are combined, they react to form a single substance with a new purity level defined by the operation $[a, b] = ab - a - b$.

An engineer named Silas starts a shift with a set of 100 containers, each holding a substance with a distinct integer purity level. The containers are labeled with every integer from $2$ to $101$ inclusive (specifically $\{2, 3, 4, \dots, 101\}$). Silas is tasked with merging these containers one by one. In each step, he selects any two containers with current purity levels $a$ and $b$, processes them to create a new substance with purity $[a, b]$, and repeats this until only a single container remains.

Let $V$ be the maximum possible purity level Silas can achieve for the final remaining substance through any sequence of combinations.

After calculating $V$, Silas looks for an integer $N$ such that the factorial $N!$ is the closest possible value to $V$ among all factorials. 

Determine the value of the nearest integer to:
$$10^{6} \cdot \frac{|V-N!|}{N!}$$

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
