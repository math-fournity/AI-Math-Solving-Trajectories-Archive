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

In a remote desert, three observation stations, Alpha ($A$), Bravo ($B$), and Charlie ($C$), form a triangular perimeter where the angle at Charlie is obtuse. A straight supply road connects Alpha and Bravo. Along this road, two relay towers, Echo ($E$) and Foxtrot ($F$), are positioned such that the road is divided into three equal segments: $AE = EF = FB$.

A technician is scouting a location for a new data hub, Delta ($D$), situated somewhere along the straight path between stations Bravo and Charlie. To ensure optimal signal propagation, two specific geometric alignments must be met:
1. The line of sight from the data hub ($D$) to the first relay tower ($E$) must be perfectly perpendicular to the supply road segment between Bravo and Charlie.
2. The line of sight from station Alpha ($A$) to the data hub ($D$) must be perfectly perpendicular to the line of sight from station Charlie ($C$) to the second relay tower ($F$).

During a calibration check, a surveyor measures the angle formed between the hub-to-Bravo path and the hub-to-Foxtrot path ($\angle BDF$) and labels it $x$. He then measures the angle formed between the Charlie-to-Foxtrot path and the Charlie-to-Alpha path ($\angle CFA$) and finds it to be exactly triple the first angle, or $3x$.

Based on these specific coordinates and alignments, calculate the exact value of the ratio of the distance between Delta and Bravo to the distance between Delta and Charlie.

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
