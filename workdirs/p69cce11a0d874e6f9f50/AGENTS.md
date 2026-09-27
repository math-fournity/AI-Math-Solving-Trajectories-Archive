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

A specialized logistics network consists of $n+1$ distinct distribution hubs, denoted as $x_0, x_1, \dots, x_n$. The cost of transferring a priority package between any two hubs $x_i$ and $x_j$ is given by a distance metric $d(x_i, x_j)$.

The network was established sequentially according to a "maximal reach" protocol: 
1. The first hub $x_0$ was placed at an arbitrary location.
2. For each subsequent step $k$ (where $k = 1, 2, \dots, n$), the hub $x_k$ was selected from the set of remaining available locations such that the product of its delivery costs to all previously established hubs, $\prod_{j=0}^{k-1} d(x_k, x_j)$, was maximized.

For any specific hub $x$ in the completed network, we define its "Total Connectivity Index," $\Pi_x$, as the product of the delivery costs from $x$ to every other hub in the network: $\Pi_x = \prod_{y \in X \setminus \{x\}} d(x, y)$.

Find the smallest constant $C(n)$, depending only on the total number of hubs minus one, such that the Connectivity Index of the final hub added, $\Pi_{x_n}$, is guaranteed to be no greater than $C(n)$ times the Connectivity Index of any other hub $x$ in the network (i.e., $\Pi_{x_n} \leq C(n) \Pi_x$).

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
