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

In a specialized data processing facility, a "Data Node" consists of a set of three integer security keys $(a, b, c)$. The facility utilizes a specific transformation algorithm, $f$, which takes a Data Node and outputs a new Node according to these rules:
1. The first key of the new Node is the sum of the original three keys $(a+b+c)$.
2. The second key of the new Node is the sum of all possible products of two original keys $(ab + bc + ca)$.
3. The third key of the new Node is the product of all three original keys $(abc)$.

The facility's system administrator is interested in "Stable Cycles." A Stable Cycle occurs when a Data Node $(a, b, c)$ returns to its exact original values after the algorithm $f$ is applied twice in succession—that is, $f(f(a, b, c)) = (a, b, c)$.

Let $S$ represent the set of all such Data Nodes that form a Stable Cycle. Within this set, the administrator identifies a specific subset, $S_{100}$, containing only those Nodes where the absolute value of every individual key is less than or equal to 100 (meaning $|a| \le 100$, $|b| \le 100$, and $|c| \le 100$).

How many unique Data Nodes are in the subset $S_{100}$?

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
