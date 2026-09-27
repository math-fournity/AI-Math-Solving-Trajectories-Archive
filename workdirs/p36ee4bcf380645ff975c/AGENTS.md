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

In a vast desert region, three observation outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. A central communications hub, the Origin ($O$), is positioned such that it is equidistant from all three outposts.

A straight supply road connects outposts Bravo and Charlie. Along this road, two specialized relay stations, Delta ($D$) and Echo ($E$), have been constructed such that station Delta lies strictly between Bravo and Echo. Surveillance logs indicate the following exact distances between the sites:
- The distance from Alpha to Delta is 6 units.
- The distance from Delta to Bravo is 6 units.
- The distance from Alpha to Echo is 8 units.
- The distance from Echo to Charlie is 8 units.

Within the smaller triangular zone formed by Alpha, Delta, and Echo, a protected Interior Vault ($I$) has been established. This vault is positioned at the unique point that is equidistant from the three supply paths connecting Alpha, Delta, and Echo (the incenter of triangle $ADE$).

Technicians have measured the direct distance from outpost Alpha to the Interior Vault ($I$) to be exactly 5 units. Based on these coordinates and measurements, what is the straight-line distance between the Interior Vault ($I$) and the central communications hub ($O$)?

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
