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

In a remote desert, four survey stations—Alpha ($A$), Bravo ($B$), Charlie ($C$), and Delta ($D$)—form a perfect parallelogram-shaped perimeter. The distance between Alpha and Bravo is distinct from the distance between Bravo and Charlie.

Two straight subterranean fiber-optic cables connect the diagonal stations: one links Alpha to Charlie ($AC$), and the other links Bravo to Delta ($BD$). A specialized signal booster, $M$, is installed in the field to optimize data transmission between these hubs.

The position of booster $M$ is determined by the following geometric alignments:
1. The angle formed between the Alpha-Charlie cable and the line to the booster ($\angle MAC$) is exactly equal to the angle between the Alpha-Charlie cable and the boundary line to Delta ($\angle DAC$). To avoid interference, $M$ is positioned on the opposite side of the Alpha-Charlie cable relative to Delta.
2. The angle formed between the Bravo-Delta cable and the line to the booster ($\angle MBD$) is exactly equal to the angle between the Bravo-Delta cable and the boundary line to Charlie ($\angle CBD$). Similarly, $M$ is positioned on the opposite side of the Bravo-Delta cable relative to Charlie.

Let $k$ represent the ratio of the length of the Alpha-Charlie cable to the length of the Bravo-Delta cable ($k = AC/BD$). 

Determine the ratio of the distance from station Alpha to the booster ($AM$) over the distance from station Bravo to the booster ($BM$) strictly in terms of $k$.

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
