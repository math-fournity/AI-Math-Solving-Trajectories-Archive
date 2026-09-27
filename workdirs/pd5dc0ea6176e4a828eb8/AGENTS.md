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

In a specialized digital grid representing a 4D security matrix, there are $3^4$ unique nodes. Each node is identified by a unique address vector $(x, y, z, w)$, where each coordinate is an integer chosen from $\{-1, 0, 1\}$.

A security drone is programmed to perform a cyclic patrol route consisting of a sequence of 2020 movement steps between nodes, denoted as $P_1, P_2, P_3, \dots, P_{2020}$. The protocol for this patrol is governed by three strict operational constraints:
1. The drone must start its patrol at the central origin node, $P_1 = (0, 0, 0, 0)$.
2. To conserve energy, every transition between consecutive nodes must satisfy a "Distance-2 Rule." Specifically, the squared Euclidean distance between $P_i$ and $P_{i+1}$ must be exactly 2 for all $i = 1, 2, \dots, 2019$.
3. The patrol must be a closed loop, meaning the step from the final node $P_{2020}$ back to the starting node $P_1$ (effectively $P_{2021} = P_1$) must also satisfy the "Distance-2 Rule."

Let $N$ be the total number of distinct valid patrol sequences $P_1, P_2, \dots, P_{2020}$ that the drone can follow. Find the largest integer $n$ such that $2^n$ divides $N$.

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
