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

In a remote industrial research facility, a specialized storage unit is built in the shape of a perfect rectangular parallelepiped, defined by the corners $ABCD$ on the floor and $A'B'C'D'$ on the ceiling (where $A'$ is directly above $A$, $B'$ above $B$, and so on). 

Engineers are installing three interior structural glass partitions to reinforce the unit:
1. The first installation consists of two intersecting triangular panes. The first pane is stretched between points $A'$, $B$, and $D$, while the second pane is stretched between $C'$, $B$, and $D$. Sensors confirm that the dihedral angle where these two glass surfaces meet along the diagonal $BD$ is exactly $90^\circ$.
2. The second installation uses two different triangular panes. One is stretched between points $A$, $B'$, and $C$, and the other is stretched between $D'$, $B'$, and $C$. Measurement tools show that the dihedral angle formed by these two planes meeting along the diagonal $B'C$ is exactly $60^\circ$.

A final pair of reinforced panels is slated for installation: one connecting points $B$, $C'$, and $D$, and the other connecting $A'$, $C'$, and $D$. Before the installation is finalized, the lead architect must calculate the exact measure of the dihedral angle that will be formed between these two planes where they meet along the diagonal $C'D$.

Determine the measure of this final dihedral angle in degrees.

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
