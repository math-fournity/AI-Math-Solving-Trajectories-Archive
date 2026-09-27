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

A specialized logistics hub is designed as a geometric campus. The main administrative offices are located at points $A$, $B$, and $C$, forming an acute triangular layout. The distance from the North Office ($A$) to the Central Hub ($B$) is exactly 11 kilometers, while the distance from the East Office ($C$) to the Central Hub ($B$) is 10 kilometers.

To expand the facility, two satellite stations, $E$ and $D$, are constructed. Station $E$ is positioned such that the path $BE$ is perpendicular to the path $BC$. Similarly, Station $D$ is positioned such that the path $BD$ is perpendicular to the path $BA$. These stations are placed so that the perimeter $A-C-E-B-D-A$ forms a non-degenerate pentagon.

Two straight utility pipelines are laid out: one connecting $E$ to $A$ and another connecting $D$ to $C$. The site surveyors note that the angle of elevation from station $E$ looking toward the North Office ($\angle AEB$) is identical to the angle from the East Office looking toward station $D$ ($\angle DCB$). Furthermore, the lengths of these two pipelines are equal ($AE = CD$). 

The direct distance between the two satellite stations $E$ and $D$ is exactly 20 kilometers. The two pipelines $EA$ and $CD$ cross each other at a junction point $P$. The length of the segment of the pipeline from the North Office to the junction ($AP$) is 4 kilometers.

Calculate the square of the distance from the East Office to the junction ($CP^2$).

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
