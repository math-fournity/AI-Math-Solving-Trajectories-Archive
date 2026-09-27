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

In a specialized logistics simulation, three supply depots—$C$, $A$, and $B$—are positioned in a coastal region such that traveling from $C$ to $A$ covers exactly $2022$ miles, from $A$ to $B$ covers $2023$ miles, and from $B$ to $C$ covers $2024$ miles. Looking at a map where the depots appear in counter-clockwise order, a drone technician defines a secondary coordinate system based on these locations.

The technician creates a virtual "backup station" $B'$ by rotating the position of depot $B$ exactly $90^\circ$ counter-clockwise around depot $A$. To establish a communication relay, a straight-line cable is projected from $B'$ to the line passing through depots $A$ and $C$, meeting it at a perpendicular junction point $D$. 

A monitoring hub $M$ is established at the exact midpoint of the straight-line path between depot $B$ and the backup station $B'$. A circular surveillance zone is then mapped out such that its perimeter passes through junction $D$, depot $C$, and the monitoring hub $M$. 

A signal beam is fired from depot $B$ directly through the monitoring hub $M$. This beam travels in a straight line and eventually exits the circular surveillance zone at a secondary exit point $N$ (where $N$ is distinct from $M$). Calculate the precise distance between the monitoring hub $M$ and the exit point $N$.

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
