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

A specialized circular nature preserve, denoted as territory $\Omega$, contains three primary ranger stations located at coordinates $A$, $B$, and $C$. The straight-line distances between these stations are $AB=4$ km, $BC=5$ km, and $CA=6$ km. Within this triangular region, there is a circular core conservation zone $\omega$.

A new circular research sector $\Gamma$ is established such that its boundary is tangent to the preserve’s outer limit $\Omega$ and also tangent to the paths $AB$ and $BC$. Let $X$ be the specific point on the boundary where the research sector $\Gamma$ meets the preserve limit $\Omega$.

Two scientists, Y and Z, are positioned at distinct locations on the perimeter of the preserve $\Omega$. Their lines of sight to each other and to station $X$ are perfectly constrained: the straight-line path $XY$ and the straight-line path $YZ$ are both perfectly tangent to the boundary of the core conservation zone $\omega$.

Find the square of the distance between the two scientists, $YZ^2$.

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
