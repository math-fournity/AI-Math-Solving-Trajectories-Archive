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

In a remote industrial sector, two logistics supervisors, Alex and Blake, oversee a fluctuating inventory of specialized fuel cells. The process begins with an initial quantity of fuel cells, denoted as $n_0$, which is a natural number greater than 1. The two supervisors take turns adjusting the inventory levels according to strict regulatory protocols.

On any given turn $k$ (starting from $k=0$):
1. **Alex’s Turn:** Given the current quantity $n_{2k}$, Alex must choose a new quantity $n_{2k+1}$ such that $n_{2k} \leq n_{2k+1} \leq n_{2k}^2$.
2. **Blake’s Turn:** Given the quantity $n_{2k+1}$ set by Alex, Blake must reduce it to a new quantity $n_{2k+2}$ such that the ratio $\frac{n_{2k+1}}{n_{2k+2}}$ is equal to $p^r$, where $p$ is any prime number and $r$ is any natural number.

The objective of the logistics operation is defined by specific targets:
- **Alex wins** if they can force the inventory level to reach exactly 1990.
- **Blake wins** if they can force the inventory level to reach exactly 1.
- **A Tie** occurs if the adjustments continue indefinitely without either supervisor reaching their target.

Let $W$ be the set of initial quantities $n_0$ for which Alex has a guaranteed winning strategy.
Let $L$ be the set of initial quantities $n_0$ for which Blake has a guaranteed winning strategy.
Let $T$ be the set of initial quantities $n_0$ for which both supervisors can force the game into a tie.

Consider only the starting quantities in the range $\{2, 3, 4, 5, 6, 7, 8, 9, 10\}$. We define the following subsets:
- $S_W = W \cap \{2, 3, \dots, 10\}$
- $S_L = L \cap \{2, 3, \dots, 10\}$
- $S_T = T \cap \{2, 3, \dots, 10\}$

Calculate the total weighted value of these starting quantities defined by the formula:
$$\left(\sum_{n \in S_W} n\right) + 2\left(\sum_{n \in S_L} n\right) + 3\left(\sum_{n \in S_T} n\right)$$

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
