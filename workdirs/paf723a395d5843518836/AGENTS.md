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

In the mountainous kingdom of Geometria, three watchtowers—Alpha (A), Bravo (B), and Charlie (C)—form a triangular defense perimeter. The direct mountain path from Alpha to Bravo measures 42 kilometers, the path from Alpha to Charlie measures 39 kilometers, and the coastal road between Bravo and Charlie is 45 kilometers long.

Two supply outposts have been established on the perimeter: Outpost Foxtrot (F) is located on the path between Alpha and Bravo, exactly 21 kilometers from Alpha. Outpost Echo (E) is located on the path between Alpha and Charlie, exactly 13 kilometers from Alpha.

Engineers are planning a central hub, Point P, located at the precise intersection of two straight supply lines: one connecting Charlie to Foxtrot, and the other connecting Bravo to Echo. To facilitate further transport, a survey line is drawn starting from Alpha, passing through the hub at P, and extending until it hits the coastal road between Bravo and Charlie at a point designated as Drop-zone D.

A regional logistics center is to be built at a location O, which is positioned such that it is equidistant from Outpost Echo, Outpost Foxtrot, and Drop-zone D. Let R represent this equal distance (the radius of the circle passing through E, F, and D).

A strategist needs to calculate a specific spatial variance for telecommunications mapping. Determine the value of the square of the distance from Watchtower Charlie to the logistics center O, minus the square of the radius R.

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
