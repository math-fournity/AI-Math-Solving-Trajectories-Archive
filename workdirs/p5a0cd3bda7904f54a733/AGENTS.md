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

In a remote desert, a logistics team has established a central command post at point $A$ on the circular boundary $\omega$ of a restricted zone. Two supply outposts, $B$ and $C$, are located on the same circular boundary. A straight pipeline connects outposts $B$ and $C$. 

The team leader determines that the angle formed between the paths $AB$ and $AC$ is exactly $60^\circ$. A straight access road is paved starting from $A$, perfectly bisecting the $60^\circ$ angle. This road travels 4 units to reach the pipeline $BC$ at junction $E$, and continues further until it hits the boundary of the zone at point $D$. The distance from the command post $A$ to outpost $B$ is measured at 3 units.

To expand operations, the team marks two landmark coordinates: $D'$ is established by projecting a line from $A$ through $D$ such that $D$ is the midpoint of $AD'$, and $C'$ is established by projecting a line from $A$ through $C$ such that $C$ is the midpoint of $AC'$.

A specialized communication beam is fired from $A$ tangent to the circular boundary $\omega$; this beam intersects the extended line of the pipeline $BC$ at a relay station $P$. A secondary circular sensor field is then generated such that its perimeter passes through points $A, P,$ and $D'$. This sensor field intersects the line of the pipeline at a specific coordinate $F$ (where $F \neq P$).

Calculate the exact distance between the coordinate $F$ and the landmark $C'$.

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
