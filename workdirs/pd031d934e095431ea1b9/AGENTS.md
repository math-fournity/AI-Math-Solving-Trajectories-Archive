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

A specialized architectural firm is designing a vertical research station defined by four corner nodes: $B$ (the base origin), $A$ (directly north of $B$), $C$ (directly east of $B$), and $D$ (the zenith point). The structural supports $BA, BC$, and $BD$ are all mutually perpendicular, forming the edges of a trirectangular tetrahedron. The horizontal floor beams $BA$ and $BC$ are of equal length.

To stabilize the structure, three planar glass panels—$AEFB, BFGC$, and $CGEA$—are installed. The points $E, F,$ and $G$ are located on the primary structural struts $AD, BD,$ and $CD$, respectively. For structural integrity and aesthetic symmetry, the dimensions of these panels are constrained such that each of the three quadrilaterals—$AEFB, BFGC$, and $CGEA$—must possess an inscribed circle (incircle).

An interior platform is formed by the triangle $EFG$. Engineers are interested in the ratio of the area of this interior platform to the area of the base floor triangle $ABC$. Let $r$ be the minimum possible real number such that the ratio $\text{Area}(EFG) / \text{Area}(ABC) \leq r$ holds true for every possible valid configuration of the points $D, E, F,$ and $G$.

If $r$ can be expressed in the form $\frac{\sqrt{a-b\sqrt{c}}}{d}$, where $a, b, c, d$ are positive integers, $\gcd(a, b)$ is squarefree, and $c$ is squarefree, calculate the value of the sum $a + b + c + d$.

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
