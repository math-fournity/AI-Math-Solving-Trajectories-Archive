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

A remote expedition has established four survey stations—$A$, $B$, $C$, and $D$—defining a quadrilateral perimeter. A straight supply road connects stations $C$ and $D$, measuring exactly $14$ kilometers in length. A central logistics hub, $M$, is positioned exactly at the midpoint of this road.

Internal survey readings provide the following data:
- The angle formed at station $A$ between the sightlines to $B$ and $D$ ($\angle BAD$) is $105^\circ$.
- From station $C$, the angle between the sightlines to $A$ and $D$ ($\angle ACD$) is $35^\circ$.
- From station $C$, the angle between the sightlines to $A$ and $B$ ($\angle ACB$) is $40^\circ$.

Two scouts, $P$ and $Q$, are deployed into the field. Scout $P$ travels along a straight path starting at $A$ and passing through the hub $M$. Scout $Q$ travels along a straight path starting at $B$ and passing through the hub $M$. They stop at positions such that the viewing angle between stations $A$ and $B$ from their respective locations is identical: $\angle APB = 40^\circ$ and $\angle AQB = 40^\circ$.

A technician notices that the straight line of sight from Scout $P$ to station $B$ crosses the $CD$ supply road at a checkpoint labeled $R$. Similarly, the line of sight from Scout $Q$ to station $A$ crosses the $CD$ supply road at a checkpoint labeled $S$. 

If the distance along the road from station $C$ to checkpoint $R$ is $2$ kilometers, what is the distance along the road from checkpoint $S$ to the central hub $M$?

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
