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

In a remote archipelago, four circular offshore wind farms are positioned such that their boundaries touch at specific maintenance hubs. Let the centers of these circular layouts be $O_1, O_2, O_3,$ and $O_4$. For each index $i$, the farms $O_i$ and $O_{i+1}$ meet at a single point $K_i$ on their perimeters (where indices wrap around such that $O_5=O_1$ and $K_4$ is the contact point between $O_4$ and $O_1$).

A logistics coordinator is mapping straight-line supply routes between these hubs. Route alpha connects hub $K_1$ to $K_3$, while route beta connects hub $K_2$ to $K_4$. The two routes intersect at a central navigation buoy labeled $A$.

Aerial surveys have provided the following geometric data regarding the circular layouts:
1. The angular span of the perimeter arc between hubs $K_4$ and $K_1$ relative to the center $O_1$ is $140^{\circ}$.
2. The angular span of the perimeter arc between hubs $K_4$ and $K_3$ relative to the center $O_4$ is $100^{\circ}$.
3. The straight-line distance between hub $K_1$ and $K_2$ is exactly equal to the distance between $K_2$ and $K_3$.
4. The straight-line distance between hub $K_4$ and $K_1$ is exactly four times the distance between $K_3$ and $K_4$.

Calculate the value of the ratio between four times the distance from buoy $A$ to hub $K_2$ and the distance from buoy $A$ to hub $K_4$ (specifically, find $\frac{4 AK_2}{AK_4}$).

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
