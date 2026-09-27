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

In a remote desert, an architect is designing a monument complex based on a massive stone structure. The central structure is a rigid, regular quadrilateral pyramid, $SABCD$. The square base $ABCD$ has a side length of $AB=4$ units, and the pyramid’s apex $S$ sits at a height of $SO=3$ units directly above the base center $O$.

Two specific structural cables are tensioned across the site. The first cable, representing line $SD$, connects the apex to a base corner. A sensor $E$ is installed at the exact midpoint of this cable. The second cable, representing line $AD$, runs along one edge of the base. A connection point $F$ is located on this edge such that the distance from corner $A$ to $F$ is exactly $\frac{3}{2}$ times the distance from $F$ to corner $D$.

The architect intends to place a cooling tower in the shape of a right circular cone. The center of the cone's circular base, $Q$, must be located somewhere along the vertical axis $SO$ of the pyramid. To ensure stability, the cone’s dimensions are determined by its axial section—a triangle $KLM$. Two vertices of this triangular section, $K$ and $M$, must lie on the infinite line extending through the pyramid's base edge $CD$. The third vertex of the triangle, $L$, must be positioned exactly on the infinite line passing through points $E$ and $F$.

Calculate the total volume of this cone.

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
