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

In a futuristic laboratory, a precise robotic arm is programmed to navigate a platform shaped like an equilateral triangle with a side length of exactly 1 meter. The three corners of this platform are designated as primary nodes $A$, $B$, and $C$.

Engineers have marked "trisection points" along the perimeter. On the edge connecting node $A$ to $B$, two sensors are placed: $A_1$ (located $1/3$ meter from $A$) and $A_2$ (located $2/3$ meter from $A$). On the edge from $B$ to $C$, sensors $B_1$ and $B_2$ are placed at the $1/3$ and $2/3$ marks respectively. On the edge from $C$ to $A$, sensors $C_1$ and $C_2$ are placed at the $1/3$ and $2/3$ marks respectively.

A thin, orange triangular plate is fabricated to exactly match the dimensions of the equilateral triangle formed by the three sensor locations $A_1, B_1,$ and $C_1$. This plate is initially placed flat on the platform so that its three vertices are perfectly aligned with $A_1$, $B_1$, and $C_1$.

The robot then performs a calibration maneuver: it rotates the orange plate around the plate's own geometric center. The plate is rotated in the direction of the smallest possible angle until its vertices are perfectly aligned with the three secondary sensor locations $A_2$, $B_2$, and $C_2$.

Calculate the total area of the surface on the platform that was covered or swept over by the orange triangular plate at any point during this rotation.

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
