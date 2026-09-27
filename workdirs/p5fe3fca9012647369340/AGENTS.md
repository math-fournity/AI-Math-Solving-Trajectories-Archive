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

A remote logistics network connects three main hubs: Base Alpha ($A$), Base Beta ($B$), and Base Gamma ($C$). The distance between Beta and Gamma is $a = 15$ units, and the distance between Alpha and Gamma is $b = 10$ units. The distance between Alpha and Beta is unknown and denoted as $c$.

Two specialized courier paths are established: Path $r$ bisects the angle at Beta, and Path $s$ bisects the angle at Gamma. Two relay stations are positioned along these paths: Station $E$ is located on path $r$, and Station $D$ is located on path $s$. The positioning of these stations is strictly constrained by the geometry of the terrain: the segment $AD$ must be parallel to $BE$, and the segment $AE$ must be parallel to $CD$.

A central coordination tower $I$ is located at the exact intersection of the two courier paths $r$ and $s$. Additionally, a monitoring point $F$ is established at the intersection of two direct service lines: the line connecting Base Beta to Station $D$ and the line connecting Base Gamma to Station $E$.

Aerial surveys confirm that the coordination tower $I$, the monitoring point $F$, and Base Alpha ($A$) all lie on a single perfectly straight line. Based on these spatial constraints, calculate the distance $c$ between Base Alpha and Base Beta.

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
