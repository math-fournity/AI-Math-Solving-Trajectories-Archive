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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are positioned such that they form an acute-angled triangle. A central communication hub, $P$, is located within the triangular perimeter formed by these depots.

To extend the network's reach, three relay towers were constructed. Tower $P_A$ was built by mirroring the position of hub $P$ across the straight boundary line $BC$. Tower $P_B$ was built by mirroring $P$ across the boundary $CA$, and Tower $P_C$ was built by mirroring $P$ across the boundary $AB$.

Engineers monitoring the signal grid discovered a unique geometric synchronization: the position of the hub $P$ functions exactly as the orthocenter of the triangle formed by the three relay towers ($P_A P_B P_C$). 

The logistics team is now analyzing the lengths of the direct fiber-optic cables connecting the hub to the depots: cable $PA$, cable $PB$, and cable $PC$. They found that these three specific lengths are capable of being rearranged to form a new triangle. 

Determine the value of $x$, where $x^\circ$ is the measure of the largest interior angle of the triangle formed by the segments $PA, PB,$ and $PC$.

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
