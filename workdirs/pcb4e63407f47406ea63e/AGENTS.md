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

In a futuristic cargo management system, a logistics engineer is organizing a set of shipments for a cargo ship. The ship can accommodate items labeled with any integer weight from $1$ up to $n$ tons, where $n \geqslant 4$.

From the master list of available weights $\{1, 2, \cdots, n\}$, the engineer selects a specific subset of items to load, denoted as $A$. To maintain the ship's stability, the engineer must be able to distribute every selected item from $A$ into one of two identical holding bays (Bay Left or Bay Right). 

If an item $a \in A$ is placed in Bay Left, it contributes $+a$ to the ship's balance; if it is placed in Bay Right, it contributes $-a$. The ship is considered "perfectly stabilized" if the absolute value of the total sum of these weighted contributions is no greater than $1$ ton.

The engineer discovers that if the number of items selected, $|A|$, exceeds a certain fraction $c$ of the total range $n$, it is always possible to find a distribution (a function $f: A \rightarrow \{1, -1\}$) that achieves this stability, regardless of which specific items were chosen for $A$.

Find the smallest positive number $c$ such that for any $n \geqslant 4$, if $|A| > cn$, a stabilizing distribution is guaranteed to exist.

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
