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

In the futuristic city of Numeropolis, two automated logistics networks, the **2016-Grid** and the **2015-Grid**, monitor delivery drones. The city is mapped on a coordinate plane where every location is defined by coordinates $(x, y)$. A location is considered a "Potential Hub" if both $x$ and $y$ are rational numbers ($\mathbb{Q}$) and neither coordinate is zero.

A Potential Hub $(x, y)$ is classified as an **Active Node** for a specific network if the product of its coordinates divided by that network's ID number results in an integer. Specifically:
- A point belongs to the **Set $A_{2016}$** if $\frac{xy}{2016} \in \mathbb{Z}$.
- A point belongs to the **Set $A_{2015}$** if $\frac{xy}{2015} \in \mathbb{Z}$.

An inspector travels along various straight-line paths $l$ across the city. For any two checkpoints $M$ and $N$ located on a path $l$, we define:
- $f_{2016}(MN)$ as the total number of Active Nodes from Set $A_{2016}$ located on the straight segment connecting $M$ and $N$.
- $f_{2015}(MN)$ as the total number of Active Nodes from Set $A_{2015}$ located on the straight segment connecting $M$ and $N$.

The city council seeks a universal efficiency constant $\lambda$. This constant must be the smallest real number such that for every possible straight-line path $l$ in the city, there exists a fixed overhead value $\beta(l)$ (unique to that path) where the following inequality always holds for any segments $MN$ chosen on that path:
$$f_{2016}(MN) \le \lambda f_{2015}(MN) + \beta(l)$$

Find the value of this smallest real number $\lambda$.

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
