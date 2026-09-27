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

In a specialized logistics center, a giant modular storage unit is built in the shape of a rectangular room with dimensions $15$ meters (length along the $x$-axis), $12$ meters (width along the $y$-axis), and $9$ meters (height along the $z$-axis). Let the floor corners be $A(0,0,0)$, $B(15,0,0)$, $C(15,12,0)$, and $D(0,12,0)$, with the corresponding ceiling corners directly above them labeled $A', B', C',$ and $D'$.

Two laser security grids are being installed:
1.  **Grid Alpha:** A laser source is placed at corner $A$. It casts two perpendicular beams onto the diagonal support struts of the side walls: one beam hits point $E$ on the strut $A'D$ such that $AE \perp A'D$, and another hits point $F$ on the strut $A'B$ such that $AF \perp A'B$. A tracking point $G$ is defined as the intersection of the floor-to-wall cables $DF$ and $BE$.
2.  **Grid Omega:** A second laser source at corner $C$ casts beams onto its adjacent walls: one beam hits point $M$ on the strut $C'D$ such that $CM \perp C'D$, and another hits point $N$ on the strut $C'B$ such that $CN \perp C'B$. A tracking point $P$ is defined as the intersection of the floor-to-wall cables $DN$ and $BM$.

The security system monitors two specific vertical planes: 
- The first plane passes through the vertical edge $A'A$ and the tracking point $G$.
- The second plane passes through the vertical edge $C'C$ and the tracking point $P$.

Given that these two planes are parallel, what is the exact distance between them?

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
