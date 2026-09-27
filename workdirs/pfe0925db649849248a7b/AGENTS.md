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

A specialized irrigation system is designed across a triangular field with three primary control valves located at coordinates $A$, $B$, and $C$. Surveyors have measured the straight-line distances between these valves: the distance from $A$ to $B$ is 13 decameters, from $B$ to $C$ is 14 decameters, and from $C$ to $A$ is 15 decameters.

To optimize water pressure, two secondary sensors are installed: sensor $E$ is placed on the line $AC$ such that the path $BE$ is perpendicular to $AC$, and sensor $F$ is placed on the line $AB$ such that the path $CF$ is perpendicular to $AB$.

A circular boundary, denoted as $\omega$, is defined as the unique circle passing through the primary valve $A$ and the two sensors $E$ and $F$. A safety perimeter is then established by constructing three straight laser fences. Each fence is perfectly tangent to the circle $\omega$: the first fence touches the circle at point $A$, the second at point $E$, and the third at point $F$. 

These three laser fences intersect to form a triangular enclosure. Calculate the area of this newly formed triangular enclosure. If the area is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a + b$?

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
