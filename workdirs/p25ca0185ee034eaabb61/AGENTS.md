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

A specialized architectural firm is designing a five-sided courtyard defined by the perimeter markers $A, B, C, D$, and $E$ in counterclockwise order. The northern boundary $AB$ and the southern boundary $ED$ are perfectly parallel. To ensure structural symmetry, the design dictates that the angle between the western wall $AE$ and the northern boundary $AB$ must be exactly equal to the viewing angle from $A$ to the marker $D$ across the courtyard (angle $ABD$), the angle from $A$ to $D$ as seen from $C$ (angle $ACD$), and the angle from $C$ to $A$ as seen from $D$ (angle $CDA$).

Surveyors have provided the following fixed measurements for the distances between the markers:
- The length of the northern boundary $AB$ is $8$ meters.
- The diagonal distance from marker $A$ to marker $C$ is $12$ meters.
- The length of the western wall $AE$ is $10$ meters.

The firm needs to calculate the surface area of the triangular garden section formed by the points $C, D$, and $E$. If this area is expressed in the form $\frac{a\sqrt{b}}{c}$ square meters, where $a, b, c$ are integers such that $b$ is square-free and the fraction $\frac{a}{c}$ is in simplest form, determine the value of $a + b + c$.

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
