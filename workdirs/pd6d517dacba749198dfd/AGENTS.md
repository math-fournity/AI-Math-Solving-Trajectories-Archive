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

In a futuristic automated logistics hub, a central computer manages a sequence of transport pods labeled $\{1, 2, 3, \dots, n\}$, where $n$ is any total number of pods at least equal to $4$. A specific cargo manifest $A$ is selected, which is a subset of these available pods.

The hub's efficiency protocol requires that for any manifest $A$ exceeding a certain density threshold (where the number of pods in the manifest $|A|$ is strictly greater than $cn$ for some constant $c$), it must be possible to assign a binary polarity—either "Positive" ($+1$) or "Negative" ($-1$)—to every pod in that manifest. 

The goal of this assignment is to achieve near-perfect balance in the magnetic distribution. Specifically, if $a$ represents the label of a pod in the manifest and $f(a) \in \{1, -1\}$ represents its assigned polarity, the magnitude of the weighted sum of all pods in the manifest must not exceed $1$:
$$\left| \sum_{a \in A} a \cdot f(a) \right| \le 1$$

What is the minimum value of the threshold constant $c$ that guarantees such a balanced polarity assignment exists for any valid $n$ and any qualifying manifest $A$?

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
