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

In a futuristic data network, a "Standard Configuration" involves assigning security clearance levels to various processing nodes. These levels are drawn from a set $R_n$, defined based on the value of $n$: if $n$ is even ($n=2k$), $R_n = \{-k, \dots, -1, 1, \dots, k\}$; if $n$ is odd ($n=2k+1$), $R_n = \{-k, \dots, 0, \dots, k\}$. A configuration is "Standard-Valid" if every pair of nodes connected by a fiber-optic cable is assigned distinct levels from $R_n$.

A new encryption protocol requires a "Strict Configuration" using levels from a different set $R_m$ (defined via $m$ using the same logic as $R_n$). In this protocol, nodes can be linked by two types of cables:
1. **Type-W Cables**: Any two nodes connected by a Type-W cable must be assigned different levels.
2. **Type-R Cables**: Any two nodes connected by a Type-R cable must be assigned levels such that their sum is not equal to zero.

The network overseer discovers that any network architecture (set of nodes and cables) that is capable of being "Standard-Valid" using levels from $R_n$ is also guaranteed to be capable of a "Strict Configuration" using levels from $R_m$, regardless of which cables are designated Type-W or Type-R.

Given $n \geq 3$, what is the minimum value of $m$ that ensures this property holds for all possible network architectures?

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
