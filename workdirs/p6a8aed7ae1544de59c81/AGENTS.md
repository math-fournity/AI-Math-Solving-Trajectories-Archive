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

On a high-tech circuit board, there are 8 toggle switches arranged in a straight line, labeled 1 through 8. Each switch $a_k$ can be in one of two states: $+1$ (representing "High Voltage") or $-1$ (representing "Low Voltage"). Initially, the switches are set in an alternating pattern: the even-numbered switches are $+1$ and the odd-numbered switches are $-1$, such that $a_k = (-1)^k$ for all $k \in \{1, 2, \ldots, 8\}$.

The board is controlled by a single operational rule: an engineer can select any switch $k$. When switch $k$ is selected, the board performs a "neighbor-sync" operation. This means the immediate left neighbor $a_{k-1}$ (if it exists) is updated to the product of its current state and switch $k$'s state ($a_{k-1} \cdot a_k$), and the immediate right neighbor $a_{k+1}$ (if it exists) is updated to the product of its current state and switch $k$'s state ($a_k \cdot a_{k+1}$). The state of the selected switch $k$ itself remains unchanged during the operation.

A configuration of the 8 switches is "stable-reachable" if it can be produced from the initial alternating state through any finite sequence of these neighbor-sync operations.

Calculate the total number of unique stable-reachable switch configurations.

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
