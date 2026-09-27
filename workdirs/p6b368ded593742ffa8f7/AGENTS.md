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

In the remote Archipelago of Geometry, three naval outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular defensive perimeter. At outpost Alpha, the angle formed by the supply lines to Bravo and Charlie is acute.

The command center has established two strategic relay stations: 
1. Station Delta ($D$) is located on the supply line between Alpha and Charlie, positioned exactly where the naval path that perfectly bisects the interior angle at Bravo hits the $AC$ line. It is known that the distance from Alpha to Station Delta is exactly 30 kilometers.
2. Station Echo ($E$) is located on the supply line between Alpha and Bravo, positioned exactly where the path that perfectly bisects the interior angle at Charlie hits the $AB$ line.

A maintenance buoy, Foxtrot ($F$), is anchored at the precise midpoint of the direct cable connecting Station Delta and Station Echo. 

To monitor environmental conditions, two sensor readings were taken from buoy Foxtrot:
- The shortest distance from Foxtrot to the supply line $AB$ (measured at point Juliet, $J$) is exactly 12 kilometers.
- The shortest distance from Foxtrot to the supply line $BC$ (measured at point Kilo, $K$) is exactly 20 kilometers.

Based on these logistical coordinates and measurements, calculate the square of the distance between Station Delta and Station Echo ($DE^2$).

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
