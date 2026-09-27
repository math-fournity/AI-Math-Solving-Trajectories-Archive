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

In the mountainous kingdom of Arithmos, two major trade routes, Route **AB** and Route **AC**, diverge from the capital city **A**. A strategic outpost, **R**, is positioned such that its distance to the coastal city **C** is exactly equal to its distance back to the capital **A**. Due to the local topography, the trade route **AC** acts as the exact angular bisector between the route leading to the outpost, **AR**, and the main trade route, **AB**.

To facilitate logistics, a straight supply line **BR** was established, which crosses the **AC** trade route at a distribution hub, **Q**. The distance from the capital **A** to this hub **Q** is measured at exactly 2 leagues.

A circular defensive perimeter, defined by the unique circle passing through the capital **A**, the outpost **R**, and the coastal city **C**, intersects the main trade route **AB** at a border checkpoint, **P**. Surveyors have recorded that the distance from the capital **A** to checkpoint **P** is 1 league, while the remaining distance from the checkpoint **P** to the city **B** is 5 leagues. 

The angle formed at the capital by the routes to **B** and **C**, the angle at **B** between the routes to **A** and **R**, and the angle at **C** between the routes to **A** and **B** are all acute.

Based on these survey measurements, determine the exact length of the route **AR** in leagues.

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
