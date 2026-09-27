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

In a remote territory, a telecommunications company has established three signal towers named **Mountain (M)**, **Nexus (N)**, and **Peak (P)**. The straight-line cables connecting them form a triangle with distances $MN = 13$ km, $NP = 89$ km, and $PM = 100$ km. 

To monitor the network, three maintenance hubs have been built at the exact midpoints of these cables: Hub **S** is at the center of the $MN$ line, Hub **R** is at the center of the $NP$ line, and Hub **B** is at the center of the $PM$ line.

A straight regional power line, denoted as line $\ell$, is constructed across the territory. This power line intersects the straight path (or its extension) between $M$ and $N$ at a service point $I$. It intersects the path (or its extension) between $N$ and $P$ at a service point $J$, and it intersects the path (or its extension) between $P$ and $M$ at a service point $A$.

A technician needs to calculate the distances between the maintenance hubs and these new service points along the respective tower-to-tower lines. Specifically, the technician measures the distance from hub $S$ to point $I$ ($SI$), from hub $R$ to point $J$ ($RJ$), and from hub $B$ to point $A$ ($BA$).

Find the minimum possible value of the expression $(SI + RJ + BA)^2$.

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
