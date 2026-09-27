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

In a remote industrial logistics hub, seven specialized transport drones are assigned to carry cargo containers. Each drone $i$ (where $i$ ranges from 1 to 7) carries a specific number of containers denoted by $a_i$. Regulations dictate that all seven counts $\{a_1, a_2, \ldots, a_7\}$ must be distinct positive integers.

The efficiency of the transport operation is measured by the "weighted load" of each drone. For the $i$-th drone, the weighted load is calculated by multiplying its assigned rank by its cargo count. Specifically, the weighted loads for the drones are:
Drone 1: $1 \times a_1$
Drone 2: $2 \times a_2$
Drone 3: $3 \times a_3$
Drone 4: $4 \times a_4$
Drone 5: $5 \times a_5$
Drone 6: $6 \times a_6$
Drone 7: $7 \times a_7$

For the synchronization of the flight path, these seven weighted loads—in the order from Drone 1 to Drone 7—must form a strict arithmetic progression (meaning the difference between consecutive weighted loads is constant).

Calculate the smallest possible positive value for the absolute difference between the cargo counts of the first and last drones, $|a_7 - a_1|$.

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
