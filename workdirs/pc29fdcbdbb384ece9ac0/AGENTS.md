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

A specialized digital archive contains a sequence of $2023$ server racks, indexed from $n = 1$ to $n = 2023$. For each rack $n$, a technician must select a group of data packets $T_n$ from a set of available IDs $\{1, 2, 3, \dots, n\}$. To prevent signal interference within the rack, the technician must follow a strict protocol: the absolute difference between the IDs of any two selected packets in $T_n$ cannot be exactly $4$ and cannot be exactly $7$.

Let $f_n$ represent the maximum possible number of data packets that can be stored in rack $n$ while adhering to this interference protocol. For instance, in a rack with only two available IDs ($n=2$), the technician can store both packets because their difference is not $4$ or $7$, so $f_1 = 1$ and $f_2 = 2$.

Calculate the total number of packets stored across all racks if every rack is filled to its maximum capacity, defined as:
$$\sum_{n=1}^{2023} f_{n}$$

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
