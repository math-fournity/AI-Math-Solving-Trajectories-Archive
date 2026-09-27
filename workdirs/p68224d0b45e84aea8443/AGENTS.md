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

A logistics company is designing a triangular delivery network between three major hubs: Hub A, Hub B, and Hub C. The straight-line distances between these hubs are 13 units from C to A, 10 units from B to C, and 9 units from A to B.

To optimize local distribution, the company places three primary warehouses—labeled $A_1$, $B_1$, and $C_1$—on the roads $BC$, $CA$, and $AB$ respectively. These warehouses are positioned such that they represent the points of tangency for a single circular bypass road $\omega$ that is inscribed within the triangle formed by the three hubs.

To expand the network, the company identifies three auxiliary sites, $A_2$, $B_2$, and $C_2$. Site $A_2$ is located on road $BC$ such that the distance from $B$ to $A_1$ is exactly equal to the distance from $C$ to $A_2$. Similarly, $B_2$ is located on road $CA$ such that $CB_1 = AB_2$, and $C_2$ is located on road $AB$ such that $AC_1 = BC_2$.

Next, the company plans three high-speed transit lines connecting each hub to its corresponding auxiliary site: line $AA_2$, line $BB_2$, and line $CC_2$. Each of these transit lines intersects the circular bypass road $\omega$ at two points. Let $A_3$ be the intersection point on line $AA_2$ that is closest to Hub A. Likewise, let $B_3$ be the intersection point on line $BB_2$ closest to Hub B, and $C_3$ be the intersection point on line $CC_2$ closest to Hub C.

If the area of the triangular zone formed by the three hubs $A, B,$ and $C$ is denoted as $[ABC]$, and the area of the zone formed by the three intersection points $A_3, B_3,$ and $C_3$ is denoted as $[A_3B_3C_3]$, determine the ratio $[A_3B_3C_3] / [ABC]$. 

If your result is an irreducible fraction $\frac{a}{b}$, calculate the sum $a+b$.

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
