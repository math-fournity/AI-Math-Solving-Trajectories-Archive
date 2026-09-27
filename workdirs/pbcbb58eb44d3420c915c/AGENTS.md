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

A maritime navigation system monitors four research buoys—Alpha ($A$), Bravo ($B$), Charlie ($C$), and Delta ($D$)—all floating on the circular perimeter of a protected coral reef. This circular boundary is centered at a central observation tower $O$ and has a radius of $R = 4$ kilometers.

Technicians are tracking the intersections of specific boundary lines and internal corridors:
- The line extending through Alpha and Delta meets the line through Bravo and Charlie at a signal relay station $Q$.
- The line extending through Alpha and Bravo meets the line through Delta and Charlie at a maintenance platform $P$.
- The two diagonal supply routes, $AC$ and $BD$, intersect at a submerged monitoring hub $M$.

The navigation system provides the exact distances from the central tower $O$ to these three locations:
- The distance to the monitoring hub $M$ is $OM = 5$ km.
- The distance to the maintenance platform $P$ is $OP = 7$ km.
- The distance to the signal relay station $Q$ is $OQ = 8$ km.

A triangular patrol zone is formed between the points $P$, $Q$, and $M$. If the lengths of the three sides of this triangular zone $PQM$ are denoted as $x, y,$ and $z$, determine the value of $x^2 + y^2 + z^2$.

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
