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

In a remote territory, three observation outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. The terrain is surveyed using two critical command hubs: the Central Relay ($O$), which is equidistant from all three outposts, and the Coordination Hub ($H$), which sits at the intersection of the altitudes of the triangle $ABC$. 

A straight supply road is constructed to pass through the exact midpoint of the path connecting the Central Relay ($O$) and the Coordination Hub ($H$). This road is built to be perfectly parallel to the boundary line connecting Bravo ($B$) and Charlie ($C$). The road intersects the perimeter path $AB$ at a checkpoint named Delta ($D$) and the path $AC$ at a checkpoint named Echo ($E$).

Advanced sensors determine that the Central Relay ($O$) is located at the unique point inside the smaller triangular sector $ADE$ that is equidistant from the road $DE$ and the perimeter paths $AD$ and $AE$. Furthermore, the distance from outpost Bravo to Alpha is exactly the same as the distance from outpost Charlie to Alpha, meaning the interior angles at $B$ and $C$ are equal.

Let the interior angles of the triangle $ABC$ at vertices $A, B,$ and $C$ be denoted by $\angle A, \angle B,$ and $\angle C$ in degrees. Calculate the value of:
$\angle A + 2\angle B + 3\angle C$

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
