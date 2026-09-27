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

In a specialized logistics hub, there are $n+1$ numbered loading docks arranged in a row, indexed from $0$ to $n$. Each dock contains exactly one cargo container. A configuration of these containers is valid if the set of labels on the containers is a permutation of $\{0, 1, 2, \dots, n\}$.

A "shift operation" can be performed on the current configuration if there exist two docks, $i$ and $j$, such that Dock $i$ contains the "Empty Marker" (labeled $0$) and Dock $j$ contains a container whose label is exactly one greater than the label of the container currently sitting in Dock $i-1$. If these conditions are met, the Empty Marker in Dock $i$ and the container in Dock $j$ swap positions.

A logistics manager is testing different hub sizes, where the number of non-zero containers $n$ is an integer such that $1 \le n \le 100$. For each $n$, the hub begins in an "Inverted State," where the containers are arranged in the order $(1, n, n-1, n-2, \dots, 2, 0)$. The manager wants to determine if this hub can reach the "Standard State," where the containers are arranged in the order $(1, 2, 3, \dots, n, 0)$, using only the shift operation described above.

Let $S$ be the set of all values of $n$ in the range $\{1, 2, \dots, 100\}$ for which the Standard State is reachable from the Inverted State. Find the sum of all elements in $S$.

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
